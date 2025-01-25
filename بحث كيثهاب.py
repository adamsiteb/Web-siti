"""
Developer :- @DF_GD_D 
Channel :- @T62RS 
In :- 2024/1/13
Remember My Source 
"""
import telebot, requests, os, sys, webbrowser 
from time import sleep 
from telebot import types
webbrowser.open('https://t.me/T62RS')
logo = ('''\033[2;36m
___
_   \   \_  _/_ |  / /    |  /  __/
  /_/ /_  /_/ /  /  | / /  /| |_  /    /
_  /_  _, _// /   |/ / _  _ |  /   _  /_
/_/     /_/ |_| /_/  _/  /_/  |_/_/    /___/

---------------------------------  
''')
print(logo)
print("Welcome Dear To The Views Bot By :- @DF_GD_D ")
token = "7830127201:AAFPtNWNtLzpnZ8GIBGlmeAA44r9Isb7JBA"
Private = telebot.TeleBot(token) 
is_bot_active = True 
A = types.InlineKeyboardMarkup(row_width=2)
Ch = types.InlineKeyboardButton(text ="𝘾𝙃𝘼𝙉𝙉𝙀𝙇" , url = "t.me/T62RS")
Dev = types.InlineKeyboardButton(text ="𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍" , url = "t.me/DF_GD_D")
A.add(Ch,Dev)
@Private.message_handler(commands=["start"])
def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("«〈 START 〉»", callback_data="search"))
    Private.send_photo(message.chat.id,"https://t.me/ifuwufuj/12",caption="""
↯︙ 👋 مرحباً بك عزيزي في بوت البحث عن الادوات والمشاريع العامة الموجودة في موقع (github.com) ارسل اسم الاداة او المستودع الذي تود في اظهار نتائج البحث الموجودة في المنصة 📩
---------------------------------  
📅 Welcome, dear to the search bot for tools and general projects on the (github.com) website, send the name of the tool or repository that you want to show the search results on the platform ⚖️ 
""", reply_markup=keyboard)
@Private.callback_query_handler(func=lambda call: True)
def callback_query_handler(call: types.CallbackQuery):
    if call.data == "search":
        Private.send_message(call.message.chat.id,"""
↯︙ الان قم بارسال اسم المستودع للبحث ✅
---------------------------------  
↯︙ Now send the name of the repository to search 🔖
""",parse_mode = "markdown" , reply_markup = A)
        Private.register_next_step_handler(call.message, search_repositories)
def GitHub(message: types.Message):
    Name = message.text
    url_aps = f"https://api.github.com/search/repositories?q={Name}&type=public"
    response = requests.get(url_aps)

    if response.status_code == 200:
        repos = response.json()["items"]
        if repos:
            Private.send_message(message.chat.id, f"ايجاد {len(repos)} مستودعات :")
            for repo in repos:
                Name = repo["full_name"]
                Urls = repo["html_url"]
                Private.send_message(message.chat.id, f"""↯︙ تم العثور على مستودعات متطابقة عزيزي
الاسم :- {Name} 👋
الرابط :- {Urls} 🌺""",parse_mode = "markdown" , reply_markup = A)
        else:
            Private.send_message(message.chat.id,"""
↯︙ لم يتم عثور مستودعات مطابقة لهذا الاسم تاكد من الاسم 🖲️
--------------------------------- 
↯︙ No repositories matching this name were found Check the name ❌
""",parse_mode = "markdown" , reply_markup = A)
    else:
        Private.send_message(message.chat.id,"ERROR : خطأ [❌] ",parse_mode = "markdown" , reply_markup = A)
private = "\033[2;32m Running... /start"
for char in private:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
Private.polling(True)
"""
Developer :- @DF_GD_D 
Channel :- @T62RS 
In :- 2024/1/13
Remember My Source 
"""