import nextcord

import sys
import asyncio

from nextcord.ext import commands

class Moderation(commands.Cog, description="For moderators only."):
  def __init__(self, client):
    self.client = client

  def botowner(ctx):
    trusted = [421247440205774872]
    return ctx.author.id in trusted

  guild_ids = [849542340522672151, 723865003626594314]

 
  @commands.command()
  @commands.check(botowner)
  async def stopbot(self, ctx):
    await ctx.send("Incoming bot shutdown in 3...")
    await asyncio.sleep(1)
    await ctx.send("2!")
    await asyncio.sleep(1)
    await ctx.send("1!")
    await asyncio.sleep(0.5)
    sys.exit()

  @commands.command(description="Kick a user.")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : nextcord.Member, *,reason=None):
      await member.kick(reason=reason)
      embed=nextcord.Embed(color=0x00ff2a)
      embed.add_field(name="Member Kicked\n", value=f"***{member}*** *has been `banned` from the guild for {reason}*", inline=False)
      await ctx.send(embed=embed)

  @commands.command(pass_context=True)
  @commands.has_permissions(administrator=True)
  async def poll(self, ctx, *, question=None):
    embed=nextcord.Embed(color=0x00ff2a)
    embed.add_field(name="Poll", value=f"***{question}***", inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
    await ctx.message.delete()





  @commands.command(brief="Ban a user.")
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : nextcord.Member, *,reason=None, guild_ids=guild_ids):
      await member.ban(reason=reason)
      embed=nextcord.Embed(color=0x00ff2a)
      embed.add_field(name="Member Banned!\n", value=f"***{member}*** *has been `banned` from the guild for {reason}*", inline=False)
      await ctx.send(embed=embed)



  @commands.command(brief="Mute a user.")
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: nextcord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = nextcord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
      mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f'Muted {member.mention} for reason of {reason}')
    await member.send(f'You have been muted in blah blah server for {reason}')

  @commands.command(brief="Unmutes the user.")
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: nextcord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = nextcord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
      mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)

    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(f'Unmuted {member.mention} for reason of {reason}')
    await member.send(f'You have been unmuted in blah blah server for {reason}')

  @commands.command(brief="Blacklist a user.")
  @commands.has_permissions(manage_messages=True)
  async def blacklist(self, ctx, member: nextcord.Member, *, reason=None):
    guild = ctx.guild
    listedRole = nextcord.utils.get(guild.roles, name="blacklisted")

    if not listedRole:
      listedRole = await guild.create_role(name="blacklisted")

    for channel in guild.channels:
      await channel.set_permissions(listedRole, speak=False, send_messages=False, read_message_history=True)

    await member.add_roles(listedRole, reason=reason)
    await ctx.send(f'Blacklisted {member.mention} for reason of {reason}')
    await member.send(f'You have been locked to the server for {reason}')

  @commands.command(brief="Whitelist the user.")
  @commands.has_permissions(manage_messages=True)
  async def pardon(self, ctx, member: nextcord.Member, *, reason=None):
    guild = ctx.guild
    listedRole = nextcord.utils.get(guild.roles, name="blacklisted")

    if not listedRole:
      listedRole = await guild.create_role(name="blacklisted")

    for channel in guild.channels:
      await channel.set_permissions(listedRole, speak=False, send_messages=False, read_message_history=True)

    await member.remove_roles(listedRole, reason=reason)
    await ctx.send(f'Pardon, {member.mention}.')
    await member.send(f'You can use the server now for {reason}')








  


  

  @commands.Cog.listener()
  async def on_message(self, message):
    print("")


def setup(client):
  client.add_cog(Moderation(client))





  