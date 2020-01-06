import requests
import sys

URL = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=47ED9FFEC08A39F65B2743F42CF3158A?date=03.01.2020'

res = requests.get(URL)

# print(res)
# print(type(res.text))
# print(res.text)
thecode = sys.argv[1]
lines = res.text.split("\n")[2:-1]
for l in lines:
    (country, currency, amount, code, rate) = l.split("|")
    if code == thecode:
        print("{} {} {}".format, country, amount, rate)


# v sys.argv[1] je kod meny
# vypise nazev statu a kurz ve formatu mnozstvi:kurz



