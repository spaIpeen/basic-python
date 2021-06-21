from requests import get

elk = get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")\
    .text.split("\n")
data = [(line.split(" ")[0], line.split(" ")[5][1:], line.split(" ")[6]) for line in elk if line]
print(data)
