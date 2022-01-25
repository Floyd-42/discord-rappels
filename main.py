from dis import disco
import os
from typing import Counter
import discord
from discord.ext import tasks
from discord.ui import Button, View, button
from discord.interactions import Interaction

from datetime import date, timedelta
from dotenv import load_dotenv
load_dotenv()


_title = "Pensez à sortir les poubelles Vertes :green_circle: et Jaunes :yellow_circle: ce soir :put_litter_in_its_place:"
embed=discord.Embed(title=_title, color=0x9ACD32)


class Connector:

    client = discord.Client()

    def run() -> None:
        print("Running Connector")
        Connector.client.run(os.getenv('BOT_TOKEN'))


    @client.event
    async def on_ready():
        print(f"Bot logged as {Connector.client.user}")
        await Connector.send.start(Connector)
        # await Connector.close()

    @classmethod
    @tasks.loop(seconds=5)
    # @tasks.loop(hours=)
    async def send(cls):

        channel = cls.client.get_channel(923976716223914026) # Testing
        # channel = cls.client.get_channel(920426362089652235) # CDC

        description = "Sinon ça va puer 🤢"
        embed.description = description
        await channel.send(embed=embed, view=ButtonView())

    @classmethod
    async def close(cls):
        await cls.client.close()

class ButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Cliquez ici quand les poubelles seront sorties", style=discord.ButtonStyle.blurple)
    async def button_callback(self, button: Button, interaction: Interaction):
        if not button.label.startswith("Merci"):
            label=f"Merci {interaction.user.name} !"
            button.label = label
            button.style = discord.ButtonStyle.success
            embed.description = "On a encore eu de la chance !"
            await interaction.response.edit_message(view=self, embed=embed)
        

def main():
    Connector.run()

if __name__ == "__main__":
    main()