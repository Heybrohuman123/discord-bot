import nextcord
import random
import io
import aiohttp
import asyncio
import functools
import urllib


from io import BytesIO
from PIL import Image, ImageEnhance
from random import randint
from urllib.request import urlopen


from asyncdagpi import ImageFeatures
from nextcord.ext import commands


class Fun(commands.Cog, description="Want to have fun? Look at these pages. So cool."):
  def __init__(self, client):
    self.client = client





  guild_ids = [849542340522672151, 723865003626594314]

  percentage = [
    "bad at minecraft.",
    "no friends",
    "good at playing games",
    "a loser",
    "a human",
    "an alien",
    "a nobody",
    "a noob at Valorant"
  ]
  randomizer1 = random.choice(percentage)

  @commands.command()
  async def _8ball(self, ctx, question="No reason provided."):
      response = [
          "Certainly",
          "I agree.",
          "Sure!",
          "That's the question I would agree on.",
          "I accept!",
          "Yes.",
          "Hmm, maybe?",
          "I really don't know",
          "BIDIBIDIBIDIBIDI maybe.",
          "I'm thinking about it.",
          "Ask again.",
          "NO!",
          "I disagree to this question.",
          "There's nobody stopping you.. except me :)"
      ]
      rc = random.choice(response)
      await ctx.send(f'Question: {question}\nAnswer: {rc}')

  @commands.command()
  async def pplong(self, ctx):
      a = random.randint(0,20)
      await ctx.send(f"PP LONG:\n{a} inches")

  @commands.command()
  async def percentage(self, ctx, *, message = f"{randomizer1}"):
      a = random.randint(0,100)
      embed=nextcord.Embed(title="Percentage")
      embed.add_field(name="Percentage", value=f"You're {a}% {message}.")
      await ctx.send(embed=embed)



  @commands.command()
  @commands.cooldown(1,20)
  async def emojify(self, ctx, *, text):
    emojis = []
    for s in text.lower():
      if s.isdecimal():
        num2emo = {
          '0':'zero',
          '1':'one',
          '2':'two',
          '3':'three',
          '4':'four',
          '5':'five',
          '6':'six',
          '7':'seven',
          '8':'eight',
          '9':'nine',
        }
        emojis.append(f':{num2emo.get(s)}:')
      elif s.isalpha():
        emojis.append(f':regional_indicator_{s}: ')
      else:
        emojis.append(s)
    await ctx.send(f''.join(emojis))


  
  @commands.command(description="Use this to make yourself or other players wanted.")
  async def wanted(self, ctx, member : nextcord.Member = None):
      if member == None:
            member = ctx.author

      wanted = Image.open("images/wanted1.jpg")

      asset = member.avatar_url_as(size = 128)
      data = BytesIO(await asset.read())
      profilepics = Image.open(data)
      
      profilepics = profilepics.resize((96,96))
      wanted.paste(profilepics, (41,103))
      
      buffer = io.BytesIO()
      wanted.save(buffer, "PNG") # async guild
      buffer.seek(0)
      file = nextcord.File(buffer, filename="image.png")
      await ctx.send(file = file)




  @commands.command(description="Use this to make a rest in peace for you or other players")
  async def rip(self, ctx, member : nextcord.Member = None):
      if member == None:
            member = ctx.author

      wanted = Image.open("images/gravestone.jpg")

      asset = member.avatar_url_as(size = 128)
      data = BytesIO(await asset.read())
      profilepics = Image.open(data)
      
      profilepics = profilepics.resize((96,96))
      wanted.paste(profilepics, (83,43))
      
      buffer = io.BytesIO()
      wanted.save(buffer, "PNG")
      buffer.seek(0)
      file = nextcord.File(buffer, filename="image.png")
      await ctx.send(file = file)

  @commands.command()
  async def helloisdavididot(self, ctx):
    message = await ctx.send("Loading.")
    await asyncio.sleep(2)
    await message.edit(content="Yes..")


 




  
    

  @commands.command(description="Heads or Tails?")
  async def coinflip(self, ctx):
    response = ["Heads", "Tails"]
    coin = random.choice(response)
    await ctx.send(coin)



  @commands.command(description="A hug is better, Always.")
  @commands.cooldown(1,60)
  async def hug(self, ctx, user: nextcord.Member):
    author = ctx.author
    embed=nextcord.Embed(title="Show love ❤️")
    embed.add_field(name='Awh.', value=f'{author} hugged {user}! ❤️❤️❤️', inline=False)
    await ctx.send(embed=embed)

  @commands.command(description="The choice is by the dice.")
  @commands.cooldown(1,20)
  async def rolladie(self, ctx):
    numbers = ["1", "2", "3", "4", "5", "6"]
    dice = random.choice(numbers)
    embed=nextcord.Embed(title="You rolled a die!")
    embed.add_field(name='Dice Number:', value=f'{dice}')
    await ctx.send(embed=embed)


  @commands.command(description="Turn a photo url into blue.")
  async def blurpify(self, ctx, url: str):
    async with aiohttp.ClientSession() as ses:
      async with ses.get(f'https://nekobot.xyz/api/imagegen?type=blurpify&image={url}') as img:
        if img.status in range(200, 299):
          data = await img.json()
          url = data['message']
          mbed = nextcord.Embed(
            title = 'Discord Blurpify lez go'
          )
          mbed.set_image(url=url)
          await ctx.send(embed=mbed)
        else:
          await ctx.send('This is not an Image URL.')
          await ses.close()










  @commands.command(description="COOL URL TURNS INTO A FRIED PHOTO")
  async def deepfry(self, ctx, url: str):
    async with aiohttp.ClientSession() as ses:
      async with ses.get(f'https://nekobot.xyz/api/imagegen?type=deepfry&image={url}') as img:
        if img.status in range(200, 299):
          data = await img.json()
          url = data['message']
          mbed = nextcord.Embed(
            title = 'This looks like fries.'
          )
          mbed.set_image(url=url)
          await ctx.send(embed=mbed)
        else:
          await ctx.send('This is not an Image URL.')
          await ses.close()


  

  @commands.Cog.listener()
  async def on_message(self, message):
    print("")


def setup(client):
  client.add_cog(Fun(client))





  