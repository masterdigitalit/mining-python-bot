from create_bot import dp, bot


async def adminNotification(err, fileName):
    await bot.send_message(5273914742, f"error: {err},\nfileName: {fileName}")
