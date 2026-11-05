users = {
"ivan": [10, 8, 12, 4, 6],
"olena": [9, 7, 3, 12, 5],
"petro": [4, 6, 8, 10, 2],
"anna": [11, 12, 9, 3, 7]
}
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login == "ivan" and password == "1234":
    grades = users["ivan"]
elif login == "olena" and password == "1111":
    grades = users["olena"]
elif login == "petro" and password == "2222":
    grades = users["petro"]
elif login == "anna" and password == "3333":
    grades = users["anna"]
else:
    grades = []

if grades != []:
    print("Ваші оцінки:", grades)

    good = 0
    bad = 0

    for grade in grades:
        if grade >= 5:
            good = good + 1
        else:
            bad = bad + 1

    print("Задовільні оцінки:", good)
    print("Незадовільні оцінки:", bad)
else:
    print("Неправильний логін або пароль!")