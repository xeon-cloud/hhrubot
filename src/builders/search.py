from .parent import Builder
from ..app import App

app = App()


class SearchBuilder(Builder):
    async def go_search(self):    
        query = self.message.text

        try:
            await app.create_session()
        except Exception as e:
            print(f'init session err - {e}')
            await self.message.answer('Произошла ошибка инициализации сессии')
            return

        request = await app.get_vacancies(query)
        if not request:
            await self.message.answer('Произошла ошибка приложения')
            return
        
        print(request[0]['id'])