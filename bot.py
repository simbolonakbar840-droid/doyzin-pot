import os
import json
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

DATA_FILE = "data.json"
def load():

    try:

        with open(DATA_FILE,"r",encoding="utf-8") as f:

            return json.load(f)

    except:

        return {}


def save():

    with open(DATA_FILE,"w",encoding="utf-8") as f:

        json.dump(

            groups,

            f,

            indent=4,

            ensure_ascii=False

        )

groups = {}

def get(chat_id):

    chat_id = str(chat_id)

    if chat_id not in groups:

        groups[chat_id] = {

            "d1":"-",
            "d2":"-",
            "d3":"-",
            "d4":"-",
            "final1":"?",
            "final2":"?",
            "winner":"?",
            "pay_photo":None,
            "welcome":"🎉 Selamat datang di DOYZIN STORE"

        }

    return groups[chat_id]


def bracket(chat_id):

    data = get(chat_id)

    return f"""
🏆 DOYZIN POT 🏆

━━━━━━━━━━

📊 SEMI FINAL

1️⃣ {data['d1']}
VS
{data['d2']}

2️⃣ {data['d3']}
VS
{data['d4']}

🔥 FINAL

🏆 {data['final1']} VS {data['final2']}

━━━━━━━━━━

🥇 PEMENANG

👑 {data['winner']}

━━━━━━━━━━
"""
    
    @bot.message_handler(commands=['pot'])
def pot(message):

    bot.send_message(

        message.chat.id,

        bracket(message.chat.id)

    )
    @bot.message_handler(commands=['d1'])
def d1(message):

    try:

        data = get(message.chat.id)

        data["d1"] = message.text.split(maxsplit=1)[1]

        save()

        bot.reply_to(

            message,

            "✅ D1 berhasil"

        )

    except:

        bot.reply_to(

            message,

            "/d1 @user"

        )
        @bot.message_handler(commands=['d2'])
def d2(message):

    try:

        data = get(message.chat.id)

        data["d2"] = message.text.split(maxsplit=1)[1]

        save()

        bot.reply_to(

            message,

            "✅ D2 berhasil"

        )

    except:

        bot.reply_to(

            message,

            "/d2 @user"

        )
        @bot.message_handler(commands=['d3'])
def d3(message):

    try:

        data = get(message.chat.id)

        data["d3"] = message.text.split(maxsplit=1)[1]

        save()

        bot.reply_to(

            message,

            "✅ D3 berhasil"

        )

    except:

        bot.reply_to(

            message,

            "/d3 @user"

        )
        @bot.message_handler(commands=['d4'])
def d4(message):

    try:

        data = get(message.chat.id)

        data["d4"] = message.text.split(maxsplit=1)[1]

        save()

        bot.reply_to(

            message,

            "✅ D4 berhasil"

        )

    except:

        bot.reply_to(

            message,

            "/d4 @user"

        )
        @bot.message_handler(commands=['final'])
def final(message):

    try:

        data = get(message.chat.id)

        args = message.text.split()

        data["final1"] = args[1]

        data["final2"] = args[2]

        save()

        bot.reply_to(

            message,

            "🔥 Final berhasil"

        )

    except:

        bot.reply_to(

            message,

            "/final @user1 @user2"

        )
        @bot.message_handler(commands=['winner'])
def winner(message):

    try:

        data = get(message.chat.id)

        data["winner"] = message.text.split()[1]

        save()

        bot.reply_to(

            message,

            "🏆 Pemenang disimpan"

        )

    except:

        bot.reply_to(

            message,

            "/winner @user"

        )
        @bot.message_handler(commands=['reset'])
def reset(message):

    chat_id = str(message.chat.id)

    groups[chat_id] = {

        "d1":"-",

        "d2":"-",

        "d3":"-",

        "d4":"-",

        "final1":"?",

        "final2":"?",

        "winner":"?",

        "pay_photo":None,

        "welcome":"🎉 Selamat datang di DOYZIN STORE"

    }

    save()

    bot.reply_to(

        message,

        "♻️ Bracket direset"

    )
    @bot.message_handler(commands=['setpay'])
def setpay(message):

    if message.reply_to_message:

        if message.reply_to_message.photo:

            data = get(message.chat.id)

            data["pay_photo"] = message.reply_to_message.photo[-1].file_id

            save()

            bot.reply_to(

                message,

                "✅ QR tersimpan"

            )

            return

    bot.reply_to(

        message,

        "Reply foto lalu /setpay"

    )
    @bot.message_handler(
func=lambda m:m.text and m.text.lower()=="pay")
def pay(message):

    data = get(message.chat.id)

    if data["pay_photo"]:

        bot.send_photo(

            message.chat.id,

            data["pay_photo"],

            caption="💳 PAYMENT DOYZIN"

        )

    else:

        bot.reply_to(

            message,

            "QR belum diatur"

        )
        @bot.message_handler(commands=['setwelcome'])
def setwelcome(message):

    text = message.text.replace(

        "/setwelcome",

        ""

    ).strip()

    if text:

        data = get(message.chat.id)

        data["welcome"] = text

        save()

        bot.reply_to(

            message,

            "✅ Welcome berhasil"

        )
        @bot.message_handler(commands=['setwelcome'])
def setwelcome(message):

    text = message.text.replace(

        "/setwelcome",

        ""

    ).strip()

    if text:

        data = get(message.chat.id)

        data["welcome"] = text

        save()

        bot.reply_to(

            message,

            "✅ Welcome berhasil"

        )
        print("DOYZIN POT ONLINE")

bot.infinity_polling()
