whitelist = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5']
a = input("Введите IP для удаления: ")
b = input("Введите новый IP: ")
whitelist.remove(a)
whitelist.insert(3,b)
whitelist.sort()
c = whitelist.index(b)
print(f'Обновленный белый список: {whitelist}')
print(f'Индекс нового IP: {c}')