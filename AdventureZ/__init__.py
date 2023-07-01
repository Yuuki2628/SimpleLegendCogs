from .adventurez import AdventureZ


async def setup(bot):
    await bot.add_cog(AdventureZ())