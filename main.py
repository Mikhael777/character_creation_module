from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name : str } блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name: str} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name: str} блокировал {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name: str} применил специальное умение'
                f' «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name: str} применил специальное умение'
                f' «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name: str} применил специальное умение'
                f' «Защита {10 + 30}»')




def choice_char_class() -> str:
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class: str = input('Введи название персонажа, за которого хочешь'
                                ' играть: Воитель — warrior, Маг — mage,'
                                ' Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый'
                  ' и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким '
                  'интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из '
                  'природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую '
                               'другую кнопку, чтобы выбрать другого '
                               'персонажа ').lower()
    return char_class


def main() -> str:
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name: str}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
