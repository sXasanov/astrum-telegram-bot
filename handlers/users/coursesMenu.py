from aiogram import types
from loader import dp


@dp.message_handler(text="👨‍💻Full-stack")
async def fullst(msg: types.Message):
    text = "🇺🇿Full-Stack Development - bu veb-ishlab chiqishning ikki jihatini o'z ichiga oladi.\n1. Sayt yoki veb-ilovaning ko'rinishi.  Foydalanuvchi saytga kirganda birinchi  ko'radidan narsasi (Frontend)\n2. Sayt yoki veb-ilovaning mantig'i.  Foydalanuvchining ko'zidan yashiringan narsa.  Serverda turli xil ma'lumotlarni qayta ishlash va foydalanuvchiga ko'rsatish (Backend)"
    text += "Umuman olganda bu Full-Stack Development va bu ko'nikmalarga ega bo'lgan kishi - FullStack Developer.\n\n"

    text += "Astrum, Yangi avlod IT akademiyasida Full-stack Development kurslari.\n\n"

    text += "🇷🇺Full Stack Development - включает в себя два аспекта веб разработки. \n"
    text += "1. Внешний вид сайта или веб приложения. То что видит пользователь в первую очередь при посещении сайта(Frontend)\n"
    text += "2. Логика сайта или веб приложения. То что скрыто от глаз пользователя. Обработка различных данных на сервере и отображение их пользователю(Backend) \n"
    text += "В совокупности - это FullStack Development, а человек который владеет этими навыками - FullStack Developer. \n \n"

    text += "Курсы Full-stack development в Аструм, IT Академия нового поколения.\n"
    await msg.answer_photo(photo='AgACAgIAAxkBAAICNmR56WHLiTjLtmOFe9eqeK4Ic1QMAAIL0DEbsrXRS_tYJcULqP9SAQADAgADeAADLwQ')
    await msg.answer(text)

@dp.message_handler(text="🤖Software Engineering")
async def soft(msg: types.Message):
    text = "🇺🇿 Software engineering - bu boshqaruv panellaridan tortib kompyuter tizimlarigacha bo’lgan keng doira dasturiy ta'minotlarni yaratish.\n"
    text += "Software engineering - bu shunday mutaxassiski, uning vazifalari quydagilardan iborat bo’lishi mumkin:\n"
    text += "- dasturiy ta'minotni proyekti;\n"
    text += "- dasturiy ta'minotni rivojlantirish\n;"
    text += "- dasturiy ta'minotga texnik xizmat ko'rsatish;\n"
    text += "- dasturiy ta'minotni sinovdan o'tkazish;\n"
    text += "- dasturiy ta'minotni baholash.\n\n"

    text += "🇬🇧 Software engineering is a wide range of software development: from control panels to computer systems.\n"
    text += "Software engineer is a specialist who deals with:\n"
    text += "- software design;\n"
    text += "- software development;\n"
    text += "- software maintenance;\n"
    text += "- software testing;\n"
    text += "- software evaluation.\n"

    await msg.answer(text)


@dp.message_handler(text="⚙️Data Science")
async def datasc(msg: types.Message):

    text = " Data Science:\n"
    text += "Preseason Data Science:\n"
    text += "- Python dasturlash tilini o'zlashtirish\n"
    text += "- ma'lumotlarni tahlil qilish yo’nalishi bilan tanisais\n "
    text += "- web.scrapping bilan tanishish\n"
    text += "Season Data Science:\n"
    text += "- Data Sience yo’nalishini chuqur o’rganish\n"
    text += "- Jupiter Lab bilan ishlash\n"
    text += "- ma'lumotlarni vizualizatsiya qilish\n"
    text += "- web.scapping yordamida to'plangan ma'lumotlar asosida CSV fayllarini yaratish\n"
    text += "- Pythonda ob'ektga yo'naltirilgan dasturlash\n"
    text += "- NumPYni o'zlashtirish\n"
    text += "- Pandasni o'zlashtirish\n"
    text += "- Matplotlib kutubxonasini o'zlashtirish\n"
    text += "- SQLni o'rganish\n"


    await msg.answer(text)
