import sqlite3
from setup_db import database_1


class AppCRUD:

    def __init__(self, database):
        self.database = database

    def get_inquiry(self):
        with sqlite3.connect(self.database) as con:
            cur = con.cursor()
            sqlite_query = ("""
                                SELECT country, price_1m3_120kg, price_2m3_220kg, price_3m3_360kg, price_4m3_480kg, 
                                price_allowance_for_1m3
                                FROM 'Прайс на личные вещи ЕВРОПА'
                """)
            cur.execute(sqlite_query)
            result = cur.fetchall()
            return result

    def get_country(self):
        result = self.get_inquiry()
        all_country = []
        for country in result:
            all_country.append(country[0])
        return all_country

    def create_dict(self, choice_country):
        country_dict = {}
        all_data = self.get_inquiry()
        for data in all_data:
            if choice_country in data[0]:
                country_dict[data[0]] = {
                    1: data[1],
                    2: data[2],
                    3: data[3],
                    4: data[4],
                    "add_mn": data[5]
                }
            # возвращает словарь где ключ страна, а значение еще один словарь
            # с количеством кубом и его значениями в виде стоимости, где последний
            # это ставка за каждый доп 1м3
                return country_dict
        return 'что то не так, я метод create_dict'

    def get_price(self, choice_cube, choice_country, trade_type):
        choice_country = str(choice_country)
        country_dict = self.create_dict(choice_country)
        direction = {'ЭКСПОРТ': {"ТО РФ": 200, "ТО ЕС": 250}, 'ИМПОРТ': {"ТО РФ": 350, "ТО ЕС": 400}}

        if choice_cube == "":
            answer = "Вы ничего не указали в поле для ввода кубометров"
            return answer

        elif not choice_cube.isdigit():
            answer = 'Поле кубометров принимает только цифры! Укажите от 1 до 100!'
            return answer


        elif int(choice_cube) in country_dict.get(choice_country):
            price = country_dict.get(choice_country).get(int(choice_cube))

            if trade_type == 1:
                result_price = f'Ставка перевозки: {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€\n' \
                               f'Итого стоимость: {price + direction.get("ЭКСПОРТ").get("ТО РФ") + direction.get("ЭКСПОРТ").get("ТО ЕС")}€\n\n'

                return result_price

            elif trade_type == 0:
                result_price = f'Ставка перевозки: {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€\n'\
                               f'Таможенное оформление в РФ = {direction.get("ИМПОРТ").get("ТО РФ")}€\n'\
                               f'Таможенное оформление в ЕС = {direction.get("ИМПОРТ").get("ТО ЕС")}€\n'\
                               f'Итого стоимость: {price + direction.get("ИМПОРТ").get("ТО РФ") + direction.get("ИМПОРТ").get("ТО ЕС")}€\n\n'
                return result_price

        elif int(choice_cube) in range(5, 101):
            need_cube = int(choice_cube) - 4
            price = (need_cube * country_dict.get(choice_country).get('add_mn')) \
                    + country_dict.get(choice_country).get(4)

            if trade_type == 1:
                result_price = f'Ставка перевозки: {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ЭКСПОРТ").get("ТО ЕС")}€\n' \
                               f'Итого стоимость: {price + direction.get("ЭКСПОРТ").get("ТО РФ") + direction.get("ЭКСПОРТ").get("ТО ЕС")}\n\n€'
                return result_price

            elif trade_type == 0:
                result_price = f'Ставка перевозки: {int(choice_cube)} м3 (вес до {int(choice_cube) * 120} кг) = {price}€\n' \
                               f'Таможанное оформление в РФ = {direction.get("ИМПОРТ").get("ТО РФ")}€\n' \
                               f'Таможенное оформление в ЕС = {direction.get("ИМПОРТ").get("ТО ЕС")}€\n' \
                               f'Итого стоимость: {price + direction.get("ИМПОРТ").get("ТО РФ") + direction.get("ИМПОРТ").get("ТО ЕС")}\n\n€'
                return result_price


app_CRUD = AppCRUD(database_1)
