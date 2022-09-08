from nonebot.rule import to_me
from nonebot.adapters import Message,Event
from nonebot.params import CommandArg
from nonebot.plugin import on_command
import re
import random

echo = on_command("", to_me())
# echo = on_command("")


@echo.handle()
async def echo_escape(event: Event, message: Message = CommandArg()):
    if re.search('狗叫', message.__str__()):
        ans = ['你cue你爹干嘛', '我建议不要狗叫']
        a = random.randint(0, len(ans)-1)
        stri = ans[a]
        await echo.send(message=stri)
    # else:
    #     await echo.send(message=message)
