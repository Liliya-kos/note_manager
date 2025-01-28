username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: 1. ")
title1 = input("Введите заголовок заметки: 2. ")
title2 = input("Введите заголовок заметки: 3. ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки из списка: 'To do', 'In process', 'Done' ")
created_date = input("Введите дату создания заметки в формате день-месяц-год: ")
issue_date = input("Введите дату истечения заметки в формате день-месяц-год: ")

temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

title_list = [title, title1, title2]

note1 = [username, content, status, temp_created_date, temp_issue_date, title_list]

print(note1)