from flask import Flask, render_template, request
from implemented import dao_personal_item

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



@application.route('/car')
def car_page():
    return render_template('car.html')

if __name__ == '__main__':
    application.run()
