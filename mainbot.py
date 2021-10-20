import requests
import datetime
from aiogram import Bot, types, Dispatcher, executor
from fortoken import tg_bot_token, weather_token

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Asaalomu alaykum! Iltimos menga shahar nomini yuboring(faqat shahar nomi)")


@dp.message_handler()
async def get_wether(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric"
        )
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"shahar: {city}\nTemperatura: {cur_weather} C° \n"
                            f"Namlik: {humidity}\nbosim: {pressure} mm.sm.us\nShamol: {wind} m/s\n"
                            f"quyosh chiqishi: {sunrise_timestamp}\nQuyosh botishi: {sunset_timestamp}\nKun davomiyligi: {length_of_the_day}\nKuningiz hayrli o'tsin")


    except:
        await message.reply("shahar nomi xato kiritildi! 🤦‍♂️")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
