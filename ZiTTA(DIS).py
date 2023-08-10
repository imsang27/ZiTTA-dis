# Copyright 2023. ZiTTA All rights reserved.
import discord

# 봇 토큰 입력
token = "YOUR_BOT_TOKEN"

# Intents 객체 생성
intents = discord.Intents.default()

# 봇 클라이언트 생성 및 intents 파라미터로 전달
client = discord.Client(intents=intents)
# discord.Client: Discord.py에서 제공하는 기본 클라이언트 클래스로, 봇의 동작을 정의하고 이벤트 핸들러를 등록할 수 있습니다.


# 봇이 준비되었을 때 실행되는 이벤트 핸들러
@client.event   # client.event: 이벤트 핸들러를 등록하는 데 사용되는 데코레이터입니다.
async def on_ready():   # on_ready(): 봇이 Discord에 로그인하고 준비되었을 때 호출되는 이벤트 핸들러입니다. 봇이 준비되면 봇의 상태를 변경하고, 터미널에 봇 사용자 이름을 출력합니다.
    # 봇의 상태(Status)를 온라인으로 설정하고 활동을 적용합니다.
    await client.change_presence(status=discord.Status.online, activity=activity)
    # client.change_presence(): 봇의 상태를 변경하는 메서드로, 봇의 상태와 활동(Activity)를 설정할 수 있습니다.

    # 봇의 활동(Activity)을 설정할 객체를 생성합니다.
    activity = discord.Activity(type=discord.ActivityType.playing, name="테스트 중")

    print(f'봇이 로그인되었습니다. 봇 이름: {client.user}')
    # client.user: 로그인한 봇의 사용자 정보를 나타냅니다.


# 메시지가 왔을 때 실행되는 이벤트 핸들러
@client.event
async def on_message(message):  # on_message(): 메시지가 올라왔을 때 호출되는 이벤트 핸들러입니다. 봇이 보낸 메시지를 무시하고, 특정 명령어를 받았을 때 해당 명령어에 대한 응답을 작성합니다.
    # 봇이 보낸 메시지면 무시
    if message.author == client.user:
        return

    # 메시지의 내용을 확인하고, 특정 명령어에 대한 응답을 작성
    if message.content.startswith('!안녕'):
        await message.channel.send('안녕하세요!')

# 봇 실행
client.run(token)
