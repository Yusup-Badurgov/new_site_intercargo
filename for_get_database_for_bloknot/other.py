with open('data_for_database', 'r', encoding='utf-8') as file:
    data = file.read()

data_list = data.split('\n')
new_data_list = []
for i in data_list:
    new_data_list.append(i.replace('\t', ' ').replace('  ', ' '))

for i in new_data_list:
    a = i.split(' ')
    if len(a) != 5:
        print(i)

# for i in new_data_list:
#     print(i)