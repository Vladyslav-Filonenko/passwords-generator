from secrets import choice
from random import shuffle
from string import digits, ascii_uppercase, ascii_lowercase, punctuation

DIGITS = digits
UPPERCASE = ascii_uppercase
LOWERCASE = ascii_lowercase
SYMBOLS = punctuation

cnt_psw = int(input("Введите желаемое количество паролей: "))
len_pw = int(input("Введите желаемую длину одного пароля: "))
file_save = (
    input("Хотите ли вы сохранить пароли в файл (passwords.txt?) (y/n): ")
    .strip()
    .lower()
)


options = {
    "Включать цифры?": DIGITS,
    "Включать прописные": UPPERCASE,
    "Включать строчные": LOWERCASE,
    "Включать символы": SYMBOLS,
}
chars = []
for question, charset in options.items():
    if input(f"{question} (y/n): ").strip().lower() == "y":
        chars.append(charset)

if not chars:
    print("Ошибка: не выбран ни один вид символов!")
    exit()

if len(chars) > len_pw:
    raise ValueError(
        f"Выбранная длина пароля - {len_pw}, и она меньше выбраных типов - {len(chars)}. Длина пароля должна быть больше или равна количеству типов"
    )


def make_password(len_pw, chars):
    password = []
    for i in chars:
        password.append(choice(i))
    if len_pw > len(chars):
        for i in range(len_pw - len(chars)):
            password.append(choice("".join(chars)))
    shuffle(password)
    return "".join(password)


if file_save == "y":
    ques_pass = (
        input(
            "Вы хотите записать новый файл или дополнить уже существующий? (new/old): "
        )
        .strip()
        .lower()
    )
    with open("passwords.txt", {"new": "w", "old": "a"}[ques_pass]) as file:
        for _ in range(cnt_psw):
            password = make_password(len_pw, chars)
            file.write(password + "\n")
    print("Пароли успешно созданы и сохранены в файл passwords.txt")
else:
    for _ in range(cnt_psw):
        print(make_password(len_pw, chars))
