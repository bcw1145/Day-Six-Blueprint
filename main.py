from babel.numbers import format_currency
from country import get_countries, get_answer, get_countries_list, get_currency

url_company = "https://www.iban.com/currency-codes"
url_currency = "https://transferwise.com/gb/currency-converter"
countries = get_countries(url_company)
country_infos = []
get_countries_list(countries, country_infos)
code1, code2, money = get_answer(country_infos)
url_currency = url_currency + f"/{code1}-to-{code2}-rate?amount={money}"
currencied_money = get_currency(url_currency) * money
print(code1 + "{:0,.2f}".format(money) + " is " + format_currency(currencied_money, code2))
