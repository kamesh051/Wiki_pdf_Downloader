import requests
import json
import wikipedia

class WikiApi:
    """
    Class for setting up API. Contains methods for loading suggestions.
    """
    url = 'http://en.wikipedia.org/w/api.php'
    headers = {
        'Content-Type': 'application/json'
    }

    def process_request(self, search_data):
        """
        Queries the wikipedia opensearch API and retreives the links along with
        matching article names

        :param search_term: search term for which suggestions has to be retreived
        :return results: nested list of title, summary for the retreived suggestions
        """
        params = {
            'action': 'opensearch',
            'search': search_data,
            'limit' : 20,
            'format': 'json'
        }
        response = requests.get(url=self.url, headers=self.headers, params=params)
        suggestions = json.loads(response.text)
        results = []
        try:
            for title, summary in zip(suggestions[1], suggestions[2]):
                results.append([title, summary])
        except KeyError:
            results = []
        return results

    def get_article(self, article_name):
        """
        Fetches the article from the wikipedia

        :param article_name: Article for which data has to be retreived
        :return: page object containing the retreived data
        """
        try:
            page = wikipedia.page(article_name)
            return page
        except wikipedia.exceptions.WikipediaException:
            print("Please provide an article name")
            return None

x = WikiApi()
x.process_request('')
