def foo(file_path):
    with open(file_path, encoding='utf8') as file_work:
        cook_book = {}
        def foo():
            dish = file_work.readline().strip()
            if dish:
                cook_book[dish] = []
                ingredient_number = file_work.readline()
                for line in range(int(ingredient_number)):
                    ingredient = file_work.readline().strip().split(' | ')
                    ingredient_dictionary = {'ingredient name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                    cook_book[dish].append(ingredient_dictionary)
            else:
                return(cook_book)
            file_work.readline()
            foo()
        foo()
    return(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = foo('Рецепты.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient name'] not in shop_list:
                    shop_list[ingredient['ingredient name']] = {'measure': ingredient['measure'], 'quantity': (int(ingredient['quantity'])*person_count)}
                else:
                    shop_list[ingredient['ingredient name']]['quantity'] += (int(ingredient['quantity'])*person_count)
    return(shop_list)
print(foo('Рецепты.txt'))
print(get_shop_list_by_dishes(["Омлет", 'Утка по-пекински'], 2))
