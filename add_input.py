username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки из списка: 'To do', 'In process', 'Done' ")
created_date = input("Введите дату создания заметки в формате день-месяц-год: ")
issue_date = input("Введите дату истечения заметки в формате день-месяц-год: ")

temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

print("Имя пользователя: ",username)
print("Заголовок заметки: ", title)
print("Содержание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", temp_created_date)
print("Дата истечения заметки: ", temp_issue_date)