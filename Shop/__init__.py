from .shop import Shop


async def setup(bot):
    await bot.add_cog(Shop())
