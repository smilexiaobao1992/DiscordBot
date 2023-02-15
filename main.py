import discord
import asyncio

# 定义要启用的消息发送权限
intents = discord.Intents.default()
intents.messages = True

# 创建一个Discord客户端，并启用所需的消息发送权限
client = discord.Client(intents=intents)

# 在客户端准备就绪时执行的事件
@client.event
async def on_ready():
    print(f'{client.user} 已经连接到了Discord！')
    while True:
        # 查找目标频道
        target_channel = discord.utils.get(client.get_all_channels(), name='target-channel-name')
        # 向目标频道发送消息
        # 后续可自定义自己想要的消息获取后发送到自己到channel进行对接
        await target_channel.send('test')
        await asyncio.sleep(60)  # 等待60s

# 运行客户端，并使用Discord API密钥登录
client.run('Your-discord-ApiKey')
