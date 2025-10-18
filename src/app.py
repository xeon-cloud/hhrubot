import aiohttp
from typing import List, Union


class Endpoints:
    vacancies = 'https://api.hh.ru/vacancies'
    areas = 'https://api.hh.ru/areas'


class App:
    def __init__(self):
        self.session: aiohttp.ClientSession = None
        self.user_agent = 'Parser/1.0 (parser-feedback@icloud.com)'
        self.timeout = 5
        self.proxy: str = None

    async def create_session(self):
        self.session = aiohttp.ClientSession(
            conn_timeout=self.timeout,
            proxy=self.proxy
        )
        self.session.headers.update({'User-Agent': self.user_agent})

    async def close_session(self):
        if self.session:
            await self.session.close()

    async def get_vacancies(
        self,
        query: str,
        per_page: Union[int, str] = 100,
        page: Union[int, str] = 0,
        area: Union[int, str] = None
    ) -> Union[List, None]:
        params = {'text': query,
                  'per_page': str(per_page),
                  'page': str(page)}
        if area:
            params['area'] = area

        try:
            async with self.session.get(Endpoints.vacancies,
                                        params=params, ssl=False) as request:
                response = await request.json()
                if 'items' in response:
                    return response['items']
        except Exception as e:
            print(f'internal app err - {e}')

    async def get_vacancy_info(self, id: Union[str, int]) -> dict:
        try:
            async with self.session.get(f'{Endpoints.vacancies}/{id}', ssl=False) as request:
                response = await request.json()
                return response
        except Exception as e:
            print(f'internal app err - {e}')

    async def get_areas(
        self,
        country_id: int = 113,
        query: str = None
    ) -> list:
        data = []
        try:
            async with self.session.get(Endpoints.areas, ssl=False) as request:
                response = await request.json()
                for country in response:
                    if int(country['id']) == country_id:
                        for area in country['areas']:
                            if not query:
                                data.append((area['id'], area['name']))
                                continue

                            if query.lower() in area['name'].lower():
                                data.append((area['id'], area['name']))
            return data
        except Exception as e:
            print(f'internal app err - {e}')