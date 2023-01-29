# CRUD
from flask import request


class PersonalItem:
    def __init__(self, data):
        self.data = data

    def get_all_data(self):
        """
        Функция из txt файла забирает все строки, далее каждую строку разделяет по (eanter \n) и кладет в список
        :return: Возвращает список, где отдельный элемент это одна строка (ид, страна, 1м3, 2м3, 3м3, 4м3 и доп. м1)
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

    def get_request_country_type_cube(self):
        """
        Функция получает request данные из html файла,а именно из form,
        такие как: название страны, тип направления(Экспорт или Импорт) и количество кубов.
        :return:
        """
        choice_country = request.form['country']
        choice_type = request.form['direction']
        choice_cube = request.form['cubes']

        need_data = [choice_country, choice_type, choice_cube]

        return need_data

    def create_dict(self, choice_country):
        country_dict = {}
        all_data_list = self.get_all_data()

        data_list = []
        for item in all_data_list:
            data_list.append(item.split(' '))

        for data in data_list:
            if choice_country in data[0]:
                country_dict[choice_country] = {
                    1: int(data[1]),
                    2: int(data[2]),
                    3: int(data[3]),
                    4: int(data[4]),
                    "add_mn": int(data[5])
                }

                return country_dict

    def calculate(self, choice_country, trade_type, choice_cube):
        country_dict = self.create_dict(choice_country)
        direction = {'ЭКСПОРТ': {"ТО РФ": 200, "ТО ЕС": 250}, 'ИМПОРТ': {"ТО РФ": 350, "ТО ЕС": 400}}

        if int(choice_cube) in country_dict.get(choice_country):
            price = country_dict.get(choice_country).get(int(choice_cube))

            if trade_type == "export":
                result_price = f'Перевозка {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€\n' \
                               f'Таможенное оформление в России = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€.\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€.\n' \
                               f'Итого {price + direction.get("ЭКСПОРТ").get("ТО РФ") + direction.get("ЭКСПОРТ").get("ТО ЕС")}€.\n' \
                               f'+Пошлины 30% от заявленной стоимости груза, но не менее чем 2-4€/кг'
                return result_price

            elif trade_type == "import":
                result_price = f'Перевозка {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€.\n' \
                               f'Таможенное оформление в России = {direction.get("ИМПОРТ").get("ТО РФ")}€.\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ИМПОРТ").get("ТО ЕС")}€\n' \
                               f'Итого {price + direction.get("ИМПОРТ").get("ТО РФ") + direction.get("ИМПОРТ").get("ТО ЕС")}€.\n' \
                               f'+Пошлины 30% от заявленной стоимости груза, но не менее чем 4€/кг'
                return result_price

        elif int(choice_cube) in range(5, 1001):
            need_cube = int(choice_cube) - 4
            price = (need_cube * country_dict.get(choice_country).get('add_mn')) \
                    + country_dict.get(choice_country).get(4)

            if trade_type == "export":
                result_price = f'Перевозка {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€\n' \
                               f'Таможенное оформление в России = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€.\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€.\n' \
                               f'Итого {price + direction.get("ЭКСПОРТ").get("ТО РФ") + direction.get("ЭКСПОРТ").get("ТО ЕС")}€.\n' \
                               f'+Пошлины 30% от заявленной стоимости груза, но не менее чем 2-4€/кг'
                return result_price

            elif trade_type == "import":
                result_price = f'Перевозка {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€.\n' \
                               f'Таможенное оформление в России = {direction.get("ИМПОРТ").get("ТО РФ")}€.\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ИМПОРТ").get("ТО ЕС")}€\n' \
                               f'Итого {price + direction.get("ИМПОРТ").get("ТО РФ") + direction.get("ИМПОРТ").get("ТО ЕС")}€.\n' \
                               f'+Пошлины 30% от заявленной стоимости груза, но не менее чем 4€/кг'
                return result_price
