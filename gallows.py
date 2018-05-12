import random

words = ['Магазин', 'Холодильник', 'Лампа', 'Кружка', 'Ножницы', 'Розетка', 'Часы']
LIFE = 6
guess_word = random.choice(words)


class TroikaIgrokov:

    def __init__(self, word):
        self._word = list(word)
        self._mask = ['*' for i in self._word]
        print(''.join(self._mask))

    def bukva(self, char):
        for i, c in enumerate(self._word):
            if char == c.lower():
                self._mask[i] = c
        return ''.join(self._mask)

    def health(self, let):
        if let not in self._word:
            global LIFE
            LIFE -= 1

    def star(self):
        if '*' not in self._mask:
            print('Вы выиграли')
            return True
        return False


def choice_word(guess_word):
    print('Загадано слово, попробуй отгадай')
    one = TroikaIgrokov(guess_word)
    while LIFE != 0:
        letter = input('Введите возможную букву: ')
        print(one.bukva(letter.lower()))
        one.health(letter.lower())
        if one.star():
            return True
        print('У вас осталось {} жизней'.format(LIFE))
    print('Вас повесили!')


if __name__ == '__main__':
    choice_word(guess_word)
