from aiogram.fsm.state import StatesGroup, State



class LevelState(StatesGroup):
    level1 = State()
    level2 = State()
    level3 = State()
    level4 = State()