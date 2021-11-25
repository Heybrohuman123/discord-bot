import nextcord
import urllib

from nextcord.ext import commands

class Misc(commands.Cog, description="You get to know about everything, well not everything." ):
  def __init__(self, client):
    self.client = client




  
  guild_ids = [849542340522672151, 723865003626594314]

  


  @commands.command(description="Tells the bots latency.")
  async def ping(self, ctx):
    await ctx.send(f":ping_pong: || {round(self.client.latency * 1000)}ms!")

  @commands.command()
  async def avatar(self, ctx):
    profilepic = ctx.author.avatar.url
    embed=nextcord.Embed(title=f"Here is {ctx.author} profile picture!")
    embed.set_image(url=profilepic)
    await ctx.send(embed=embed)


  @commands.command()
  async def google(self, ctx, *, arg):
    parse = urllib.parse.quote(arg)
    embed = nextcord.Embed(title="Search found!")
    embed.description = f"[Link! Click here.](https://www.google.com/search?q={parse})"
    await ctx.send(embed=embed)

  @commands.command()
  async def dictionary(self, ctx, *, arg):
    parse = urllib.parse.quote(arg)
    embed = nextcord.Embed(title="Dictionary found!")
    embed.description = f"[Link! Click here.](https://www.urbandictionary.com/define.php?term={parse})"
    await ctx.send(embed=embed)
    await ctx.send(f"https://www.urbandictionary.com/define.php?term={parse}")

  






  

@commands.Cog.listener()
async def on_message(self, message):
  print(f"{message.author} replied something so cool.")




def setup(client):
  client.add_cog(Misc(client))





  