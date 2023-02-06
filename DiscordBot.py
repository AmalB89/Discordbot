import asyncio
import requests
import discord
import random
import string
from captcha.image import ImageCaptcha

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)

# task runs every 60 seconds

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # mUrl = "https://discord.com/api/webhooks/1071454449333186671/mAgh9lBEqWd1K54jCEv82FnYkWNXBnTuqeQFK2X_iy9E3w_A2Yssm5r3Re25KqTRql7o"
    #
    # data = {"content": 'abc'}
    # response = requests.post(mUrl, json=data)
    #
    # print(response.status_code)


@client.event
async def on_member_join(member):
    channel = client.get_channel("1070302102527692810")
    # image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])
    # data = image.generate('1234')
    # image.write('1234', 'out.png')
    # captcha_image = discord.File("captcha.png")
    # letters = string.ascii_letters
    # captcha = ''.join(random.choice(letters) for i in range(5))
    # await channel.send("welcome {member.mention}! please complete the captcha",captcha)

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('!captcha'):
        # Generate a random 5-letter CAPTCHA
        letters = string.ascii_letters
        captcha = ''.join(random.choice(letters) for i in range(5))

        # Send the CAPTCHA to the user
        await message.author.send(f'Your CAPTCHA is: {captcha}')


client.run('MTA2OTMyNDE0MjU4ODk5Nzc2NA.G7ToI-.zT6gk5GnIgeleyg47uGxoA9lo7B2DPR7SZnolE')


