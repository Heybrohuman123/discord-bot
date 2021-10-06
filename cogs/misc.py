import nextcord



from nextcord.ext import commands


class Misc(commands.Cog, description="You get to know about everything, well not everything." ):
  def __init__(self, client):
    self.client = client




  
  guild_ids = [849542340522672151, 723865003626594314]

  


  @commands.command(description="Tells the bots latency.")
  async def ping(self, ctx):
    await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

  
      
     






  

  @commands.Cog.listener()
  async def on_message(self, message):
    print(f"{message.author} replied something so cool.")




def setup(client):
  client.add_cog(Misc(client))





  