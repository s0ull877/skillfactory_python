# Мейн файл, запуск для корректной работы зависимости: /path/to/main> python main.py
import os
import time
from funcs import choose_side, print_game_map, user_insert,bot_insert, check_map
from consts import START_MUP


answer = None # переменная ответа пользователя, служит для выхода из мейн цикла и выбора сайда
good_insert = False # юзер будет писать координаты хода, пока не даст чтото валидное
try:
    while answer != 'q':

        answer, side_choosen = choose_side()

        answer = 'O' if answer == '0' else answer # O выглядит красивее 0

        # если ответ на choose_side() не вылидный
        if not side_choosen:
            continue

        
        game_continue = True
        #двумерный массив не работате на обычном list.copy()
        game_map = [START_MUP[0].copy(),START_MUP[1].copy(),START_MUP[2].copy()]

        # если юзер выбрал x, он ходит 1й
        if answer =='x':
        
            while game_continue:

                print_game_map(game_map)
                
                # ! реаоизация хода юзера
                while not good_insert:
                    print('Введите координаты x, y.\nГде x - строка, y - столбец.')
                    good_insert = user_insert(game_map,answer)
                    print_game_map(game_map)
                
                good_insert = False #чтобы после хода бота войти в цикл выше
            
                game_continue = check_map(game_map,answer)
                # если game_continue был бы False на этом этапе, следующий ход всеравно бы
                # был выполнен, поэтому если игра оконччена, то мы прерываем скипаем все
                if not game_continue:
                    continue

                # ! реализация хода бота
                bot_insert(game_map, answer)
                print_game_map(game_map)
                print('Бот сделал ход')
                
                game_continue = check_map(game_map,answer)

        # если юзер выбрал 0, бот ходит 1й
        elif answer == 'O':
            while game_continue:
                # ! реализация хода бота
                bot_insert(game_map, answer)
                print_game_map(game_map)
                print('Бот сделал ход')

                game_continue = check_map(game_map,answer)
                if not game_continue:
                    continue

                # ! реаоизация хода юзера
                while not good_insert:
                    print('Введите координаты x, y.\nГде x - строка, y - столбец.')
                    good_insert = user_insert(game_map,answer)
                    print_game_map(game_map)

                good_insert = False
except KeyboardInterrupt:
    pass

finally:
    print('\nСессия завершена!')
