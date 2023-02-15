import requests
import pandas as pd
import discord
import asyncio
from tabulate import tabulate

# 设置 Discord API 密钥和要发送消息的频道名称
discord_api_key = ''
channel_name = ''


# 获取币安 API 的交易量排名数据
def get_data():
    response = requests.get('https://api.binance.com/api/v3/ticker/24hr')
    data = response.json()
    return data


# 将数据转换为 DataFrame 格式
def get_df(data):
    df = pd.DataFrame(data)
    return df


# 筛选出交易量排名前 10 的币种
def get_top_volume(df):
    top_volume = df.sort_values(by='quoteVolume', ascending=False).iloc[:10]
    top_volume_with_price = top_volume[['symbol', 'quoteVolume']].copy()
    top_volume_with_price['price'] = [float(df[df['symbol'] == symbol]['lastPrice'].values[0]) for symbol in
                                      top_volume_with_price['symbol']]
    return top_volume_with_price


# 筛选出涨幅排名前 10 的币种及其价格
def get_top_gainers(df):
    df['price'] = pd.to_numeric(df['lastPrice'])
    df['priceChangePercent'] = pd.to_numeric(df['priceChangePercent'])
    top_gainers = df.sort_values(by='priceChangePercent', ascending=False).iloc[:10]
    top_gainers_with_price = top_gainers[['symbol', 'priceChangePercent']].copy()
    top_gainers_with_price['price'] = top_gainers['price'].values
    return top_gainers_with_price


# 发送消息到 Discord 频道
async def send_message(channel, top_volume, top_gainers):
    # 将交易量和涨幅排名数据转换成表格
    volume_table = tabulate(top_volume.values, headers=top_volume.columns, tablefmt='pretty')
    gainers_table = tabulate(top_gainers.values, headers=top_gainers.columns, tablefmt='pretty')
    # 创建 Discord 富文本格式
    embed = discord.Embed(title='币安交易数据', color=0x00ff00)
    # 将表格作为 Discord 富文本消息的一部分
    embed.add_field(name='交易量排名前 10 的币种：', value=f'```\n{volume_table}\n```', inline=False)
    embed.add_field(name='涨幅排名前 10 的币种：', value=f'```\n{gainers_table}\n```', inline=False)
    # 向目标频道发送消息
    await channel.send(embed=embed)


# 创建一个 Discord 客户端，并启用所需的消息发送权限
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


# 在客户端准备就绪时执行的事件
@client.event
async def on_ready():
    print(f'{client.user} 已经连接到了 Discord！')
    while True:
        # 获取数据
        data = get_data()
        df = get_df(data)
        top_volume = get_top_volume(df)
        top_gainers = get_top_gainers(df)
        # 查找目标频道
        target_channel = discord.utils.get(client.get_all_channels(), name=channel_name)
        # 发送消息
        await send_message(target_channel, top_volume, top_gainers)
        # 等待半小时
        await asyncio.sleep(1800)


# 运行客户端，并使用 Discord API 密钥登录
client.run(discord_api_key)
