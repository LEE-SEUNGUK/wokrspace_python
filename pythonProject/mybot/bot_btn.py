#pip install python-telegram-bot==13.11
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time
import os
API_KEY = '7452924556:AAF6nsJ0J823mT_Cu0m3uXTZqbfTpVz3Xto'
updater = Updater(token=API_KEY, use_context=True)

def show_btn(update, context):
    keyboard = [
        [InlineKeyboardButton("시작!", callback_data='1'),
         InlineKeyboardButton("종료!", callback_data='2')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    # 메시지와 버튼 보내기
    update.message.reply_text('선택 하세요!:', reply_markup=reply_markup)

def btn_event(update, context):
    query = update.callback_query
    query.answer(text='선택 확인!!') # 알림창
    # 선택버튼 응답
    query.edit_message_text(text = f'선택 값은{query.data}')
updater.dispatcher.add_handler(CommandHandler('stock', show_btn))
updater.dispatcher.add_handler(CallbackQueryHandler(btn_event))
updater.start_polling()
updater.idle()