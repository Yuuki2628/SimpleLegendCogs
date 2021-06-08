from redbot.core import Config
from redbot.core import commands
import discord

class JoinLeave(commands.Cog):
    """A cog to notify when someone joins or leaves the server"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier = 26282562628)
        default_guild = {
            "blwords": [],
            "jlchannel": None
        }

        self.config.register_guild(**default_guild)

    @commands.command()
    @commands.guild_only()
    async def setchannel(self, ctx, ch: discord.TextChannel):
        await self.config.guild(ctx.guild).jlchannel.set(ch.id)
        return await ctx.send("Success!")


    @commands.group(pass_context=True)
    @commands.guild_only()
    async def jlblacklist(self, ctx):
        """Used to manage the words blacklist that people can't have in their name when joining"""
        pass

    @jlblacklist.command(name="add")
    @commands.guild_only()
    async def add_blacklist(self, ctx, *, words: str):
        """Adds one or more words to the blacklist"""
        words = ' '.join(words.split())
        wlist = words.split((' '))
        async with self.config.guild(ctx.guild).blwords() as lst:
            for word in wlist:
                if not word in lst:
                    lst.append(word)
        return await ctx.send("Success.")

    @jlblacklist.command(name="remove")
    @commands.guild_only()
    async def rem_blacklist(self, ctx, *, words: str):
        """Removed one or more words to the blacklist"""
        words = ' '.join(words.split())
        wlist = words.split((' '))
        async with self.config.guild(ctx.guild).blwords() as lst:
            for word in wlist:
                if word in lst:
                    lst.remove(word)
                    await ctx.send(f"Removed {word}")

    @jlblacklist.command(name="show")
    @commands.guild_only()
    async def show_blacklist(self, ctx):
        """Displays the list of all blacklisted words"""
        wlist = []
        async with self.config.guild(ctx.guild).blwords() as lst:
            for word in lst:
                wlist.append(word)
            if len(wlist) is 0:
                slist = "There are no blacklister words right now"
            else:
                slist = '\n'.join(wlist)
        embed=discord.Embed(title="Blacklisted words", description=slist, color = 0x663399)
        return await ctx.send(embed=embed)



    @commands.Cog.listener()
    async def on_member_join(self, member):
        myguild = member.guild
        chid = await self.config.guild(myguild).jlchannel()
        channel = discord.utils.get(myguild.channels, id = chid)
        if channel is None:
            return
        async with self.config.guild(myguild).blwords() as lst:
            for word in lst:
                if(word.lower() in member.name.lower()):
                    embed = discord.Embed(title="Someone tried joining", color = 0x663399)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.add_field(name="**Member**", value=member.mention, inline=False)
                    embed.add_field(name="**Name**", value=f"{member.name}#{member.discriminator}", inline=False)
                    embed.add_field(name="**Blacklisted word**", value=f"{word}", inline=False)

                    dm_channel = await member.create_dm()
                    await dm_channel.send(f"You tried joining the server, but I found that your name contains something that might be self advertisement\nPlease remove `{word}` from your name and try joining again")
                    await myguild.kick(member, reason=f"Username contained: {word}, possible spam")
                    return await channel.send(embed=embed)

        if(channel in member.guild.channels):
            embed = discord.Embed(title="Someone joined", color = 0x2ECC71)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="**Member**", value=member.mention, inline=False)
            embed.add_field(name="**Name**", value=f"{member.name}#{member.discriminator}", inline=False)

            await channel.send(embed=embed)
        return

    @commands.Cog.listener()
    async def on_member_remove(self,  member):
        myguild = member.guild
        chid = await self.config.guild(myguild).jlchannel()
        channel = discord.utils.get(myguild.channels, id = chid)
        if channel is None:
            return
        if(channel in member.guild.channels):
            embed = discord.Embed(title="Someone left", color = 0xff0000)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="**Member**", value=member.mention, inline=False)
            embed.add_field(name="**Name**", value=f"{member.name}#{member.discriminator}", inline=False)

            await channel.send(embed=embed)
        return
        