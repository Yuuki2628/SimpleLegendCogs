from redbot.core import commands
import discord

class JoinLeave(commands.Cog):
    """A cog to notify when someone joins or leaves the server"""

    @client.event
    async def on_member_join(self, member):
        channel = 374597911436328971
        message = f"{member.mention} has joined the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        await channel.send(message)

    @client.event
    async def on_member_remove(self, member):
        channel = 374597911436328971
        message = f"{member.mention} has joined the server\nUser id: {member.id}\nCurrent name: {member.name}#{member.discriminator}"
        await channel.send(message)
        