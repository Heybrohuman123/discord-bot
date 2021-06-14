import discord
import random





from discord.ext import commands

class Fun(commands.Cog):
  def __init__(self, client):
    self.client = client




  @commands.command(brief="Your future. It's here.")
  @commands.cooldown(1,60)
  async def eightball(self, ctx, question):
    responses = ['As I see it, yes.',
             'Yes.',
             'Positive',
             'From my point of view, yes',
             'Convinced.',
             'Most Likley.',
             'Chances High',
             'No.',
             'Negative.',
             'Not Convinced.',
             'Perhaps.',
             'Not Sure',
             'Mayby',
             'I cannot predict now.',
             'Im to lazy to predict.',
             'I am tired. *proceeds with sleeping*']
    response = random.choice(responses)
    embed=discord.Embed(title="The 8ball has answered your question.")
    embed.add_field(name='Question: ', value=f'{question}', inline=True)
    embed.add_field(name='Answer: ', value=f'{response}', inline=False)
    
    await ctx.send(embed=embed)
    

  @commands.command(brief="Head or Tails?")
  @commands.cooldown(1,60)
  async def coinflip(self, ctx):
    response = ["Heads", "Tails"]
    coin = random.choice(response)
    await ctx.send(coin)



  @commands.command()
  @commands.cooldown(1,60)
  async def hug(self, ctx, user : discord.Member):
    player = ctx.message.author.name
    embed=discord.Embed(title="Show love ❤️")
    embed.add_field(name='Awh.', value=f'{player} hugged {user}! ❤️❤️❤️', inline=False)
    await ctx.send(embed=embed)

  @commands.command()
  @commands.cooldown(1,20)
  async def rolladie(self, ctx):
    numbers = ["1", "2", "3", "4", "5", "6"]
    dice = random.choice(numbers)
    embed=discord.Embed(title="You rolled a die!")
    embed.add_field(name='Dice Number:', value=f'{dice}')
    await ctx.send(embed=embed)








  

  @commands.Cog.listener()
  async def on_message(self, message):
    print("")


def setup(client):
  client.add_cog(Fun(client))





  