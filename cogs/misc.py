import discord
from faker import Faker

from discord.ext import commands

class Misc(commands.Cog):
  def __init__(self, client):
    self.client = client



  @commands.command(brief="What's your ping?")
  @commands.cooldown(1,60)
  async def ping(self, ctx):
    await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms') 

  @commands.command()
  @commands.cooldown(1,20)
  async def generator(self, ctx):
    fake = Faker()
    embed=discord.Embed(title="Name Generator")
    embed.add_field(name="Random Names", value=f'{fake.name()}. Is this right?')
    await ctx.send(embed=embed)
    


  


  

  @commands.Cog.listener()
  async def on_message(self, message):
    print(f"{message.author} replied something so cool.")


def setup(client):
  client.add_cog(Misc(client))





  