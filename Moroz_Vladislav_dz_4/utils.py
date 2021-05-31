from requests import get
import datetime


def currency_rates(val):
    val = "".join(val)
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("><")
    course, user = 0, ""
    for line in response:
        if line.find(val.upper()) != -1:
            course = float(response[response.index(line)+3][6:13].replace(",", "."))
        elif line.find("Date") != -1:
            day, month, year = line[line.index('"') + 1: line.index('"') + 11].split(".")
            user = datetime.date(year=int(year), month=int(month), day=int(day))
    if course != 0:
        print(f"{course:.2f}, {user}")
    else:
        print("None")
