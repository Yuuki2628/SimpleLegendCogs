from redbot.core import Config
from redbot.core import commands
import discord
import random

class BobAlice(commands.Cog):
    """A cog to notify when someone joins or leaves the server"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier = 26282562628)
        default_guild = {
            "bobkey": 0,
            "alicekey": 0,
            "publicgen": 0,
            "publicmod": 0
        }

        self.config.register_guild(**default_guild)
            
    @commands.command()
    @commands.guild_only()
    async def setbobkey(self, ctx, key: int):
        """Set bob's private key"""
        await self.config.guild(ctx.guild).bobkey.set(key)
        return ctx.send("Key set")

    @commands.command()
    @commands.guild_only()
    async def setalicekey(self, ctx, key: int):
        """Set bob's private key"""
        await self.config.guild(ctx.guild).alicekey.set(key)
        return ctx.send("Key set")

    @commands.command()
    @commands.guild_only()
    async def setpublickey(self, ctx, key: int = 0):
        """generate a new public key key"""
        if key == 0:
            key = random.randint(0, 1000)
        await self.config.guild(ctx.guild).publicgen.set(key)
        return ctx.send(f"Key set to {key}")

    @commands.command()
    @commands.guild_only()
    async def setpublicmod(self, ctx, key: int = 0):
        """generate a new public key"""
        if key == 0:
            key = random.randint(0, 1000)
        await self.config.guild(ctx.guild).publicmod.set(key)
        return ctx.send(f"Key set to {key}")

    @commands.command()
    @commands.guild_only()
    async def elaborate(self, ctx, key: int = 0):
        """Elaborates the data inputted"""
        bobkey = await self.config.guild(ctx.guild).bobkey()
        alicekey = await self.config.guild(ctx.guild).alicekey()
        publicgen = await self.config.guild(ctx.guild).publicgen()
        publicmod = await self.config.guild(ctx.guild).publicmod()

        if bobkey == 0 or alicekey == 0 or publicgen == 0 or public mod == 0:
            return await ctx.send("Devi impostare tutti i valori)
        
        bobkeypriv = publicgen ** bobkey
        alicekeypriv = publicgen ** alicekey
        embed = discord.Embed(title=Comunicazione Bob Alice, color=0xFFD700)
        embed.add_field(name="Chiave privata di Bob", value=f"```\n{bobkeypriv}\n```")
        embed.add_field(name="Chiave privata di Alice", value=f"```\n{alicekeypriv}\n```")
        embed.add_field(name="Chiave privata", value=f"```\n{bobkeypriv%publicmod}\n```")
        return ctx.send(embed=embed)
