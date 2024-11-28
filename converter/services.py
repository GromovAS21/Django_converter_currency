import requests

from config.settings import API_ACCESS_TOKEN

TOKEN = API_ACCESS_TOKEN

def get_current_currency(cur_from, cur_to) -> list | int:
    """
    Запрос о текущем курсе с сайта https://fixer.io
    """

    url = f"http://data.fixer.io/api/latest?access_key={TOKEN}&base={cur_from.upper()}&symbols={cur_to.upper()}"
    response = requests.get(url)
    try:
        result = response.json()["rates"][cur_to.upper()]
    except KeyError:
        return 0
    return result
