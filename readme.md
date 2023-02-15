# Discord Bot 使用说明

## 安装discord.py

在终端中执行以下命令安装discord.py:pip install discord.py

## 创建Bot

1. 创建一个Discord开发者帐户，并创建一个新的应用程序。
2. 在应用程序页面中，点击“Bot”选项卡，然后点击“Add Bot”按钮。
3. 记录下你的Bot的Token。

## 代码对接

1. 创建一个新的Python文件，并输入以下代码：
```python
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run('YOUR_BOT_TOKEN')
```

2.将YOUR_BOT_TOKEN替换为你的Bot的Token。
3.运行代码，你的Bot已经与Discord对接了


## 添加Bot到服务器
1.在你的应用程序页面中，点击“OAuth2”选项卡。
2.在“Scopes”部分中选择“bot”。
3.在“Bot Permissions”部分中选择你希望你的Bot具有的权限。
4.点击“Generate OAuth2 URL”按钮，并将生成的URL发送给你的服务器的管理员。
5.管理员只需要点击该链接，然后选择要添加Bot的服务器，并点击“Authorize”按钮。

# Introduction
This guide will help you to integrate your Discord bot with the Discord platform.

# Prerequisites
- A Discord account and a Discord server
- Python 3.8 or later installed on your system
- The Discord API Wrapper for Python: `discord.py`

# Installation
To install the `discord.py` library, run the following command in your terminal:
pip install discord.py

# Setting up the Bot Account
1. Go to the Discord Developer Portal at https://discord.com/developers/applications
2. Click on the "New Application" button to create a new Discord app.
3. Give your app a name and click on the "Create" button.
4. Go to the "Bot" section and click on the "Add Bot" button.
5. Copy the token provided under the "Token" section. You will use this token to log in to the bot account.

# Writing the Code
1. Create a new file in your preferred code editor and name it `suibot.py`.
2. Import the `discord` library at the top of your file.
3. Create a new instance of the `Client` class from the `discord` library.
4. Define an event handler for the `on_ready` event. This event will be triggered when the bot is successfully logged in.
5. Add the following code to log in to the bot account using the token.
6. Replace `'YOUR_BOT_TOKEN'` with the token you copied from the Discord Developer Portal.
7. Save the file and run the code using the following command:

# Conclusion
You should now have a working Discord bot that is connected to your Discord server. You can now build upon this foundation to add more functionality to your bot.

