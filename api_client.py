class InvitationAPI:
    base_url = 'your-wedding.com/wessel'

    def add(self, name):
        self._send_request(f'/add/{name}')

    def remove(self, name):
        self._send_request(f'/delete/{name}')

    def _send_request(self, path):
        # some stuff actually talking to the API
        print(f'sending request with path {self.base_url + path}')


def main(api_client):
    api_client.add('Mary Antoinette')
    api_client.add('North West')
    api_client.remove('Salieri')


if __name__ == '__main__':
    api = InvitationAPI()
    main(api)
