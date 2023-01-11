from redbot.core import commands
import discord

class CustomEmbeds(commands.Cog):
    """Embeds for Emilia and Alex"""

    emilia_embed_text = "```ansi"
    "[1;35m┌──────────────────────────────────┐"
    "│Emilia/[34mSpecter    [35m[[36mEmily[35m]         │"
    "└──────────────────────────────────┘"
    "┌──────────────────────────────────┐"
    "│[35mGardevoir     [[36mSapphire[35m/[34mAmethyst[35m] │"
    "├──────────────────────────────────┤[35m"
    "│[36mAbility: [31m         Trace           [35m│"
    "[35m│[34mSpectral Ability: [35mStar Illusionist│[35m"
    "├──────────────────────────────────┤"
    "│[32mDazzling Gleam    Psychic         [35m│"
    "│[32mShadow Ball       Calm Mind       [35m│"
    "│[35mBlack Hole[35m                        │"
    "└──────────────────────────────────┘"
    "[33m┌──────────────────────────────────┐"
    "│Jolteon           [Blitz]         │"
    "├──────────────────────────────────┤"
    "│[36mAbility:          [31mVolt Absorb     [33m│"
    "├──────────────────────────────────┤"
    "│[0;32mThunderbolt       Bite            [1;33m│"
    "│[0;32mHelping Hand      Swift           [1;33m│"
    "└──────────────────────────────────┘"
    "[30m┌──────────────────────────────────┐"
    "│Lairon            [Gundam]        │"
    "├──────────────────────────────────┤"
    "│[36mAbility:[0m [31m         Rock Head       [30m│"
    "├──────────────────────────────────┤"
    "│[0;32mRock Slide        Headbutt        [30m│"
    "│[0;32mIron head         Protect         [30m│"
    "└──────────────────────────────────┘"
    "[34m┌──────────────────────────────────┐"
    "│Primarina         [Melody]        │"
    "├──────────────────────────────────┤"
    "│[36mAbility: [31m         Liquid voice    [34m│"
    "├──────────────────────────────────┤"
    "│[0;32mDisarming voice   Icy wind        [34m│"
    "│[0;32mSparkling Aria    Sing            [34m│"
    "└──────────────────────────────────┘"
    "[36m┌──────────────────────────────────┐"
    "│Bagon             [Blueberry]     │"
    "├──────────────────────────────────┤"
    "│[36mAbility: [31m         Sheer force     [36m│"
    "├──────────────────────────────────┤"
    "│[0;32mDragon claw       Crunch          [36m│"
    "│[0;32mZen headbutt      Headbutt        [36m│"
    "└──────────────────────────────────┘"
    "[35m┌──────────────────────────────────┐"
    "│              Theme               │"
    "└──────────────────────────────────┘```"
    "<https://youtu.be/WjpVUq7S0qY>"

    @commands.command(name="es_yuuki")
    async def Emilia(self, ctx):
        emily = ctx.guild.get_member(675020556655001611)
        embed = discord.Embed(color=0x8A42F5)
        embed.set_thumbnail(url=emily.avatar_url)
        embed.add_field(name="", value=emilia_embed_text, inline=False)
        embed.set_footer(text="")        
        await ctx.send(embed=embed)