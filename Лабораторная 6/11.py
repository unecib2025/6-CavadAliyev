a = ['ok', 'fail', 'fail', 'ok', 'fail']
b = a.count('fail')
while b > 0:
    a.remove('fail')
    b -=1
a.append('audit_completed')
a.reverse()
c = a.index('ok')
print(f'Количество неудачных входов: {b}')
print(f'Итоговый список: {a}')
print(f'Первый индекс "ok": {c}')