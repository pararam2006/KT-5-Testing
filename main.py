import requests
import pprint
import allure


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Sending {request_type} request to {url}")
    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, json=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        allure.attach(f"Response: {response.text}", name="API Response", attachment_type=allure.attachment_type.JSON)
        pprint.pprint(f'{request_type} example')
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.text)
        pprint.pprint('**********')
        return response

    @allure.step("GET request to {endpoint}/{endpoint_id}")
    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    @allure.step("POST request to {endpoint}/{endpoint_id} with data: {data}")
    def post(self, endpoint, endpoint_id, data):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=data)
        return response.json()

    @allure.step("DELETE request to {endpoint}/{endpoint_id}")
    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()
