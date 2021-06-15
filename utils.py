import telebot as tl
from io import BytesIO
import matplotlib.pyplot as plt

default_companies = (('Microsoft', 'MSFT'), ('Apple', 'AAPL'), ('Amazon', 'AMZN'),
                     ('Google', 'GOOG'), ('Facebook', 'FB'), ('Tesla', 'TSLA'))


def get_byte_plot(data):
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    ax.set_ylabel('$USD$')
    ax.set_xlabel('$Date$')
    fig.suptitle('Dynamic since 2020')
    ax.grid()
    figure_file = BytesIO()
    fig.savefig(figure_file, format='jpg')
    return figure_file.getvalue()


def generate_keyboard(buttons=default_companies):
    keyboard = tl.types.InlineKeyboardMarkup()
    for key, value in buttons:
        keyboard.add(tl.types.InlineKeyboardButton(key, callback_data='$$' + value))
    return keyboard

