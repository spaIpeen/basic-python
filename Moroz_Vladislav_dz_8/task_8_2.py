import re
from requests import get


def email_parse(log_str):
    data = re.findall(r"(?:\w\d{0,4}[.:]){3}\d{1,3}", log_str)[0],\
         re.findall(r"([\[][\w/:+\s]+[]])", log_str)[0][1:-1],\
         re.findall(r"([\"][\w\s]+[/])", log_str)[0][1:-2],\
         re.findall(r"([/][\w/]+_\d)", log_str)[0],\
         re.findall(r"\s\d{3}\s", log_str)[0][1:-1],\
         re.findall(r"\d{1,10}\s[\"]", log_str)[0][0:-2]
    print(data)


temp = get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")\
    .text.split("\n")
parsed = (email_parse(line) for line in temp if line and line != "")
next(*parsed)

