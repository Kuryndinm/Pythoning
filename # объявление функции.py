from decimal import Decimal
import datetime

goods = {
    22
}

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    exp_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d')
                                          
    if title not in items:
        items[title] = []
        #temp_list_of_product_data = []
        amount_expiration_date_dict = {
            'amount': Decimal(amount),
            'expiration_date': datetime.datetime.date(exp_date)
        }
      # amount_expiration_date_dict['amount']['expiration_date'] = amount, expiration_date
        #temp_list_of_product_data.append(amount_expiration_date_dict)
    
        items[title].append(amount_expiration_date_dict)
        return items, 'Продукт успешно добавлен!'
    
    elif title in items:
        #temp_list_of_product_data = []
        amount_expiration_date_dict = {
            'amount': Decimal(amount),
            'expiration_date': datetime.datetime.date(exp_date)
        }
      
    
        items[title].append(amount_expiration_date_dict)
        
        return items, 'Продукт успешно добавлен!'
        
    else:
        return 'Что-то пошло не так, продукт не добавлен...'
    


def add_by_note(items, note):
    temp_dict_of_data = [i for i in note.split(', ')]
    if len(temp_dict_of_data[2].split('-')) == 3:
        try:
            datetime.datetime.strptime(temp_dict_of_data[2], '%Y-%m-%d')
    
            name_of_product = temp_dict_of_data[0]
            amount_of_product = Decimal(temp_dict_of_data[1])
            expiration_date_of_product = temp_dict_of_data[2]
        
            return add(items, name_of_product, amount_of_product, expiration_date_of_product)
        except Exception:
            return 'Не пойдет'
    
    
    


def find(items, needle):
    keyword = needle.lower()
    temp_items_keys = [i for i in items.keys()]
    items_by_needle = [i for i in temp_items_keys if keyword in i]
    if items_by_needle:
        return items_by_needle
    else:
        return 'Продукт не найден!'
    #else:
    #    return 'Продукт не найден!'


def amount(items, needle):
    total_amount = 0
    keyword = needle.lower()
    list_of_required_products = find(items,keyword)
    
    for product in list_of_required_products:
        for amount in items[product]:
            temp = amount['amount']
            total_amount += temp
            print(f'{product} - {temp} кг.')
            
    return f'Общий вес оставшегося продукта: {total_amount} кг.'

def expire(items, in_advance_days=0):
    counter = 0
    list_of_expired_products = []
    
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=in_advance_days)
    
    for name_of_product, products_data in items.items():
        for product in products_data:
            if datetime.datetime.date(product['expiration_date'])  < future_date:
                counter += 1
                list_of_expired_products.append(name_of_product)  
            
    if counter == 0:
        return 'Все продукты в порядке!'
    else:
        return f'Список просроченных продуктов: {list_of_expired_products}.'
            
            
            #if datetime.date(product['expiration_date'])  < current_date:
                #return f'Срок годности продукта {name_of_product} истек!'
            #elif datetime.date(product['expiration_date'])  > current_date:
             #   return f'Срок годности продукта {name_of_product} в порядке.'
            #elif datetime.date(product['expiration_date'])  == current_date:
             #   return f'Срок годности продукта {name_of_product} истекает сегодня!'
    #if >= 0:
    #    if == 1:
    #        return f'Срок годности истекает через {} день.'
    #    elif > 1 and < 5:
    #        return f'Срок годности истекает через {} дня.'
    #    else:
    #        return f'Срок годности истекает через {} дней.'
    #else: < 0:
    #    return f'Срок годности истек!!'
    
    

print(add_by_note(goods, 'сыр российский, 0.2, 2024-2-22'))
print(add_by_note(goods, 'собака корейская, 1, 2025-3-24'))
print(add_by_note(goods, 'колбаса китайская, 0.123, 2026-5-26'))
print(add_by_note(goods, 'сыр российский, 0.6, 2025-2-22'))
print(add(goods, 'title', Decimal('13'), expiration_date='2024-2-4'))
print(add_by_note(goods, 'сыр российсикй, 0.420, 2024-2-22'))

print(add_by_note(goods, 'сыр гауда, 0.4, 2024-2-22'))
#print(find(goods, 'сыр российский'))
#print(find(goods, 'сыр'))
#print(find(goods, 'российский'))
#print(find(goods, 'хуй'))
#print()
#print(amount(goods, 'сыр'))
#print(expire(goods))
#print(expire(goods, 123))
#print(expire(goods))
#print(expire(goods, 0))
#print(expire(goods, 2), goods)





temp_dict_of_data = [i for i in note.split(' ')]
    if len(temp_dict_of_data[:-2]) > 1:
        true_name_of_product = '_'.join(temp_dict_of_data[:-2])
    else:
        true_name_of_product = temp_dict_of_data[0]
    if len(temp_dict_of_data) < 3:
        if len(temp_dict_of_data) == 2 and temp_dict_of_data[-1] is int():
            name_of_product = true_name_of_product
            amount_of_product = Decimal(temp_dict_of_data[-1])
            return add(items, name_of_product, amount_of_product)
        else:
            name_of_product = true_name_of_product
            return add(items, name_of_product, 0)

    elif len(temp_dict_of_data[2].split('-')) == 3:
        try:
            datetime.datetime.strptime(temp_dict_of_data[-1], '%Y-%m-%d')
            if len(temp_dict_of_data) == 3:
                name_of_product = true_name_of_product
                amount_of_product = Decimal(temp_dict_of_data[-2])
                expiration_date_of_product = temp_dict_of_data[-1]
                return add(items, name_of_product, amount_of_product, expiration_date_of_product)
            elif len(temp_dict_of_data) == 2:
                name_of_product = true_name_of_product
                amount_of_product = Decimal(temp_dict_of_data[-2])
                return add(items, name_of_product, amount_of_product)
            else:
                name_of_product = true_name_of_product
                return add(items, name_of_product, 0)
        
            
        except Exception:
            return 'Не пойдет'
        






list_of_data = note.split(' ')
      # проверка последней строки на дату
    list_for_date = list_of_data[-1].split('-')
      # проверка предпоследней(последней строки на число)
    is_num_2 = list_of_data[-2].replace('.', '') 
    is_num_1 = list_of_data[-1].replace('.', '') 
    if len(list_for_date) == 3 and len(list_for_date[0]) == 4 and is_num_2.isdigit() and 0 < int(list_for_date[1]) < 13 and 0 < int(list_for_date[2]) < 31:
        name_of_product = ' '.join(list_of_data[:-2])
        amount_of_product = Decimal(list_of_data[-2])
        expiration_date_of_product = list_of_data[-1]
        return add(items, name_of_product, amount_of_product, expiration_date_of_product)
    elif is_num_1.isdigit():
        name_of_product = ' '.join(list_of_data[:-1])
        amount_of_product = Decimal(list_of_data[-1])
        return add(items, name_of_product, amount_of_product)
    elif len(list_for_date) == 3 and len(list_for_date[0]) == 4 and not is_num_2.isdigit() and 0 < int(list_for_date[1]) < 13 and 0 < int(list_for_date[2]) < 31:
        name_of_product = ' '.join(list_of_data[:-1])
        expiration_date_of_product = list_of_data[-1]
        return add(items, name_of_product, 0, expiration_date_of_product)
    else:
        name_of_product = ' '.join(list_of_data)
        return add(items, name_of_product, 0)