from dao.dao_personal_item import PersonalItem
from dao.dao_car import Car

from setup_txt import data_personal_item
from setup_txt import data_car

dao_personal_item = PersonalItem(data_personal_item)
dao_car = Car(data_car)
