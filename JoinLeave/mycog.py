from redbot.core import commands
import discord

class JoinLeave(commands.Cog):
    """A cog to notify when someone joins or leaves the server"""

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name="gate-in-out")
        #message = f"{member.mention} has joined the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        embed = discord.Embed(title="A new member joined")
        embed.set_thumbnail(f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png?size=1024".format(member))
        embed.add_field(name="**Member**", value=member.mention, inline=False)
        embed.add_field(name="**Name**", value="{member.name}#{member.discriminator}", inline=False)

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name="gate-in-out")
        #message = f"{member.mention} has left the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        embed = discord.Embed(title="A member left")
        embed.set_thumbnail(f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png?size=1024".format(member))
        embed.add_field(name="**Member**", value=member.mention, inline=False)
        embed.add_field(name="**Name**", value="{member.name}#{member.discriminator}", inline=False)

        await channel.send(embed=embed)
        