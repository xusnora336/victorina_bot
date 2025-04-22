from aiogram import Dispatcher, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import stop_button
from state import LevelState
import random
router = Router()

@router.message(F.text=="LEVEL 1")
async def lvl1_handler(message:Message,state:FSMContext,):
    if message.text == "LEVEL 1":
        question=f"{random.randrange(1,11)} {random.choice(["+","-","*"])} {random.randrange(1,11)}"

        answer=eval(question)
        await state.update_data(answer=answer,level1=message.text,true=0, false=0)
        await message.answer(f"SAVOL: {question} = ?")
        await state.set_state(LevelState.level1)

@router.message(F.text=="LEVEL 2")
async def lvl2_handler(message:Message,state:FSMContext,):
    if message.text == "LEVEL 2":
        question2=f"{random.randrange(1,51)} {random.choice(["+","-","*"])} {random.randrange(1,51)}"

        answer2=eval(question2)
        await state.update_data(answer2=answer2,level2=message.text,true=0, false=0)
        await message.answer(f"SAVOL: {question2} = ?")
        await state.set_state(LevelState.level2)

@router.message(F.text=="LEVEL 3")
async def lvl3_handler(message:Message,state:FSMContext,):
    if message.text == "LEVEL 3":
        question3=f"{random.randrange(1, 101)} {random.choice(["+","-","*"])} {random.randrange(1, 101)}"

        answer3=eval(question3)
        await state.update_data(answer3=answer3,level3=message.text,true=0, false=0)
        await message.answer(f"SAVOL: {question3} = ?")
        await state.set_state(LevelState.level3)


@router.message(F.text=="LEVEL 4")
async def lvl4_handler(message:Message,state:FSMContext,):
    if message.text == "LEVEL 4":
        question4=f"{random.randrange(1,101)} {random.choice(["+","-","*","/"])} {random.randrange(1,101)}"

        answer4=eval(question4)
        await state.update_data(answer=answer4,level4=message.text,true=0, false=0)
        await message.answer(f"SAVOL: {question4} = ?")
        await state.set_state(LevelState.level4)