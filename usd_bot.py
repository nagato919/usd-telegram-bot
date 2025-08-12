import logging
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔐 Thay bằng token bot của bạn
API_TOKEN = '8152476058:AAHiWJ071f2T8nGuSqy25wJkBwbVXO8KHRo'

# ⚙️ Khởi tạo bot và dispatcher
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 📈 Hàm lấy giá USD từ Google Finance
def get_usd_rate_google():
    try:
        url = "https://www.google.com/finance/quote/USD-VND?hl=vi"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm phần chứa tỷ giá USD/VND
        price_tag = soup.find("div", {"class": "YMlKec fxKbKc"})
        if price_tag:
            rate = price_tag.text.strip().replace(",", "")
            return f"💵 Giá USD hôm nay:\n1 USD = {rate} VND\n(Nguồn: Google Finance)"
        else:
            return "⚠️ Không tìm thấy tỷ giá USD trên Google Finance."
    except Exception as e:
        return f"⚠️ Lỗi khi lấy dữ liệu: {e}"

# 📲 Xử lý lệnh /giado
@dp.message_handler(commands=['giado'])
async def send_usd_price(message: types.Message):
    usd_info = get_usd_rate_google()
    await message.reply(usd_info)

# ▶️ Khởi chạy bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
