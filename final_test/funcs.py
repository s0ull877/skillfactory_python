import os
import time
from decorators import counter
from consts import bot_side
from bot_side import bot_side_x, bot_side_0

# счетчик на неправильные ответы
@counter
def choose_side() -> (str,bool):
# достижение валидного ответа
    answer = input("Выберите сторону (x/0) либо 'q' для выхода: ").lower()
    if answer not in ('x','0','q'):
        print('Некорректный ввод!')
        return answer, False
    else:
        return answer, True

# принтит игровую карту(?)
def print_game_map(game_map: list):
    os.system('cls')
    temp = [game_map[0].copy(),game_map[1].copy(),game_map[2].copy()] #траблы двумерного массива

    print('  0 1 2')
    for row in range(0,3):
        temp[row] = ' '.join(temp[row])
        print(f'{row} ' +temp[row])
    

# ход юзера
def user_insert(game_map: list, answer: str):
    try:
    
        x = int(input('x: '))
        y = int(input('y: '))
    
    except ValueError:
        # обработка ValueError
        print('Некоректный ввод!')
        time.sleep(2)
        return False
    
    if x not in [0,1,2] or y not in [0,1,2]:
        # обработка некорректного места на мапе
        print('Ответ должен быть в дипазоне от 0 до 2!')
        time.sleep(2)
        return False

    if game_map[x][y] == '-':
        # ход засчитан, если координаты пустые
        game_map[x][y] = answer
        return True

    else:
        # координаты заняты
        print('Место занято, лол.')
        time.sleep(2)
        return False

        
# ход бота
def bot_insert(game_map:list, answer: str) -> list:
    check_edit = [game_map[0].copy(),game_map[1].copy(),game_map[2].copy()]

    # берем сторону бота
    bot_answer = bot_side[answer]


    if bot_answer == 'x':
        game_map = bot_side_x(game_map)
        return game_map

    game_map = bot_side_0(game_map)
    return game_map
        

# проверка результатов хода
def check_map(game_map: list, answer: str) -> bool:
    for row in range(0,3):
        #! проверка по горизонтали
        if set(game_map[row]) == {f'{answer}'}:
            print('Вы победили!')
            time.sleep(5)
            return False
        if set(game_map[row]) == {f'{bot_side[answer]}'}:
            print('Вы проиграли(')
            time.sleep(5)
            return False
        
        #! проверка по вертикали
        temp = game_map[0][row] + game_map[1][row] + game_map[2][row]
        if set(temp) == {f'{answer}'}:
            print('Вы победили!')
            time.sleep(5)
            return False
        if set(temp) == {f'{bot_side[answer]}'}:
            print('Вы проиграли(')
            time.sleep(5)
            return False

    #! проверка по диагонали
    temp = game_map[0][0] + game_map[1][1] + game_map[2][2]
    if set(temp) == {f'{answer}'}:
        print('Вы победили!')
        time.sleep(5)
        return False
    if set(temp) == {f'{bot_side[answer]}'}:
        print('Вы проиграли(')
        time.sleep(5)
        return False
        
    #! проверка по диагонали
    temp = game_map[0][2] + game_map[1][1] + game_map[2][0]
    if set(temp) == {f'{answer}'}:
        print('Вы победили!')
        time.sleep(5)
        return False
    if set(temp) == {f'{bot_side[answer]}'}:
        print('Вы проиграли(')
        time.sleep(5)
        return False

    temp = [*game_map[0],*game_map[1],*game_map[2]]
    if '-' not in set(temp):
        print('Ничья!')
        time.sleep(5)
        return False

    return True
 


