import random
import datetime

import nextcord
from nextcord.ext import commands



class Social(commands.Cog, description="Events :)"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")



def setup(bot):
    bot.add_cog(Social(bot))