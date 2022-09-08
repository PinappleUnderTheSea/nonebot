from nonebot.adapters.onebot.v11 import Message
from nonebot import on_command, on
import time
from nonebot.rule import to_me
import re

nowtime = on_command('现在几点了', aliases={"时间", "几点了"})


@nowtime.handle()
async def time_answer():
    await nowtime.finish('现在是' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), at_sender=True)


pafd = on("")


@pafd.handle()
async def paf():
    if re.search("00:00:00" , time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())):
        await pafd.finish(Message("pafd bot 提醒您 应该pafd了"), group_id="742601958")