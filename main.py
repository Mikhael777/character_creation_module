from random import randint




def defence(char_name: str, char_class: str) -> str:
    """Battle defence processing."""
    if char_class == 'warrior':
        return (f'{char_name : str } блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name: str} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name: str} блокировал {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    """Battle special ability processing."""
    if char_class == 'warrior':
        return (f'{char_name: str} применил специальное умение'
                f' «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name: str} применил специальное умение'
                f' «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name: str} применил специальное умение'
                f' «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """Training processing."""
    if char_class == 'warrior':
        print(f'{char_name: str}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name: str}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name: str}, ты Лекарь — чародей, способный исцелять'
              ' раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence '
          '— чтобы блокировать атаку противника или special — чтобы '
          'использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'




if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
