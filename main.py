from datetime import datetime


def hello(now):
    noon = now.replace(hour=12)

    if noon == now:
        return 'Il va falloir penser à aller manger'
    elif now < noon:
        return 'C\'est l\'heure du café'
    else:
        return 'Bonne journée'


def goodbye(now):
    noon = now.replace(hour=12)

    if noon == now:
        return 'Bon apétit'
    elif now < noon:
        return 'Bonne fin de matinée'
    else:
        return 'La journée est bientôt finit'


def miror(word):
    return word.lower()[::-1]


def isPalindrome(word):
    return word.lower() == word.lower()[::-1]


if __name__ == '__main__':
    now = datetime.now()
    print(hello(now))

    while True:
        word = input("Ecrivez un mot\n")
        if word == 'S\'il vous plaît, je veux quitter ce programme':
            break
        print('Le mot à l\'envers est :' + miror(word))

        if isPalindrome(word):
            print('Bien dit')
    goodbye(now)
