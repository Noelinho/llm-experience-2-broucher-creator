from openai import OpenAI
import os

from Dtos.Webpage import Webpage

from Services.LinksSelector.BadKeyException import BadKeyException

MAX_TOKENS = 150
MODEL = "gpt-4o-mini"

class OpenAIBroucherCreator():
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.checkKey(self.api_key)

        self.client = OpenAI(api_key=self.api_key)

    def create_broucher(self, webpage: Webpage):
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.generateSystemPrompt()},
                {"role": "user", "content": self.generatePrompt(webpage)}
            ],
        )
        result = response.choices[0].message.content
        return result

    def generateSystemPrompt(self) -> str:
        link_system_prompt = ("Eres un asistente que analiza el contenido de diferentes páginas web de cursos de formación \
        y crea un folleto con la información más relevante del curso enfocado a potenciales alumnos. El folleto debe tener como mínimo 500 palabras. \
        El título del folleto no debe incluir el concepto 'folleto', será simplemente el nombre del curso. \
        Incluye detalles de precio, duración, temario, requisitos, y cualquier otra información relevante, así como información del centro. No añadas en el contenido \
        datos de contacto ni como contactar para matricularse. Acuérdate de usar las reviews de los usuarios si existen.\n")

        return link_system_prompt

    def generatePrompt(self, webpage: Webpage) -> str:
        user_prompt = f"Estás analizando un curso con una url {webpage.url} - "
        user_prompt += "\n Me gustaría que añadieras en la cabecera del folleto el logo del centro, siempre por encima del h1, que tiene la url:" + f" {webpage.logoUrl} \n"
        user_prompt += "\n Me gustaría que añadieras la imagen principal del curso (en caso de tenerla), siempre por debajo del h1, que tiene la url:" + f" {webpage.mainImageURl} \n"
        user_prompt += "Aquí tienes el contenido de su página web; usa esta información para crear un folleto del curso, \n"
        user_prompt += webpage.content
        user_prompt = user_prompt[:5000]

        return user_prompt

    def checkKey(self, api_key):
        if not api_key:
            raise BadKeyException(
                "No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")

        elif not api_key.startswith("sk-proj-"):
            raise BadKeyException(
                "An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
        elif api_key.strip() != api_key:
            raise BadKeyException(
                "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
