import telebot
from telebot import types

bot = telebot.TeleBot('7477324361:AAHKHaaEiRQccRS-L2KP5-am1NRodFQC8Bw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Инфо')
    btn2 = types.KeyboardButton('PP Recalculation')
    btn3 = types.KeyboardButton('kuuube\'s tablet guide')
    btn4 = types.KeyboardButton('osu-pps')
    btn5 = types.KeyboardButton('OpenTabletDriver')
    btn6 = types.KeyboardButton('Anti-Mindblock')
    btn7 = types.KeyboardButton('osuplus')
    btn8 = types.KeyboardButton('osr2mp4')
    btn9 = types.KeyboardButton('Mapset Verifier')
    btn10 = types.KeyboardButton('Mapping Tools')
    btn11 = types.KeyboardButton('osu trainer')
    btn12 = types.KeyboardButton('Rewind')
    markup.row(btn4, btn5, btn6, btn7)
    markup.add(btn8, btn9, btn10, btn11)
    markup.row(btn1, btn2, btn3, btn12)
    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text == 'Инфо':
        bot.send_message(message.chat.id, 'Этот бот был создан @Arfi1i\nЗдесь собраны различные материалы, ресурсы, сайты и софт для osu!')
    elif message.text == 'PP Recalculation':
        bot.send_message(message.chat.id, 'PP Recalculation - сайт, созданный Mr HeliX. С его помощью можно посмотреть, как повлияет грядущий пп-реворк на ваше количество пп и топ скоры. В первые часы после публичного объявления о реворке, очередь может занимать до 5 часов.\nСсылка - https://pp.huismetbenen.nl/rankings/players/live')
    elif message.text == 'kuuube\'s tablet guide':
        bot.send_message(message.chat.id, 'kuuube\'s tablet buying guide - Гугл документ от kuuube, где представлен большой список графических планшетов (ГП) и информация о них. Цена в долларах может отличаться от нынешней цены в рублях, так что цену понравившегося планшета стоит проверять самостоятельно.\nСсылка - https://docs.google.com/spreadsheets/d/1DYVfiSpQqdpa4sWWYUALPmliOIuGyKog7B7LJJdmlhE/edit?gid=2077726645#gid=2077726645')
    elif message.text == 'osu-pps':
        bot.send_message(message.chat.id,'osu-pps - Сайт, созданный СНГ игроком и маппером grumd. В нём собрано большинство самых ППшных карт и мапперов. Присутствуют фильтры, чтобы найти карту под свой скиллсет.\nСсылка - https://osu-pps.com/#/osu/maps')
    elif message.text == 'OpenTabletDriver':
        bot.send_message(message.chat.id, 'OpenTabletDriver - лучший драйвер для графические планшеты, созданный kuuuube, по крайней мере для osu!. Поддерживаются все базовые планшеты, используемые 99% осу игроков. Есть фильтры, позволяющие изменить задержку и уменьшить тряску курсора.\nСсылка - https://github.com/OpenTabletDriver/OpenTabletDriver')
    elif message.text == 'Anti-Mindblock':
        bot.send_message(message.chat.id, 'Anti-Mindblock - полезная программа от Shikkesora, которая действительно убирает майндблок путём программного переворота экрана.\nСсылка - https://github.com/ShikkesoraSIM/anti-mindblock\nГайд - https://youtu.be/ZVPWjgldezk?si=gIdtM3_HAGAYfFD3')
    elif message.text == 'osuplus':
        bot.send_message(message.chat.id, 'osuplus - Расширения для вебсайта osu!, созданное limjeck. Имеет огромную кучу полезных фич, одна из которых - показ топа 100 скоров, вместо топа 50. Полный список фич в гитхабе.\nСсылка - https://github.com/limjeck/osuplus')
    elif message.text == 'osr2mp4':
        bot.send_message(message.chat.id, 'osr2mp4 - Программа от yuitora, которая конвертирует реплей скора осу в видео.\nСсылка - https://github.com/uyitroa/osr2mp4-app')
    elif message.text == 'Mapset Verifier':
        bot.send_message(message.chat.id, 'Mapset Verifier - программа от Naxess для мапперов. Она сканирует карту и показывает ошибки, которые противоречат ранкинг критериям. Поможет приблизить вашу карту к становлению рейтинговой.\nСсылка - https://github.com/Naxesss/MapsetVerifier')
    elif message.text == 'Mapping Tools':
        bot.send_message(message.chat.id, 'Mapping Tools - программа от OliBomby, опять для мапперов. Имеет тонну полезных функций, помогающих для создания метадаты, хитсаундинга и самого маппинга.\nСсылка - https://github.com/OliBomby/Mapping_Tools')
    elif message.text == 'osu trainer':
        bot.send_message(message.chat.id, 'osu trainer - программа от FunOrange, которая позволяет создавать тренировочные диффы с кастомным бпм и характеристиками карты.\nСсылка - https://github.com/FunOrange/osu-trainer')
    elif message.text == 'Rewind':
        bot.send_message(message.chat.id, 'Rewind - программа от abstrakt. Считывает реплеи и воспроизводит их в приложении. Можно использовать как для анализирования своих скоров, так и для вычисления читеров.\nСсылка - https://github.com/abstrakt8/rewind')
bot.polling()

bot.polling(non_stop=True)