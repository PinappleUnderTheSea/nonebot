from nonebot import on_command, export
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent, Message, MessageSegment
from nonebot.typing import T_State
from nonebot.adapters import Bot
from nonebot import on_notice

export.name = '进群欢迎'
export.usage = '欢迎新人'

welcom = on_notice()


# 群友入群
@welcom.handle()  # 监听 welcom
async def h_r(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):  # event: GroupIncreaseNoticeEvent  群成员增加事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "本群通过祈愿召唤了水群怪：[CQ:at,qq={}]".format(user)
    msg = at_ + '欢迎水群：\n 不水不是技科人！'

    if event.group_id == 700258359 or event.group_id == 742601958:
        await welcom.send(message=Message(msg))  # 发送消息


# 群友退群
@welcom.handle()
async def h_r(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):  # event: GroupDecreaseNoticeEvent  群成员减少事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "[CQ:at,qq={}] ".format(user)
    msg = at_ + '完了完了怎么有人退群跑路了，在卷的各位都有责任'

    if event.group_id == 700258359 or event.group_id == 742601958:
        await welcom.send(message=Message(msg))  # 发送消息
