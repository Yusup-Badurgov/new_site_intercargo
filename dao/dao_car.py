# CRUD
from flask import request


class Car:
    def __init__(self, data):
        self.data = data

    def get_all_data(self):
        """
        ункция из txt файла забирает все строки, далее каждую строку разделяет по
         (eanter \n) и кладет в список
        :return: Возвращает список, где отдельный элемент это одна
        строка (cтрана, ПрайсМосква, ПрайсСПБ, ПрайсНовосибирск, ПрайсКраснодар
        """
        data_list = self.data.split('\n')
        return data_list

    def get_all_country(self):
        """
        Функция берет список из метода get_all_data
        :return: возвращает отдельный список только названий стран
        """
        data_list = self.get_all_data()

        all_country = []
        for country_data_str in data_list:
            list_country_data = country_data_str.split(' ')
            all_country.append(list_country_data[0])

        return all_country

    def get_cities(self):
        city = ['Москва', 'Санкт Петербург', 'Новосибирск', 'Краснодар']
        return city

    def get_request_country_city(self):
        """
        Функция получает request данные из html файла,а именно из form,
        такие как: название страны и выбранный город
        :return:
        """
        choice_country = request.form['country']
        choice_city = request.form['city']

        need_data = [choice_country, choice_city]

        return need_data

    def create_dict(self, choice_country):
        country_dict = {}
        cities = self.get_cities()
        all_data_list = self.get_all_data()

        data_list = []
        for item in all_data_list:
            data_list.append(item.split(' '))

        for data in data_list:
            if choice_country in data[0]:
                country_dict[choice_country] = {
                    cities[0]: data[1],
                    cities[1]: data[2],
                    cities[2]: data[3],
                    cities[3]: data[4]
                }

                return country_dict

    def calculate(self, choice_country, choice_city):
        country_dict = self.create_dict(choice_country)
        price = country_dict.get(choice_country).get(choice_city)
        result = f'Стоимость перевозки автомобиля составит {price}€'
        return result
