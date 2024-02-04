import time

start = time.time()

def is_password_good(password):
    if len(password) < 8:
        return False
    if password.isdigit():
        return False
    if password.isalpha():
        return False
    if password.islower():
        return False
    if password.isupper():
        return False
    if password.isalnum():
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

end = time.time()

print(f' Код выполнялся {start-end} сек')