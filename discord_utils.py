import discord
import asyncio
import pandas as pd
from coingecko import CoinGeckoAPI

# 设置 Discord API 密钥和要发送消息的频道名称
discord_api_key = 'Discord API 密钥'
channel_name = '发送消息的频道名称'

# 创建一个 Discord 客户端，并启用所需的消息发送权限
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


def create_embed(data):
    # 创建表格
    embed = discord.Embed(title='热门加密货币排行', color=0x00ff00)
    # 为表格添加字段
    embed.add_field(name='Symbol', value='\n'.join(data['symbol']), inline=True)
    embed.add_field(name='Market Cap Rank', value='\n'.join(data['market_cap_rank'].astype(str)), inline=True)
    embed.add_field(name='Price (USD)', value='\n'.join(data['price_usd'].apply(lambda x: f'${x:,.2f}')), inline=True)
    return embed


def create_embed_rank(data):
    # 创建表格
    embed = discord.Embed(title='1小时涨幅排行', color=0x00ff00)
    # 为表格添加字段
    embed.add_field(name='Symbol', value='\n'.join(data['symbol']), inline=True)
    embed.add_field(name='Price (USD)', value='\n'.join(data['current_price'].apply(lambda x: f'${x:,.2f}')), inline=True)
    embed.add_field(name='Change(1h)',
                    value='\n'.join(data['price_change_percentage_1h_in_currency'].apply(lambda x: f"{x:.2f}%")),
                    inline=True)

    return embed


# 在客户端准备就绪时执行的事件
@client.event
async def on_ready():
    print(f'{client.user} 已经连接到了 Discord！')
    while True:
        # 查找目标频道
        target_channel = discord.utils.get(client.get_all_channels(), name=channel_name)
        # 在这里将数据发送到Discord机器人或其他地方
        trending_coins = CoinGeckoAPI.get_trending_coins()

        rank_coins = CoinGeckoAPI.get_trend_rank_coin()
        # 发送消息
        await target_channel.send(embed=create_embed(trending_coins))
        await target_channel.send(embed=create_embed_rank(rank_coins))
        # 等待4小时
        await asyncio.sleep(14400)


# 运行客户端，并使用 Discord API 密钥登录
client.run(discord_api_key)
