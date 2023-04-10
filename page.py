from buttons import left_button, right_button, web_button
from helper import clean
from news import news, create_image, create_text


def page(n=0):
    clean()
    news_1 = news()
    create_image(news_1["articles"][n]['media'])
    create_text(news_1["articles"][n]['title'], news_1["articles"][n]['excerpt'])

    if n > 0:
        left_button(n)
    if n < 10:
        right_button(n)

    web_button(news_1['articles'][n]["link"])