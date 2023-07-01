from .joinleave import JoinLeave


async def setup(bot):
    await bot.add_cog(JoinLeave())