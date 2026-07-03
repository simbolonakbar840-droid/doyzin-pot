import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

d1 = "-"
d2 = "-"
d3 = "-"
d4 = "-"

final1 = "?"
final2 = "?"

winner = "?"

pay_photo = None

welcome_text = "🎉 Selamat datang di DOYZIN STORE"


def bracket():

    return f"""
POTDOYZIN

🏆 DOYZIN POT 🏆

━━━━━━━━━━

📊 BRACKET TURNAMEN

🔴 SEMI FINAL

1️⃣ 
{d1}
VS
{d2}

2️⃣ 
{d3}
VS
{d4}

🔥 FINAL

🏆 {final1} VS {final2}

━━━━━━━━━━

🥇 PEMENANG

👑 {winner}

━━━━━━━━━━
"""


@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(
        message,
        "🏆 DOYZIN POT PREMIUM AKTIF"
    )


@bot.message_handler(commands=['help'])
def help(message):

    txt = """
/pot

/d1 @user
/d2 @user
/d3 @user
/d4 @user

/aoa @user1 @user2

/final @user

/reset

/setpay

pay

/setwelcome pesan
"""

    bot.reply_to(message, txt)


@bot.message_handler(commands=['pot'])
def pot(message):

    bot.send_message(
        message.chat.id,
        bracket()
    )


@bot.message_handler(commands=['d1'])
def cmd_d1(message):

    global d1

    try:

        d1 = message.text.split(maxsplit=1)[1]

        bot.reply_to(message, "✅ D1 berhasil")

    except:

        bot.reply_to(message, "/d1 @user")


@bot.message_handler(commands=['d2'])
def cmd_d2(message):

    global d2

    try:

        d2 = message.text.split(maxsplit=1)[1]

        bot.reply_to(message, "✅ D2 berhasil")

    except:

        bot.reply_to(message, "/d2 @user")


@bot.message_handler(commands=['d3'])
def cmd_d3(message):

    global d3

    try:

        d3 = message.text.split(maxsplit=1)[1]

        bot.reply_to(message, "✅ D3 berhasil")

    except:

        bot.reply_to(message, "/d3 @user")


@bot.message_handler(commands=['d4'])
def cmd_d4(message):

    global d4

    try:

        d4 = message.text.split(maxsplit=1)[1]

        bot.reply_to(message, "✅ D4 berhasil")

    except:

        bot.reply_to(message, "/d4 @user")


@bot.message_handler(commands=['aoa'])
def aoa(message):

    global final1
    global final2

    try:

        data = message.text.split()

        final1 = data[1]
        final2 = data[2]

        bot.reply_to(
            message,
            "🔥 Final berhasil diatur"
        )

    except:

        bot.reply_to(
            message,
            "/aoa @user1 @user2"
        )


@bot.message_handler(commands=['final'])
def final(message):

    global winner

    try:

        winner = message.text.split()[1]

        bot.reply_to(
            message,
            "🏆 Pemenang disimpan"
        )

    except:

        bot.reply_to(
            message,
            "/final @user"
        )


@bot.message_handler(commands=['reset'])
def reset(message):

    global d1
    global d2
    global d3
    global d4

    global final1
    global final2

    global winner

    d1="-"
    d2="-"
    d3="-"
    d4="-"

    final1="?"
    final2="?"

    winner="?"

    bot.reply_to(
        message,
        "♻️ Bracket direset"
    )


@bot.message_handler(commands=['setpay'])
def setpay(message):

    global pay_photo

    if message.reply_to_message:

        if message.reply_to_message.photo:

            pay_photo = message.reply_to_message.photo[-1].file_id

            bot.reply_to(
                message,
                "✅ QR pembayaran tersimpan"
            )

            return

    bot.reply_to(
        message,
        "Reply foto QR lalu ketik /setpay"
    )


@bot.message_handler(func=lambda m: m.text and m.text.lower()=="pay")
def pay(message):

    if pay_photo:

        bot.send_photo(

            message.chat.id,

            pay_photo,

            caption="💳 QR PAYMENT DOYZIN"

        )

    else:

        bot.reply_to(

            message,

            "QR belum diatur"

        )


@bot.message_handler(commands=['setwelcome'])
def setwelcome(message):

    global welcome_text

    text = message.text.replace(

        "/setwelcome",

        ""

    ).strip()

    if text:

        welcome_text = text

        bot.reply_to(

            message,

            "✅ Welcome berhasil diubah"

        )

    else:

        bot.reply_to(

            message,

            "/setwelcome pesan"

        )


@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):

    for user in message.new_chat_members:

        bot.send_message(

            message.chat.id,

            f"👋 {user.first_name}\n\n{welcome_text}"

        )


print("DOYZIN POT PREMIUM ONLINE")

bot.infinity_polling()
