from typing import Union

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


    async def go_search(self):
        if not self.state:
            return
        
        query = self.message.text
        area = (await self.state.get_data())['area']

        try:
            await app.create_session()
            result = await app.get_vacancies(query, area=area)
            print(result)
        except Exception as e:
            print(f'internal app err - {e}')
            await self.message.answer('Произошла ошибка приложения')
            return
        finally:
            await app.close_session()