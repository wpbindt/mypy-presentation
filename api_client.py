import requests


class InvitationAPI:
    base_url = 'your-wedding.com/wessel'

    def add(self, name: str) -> None:
        self._send_request(f'/add/{name}')

    def remove(self, name: str) -> None:
        self._send_request(f'/delete/{name}')

    def _send_request(self, path: str) -> requests.Response:
        # some stuff actually talking to the API
        print(f'sending request with path {self.base_url + path}')
        return requests.Response()


class DRInvitationAPI:
    def add(self, name: str) -> None:
        print(f'Not really adding {name}')

    def remove(self, name : str) -> None:
        print(f'Not really removing {name}')


def main(api_client: InvitationAPI) -> None:
    api_client.add('Mary Antoinette')
    api_client.add('North West')
    api_client.remove('Salieri')


if __name__ == '__main__':
    api = DRInvitationAPI()
    main(api)
