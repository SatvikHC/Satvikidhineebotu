from pyrogram import filters
from bot import app, data, sudo_users, LOG_CHANNEL
from bot.helper.function import change_ffmpeg, get_ffmpeg, movie_mode, anime_mode, upload_handle
from bot.helper.utils import add_task
from bot.helper.devtools import exec_message_f , eval_message_f
from bot.helper.ffmpeg_utils import startup, LOGGER, sample_gen
import asyncio
import traceback
import time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

video_mimetype = [
  "video/x-flv",
  "video/mp4",
  "application/x-mpegURL",
  "video/MP2T",
  "video/3gpp",
  "video/quicktime",
  "video/x-msvideo",
  "video/x-ms-wmv",
  "video/x-matroska",
  "video/webm",
  "video/x-m4v",
  "video/quicktime",
  "video/mpeg"
  ]


@app.on_message(filters.incoming & filters.command(["cmds", "cmd", "commands"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    await message.reply_text(f"Hi {message.from_user.mention()}\n**•The List Of Commands Are As Follows -:**\n•```/start```**- To Start The Bot\n**•```/cmds```**-To Repeat This List**\n•**Maintained By @FIERCE_TOONS**")

@app.on_message(filters.incoming & filters.command(["start", "help"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    REXT = f"Hi {message.from_user.mention()}\n**•I can Encode Telegram files And Send Sample (Especially Movies,Animes), just send me a video.**\n**•This Bot is Developed by @NIRUSAKI_AYEDAEMON**\n**•Simple, Easy and Convenient to use**\n**Thanks**"
    await app.send_message(
        chat_id=message.chat.id,
        text=REXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Join Anixpo', url='https://t.me/AniXpo')
                ]
            ]
        ),
        reply_to_message_id=message.id,
    )
@app.on_message(filters.incoming & (filters.video | filters.document))
async def encode_video(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    if message.document:
      if not message.document.mime_type in video_mimetype:
        await message.reply_text("**Send Any Video File**", quote=True)
        return
    a = await message.reply_text("**Added To Queue Please Wait...**", quote=True)
    data.append(message)
    if len(data) == 1:
     await a.delete()
     await add_task(message)
     time.sleep(1.8)
    
@app.on_message(filters.incoming & filters.command(["execute", "exec", "bash"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await exec_message_f(app, message)
    
@app.on_message(filters.incoming & filters.command(["eval", "py", "evaluate"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await eval_message_f(app, message)    
    
@app.on_message(filters.incoming & filters.command(["sample", "cut", "simp"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await sample_gen(app, message)
    
@app.on_message(filters.incoming & filters.command(["ffmpeg", "setc", "setcode"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await change_ffmpeg(app, message)
    
    
@app.on_message(filters.incoming & filters.command(["getcode"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await get_ffmpeg(app, message)

@app.on_message(filters.incoming & filters.command(["Movie"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await movie_mode(app, message)  

@app.on_message(filters.incoming & filters.command(["Anime"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await anime_mode(app, message)  

@app.on_message(filters.incoming & filters.command(["logs", "log"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    await app.send_document(chat_id=message.chat.id, reply_to_message_id=message.id, force_document=True, document="Encoder@Log.txt")
    
@app.on_message(filters.incoming & filters.command(["ulmode"]))
async def help_message(app, message):
    if message.chat.id not in sudo_users:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    await upload_mode(app, message):
    
    
##Run App
app.loop.run_until_complete(startup())
app.run()
