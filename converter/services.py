import requests

from config.settings import API_ACCESS_TOKEN

TOKEN = API_ACCESS_TOKEN

def get_current_currency(cur_from, cur_to) -> list:
    """
    Запрос о текущем курсе с сайта https://fixer.io
    """

    url = f"http://data.fixer.io/api/latest?access_key={TOKEN}&base={cur_from}&symbols={cur_to}"
    response = requests.get(url)
    return response.json()["rates"][cur_to]
