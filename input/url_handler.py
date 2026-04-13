import requests


class URLHandler:
    def __init__(self, cli):
        self.url = cli.url_input(self.validateURL)

    def validateURL(self, url):
        """requests the header to the oembed api youtube with the media url"""

        response = requests.head(
            f"https://www.youtube.com/oembed?format=json&url={url}"
        )

        if response.status_code == 200:
            return True
        else:
            return "Please input a valid url"
