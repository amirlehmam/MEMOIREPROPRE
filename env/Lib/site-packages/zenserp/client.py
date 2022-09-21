import zenserp
import requests
import json
import requests.exceptions
import os.path
import os
import errno
import logging


class Client(object):
    api_key = None
    headers = {}
    debug = False

    def __init__(self, api_key=None, business_id=None):

        self.headers['User-Agent'] = 'Zenserp_Python_V2'

        if api_key:
            self.api_key = api_key

        self.api_base = zenserp.api_base

        if zenserp.debug:
            self.debug = True
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(message)s')

    def status(self):
        return self._request('/status')

    def search(self, params):
        """
        
        Parameter | Description | Default
        --------- | ----------- | -----------
        q | The keyword to query | None (required)
        location | The location used in the query | Optional
        search_engine | The url of the search engine to query | google.com
        hl | The language of the search engine, autodetected from the search_engine if not supplied | Optional
        gl | Geolocation to be used in the search query, autodetected from the search_engine if not supplied | Optional
        num | The number of search results. Values can be 1-100 | 10
        start | Offset for the search results | 0
        tbm | For image search: 'isch', for Maps 'lcl' | Optional
        timeframe | See below | Optional

        Possible values for timeframe:

        h – past hour
        d – past 24 hours
        w – past week
        m – past month
        mn – the past n number of months. Double digits are supported
        y – past year
        """
        if type(params) is not tuple:
            raise Exception("Params need to be pair of tuples")

        return self._request('/search', params=params)

    def _request(self, url, method="GET", params=dict(), data=None,
                 return_type=None):
        url = self.api_base + url

        if self.api_key:
            self.headers['apikey'] = self.api_key

        try:
            if method in ["GET", "DELETE"]:
                response = requests.request(
                    method, url, headers=self.headers, params=params)

            elif method == "POST":
                if self.debug:
                    logging.debug(data)
                response = requests.request(
                    method, url, headers=self.headers, params=params, json=data)

            else:
                raise Exception("Method not supported")

            response_obj = json.loads(response.text)

            if self.debug:
                logging.debug(response_obj)

            if "errors" in response_obj:
                return Exception("API returned errors:", response_obj['errors'])

            return response_obj

        except requests.exceptions.RequestException:
            raise
