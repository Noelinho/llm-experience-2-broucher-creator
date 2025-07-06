from openai import OpenAI
import os
import json

from Services.LinksSelector.BadKeyException import BadKeyException

MAX_TOKENS = 150
MODEL = "gpt-4o-mini"

class OpenAILinksSelector():
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.checkKey(self.api_key)

        self.client = OpenAI(api_key=self.api_key)

    def retrieve(self, links: list, url: str) -> list:
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.generateSystemPrompt()},
                {"role": "user", "content": self.generatePrompt(links, url)}
            ],
            response_format={"type": "json_object"}
        )

        result = response.choices[0].message.content
        return json.loads(result)

    def generateSystemPrompt(self) -> str:
        link_system_prompt = "Te voy a dar un listado de links que se encuentran en una página web que describe un curso de formación. \
Tienes que devolverme los enlaces de datos de centro (url contiene centrodetalles) \n"

        link_system_prompt += "Deberías responder en formato JSON como en el siguiente ejemplo:"
        link_system_prompt += """
        {
            "links": [
                {"type": "about page", "url": "https://full.url/goes/here/about"},
                {"type": "careers page": "url": "https://another.full.url/careers"}
            ]
        }
        """

        return link_system_prompt

    def generatePrompt(self, links: list, url: str) -> str:
        user_prompt = f"Aquí tienes un listado de links de la página web {url} - "
        user_prompt += "Por favor, decide cual de esos enlaces son relevantes para el folleto de la compañía, responde con las urls completas con https en formato JSON. \
no incluyas enlaces de términos legales, privacidad, emails...\n"
        user_prompt += "Los links son estos (pueden ser relativos):\n"
        user_prompt += "\n".join(links)

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
