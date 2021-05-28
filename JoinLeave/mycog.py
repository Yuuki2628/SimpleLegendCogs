from redbot.core import commands
import discord

class JoinLeave(commands.Cog):
    """A cog to notify when someone joins or leaves the server"""

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name="gate-in-out")
        message = f"{member.mention} has joined the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        await channel.send(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name="gate-in-out")
        message = f"{member.mention} has left the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        await channel.send(message)
        