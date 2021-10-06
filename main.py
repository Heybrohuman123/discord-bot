import keep_alive
import nextcord
import os
import asyncio


from nextcord.ext import commands


intents = nextcord.Intents.default()
intents.members = True

client = nextcord.Client(intents=intents)
client = commands.Bot(command_prefix="p!")
client.remove_command("help")






VERSION = 'v.0.1 Beta'
DEFAULTPREFIX = '!'



client.colors = {
    'BLURPLE': 0x5865F2,
    'WHITE': 0xFFFFFF,
    'GREYPLE': 0x23272A,  
    'COLOR1': 0x99AAB5,
    'COLOR2': 0xF6F6F6
}

client.color_list = [c for c in client.colors.values()]
client.DEFAULTPREFIX = DEFAULTPREFIX

# events
# idk lolll


@client.event
async def on_ready():
    print(f"Prefix: {DEFAULTPREFIX}\nVersion: {VERSION}")
    print("This bot is ready.")






    


# cogs
# to store stuff and things

if __name__ == '__main__':
	for file in os.listdir("cogs"):
		if file.endswith(".py") and not file.startswith("_"):
			client.load_extension(f"cogs.{file[:-3]}")





# client.run

keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
