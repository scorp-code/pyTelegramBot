import requests
from telegram import KeyboardButton, ReplyKeyboardMarkup


def btn_val(page=None):
    button = []
    url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'
    res = requests.get(url).json()

    if page:
        for i in range(page, page+8, 3):
            a = res[i]
            button.append([KeyboardButton(f"{a['CcyNm_UZ']} ({a['Ccy']})"),
                           KeyboardButton(f"{res[i + 1]['CcyNm_UZ']} ({res[i + 1]['Ccy']})"),
                           KeyboardButton(f"{res[i + 2]['CcyNm_UZ']} ({res[i + 2]['Ccy']})")], )
    else:
        for i in range(0, 9, 3):
            a = res[i]
            button.append([KeyboardButton(f"{a['CcyNm_UZ']} ({a['Ccy']})"),
                           KeyboardButton(f"{res[i + 1]['CcyNm_UZ']} ({res[i + 1]['Ccy']})"),
                           KeyboardButton(f"{res[i + 2]['CcyNm_UZ']} ({res[i + 2]['Ccy']})")], )

    button.append([KeyboardButton('⬅back'), KeyboardButton('next➡')])
    return ReplyKeyboardMarkup(button, resize_keyboard=True)


def valyuta(ccy):
    url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'
    res = requests.get(url).json()

    for i in res:
        if i['Ccy'] == ccy:
            return i

