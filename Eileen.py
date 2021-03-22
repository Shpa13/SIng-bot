__author__= "Ronin_1_3"
#Eileen Bot

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

#print(certifi.where())
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

 #bot = commands.Bot(command_prefix="!") 
bot = discord.Client()

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        if guild.name == GUILD:
            break          
    print(
        f' {bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.event
async def on_message(message):
    if message.content.upper() == "EILEEN":
        await message.channel.send("Come on Eileen")
        await message.channel.send("Come on Eileen")    
        await message.channel.send("""
                Poor old Johnny Ray
            Sounded sad upon the radio
            Moved a million hearts in mono
            Our mothers cried
            Sang along, who'd blame them?
            """)

        await message.channel.send("""
                You're grown (you're grown up)
            So grown (so grown up)
            Now I must say more than ever
            (Come on Eileen)
            Toora loora toora loo rye ay
            And we can sing just like our fathers
            """)

        await message.channel.send("""
                Come on Eileen, oh I swear what he means
            At this moment, you mean everything
            You in that dress, my thoughts I confess
            Verge on dirty, ah, come on Eileen
            """)

        await message.channel.send("Come on Eileen")

        await message.channel.send("""
                These people round here
            Wear beatdown eyes sunk in smoke dried face
            So resigned to what their fate is
            """)

        await message.channel.send("""
                But not us (no never)
            No not us (no never)
            We are far too young and clever
            """)

        await message.channel.send("""
                Toora loora, toora loo rye ay
            Eileen, I'll hum this tune forever
            """)

        await message.channel.send("""
                Come on Eileen, oh I swear (what he means)
            Ah come on let's, take off everything
            Pretty red dress, Eileen, tell him yes
            Ah come on let's, ah, come on Eileen
            That pretty red dress, Eileen, tell him yes
            Ah, come on let's, ah come on Eileen, please
            """)

        await message.channel.send("""
                Come on Eileen, too loo rye ay
            Come on Eileen, too loo rye ay
            Now you have grown, and now you have shown
            Oh, Eileen
            """)

        await message.channel.send("""
                Said
            Come on Eileen, too loo rye ay
            Come on Eileen, too loo rye ay
            Now I must say more than ever
            Things round here change
            I said, toora loora, toora loo rye ayyyyyyyy
            """)

                #X2
        await message.channel.send(""" 
                Come on Eileen, oh I swear what he means
            At this moment, you mean everything
            In that dress, oh my thoughts, I confess
            Well, they're dirty, come on Eileen
            """)

        await message.channel.send("Come on Eileen")

bot.run(TOKEN)
async def client_start():
    await bot.start(TOKEN)