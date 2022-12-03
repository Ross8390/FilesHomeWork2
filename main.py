def read_cook_book(file):
    cook_book = {}
    with open('data.txt', encoding='utf-8') as f:
        for line in f:
            dishes = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []
            for i in range(ingredients_count):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dishes] = ingredients
            f.readline()
    return cook_book


file = 'data.txt'
cook_book = read_cook_book(file)


def get_shop_list_by_dishes(dishes, person_count):
    new_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                dict_ing = {}
                if ingredients['ingredient_name'] in new_dict:
                    quantity = new_dict[ingredients['ingredient_name']].get('quantity') + \
                               ingredients['quantity'] * person_count
                    new_dict[ingredients['ingredient_name']].update(quantity=quantity)
                else:
                    dict_ing['measure'] = ingredients['measure']
                    dict_ing['quantity'] = ingredients['quantity'] * person_count
                    new_dict[ingredients['ingredient_name']] = dict_ing
    return new_dict


print(get_shop_list_by_dishes({'Омлет', 'Запеченный картофель'}, 2))




