from redbot.core import commands
import discord

class JoinLeave(commands.Cog):
    """A cog to notify when someone joins or leaves the server"""

    def listener(name=None):
        return lambda x:x

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = 746001104336322611
        message = f"{member.mention} has joined the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        await channel.send(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = 746001104336322611
        message = f"{member.mention} has joined the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        await channel.send(message)
        