from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.onebot.v11 import Event

weather = on_command("问", rule=to_me(), aliases={"提问", "求问"}, priority=5)

QA = {"你什么成分": "纯憨批"}


@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你讲")
async def handle_city(event: Event, city: Message = Arg(), city_name: str = ArgPlainText("city")):
    if city_name not in QA:  # 如果参数不符合要求，则提示用户重新输入
        # 可以使用平台的 Message 类直接构造模板消息
        user = event.get_user_id()  # 获取新成员的id
        at_ = "不想问就说 算了 [CQ:at,qq={}]".format(user)
        if city_name == "算了":
            await weather.finish("彳亍")
        else:
            await weather.send(city.template("我不会^_^ 建议问点别的"))

            await weather.reject(Message(at_))

    city_weather = await get_weather(city_name)
    await weather.finish(city_weather)


# 在这里编写获取天气信息的函数
async def get_weather(city: str) -> str:
    return QA[city]