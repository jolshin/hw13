import requests
import json

class SuperHeroComparison:

    def __init__(self, heroes):
        self.url = 'https://akabab.github.io/superhero-api/api/'
        self.query = self.get_query()
        self.heroes = heroes

    def get_query(self):
        """Method gets response from server and returns dictionary"""
        try:
            response = requests.get(self.url+'all.json') #kept it, but before I thought to use different ROUTES
            response.raise_for_status()
            return json.loads(response.text)

        except(requests.RequestException, ValueError):
            print('Ошибка')
            return False

    def get_the_truth(self):
        """Method checks for certain heroe and gets his intelligence value, \
        compares heroes by intelligence and returns the name of smartest one"""
        intelligence = {}

        for heroe in self.heroes:
            for item in self.query:
                if item['name'] == heroe:
                    intelligence.update({item['name'] : item['powerstats']['intelligence']})
        smartest = max(intelligence.items(), key=lambda item: item[1])
        return smartest 
        
if __name__ == '__main__':
    heroes = (input('Кого сравнить по уму? (введите Героев через запятую) \nИЛИ\nнажми ' \
            'Enter для проерки лиц по списку: Hulk, Captain America, Thanos: ').split(', '))

    if heroes == ['']:
        heroes = ['Hulk', 'Captain America', 'Thanos']

    result = SuperHeroComparison(heroes)

    print(f'Самый умный тов. {result.get_the_truth()[0]} ')
    print(f'Его ум равен {result.get_the_truth()[1]} единиц(-е, -ам)')