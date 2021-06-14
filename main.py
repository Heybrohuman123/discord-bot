import keep_alive
import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = "!")



#if __name__ == '__main__':
#  for extension in intial_extensions:
#    try:  #So, every try: has to have an except: after it. So because that it will give an error.
#      client.load_extension(extension)
#    except:
#      pass




# events
# idk lolll

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!help"))




# cogs
# to store stuff and things

cogs = ['cogs.fun', 'cogs.misc', 'cogs.mod']

for cog in cogs:
  try:
    client.load_extension(cog)
  except Exception as e:
    print(f'Could not load cog {cog}: {str(e)}')

@client.command()
@commands.has_permissions(administrator=True)
async def loadcog(ctx, cogname = None):

  if cogname is None:
    return

  try:
    client.load_extension(cogname)
  except Exception as e:
    embed=discord.Embed(title="Oopsie", colour=discord.Colour(0xdf2723))
    embed.add_field(name="Output:", value=(f"Could not load cog {cog}: {str(e)}"))
    await ctx.send(embed=embed)
  else:
    embed=discord.Embed(title="Woohoo!")
    embed.add_field(name="You successfully:", value=(f"loaded {cog}"))
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def unloadcog(ctx, cogname = None):

  if cogname is None:
    return

  try:
    client.unload_extension(cogname)
  except Exception as e:
    embed=discord.Embed(title="Oopsie", colour=discord.Colour(0xdf2723))
    embed.add_field(name="Output:", value=(f"Could not unload cog {cog}: {str(e)}"))
    await ctx.send(embed=embed)
  else:
    embed=discord.Embed(title="Woohoo!")
    embed.add_field(name="You successfully:", value=(f"unloaded {cog}"))
    await ctx.send(embed=embed)













# client.run

keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
