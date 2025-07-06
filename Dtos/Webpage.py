from Services.Scrapper.Scrapper import Scrapper
from Services.LinksSelector.OpenAI.OpenAILinksSelector import OpenAILinksSelector

class Webpage:
    def __init__(self, url: str):
        self.url = url
        self.title = None
        self.content = None
        self.logoUrl = None
        self.mainImageURl = None
        self.links = []
        self.scrapper = Scrapper()
        self.linksSelector = OpenAILinksSelector()

    def retrieveContent(self, lookForLinks: bool = True):
        data = self.scrapper.scrape(self.url)
        self.title = data.get('title')
        self.content = data.get('content')
        self.logoUrl = data.get('logo_img_url')
        self.mainImageURl = data.get('main_img_url')

        if lookForLinks:
            self.links = self.linksSelector.retrieve(data.get('links', []), self.url)

        return self
