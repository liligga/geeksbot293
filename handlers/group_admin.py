from aiogram import types


async def example(message: types.Message):
    userid = message.from_user.id
    id = message.from_id
    chat = message.chat.type
    await message.answer(f"{userid=} {id=} {chat=}")
    if chat != 'private':
        # проверка явл ли автор сообщения админом
        admins = await message.chat.get_administrators()
        for admin in admins:
            if userid == admin['user']['id']:
                await message.answer("Да, шеф")
                break
        await message.answer(admins)

        is_reply = message.reply_to_message
        # None
        # types.Message
        if is_reply:
            await message.answer(is_reply)
        else:
            await message.answer("Не реплай")


async def check_admin(message: types.Message):
    member = await message.chat.get_member(
        message.from_user.id
    )
    return member['status'] != 'member'


async def check_words(message: types.Message):
    BAD_WORDS = ('плохой', 'дурак')
    text = message.text.lower().strip().replace(' ', '')
    is_admin = await check_admin(message)
    if not is_admin:
        for w in BAD_WORDS:
            if w in text:
                await message.reply("Нельзя такое писать")
                await message.delete()
                break


async def pin_message(message: types.Message):
    is_admin = await check_admin(message)
    if is_admin and message.reply_to_message:
        await message.reply_to_message.pin()


async def ban_user(message: types.Message):
    if message.reply_to_message:
        is_admin = await check_admin(message.reply_to_message)
        if not is_admin:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
            await message.answer(f"Пользователь {message.reply_to_message.from_user.username} был забанен")


def get_mentions(message: types.Message):
    entities = message.entities
    print(entities)
    return list(filter(lambda e: e['type']=='mention' , entities))


async def check_mention(message: types.Message):
    mentions = get_mentions(message)
    

def register_admin_handlers(dp):
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix="!")
    dp.register_message_handler(ban_user, commands=["ban"], commands_prefix="!")
    dp.register_message_handler(check_mention)

