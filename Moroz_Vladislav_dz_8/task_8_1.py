import re


def email_parse(email):
    info_dict = {"username": "".join(re.findall(r"([\w]+)@", email)),
                 "domain": "".join(re.findall(r"@([\w]+\.[\w]+)", email))}
    if info_dict["domain"] == "":
        raise ValueError("wrong email")
    print(info_dict)


email_parse("someone@geekbrains.ru")

