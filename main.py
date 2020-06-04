import os
from random import randrange
import discord
import nekos #nekos.py
from dotenv import load_dotenv
import re





# def loadneko():
#         link="https://cdn.nekos.life/neko/neko"
#         num=randrange(1000)
#         link1=link+str(num)
#         link1=link1+".jpg"
#         return link1


load_dotenv()

flag=0

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
    global flag
    if flag==0:

        if message.author == client.user:
            return

        

        if message.content == '!neko':
            response = nekos.img("neko")
            await message.channel.send(response)
        

        
        if message.content=='!nekos':
            for i in range(5):
                response=nekos.img("neko")
                await message.channel.send(response)

        if message.content=='!nekostorm':
            response="Nekostorm activated, enter the number of nekos required!"
            await message.channel.send("Nekostorm activated, enter the number of nekos required!")
            flag=1
        
    else:
        
        
            
        arr=int(re.search(r'\d+', message.content).group())
        
        number=arr
        if number !=0 and number>0 and number<50:
            
            for i in range(number):
                response=nekos.img("neko")
                flag=0
                await message.channel.send(response)
        flag=0
        
client.run(TOKEN)