import aiohttp
from typing import List, Union


class App:
    def __init__(self):
        self.endpoint = 'https://api.hh.ru/vacancies'

        self.session: aiohttp.ClientSession = None
        self.user_agent = 'Parser/1.0 (parser-feedback@icloud.com)'
        self.timeout = 5
        self.proxy: str = None

    async def create_session(self):
        self.session = aiohttp.ClientSession(
            conn_timeout=self.timeout, proxy=self.proxy
        )
        self.session.headers.update({'User-Agent': self.user_agent})

    async def get_vacancies(
        self,
        query: str,
        per_page: int = 100,
        page: int = 0
    ) -> Union[List, None]:
        try:
            async with self.session.get(self.endpoint, params={'text': query,
                                                               'per_page': str(per_page),
                                                               'page': str(page)}, ssl=False) as request:
                response = await request.json()
                if 'items' in response:
                    return response['items']
        except Exception as e:
            print(f'internal app err - {e}')