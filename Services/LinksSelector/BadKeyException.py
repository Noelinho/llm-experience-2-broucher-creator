class BadKeyException(Exception):
    def __init__(self):
        super().__init__(f"There is a problem with the API key")