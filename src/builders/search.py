from typing import Union, Tuple, List
import re
import datetime

from .parent import Builder
from ..app import App
from ..keyboards import search as search_key
from ..states import App as app_states

app = App()


class SearchBuilder(Builder):
    async def handle_city(self):
        if self.state:
            await self.state.set_state(None)

        city = self.message.text
        if city == 'all':
            await self.save_area()
            return

        try:
            await app.create_session()
            cities = await app.get_areas(query=city)

            await self.message.answer('Выберите город из списка', reply_markup=await search_key.cities_key(cities))
        except Exception as e:
            print(f'internal app err - {e}')
            await self.message.answer('Произошла ошибка приложения')
            return
        finally:
            await app.close_session()


    async def save_area(self, area: Union[str, int] = None):
        if not self.state:
            return
        
        await self.state.update_data({'area': area})

        await self.message.answer('Введите ваш запрос для поиска вакансий')
        await self.state.set_state(app_states.query_search)


    async def get_area(self) -> Union[int, None]:
        if self.state:
            return (await self.state.get_data())['area']
        

    async def format_response(self, data: list) -> List[Tuple[Union[int, str]]]:
        return [(item['id'], item['name']) for item in data]


    async def pagination(self, page: int, area: int):
        if page == -1:
            await self.callback.answer('Это первая страница', show_alert=True)
            return

        query = (await self.state.get_data())['query']
        try:
            result, pages = await app.get_vacancies(
                query,
                area=area,
                page=page
            )
            result = await self.format_response(result)
            await self.message.edit_reply_markup(
                reply_markup=await search_key.items_key(
                    result, page, end_page=pages
                )
            )
        except Exception as e:
            print(f'internal app err - {e}')
            if self.callback:
                await self.callback.answer('searcher was destroyed with error', show_alert=True)


    async def go_search(
        self,
        per_page: int = 15,
        pagination: bool = False
    ):
        if not self.state:
            return

        try:
            await app.create_session()
            area = await self.get_area()

            if pagination:
                await self.pagination(int(self.callback.data.split('=')[1]), area)
                return
            
            query = self.message.text
            await self.state.update_data({'query': query})
            
            result, pages = await app.get_vacancies(
                query, area=area,
                per_page=per_page
            )
            result = await self.format_response(result)
            await self.message.answer(
                f'По вашему запросу найдено {per_page * pages} вакансий',
                reply_markup=await search_key.items_key(result, 0, end_page=pages)
            )
        except Exception as e:
            print(f'internal app err - {e}')
            await self.message.answer('Произошла ошибка приложения')
            return
        finally:
            await app.close_session()


    async def init_vacancy(self):
        id, page = map(int, self.callback.data.split('=')[1].split('_'))
        try:
            await app.create_session()
            result = await app.get_vacancy_info(id)
            await self.message.edit_text(
                '{}\n\nОписание: {}\nОпубликовано: {}'.format(
                    result['name'], await self.clean_description(result['description']),
                    await self.format_publish_date(result['published_at'])
                ),
                reply_markup=await search_key.vacancy_key(result['alternate_url'], page)
            )
        except Exception as e:
            print(f'internal app err - {e}')
            await self.message.answer('Произошла ошибка приложения')
            return
        finally:
            await app.close_session()


    async def format_publish_date(self, date: str) -> Union[str, None]:
        try:
            obj = datetime.datetime.fromisoformat(date)
            return obj.strftime("%d %B %Y г. %H:%M:%S")
        except ValueError:
            print('invalid format')


    async def clean_description(self, text: str) -> str:
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)