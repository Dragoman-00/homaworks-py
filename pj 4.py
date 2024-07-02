def send_email(message, recipient, *, sender="university.help@gmail.com"):
    l1 = [".com", ".ru", ".net"]
    b = 0

    if ("@" in recipient) and ("@" in sender):
        for el1 in l1:
            for el2 in l1:
                if (el1 in recipient) and (el2 in sender):
                    b = b + 1
    if b == 0:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    else:
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


# send_email("123","university.help@gmail.com")
send_email("123", "asda@mail.net", sender="asda@mail.net")