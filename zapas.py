import tkinter as tk
from func import app_CRUD


# Создаем главное окно
window = tk.Tk()
window.geometry("500x300")
window.title("Trade Calculator")


# Создаем поле со списком для выбора страны
country_label = tk.Label(text="Выбрать страну:")
country_label.pack()


country_options = app_CRUD.get_country()
country_var = tk.StringVar(window)
country_var.set(country_options[0])  # значение по умолчанию

country_combobox = tk.OptionMenu(window, country_var, *country_options)
country_combobox.pack()

# Создаем тумблер для выбора типа сделки
trade_type_label = tk.Label(text="Выбрать направление:")
trade_type_label.pack()

trade_type_var = tk.BooleanVar(window)

export_radiobutton = tk.Radiobutton(window, text="Экспорт", value='True', variable=trade_type_var)
export_radiobutton.pack()

import_radiobutton = tk.Radiobutton(window, text="Импорт", value=False, variable=trade_type_var)
import_radiobutton.pack()

# Создаем поле для ввода значения
value_label = tk.Label(text="Введите количество кубов N m3:")
value_label.pack()

value_entry = tk.Entry(window)
value_entry.pack()


# Создаем кнопку "Рассчитать"
def calculate():
    # Получить выбранную страну и тип сделки
    country = country_var.get()
    trade_type = trade_type_var.get()

   # Получить значение кубометров введеное пользователем
    value_cube = value_entry.get()

    # Выполняем расчет и отображаем результат
    result = app_CRUD.get_price(value_cube, country, trade_type)
    result_label.config(text=result)


calculate_button = tk.Button(window, text="Рассчитать", command=calculate)
calculate_button.pack()

# Создаем метку для отображения результата
result_label = tk.Label(text="")
result_label.pack()

# Запустить цикл событий tkinter
window.mainloop()

