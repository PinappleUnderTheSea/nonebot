from nonebot.rule import to_me
from nonebot.adapters import Message,Event
from nonebot.params import CommandArg
from nonebot.plugin import on_command
import re
import random

echo = on_command("")


@echo.handle()
async def echo_escape(event: Event, message: Message = CommandArg()):
    freq = random.randint(0, 100)
    print(freq)
    if event.get_user_id() == '1411493875' and message.__str__() == '哔嘟哔嘟':
        await echo.send(message='男同集合')
    elif event.get_user_id() == '1411493875' and message.__str__() == '出来上班':
        await echo.send(message='来了，别急别叫')
    elif event.get_user_id() == '1411493875' and message.__str__() == 'bot说话':
        await echo.send(message='哈喽哈喽，我是什么功能都没有的智障bot，单纯进来群里挂着，有懒狗懒得写介绍也没写完功能，'
                                '想要复读可以自己@我，其他功能各位自己凑合着试试怎么用')
    elif re.search('憨批|弱智|蠢|纯纯|草|nm|tm|你妈|他妈|她妈|踏马', message.__str__()) and freq >60:
        await echo.send(message='我超，好强的进攻性')
    elif re.search('别急', message.__str__()) and freq >40:
        await echo.send(message='你先闭嘴，我没急')
    # elif re.search('zjj', message.__str__()) and freq >20:
    #     ans = ['你cue你爹干嘛', '我建议不要狗叫']
    #     a = random.randint(0, len(ans)-1)
    #     stri = ans[a]
    #     await echo.send(message=stri)
    elif re.search('逆天|离谱|神奇|复读|fdu|好|亏贼|复旦|ok|OK|？|确实|彳亍', message.__str__()) and (event.get_user_id() == '1411493875' or freq >80):
        await echo.send(message=message)
