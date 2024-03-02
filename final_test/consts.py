# базовая игровая карта
START_MUP = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# сторона бота {key: user_side, value: bot_side}
bot_side = {
    'x': 'O',
    'O': 'x'
}

# если сторона бота x, при нахождении key паттернов, детает value ход
pattern_x = {
    'OO-':'OOx',
    'O-O':'OxO',
    '-OO':'xOO',
    '-xx':'xxx',
    'xx-':'xxx',
    'x-x':'xxx'
}

# то же самое для 0
pattern_0 = {
    'OO-':'OOO',
    'O-O':'OOO',
    '-OO':'OOO',
    '-xx':'Oxx',
    'xx-':'xxO',
    'x-x':'xOx'
}

