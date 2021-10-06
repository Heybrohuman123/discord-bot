import random
import datetime

import nextcord
from nextcord.ext import commands



class Events(commands.Cog, description="Events :)"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Ignore these errors
        ignored = (commands.CommandNotFound, commands.UserInputError)
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.CommandOnCooldown):
            # If the command is currently on cooldown trip this
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                await ctx.send(f" Wait for {int(s)} seconds to execute this command!")
            elif int(h) == 0 and int(m) != 0:
                await ctx.send(
                    f" Wait for {int(m)} minutes and {int(s)} seconds to execute this command!"
                )
            else:
                await ctx.send(
                    f" Wait for {int(h)} hours, {int(m)} minutes and {int(s)} seconds to execute this command."
                )
        elif isinstance(error, commands.CheckFailure):
            # If the command has failed a check, trip this
            await ctx.send(f"You don't have that type of permission in {ctx.guild.name}.")
        # Implement further custom checks for errors here...
        raise error

def setup(bot):
    bot.add_cog(Events(bot))