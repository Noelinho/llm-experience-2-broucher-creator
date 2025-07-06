class Webpage:
    def __init__(
            self,
            url: str,
            title: str,
            content: str,
            logoUrl: str = None,
            mainImageURl: str = None,
    ):
        self.url = url
        self.title = title
        self.content = content
        self.logoUrl = logoUrl
        self.mainImageURl = mainImageURl