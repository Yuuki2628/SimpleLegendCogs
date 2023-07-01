from .rep import Reputation

async def setup(bot):
    await bot.add_cog(Reputation(bot))