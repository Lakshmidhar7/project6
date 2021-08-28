import requests


class Keyword:
    """

    """

    def __init__(self):
        pass

    def get_function(self, url):
        """

        :return:
        """
        res = requests.get(url)
        print(res.status_code)
        print(res.json())

    def post(self, url):
        """

        :param url:
        :return:
        """
        payload = {
            "name": "Luckey",
            "job": "QaTest"
        }

        response = requests.post(url, payload)
        print(response)
        print(response.content)

    def put(self, url):
        """

        :param url:
        :return:
        """
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = requests.put(url, payload)
        print(response)
        print(response.content)

    def patch(self, url):
        """

        :param url:
        :return:
        """
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = requests.patch(url, payload)
        print(response)
        print(response.content)

    def delete(self, url):
        """

        :param url:
        :return:
        """
        response = requests.delete(url)
        print(response)

    def post_res(self, url):
        """

        :param url:
        :return:
        """
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        res = requests.post(url, payload)
        print(res)
        print(res.content)

    def post_register(self, url):
        """

        :param url:
        :return:
        """
        payload = {
            "email": "lakshmidhar@reqres.in"
        }
        res = requests.post(url, payload)
        print(res)
        print(res.content)

    def post_login(self, url):
        """

        :param url:
        :return:
        """
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"

        }
        res = requests.post(url, payload)
        print(res)
        print(res.content)

    def post_log(self, url):
        """

        :param url:
        :return:
        """
        payload = {
            "email": "peter@klaven"
        }
        res = requests.post(url, payload)
        print(res)
        print(res.content)

    