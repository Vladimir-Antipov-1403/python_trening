from task_9_checks import Checks

class Button1(Checks):
    pass

class Button2(Checks):
    pass

class Button3(Checks):
    pass

class Button4(Checks):
    pass


# Создаём объекты
btn1 = Button1("Кнопка 1")
btn2 = Button2("Кнопка 2")
btn3 = Button3("Кнопка 3")
btn4 = Button4("Кнопка 4")

# Выводим результаты check_text()
for btn in (btn1, btn2, btn3, btn4):
    print(btn.check_text())
