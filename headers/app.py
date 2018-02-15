import pprint
import requests


class HeaderChecker(object):

    def __init__(self, url):
        self.url = url

    def check(self):
        response = requests.get(self.url)
        headers_to_check = {
            'X-Frame-Options': ['deny', 'sameorigin', 'allow-from'],
            'X-XSS-Protection': ['1', '1; mode=block', '1; report='],
            'X-Content-Type-Options': ['nosniff'],
        }
        self.result = {}

        for header, valid_options in headers_to_check.items():
            if header not in response.headers:
                self.result[header] = 'Header is missing!'
                continue

            valid = False
            for option in valid_options:
                if response.headers[header].startswith(option):
                    valid = True
                    break

            if not valid:
                self.result[header] = 'Not secure option! Use one of the following values %s' % valid_options
            else:
                self.result[header] = 'All oke!'

    def report(self):
        pprint.pprint(self.result)
