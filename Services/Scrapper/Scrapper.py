from bs4 import BeautifulSoup
import requests

from Dtos.Webpage import Webpage

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

irrelevantElements = ["script", "style", "input"]

class Scrapper:
    def __init__(self):
        pass

    def scrape(self, url: str) -> Webpage:
        title = ""
        body = ""

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"

        logo_img_url = None
        main_img_url = None

        logo_container = soup.find(class_='boxes-untrack__logo')
        main_image_container = soup.find(class_='course-page-top-bg')

        if logo_container:
            logo_img = logo_container.find('img')
            if logo_img and logo_img.get('src'):
                logo_img_url = logo_img['src']

        if main_image_container:
            main_img = main_image_container.find('img')
            if main_img and main_img.get('src'):
                main_img_url = main_img['src']

        for img in soup.find_all('img'):
            if not img.find_parent(class_='boxes-untrack__logo'):
                img.decompose()

        for tag in irrelevantElements:
            for elem in soup.body.find_all(tag):
                elem.decompose()

        body = soup.body.get_text(separator="\n", strip=True)

        return Webpage(
            url=url,
            title=title,
            content=body,
            logoUrl=logo_img_url,
            mainImageURl=main_img_url
        )


