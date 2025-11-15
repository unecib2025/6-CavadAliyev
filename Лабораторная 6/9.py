a = ["alert", "spam", "login", "error", "spam", "alert"]
a.remove('spam')
a.append('END_LOG')
a.reverse()
b = a.count('alert')
print(f'Журнал после очистки: {a}')
print(f"Количество 'alert': {b}")