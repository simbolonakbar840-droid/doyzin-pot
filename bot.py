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
        json.dump(groups,f,indent=4,ensure_ascii=False)

groups = load()

global_rules = ""

global_done = ""


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
    "welcome":"🎉 Selamat datang di DOYZIN STORE",

}

    return groups[chat_id]


def bracket(chat_id):

    data = get(chat_id)

    return f"""
🏆 DOYZIN POT 🏆

━━━━━━━━━━

📊 SEMI FINAL

1️⃣ 
{data['d1']}
VS
{data['d2']}

2️⃣ 
{data['d3']}
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
    bot.send_message(message.chat.id, bracket(message.chat.id))


@bot.message_handler(commands=['d1'])
def d1(message):
    try:
        data = get(message.chat.id)
        data["d1"] = message.text.split(maxsplit=1)[1]
        save()
        bot.reply_to(message,"✅ D1 berhasil")
    except:
        bot.reply_to(message,"/d1 @user")


@bot.message_handler(commands=['d2'])
def d2(message):
    try:
        data = get(message.chat.id)
        data["d2"] = message.text.split(maxsplit=1)[1]
        save()
        bot.reply_to(message,"✅ D2 berhasil")
    except:
        bot.reply_to(message,"/d2 @user")


@bot.message_handler(commands=['d3'])
def d3(message):
    try:
        data = get(message.chat.id)
        data["d3"] = message.text.split(maxsplit=1)[1]
        save()
        bot.reply_to(message,"✅ D3 berhasil")
    except:
        bot.reply_to(message,"/d3 @user")


@bot.message_handler(commands=['d4'])
def d4(message):
    try:
        data = get(message.chat.id)
        data["d4"] = message.text.split(maxsplit=1)[1]
        save()
        bot.reply_to(message,"✅ D4 berhasil")
    except:
        bot.reply_to(message,"/d4 @user")


@bot.message_handler(commands=['final'])
def final(message):
    try:
        data = get(message.chat.id)
        args = message.text.split()
        data["final1"] = args[1]
        data["final2"] = args[2]
        save()
        bot.reply_to(message,"🔥 Final berhasil")
    except:
        bot.reply_to(message,"/final @user1 @user2")


@bot.message_handler(commands=['winner'])
def winner(message):
    try:
        data = get(message.chat.id)
        data["winner"] = message.text.split()[1]
        save()
        bot.reply_to(message,"🏆 Winner disimpan")
    except:
        bot.reply_to(message,"/winner @user")

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
    bot.reply_to(message,"♻️ Reset berhasil")

@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):

    data = get(message.chat.id)

    for user in message.new_chat_members:

        bot.send_message(
            message.chat.id,
            data.get("welcome", "")
        )

@bot.message_handler(commands=['setwelcome'])
def setwelcome(message):

    text = message.text.replace("/setwelcome","").strip()

    if text:

        data = get(message.chat.id)

        data["welcome"] = text

        save()

        bot.reply_to(message,"✅ Welcome disimpan")

    else:

        bot.reply_to(message,"/setwelcome pesan")

@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(
        message,
        """🏆 DOYZIN POT AKTIF

Gunakan:
/pot
/help
/rules
/pay"""
    )

@bot.message_handler(commands=['help'])
def help(message):

    bot.reply_to(
        message,
        """
🏆 DOYZIN POT

/pot
/d1
/d2
/d3
/d4

/final
/winner
/reset

/setpay
pay

/setwelcome
/setrules
/rules
"""
    )

@bot.message_handler(commands=['setrules'])
def setrules(message):

    global global_rules

    if message.reply_to_message:

        if message.reply_to_message.text:

            global_rules = message.reply_to_message.text

            bot.reply_to(
                message,
                "✅ Rules berhasil disimpan"
            )

        else:

            bot.reply_to(
                message,
                "Reply pesan teks rules lalu /setrules"
            )

    else:

        bot.reply_to(
            message,
            "Reply pesan rules lalu /setrules"
        )

@bot.message_handler(commands=['rules'])
def rules(message):

    if global_rules:

        bot.send_message(

            message.chat.id,

            global_rules

        )

    else:

        bot.reply_to(

            message,

            "Rules belum diatur"

        )

@bot.message_handler(commands=['setdone'])
def setdone(message):

    global global_done

    if message.reply_to_message:

        if message.reply_to_message.text:

            global_done = message.reply_to_message.text

            bot.reply_to(

                message,

                "✅ Done berhasil disimpan"

            )

        else:

            bot.reply_to(

                message,

                "Reply pesan teks lalu /setdone"

            )

    else:

        bot.reply_to(

            message,

            "Reply pesan done lalu /setdone"

        )

@bot.message_handler(commands=['done'])
def done(message):

    if global_done:

        bot.send_message(

            message.chat.id,

            global_done

        )

    else:

        bot.reply_to(

            message,

            "Done belum diatur"

        )



print("DOYZIN POT ONLINE")

bot.infinity_polling()




