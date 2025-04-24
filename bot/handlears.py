from aiogram import Dispatcher, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import start_btn
from keyboards import btn_keyboard
from keyboards import stop_button
from state import LevelState
import random
router = Router()

def get_min_max_number(level):
    print(level)
    if level == "LEVEL 1":
        return 1, 11
    elif level == "LEVEL 2":
        return 1, 51
    elif level=="LEVEL 3":
        return 1, 101
    elif level == "LEVEl 4":
        return 1, 101

@router.message(F.text=="🎲Boshlash")
async def start_game(message: Message):
    await message.answer("Oyin qaytadan boshlandi",reply_markup=btn_keyboard)

@router.message(F.text == "LEVEL 1")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(1, 11)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(1, 11)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL 1",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_button)
    await state.set_state(LevelState.javob)

@router.message(F.text == "LEVEL 2")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(1, 51)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(1, 51)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL 2",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_button)
    await state.set_state(LevelState.javob)

@router.message(F.text == "LEVEL 3")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(1, 101)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(1, 101)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL 3",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_button)
    await state.set_state(LevelState.javob)

@router.message(F.text == "LEVEL 4")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(1, 101)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(1, 101)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEl 4",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_button)
    await state.set_state(LevelState.javob)


@router.message(StateFilter(LevelState.javob))
async def process_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    correct_answer = data.get("answer")
    correct = data.get("correct", 0)
    incorrect = data.get("incorrect", 0)
    level = data.get("level")

    if message.text == "STOP":
        text=(f"{level}\n"
              f"Savollar soni: {correct+incorrect}\n"
              f"✅To'g'ri javoblar: {correct}\n"
              f"❌Noto'gri javoblar: {incorrect}\n")
        await message.answer(text,reply_markup=start_btn)

        return



    try:
        user_answer = int(message.text)
        if user_answer == correct_answer:
            correct += 1
            await message.answer("Javob to'g'ri✅!")
        else:
            incorrect += 1
            await message.answer(f"Javob noto'g'ri❌!\n"
                                 f" To'g'ri javob {correct_answer}!")
    except ValueError:
        await message.answer("Iltimos raqam kiriting")

    min_number,max_number = get_min_max_number(level)

    question = (f"{random.randint(min_number, max_number)}"
                f"{random.choice(['+', '-', '*'])}"
                f"{random.randint(min_number, max_number)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, correct=correct, incorrect=incorrect)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_button)

