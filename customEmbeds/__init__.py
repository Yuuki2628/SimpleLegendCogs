from .customEmbeds import CustomEmbeds


async def setup(bot):
    await bot.add_cog(CustomEmbeds())