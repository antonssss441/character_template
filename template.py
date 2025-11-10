from jinja2 import Environment, FileSystemLoader, select_autoescape
import random


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')
    character_races = ['человек', 'орк', 'эльф', 'гоблин']
    character_classes = ['охотник', 'ассасин', 'бард', 'воин', 'маг']
    clases_base = {
        'охотник': {
            'skills':  ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
            'strength': random.randint(1,3),
            'agility': 15,
            'intelligence': random.randint(1,3),
            'luck': random.randint(1,3),
            'temper': random.randint(1,3),
            'image': '../images/archer.png'
        },
        'ассасин': {
            'skills': ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
            'strenght': random.randint(1,3),
            'agility': random.randint(1,3),
            'intelligence': random.randint(1,3),
            'luck': 15,
            'temper': random.randint(1,3),
            'image': '../images/assasin.png'
        },
        'бард': {
            'skills': ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
            'strenght': random.randint(1,3),
            'agility': random.randint(1,3),
            'intelligence': random.randint(1,3),
            'luck': random.randint(1,3),
            'temper': 15,
            'image': '../images/bard.webp'
        },
        'воин': {
            'skills': ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
            'strenght': 15,
            'agility': random.randint(1,3),
            'intelligence': random.randint(1,3),
            'luck': random.randint(1,3),
            'temper': random.randint(1,3),
            'image': '../images/warrior.png'
        },
        'маг': {
            'skills': ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
            'strenght': random.randint(1,3),
            'agility': random.randint(1,3),
            'intelligence': 15,
            'luck': random.randint(1,3),
            'temper': random.randint(1,3),
            'image': '../images/wizard.png'
        }
    }
    cards_number = int(input('Сколько карточек хотите сделать?: '))
    for card in range(cards_number):
        races = int(input('выберите расу из списка: 1-человек, 2-орк, 3-эльф, 4-гоблин: '))
        classes = int(input('Выберите класс из списка: 1-охотник, 2-ассасин, 3-бард, 4-воин, 5-маг: '))
        skills = random.sample(clases_base[character_classes[classes - 1]]['skills'], 3)
        rendered_page = template.render(
            name = input('Введите имя персонажа: '),
            race = character_races[races - 1],
            character_class = character_classes[classes - 1],
            image = clases_base[character_classes[classes - 1]]['image'],
            strength = clases_base[character_classes[classes - 1]]['strenght'],
            agility = clases_base[character_classes[classes - 1]]['agility'],
            intelligence = clases_base[character_classes[classes - 1]]['intelligence'],
            luck = clases_base[character_classes[classes - 1]]['luck'],
            temper = clases_base[character_classes[classes - 1]]['temper'],
            first_skill = skills[0],
            second_skill = skills[1],
            third_skill = skills[2]
        )
        with open(f'characters/index{card + 1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()

    
