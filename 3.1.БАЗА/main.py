# Функція для додавання нового відправлення в довідник
def add_mail(mail_list):
    new_mail = {}
    # Перевірка унікальності ID відправлення та того, що ID складається лише з цифр
    while True:
        new_mail["ID"] = input("Введіть унікальне ID відправлення (лише цифри): ")
        if new_mail["ID"].isdigit() and not any(mail["ID"] == new_mail["ID"] for mail in mail_list):
            break
        elif not new_mail["ID"].isdigit():
            print("ID повинен складатися лише з цифр. Спробуйте ще раз.")
        else:
            print(f"Відправлення з ID {new_mail['ID']} вже існує. Спробуйте ще раз.")

    # Введення інформації про відправлення
    new_mail["Відправник"] = input("Введіть ім'я відправника: ")
    new_mail["Одержувач"] = input("Введіть ім'я одержувача: ")
    new_mail["Адреса"] = input("Введіть адресу одержувача: ")
    # Перевірка коректності введення ваги відправлення
    while True:
        try:
            new_mail["Вага"] = float(input("Введіть вагу відправлення: "))
            break
        except ValueError:
            print("Будь ласка, введіть коректне число для ваги.")
    # Додавання нового відправлення до довідника
    mail_list.append(new_mail)

# Функція для видалення відправлення з довідника за ID
def delete_mail(mail_list):
    id_to_delete = input("Введіть ID відправлення для видалення: ")
    mail_to_delete = next((mail for mail in mail_list if mail["ID"] == id_to_delete), None)
    if mail_to_delete:
        mail_list.remove(mail_to_delete)
        print(f"Відправлення з ID {id_to_delete} успішно видалено.")
    else:
        print(f"Відправлення з ID {id_to_delete} не знайдено.")

# Функція для редагування відправлення в довіднику за ID
def edit_mail(mail_list):
    id_to_edit = input("Введіть ID відправлення для редагування: ")
    mail_to_edit = next((mail for mail in mail_list if mail["ID"] == id_to_edit), None)
    if mail_to_edit:
        field = input("Введіть поле для редагування (Відправник, Одержувач, Адреса, Вага): ")
        if field in mail_to_edit:
            new_value = input(f"Введіть нове значення для {field}: ")
            mail_to_edit[field] = new_value
            print(f"Відправлення з ID {id_to_edit} успішно відредаговано.")
        else:
            print(f"Поле {field} не знайдено.")
    else:
        print(f"Відправлення з ID {id_to_edit} не знайдено.")

# Функція для виведення інформації про всі відправлення в довіднику
def print_mail(mail_list):
    for mail in mail_list:
        for key, value in mail.items():
            print(f"{key}: {value}")
        print()

# Функція для знаходження відправлень з вагою більше заданого порогу
def find_heavy_mail(mail_list):
    weight_threshold = float(input("Введіть мінімальну вагу: "))
    heavy_mails = [mail for mail in mail_list if float(mail["Вага"]) > weight_threshold]
    if heavy_mails:
        print_mail(heavy_mails)
    else:
        print(f"Немає відправлень з вагою більше {weight_threshold}.")

# Функція для отримання коректного вибору користувача
def get_choice():
    while True:
        a = input("Дія: ")
        if a.isdigit():
            return int(a)
        else:
            print("Будь ласка, введіть ціле число.")

#----------------------------новинка----------------------------------------------
# Функція для збереження довідника до файлу
def save_file(mail_list, filename="Пошта.txt"):
    try:
        with open(filename, "w") as file:
            for mail in mail_list:  # Проходження по кожному запису в списку
                for key, value in mail.items():  # Проходження по ключам та значенням кожного запису
                    file.write(f"{key}: {value}\n")  # Запис пари ключ-значення в файл
                file.write("\n")  # Додавання порожнього рядка між записами
        print("Довідник успішно збережено у файлі:", filename)
    except IOError:
        print("Помилка: Неможливо записати у файл.")

# Функція для збереження довідника до файлу
def read_file(filename="Пошта.txt"):
    list = []  # Ініціалізуємо порожній список для збереження даних про пошту
    try:
        with open(filename, "r") as file:  # Відкриваємо файл для читання
            mail_data = file.read().split('\n\n')  # Розділяємо дані про пошту на окремі записи
            for mail_str in mail_data:
                if mail_str:  # Ігноруємо порожні записи
                    mail_info = {}  # Ініціалізуємо порожній словник для збереження даних про кожен запис
                    for item in mail_str.split('\n'):  # Розділяємо кожен запис на ключ та значення
                        key, value = item.split(': ', 1)  # Розділяємо рядок на ключ та значення
                        mail_info[key] = value  # Додаємо дані до словника
                    list.append(mail_info)  # Додаємо словник з даними про пошту до списку
        print("Довідник успішно завантажено з файлу:", filename)
    except FileNotFoundError:
        print("Файл не знайдено. Повертається порожній довідник.")
    except IOError:
        print("Помилка: Неможливо прочитати файл.")
    return list

mail_list = read_file()
while True:
    print("Меню")
    print("1. Додати відправлення")
    print("2. Видалити відправлення")
    print("3. Редагувати відправлення")
    print("4. Переглянути всі відправлення")
    print("5. Знайти відправлення з вагою більше N")
    print("0. Збереження довідника")

    choice = get_choice()

    if choice == 1:
        add_mail(mail_list)
    elif choice == 2:
        delete_mail(mail_list)
        save_file(mail_list)
    elif choice == 3:
        edit_mail(mail_list)
        save_file(mail_list)
    elif choice == 4:
        print_mail(mail_list)
    elif choice == 5:
        find_heavy_mail(mail_list)
    elif choice == 0:
        save_file(mail_list)
        break
    else:
        print("Невірний вибір.")
