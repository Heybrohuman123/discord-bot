import nextcord



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
    

  
      
     






  

  @commands.Cog.listener()
  async def on_message(self, message):
    print(f"{message.author} replied something so cool.")




def setup(client):
  client.add_cog(Misc(client))





  