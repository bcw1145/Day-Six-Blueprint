import os
import requests
from bs4 import BeautifulSoup


def get_countries(url):
    os.system("clear")
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    return soup.find_all("tr")


def get_name_code(country):
    try:
        name, currency, code, num = country.find_all("td")
        if currency.get_text() == 'No universal currency':
            pass
        else:
            return {"name": name.get_text(), "code": code.get_text()}

    except:
        pass


def get_countries_list(countries, country_infos):
    for country in countries:
        country_info = get_name_code(country)
        if country_info:
            country_infos.append(country_info)

    print("Welcome to CurrencyConvert PRO2000")
    for num in range(len(country_infos)):
        print(f"# {num} {country_infos[num]['name']}")


def get_answer(country_infos):
    print("Where are you from? Choose a country by number", end='\n\n')
    a = input("#: ")
    try:
        num1 = int(a)
    except ValueError:
        print("That wasn't a number.")
        return get_answer(country_infos)

    if num1 > len(country_infos):
        print("Choose a number from a list.")
        return get_answer(country_infos)
    else:
        print(f"{country_infos[num1]['name']}", end='\n\n')
        num2 = get_answer2(country_infos)
        str_convert = (
            f"How many {country_infos[num1]['code']} do you want to convert to {country_infos[num2]['code']}?"
        )
        print(str_convert)
        num3 = get_answer3(str_convert)
        return country_infos[num1]['code'], country_infos[num2]['code'], num3


def get_answer2(country_infos):
    print("Now choose another country", end='\n\n')
    try:
        num = int(input("#: "))
        if num > len(country_infos):
            print("Choose a number from a list.")
            return get_answer2(country_infos)
        else:
            print(f"{country_infos[num]['name']}", end='\n\n')
            return num
    except ValueError:
        print("That wasn't a number.")
        return get_answer2(country_infos)


def get_answer3(str1):
    try:
        num = float(input("#: "))
        return num
    except :
        print("That wasn't a number.",end='\n\n')
        print(str1)
        return get_answer3(str1)


def get_currency(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    return float(soup.find("span", class_="text-success").text)
