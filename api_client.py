from dataclasses import dataclass
from typing import Union, Set

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


@dataclass
class FakeInvitationAPI:
    guests: Set[str]

    def add(self, name: str) -> None:
        self.guests.add(name)

    def remove(self, name: str) -> None:
        self.guests.remove(name)


def main(api_client: Union[InvitationAPI, DRInvitationAPI]) -> None:
    api_client.add('Mary Antoinette')
    api_client.add('North West')
    api_client.remove('Salieri')


def api_factory(dry_run: bool = False) -> Union[InvitationAPI, DRInvitationAPI]:
    if dry_run:
        return DRInvitationAPI()
    return InvitationAPI()


if __name__ == '__main__':
    dry_run = False
    api = api_factory(dry_run)
    main(api)
