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
            "public": 0
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
    async def setpublic(self, ctx, key: int = 0):
        """generate a new public key"""
        if key == 0:
            key = random.randint(0, 1000)
        await self.config.guild(ctx.guild).public.set(key)
        return ctx.send(f"Key set to {key}")

    @commands.command()
    @commands.guild_only()
    async def elaborate(self, ctx, key: int = 0):
        """Elaborates the data inputted"""
        bobkey = await self.config.guild(ctx.guild).bobkey()
        alicekey = await self.config.guild(ctx.guild).bobkey()
        publicgen = await self.config.guild(ctx.guild).bobkey()
        public = await self.config.guild(ctx.guild).bobkey()

    