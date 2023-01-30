from flask import Flask, render_template, request
from implemented import dao_personal_item, dao_car

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def personal_items():
    countries = dao_personal_item.get_all_country()
    if request.method == 'GET':
        return render_template('personal_items.html', countries=countries)

    elif request.method == 'POST':

        data = dao_personal_item.get_request_country_type_cube()

        if data[2] == "":
            shipping_cost = 'Вы не указали количество кубов'
        else:
            shipping_cost = dao_personal_item.calculate(data[0], data[1], data[2])

        return render_template('personal_items.html', countries=countries, shipping_cost=shipping_cost)


@application.route('/car', methods=['GET', 'POST'])
def car_page():
    countries = dao_car.get_all_country()
    cities = dao_car.get_cities()

    if request.method == 'GET':
        return render_template('car.html', countries=countries, cities=cities)

    elif request.method == 'POST':
        data = dao_car.get_request_country_city()
        shipping_cost = dao_car.calculate(data[0], data[1])
        return render_template("car.html", countries=countries, cities=cities, shipping_cost=shipping_cost)


if __name__ == '__main__':
    application.run()
