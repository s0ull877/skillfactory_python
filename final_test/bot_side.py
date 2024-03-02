from consts import pattern_x, pattern_0


# если юзер выбрал нолик
def bot_side_x(game_map: list) -> list:
    check_edit = [game_map[0].copy(),game_map[1].copy(),game_map[2].copy()]

    #! проверка по горизонтали
    for row in range(0,3):
        try:
            temp = ''.join(game_map[row])
            game_map[row] = list(pattern_x[temp])
            break
        except KeyError:
            pass
    
    # так же не придумал как сделать без постоянных сравнений
    if check_edit != game_map:
        return game_map

    #! проверка по вертикали
    for column in range(0,3):
        try:
            temp = game_map[0][column] + game_map[1][column] + game_map[2][column]
            data = pattern_x[temp]
            # не придумал как сделать без доп цикла
            for i in range(0,3):
                game_map[i][column] = data[i]
            break
        except KeyError:
            pass

    if check_edit != game_map:
        return game_map

    #! проверка на искосок с лева на право
    temp = game_map[0][0] + game_map[1][1] + game_map[2][2]
    try:
        data = pattern_x[temp]
        for i in range(0,3):
            game_map[i][i] = data[i]
    except KeyError:
        pass

    if check_edit != game_map:
        return game_map

    #! проверка на искосок с права на лево
    temp = game_map[0][2] + game_map[1][1] + game_map[2][0] #-00
    try:
        data = pattern_x[temp] #x00
        for i in range(0,3):
            game_map[i][-i-1] = data[i]
    except KeyError:
        pass

    if check_edit != game_map:
        return game_map

    #! обычный ход
    for row in range(0,3):
        try:
            column = game_map[row].index('-')
            game_map[row][column] = 'x'
            break
        except ValueError:
            pass

    if check_edit != game_map:
        return game_map





# если юзер выбрал x
def bot_side_0(game_map: list) -> list:
    check_edit = [game_map[0].copy(),game_map[1].copy(),game_map[2].copy()]

    #! проверка по горизонтали
    for row in range(0,3):
        try:
            temp = ''.join(game_map[row])
            game_map[row] = list(pattern_0[temp])
            break
        except KeyError:
            pass

    if check_edit != game_map:
        return game_map

    #! проверка по вертикали
    for column in range(0,3):
        try:
            temp = game_map[0][column] + game_map[1][column] + game_map[2][column]
            data = pattern_0[temp]
            # не придумал как сделать без доп цикла
            for i in range(0,3):
                game_map[i][column] = data[i]
            break
        except KeyError:
            pass

    if check_edit != game_map:
        return game_map

    #! проверка на искосок с лева на право
    temp = game_map[0][0] + game_map[1][1] + game_map[2][2]
    try:
        data = pattern_0[temp]
        for i in range(0,3):
            game_map[i][i] = data[i]
    except KeyError:
        pass

    if check_edit != game_map:
        return game_map

    #! проверка на искосок с права на лево
    temp = game_map[0][2] + game_map[1][1] + game_map[2][0] #-00
    try:
        data = pattern_0[temp] #x00
        for i in range(0,3):
            game_map[i][-i-1] = data[i]
    except KeyError:
        pass

    if check_edit != game_map:
        return game_map

    #! обычный ход
    for row in range(0,3):
        try:
            column = game_map[row].index('-')
            game_map[row][column] = 'O'
            break
        except ValueError:
            pass
    
    if check_edit != game_map:
        return game_map


