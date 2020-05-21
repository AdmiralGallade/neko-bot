import os
from random import randrange
import discord
import nekos #nekos.py
from dotenv import load_dotenv





# def loadneko():
#         link="https://cdn.nekos.life/neko/neko"
#         num=randrange(1000)
#         link1=link+str(num)
#         link1=link1+".jpg"
#         return link1


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

# @client.event
# async def on_ready():
#     guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

# arr1=["https://cdn.nekos.life/neko/neko344.jpg"]
# for i in list(range(1000)):
#     arr1=arr1+loadneko()



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    

    if message.content == '!neko':
        response = nekos.img("neko")
        await message.channel.send(response)
    
    if message.content=='!nekos':
        for i in range(5):
            response=nekos.img("neko")
            await message.channel.send(response)
client.run(TOKEN)