from .embedshop import EmbedShop


async def setup(bot):
    await bot.add_cog(EmbedShop())