from redbot.core import commands
import discord

class AdventureZ(commands.Cog):
    """Extra adventure commands, like the good ol'Z commands and grindsquad"""

    @commands.command(name="z")
    async def zCMD(self, ctx, *, msg):
        msg = msg.under()
        """Followed by a personality value it'll return it's multiplier"""
        if msg == "absolutely-brutal-looking":
            await ctx.send("1.9 / 1.1")
        elif msg == "ancient":
            await ctx.send("0.8 / 2")
        elif msg == "cunning":
            await ctx.send("1.2 / 1.2")
        elif msg == "delirious":
            await ctx.send("0.6 / 0.8")
        elif msg == "disgusting":
            await ctx.send("1 / 0.7")
        elif msg == "dumb":
            await ctx.send("1 / 0.8")
        elif msg == "enlightened":
            await ctx.send("1.2 / 1.8")
        elif msg == "fairly-intelligent":
            await ctx.send("1 / 1.2")
        elif msg == "fat":
            await ctx.send("1.1 / 0.9")
        elif msg == "flustered":
            await ctx.send("0.9 / 1.1")
        elif msg == "focused":
            await ctx.send("1.2 / 1")
        elif msg == "gigantic":
            await ctx.send("1.4 / 1")
        elif msg == "hideous":
            await ctx.send("1 / 1")
        elif msg == "highly-scarred":
            await ctx.send("1.4 / 1.1")
        elif msg == "humongous":
            await ctx.send("2 / 0.8")
        elif msg == "immortal":
            await ctx.send("100 / 1.1")
        elif msg == "lazy":
            await ctx.send("0.4 / 0.9")
        elif msg == "minuscule":
            await ctx.send("0.2 / 1.1")
        elif msg == "muscle-bound":
            await ctx.send("1.2 / 0.7")
        elif msg == "old":
            await ctx.send("0.8 / 1.5")
        elif msg == "ordinary":
            await ctx.send("1 / 1")
        elif msg == "plagued":
            await ctx.send("1.2 / 0.9")
        elif msg == "possessed":
            await ctx.send("1.8 / 100")
        elif msg == "prodigious":
            await ctx.send("1.6 / 0.8")
        elif msg == "sad-looking":
            await ctx.send("0.9 / 0.8")
        elif msg == "savage":
            await ctx.send("1.8 / 0.9")
        elif msg == "scheming":
            await ctx.send("1.3 / 1")
        elif msg == "sick":
            await ctx.send("0.3 / 0.9")
        elif msg == "small":
            await ctx.send("0.8 / 1")
        elif msg == "staunch":
            await ctx.send("1.15 / 1")
        elif msg == "stupid":
            await ctx.send("1 / 0.5")
        elif msg == "terrifying":
            await ctx.send("1 / 1.2")
        elif msg == "tiny":
            await ctx.send("0.7/ 1")
        elif msg == "weak":
            await ctx.send("0.5 / 1")
        elif msg == "weary":
            await ctx.send("0.6 / 0.9")
        else:
            await ctx.send("You just mentioned a non existent-personality\nFor personalities with spaces in them replace the spaces with a -")
