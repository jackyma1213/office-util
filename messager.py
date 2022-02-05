from telethon import TelegramClient

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345678
api_hash = 'asdasdasdasdasdasdasdasdasdasd'
phone_num = '+85212345678'

class Messager:

    async def __create(self):
        self.__client = TelegramClient('session_name', api_id, api_hash)
        await self.__client.start(phone_num)

    async def sendMessage(self,targets,msg):
        await self.__create()

        for idx in range(len(targets)):
            await self.__client.send_message( targets[idx]["username"], msg)

        await self.__client.disconnect()
