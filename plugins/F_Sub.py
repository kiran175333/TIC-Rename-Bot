from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢 CLICK HERE TO JOIN 📢", url=client.invitelink) ]]
    text = "**SORRY DUDE YOU'VE NOT JOINED MY CHANNEL 😔\n\nPLEASE JOIN MY CHANNEL TO USE THIS BOT 🙏 **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



