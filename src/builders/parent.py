from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


class Builder:
    def __init__(
        self,
        message: Message = None,
        callback: CallbackQuery = None,
        state: FSMContext = None
    ):
        self.message = message
        self.callback = callback
        self.state = state

        if self.callback and not self.message:
            self.message = self.callback.message