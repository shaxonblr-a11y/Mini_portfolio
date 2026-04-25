from random import randint
import os
import sys


# ✅ Правильный путь к файлу рекордов (работает и как .py и как .exe)
def get_path(filename):
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, filename)

SCORE_FILE = get_path('best_score.txt')

# ✅ Создаём файл автоматически если его нет
if not os.path.exists(SCORE_FILE):
    with open(SCORE_FILE, 'w', encoding="utf-8") as f:
        f.write('0')

with open(SCORE_FILE, 'r', encoding="utf-8") as f:
    best_result = int(f.read())


game_difficulty={"1": {"low":0, "high":10}, "2":{"low":0,"high":50}, "3":{"low":0, "high":100}}
print("Привет, это игра угадай число."
      "\nВ игре тебе необходимо угадать число,"
      "\nтакже присутствует счётчик попыток.")
print("Выбери уровень сложности:"
      "\n1-легкий (от 0 до 10),"
       "\n2-средний (от 0 до 50)" 
       "\n3-сложный (от 0 до 100)",)
while True:
    user_chose = (input('Введите какой уровень сложности '
                               'вы желаете выбрать, (1/2/3):'))
    print(f'Вы выбрали уровень сложности: {user_chose}')
    if user_chose not in game_difficulty:
        print("Такого уровня нет, введите 1, 2 или 3")
        continue
    break
low=game_difficulty[user_chose]["low"]
high=game_difficulty[user_chose]["high"]
secret_number = randint(low, high)
result = 0

if best_result == 0:
    print(f'Рекорд пока не установлен')
else:
    print(f'Текущий рекорд: {best_result}')

while True:

    try:
        guess = int(input('Введите число: '))
    except ValueError:
        print('Ошибка, введите целое число')
        continue

    result += 1

    if guess < secret_number:
        print('Загаданное число больше')
    elif guess > secret_number:
        print('Загаданное число меньше')
    else:
        print('Ура, вы выиграли!!!')
        print(f'Количество попыток: {result}')
        if best_result == 0 or result < best_result:
            best_result = result
            print(f'Новый рекорд: {best_result}!')
            with open(SCORE_FILE, 'w', encoding="utf-8") as f:
                f.write(str(result))
        print(f'Лучший результат: {best_result}')
        input('\nНажмите Enter для выхода...')  # ✅ окно не закроется мгновенно
        break