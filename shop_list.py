from pprint import pprint
cook_book = {}
with open('recipes.txt', encoding='utf-8') as file:
    for line in file:
        dish_name = line.strip()
        quantity = int(file.readline().strip())
        dish_list = []
        for ingredients in range (quantity):
            ing_dict = {}
            ing = file.readline().split('|')
            ing_dict['ing_name'] = ing[0].strip()
            ing_dict['quantity'] = ing[1].strip()
            ing_dict['measure'] = ing[2].strip()
            dish_list.append(ing_dict)
        file.readline()
        cook_book[dish_name] = dish_list


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name in dishes:

        for ing in cook_book[dish_name]:
            if ing['ing_name'] not in shop_list:
                value ={'measure': ing['measure'], 'quantity':int(ing['quantity']) * person_count}
                shop_list[ing['ing_name']] = value
            else:
                shop_list[ing['ing_name']]['quantity'] += int(ing['quantity']) * person_count
    return shop_list
pprint(get_shop_list_by_dishes (['Запеченный картофель', 'Омлет'], 2))
