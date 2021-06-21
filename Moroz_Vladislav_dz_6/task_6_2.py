from requests import get

elk = get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")\
    .text.split("\n")
data, count, ip = {}, 0, 0
for line in elk:
    if line:
        if line.split(" ")[0] not in data:
            data[line.split(" ")[0]] = 1
        else:
            data[line.split(" ")[0]] += 1
for i, k in data.items():
    if k > count:
        ip, count = i, k
print(ip, count)
