import keep_alive
import nextcord
import os



from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = nextcord.Client(intents=intents)
client = commands.Bot(command_prefix="p!")





VERSION = 'v.0.1 Beta'
DEFAULTPREFIX = '!'



client.colors = {
    'BLURPLE': 0x5865F2,
    'WHITE': 0xFFFFFF,
    'GREYPLE': 0x23272A,  
    'COLOR1': 0x99AAB5,
    'COLOR2': 0xF6F6F6
}

client.color_list = [c for c in client.colors.values()]
client.DEFAULTPREFIX = DEFAULTPREFIX

# events
# idk lolll


@client.event
async def on_ready():
    print(f"Prefix: {DEFAULTPREFIX}\nVersion: {VERSION}")
    print("This bot is ready.")




class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.blurple)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("https://discord.gg/eabgwr27sk", ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.danger)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Oh. Okay, goodbye :(", ephemeral=True)
        self.value = False
        self.stop()



@client.command()
async def discord(ctx):
    view = Confirm()
    await ctx.send("Do you want to confirm somthing.", view=view)

    await view.wait()

    if not view.value == None:
        print("Timed Out")
    if view.value == True:
        print("True i guess lemao")
    if view.value == False:
        print("False i guess lemao")



# cogs
# to store stuff and things

if __name__ == '__main__':
	for file in os.listdir("cogs"):
		if file.endswith(".py") and not file.startswith("_"):
			client.load_extension(f"cogs.{file[:-3]}")





# client.run

keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
