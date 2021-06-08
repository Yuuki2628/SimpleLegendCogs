from redbot.core import Config
from redbot.core import commands
import discord

class JoinLeave(commands.Cog):
    """A cog to notify when someone joins or leaves the server"""

    def __init__(self,bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier = 26282562628)
        default_guild = {
            "blacklisted_words": []
        }

    @commands.group(pass_context=True)
    async def jlblacklist(self, ctx):
        pass

    # Type of retrieved value must be mutable (i.e. list or dict) in order to use a config value as a contextmanager.
    @jlblacklist.command(name="add")
    async def add_blacklist(self, ctx, *, words: str):
        """Adds one or more words to the blacklist"""
        words = ' '.join(words.split())
        wlist = words.split((' '))
        for word in wlist:
            async with self.config.guild(ctx.guild).blacklisted_words() as lst:
                if not word in lst:
                    lst.append(word)
        return ctx.send("Success.")

    @jlblacklist.command(name="remove")
    async def rem_blacklist(self, ctx, *, words: str):
        """Removed one or more words to the blacklist"""
        words = ' '.join(words.split())
        wlist = words.split((' '))
        for word in wlist:
            async with self.config.guild(ctx.guild).blacklisted_words() as lst:
                if word in lst:
                    lst.remove(word)
        return ctx.send("Success.")

    @jlblacklist.command(name="show")
    async def show_blacklist(self, ctx):
        """Displays the list of all blacklisted words"""
        async with self.config.guild(ctx.guild).blacklisted_words() as lst:
            for word in lst:
                wlist.append(word)
        slist = '\n'.join(wlist)
        embed=discord.Embed(title="Blackilsted words", description=slist)
        return ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name="gate-in-out")
        async with self.config.guild(ctx.guild).blacklisted_words() as lst:
            for word in lst:
                if(word.lower() in member.name.lower()):
                    embed = discord.Embed(title="Someone tried joining", color = 0x663399)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.add_field(name="**Member**", value=member.mention, inline=False)
                    embed.add_field(name="**Name**", value=f"{member.name}#{member.discriminator}", inline=False)

                    dm_channel = await member.create_dm()
                    await channel.send(f"You tried joining the server, but I found that your name contains something that might be self advertisement\nPlease remove {word} from your name and try joining again")
                    await self.kick(member)
                    return await ctx.send(embed=embed)

        if(channel in member.guild.channels):
            embed = discord.Embed(title="Someone joined", color = 0x2ECC71)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="**Member**", value=member.mention, inline=False)
            embed.add_field(name="**Name**", value=f"{member.name}#{member.discriminator}", inline=False)

            await channel.send(embed=embed)
        return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name="gate-in-out")
        if(channel in member.guild.channels):
            embed = discord.Embed(title="Someone left", color = 0xff0000)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="**Member**", value=member.mention, inline=False)
            embed.add_field(name="**Name**", value=f"{member.name}#{member.discriminator}", inline=False)

            await channel.send(embed=embed)
        return
        