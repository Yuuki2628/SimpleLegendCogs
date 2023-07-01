from .roleplay import Roleplay


async def setup(bot):
    await bot.add_cog(Roleplay())
