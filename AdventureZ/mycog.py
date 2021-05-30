from redbot.core import commands
import discord

class AdventureZ(commands.Cog):
    """Extra adventure commands, like the good ol'Z commands and grindsquad"""

    @commands.command(name="z")
    async def zCMD(self, ctx, *, msg):
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
            await ctx.send("0.8 / 2")
        elif msg == "dumb":
            await ctx.send("0.8 / 2")
        elif msg == "enlightened":
            await ctx.send("0.8 / 2")
        elif msg == "fairly-intelligent":
            await ctx.send("0.8 / 2")
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

    @commands.command(name="grindsquad", aliases=["gs"])
    async def grindsquad(ctx):
        file = open(".grindsquad.txt", "r")
        flines = file.read()
        gs = flines.split("\n")

        msg = f"{ctx.author.mention} is a nab and is begging for the help of "

        for member in gs:
            if ctx.guild.get_member(member.id) is not None:
                msg = msg + f"{member.mention}, "
        msg.removesuffix(", ")
        msg = msg + "to defeat a powerful foe\n||not actually that powerful||"

        await ctw.send(msg)

    @commands.command(name="grindsquad add", aliases=["gsa"])
    async def grindsquad_add(ctx, grinder: discord.Member = None):
        file = open(".grindsquad.txt", "r")
        flines = file.read()
        gs = flines.split("\n")
        if grinder:
            gs.append(grinder.id)
        else:
            gs.append(ctx.author.id)
        file.truncate(0)
        file.close()
        with open(".grindsquad.txt", "w") as flines:
            flines = "\n".join(gs)
            file.write(flines)

    @commands.command(name="grindsquad remove", aliases=["gsr"])
    async def grindsquad_rem(ctx, grinder: discord.Member = None):
        file = open("grindsquad.txt", "r")
        flines = file.read()
        gs = flines.split("\n")
        file.close()

        if grinder is None:
            todelete = ctx.author.id
        else:
            todelete = grinder.id
        
        if todelete in gs:
            pos = gs.index(todelete)
        else:
            return await ctx.send("I can't find the person in the grindsquad")
        
        file = open("grindsquad.txt", "w")
        file.truncate(0)
        del gs[pos]
        for line in gs:
            file.write(line)