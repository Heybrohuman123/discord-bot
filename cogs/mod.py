import discord


from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client



  @commands.command(brief="kick")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user : discord.Member, *, reason="No reason was provided"):
    kick_dm = discord.Embed(
      title='You have been kicked.',
      description=f"You have been kicked from {ctx.message.guild.name}!\nReason: {reason}"
    )

    kick_msg = discord.Embed(
      title=f"Kicked {user}",
      description=f'Reason: {reason}'
    )

    await user.send(embed=kick_dm)
    await user.kick(reason=reason)
    await ctx.channel.send(embed=kick_msg)


  @commands.command(brief="ban")
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user : discord.Member, *, reason="No reason was provided"):
    ban_dm = discord.Embed(
      title='You have been banned.',
      description=f"You have been banned from {ctx.message.guild.name}!\nReason: {reason} "
    )

    ban_msg = discord.Embed(
      title=f"Banned {user}",
      description=f'Reason: {reason}'
    )

    await user.send(embed=ban_dm)
    await user.ban(reason=reason)
    await ctx.channel.send(embed=ban_msg)



  @commands.command(brief="hello")
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
      mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f'Muted {member.mention} for reason of {reason}')
    await member.send(f'You have been muted in blah blah server for {reason}')

  @commands.command(brief="1hello")
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
      mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)

    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(f'Unmuted {member.mention} for reason of {reason}')
    await member.send(f'You have been unmuted in blah blah server for {reason}')





  


  

  @commands.Cog.listener()
  async def on_message(self, message):
    print(f"{message.author} said something. cool")


def setup(client):
  client.add_cog(Moderation(client))





  