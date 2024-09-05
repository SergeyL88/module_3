def check_mail(mail: str) -> bool:
    is_contain: bool = False
    must_contain: list = ['.com', '.ru', '.net']
    for chars in must_contain:
        if chars.lower() in mail.lower() and '@' in mail:
            is_contain = True
            break
    
    return is_contain


def send_email(message: str, recipient: str, sender: str = 'university.help@gmail.com'):
    if check_mail(sender) and check_mail(recipient):
        if sender.lower() == recipient.lower():
            print("Нельзя отправить письмо самому себе!")
        elif sender.lower() == 'university.help@gmail.com':
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
