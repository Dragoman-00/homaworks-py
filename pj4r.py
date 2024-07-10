def send_email(message, recipient, *, sender="university.help@gmail.com"):
    domains = (".com", ".net", ".ru")
    if ("@" in recipient and "@" in sender and recipient.endswith(domains) and
            sender.endswith(domains)):
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)


# send_email("123","university.help@gmail.com")
send_email("123", "asda@mail.com", sender="asda@mail.net")