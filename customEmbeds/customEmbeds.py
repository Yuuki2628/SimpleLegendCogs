from redbot.core import commands
import discord

class CustomEmbeds(commands.Cog):
    """Embeds for Emilia and Alex"""

    @commands.command(name="emilia")
    async def Emilia(self, ctx):
        embed = discord.Embed(color=0x8A42F5)
        embed.add_field(name="", value="""```ansi
[1;35m┌─────────────────────┐
│Emilia     [35m[[36mEmily[35m]   │
│[34mSpecter    [35m[[34mSpecter[35m] │
└─────────────────────┘```
```ansi
[1;33m┌────────────────────────┐
│Jolteon      [Blitz]    │
├────────────────────────┤
│[36mAbility:     [31mVolt Absorb[33m│
├────────────────────────┤
│[0;32mThunderbolt  Bite       [1;33m│
│[0;32mHelping Hand Swift      [1;33m│
└────────────────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;35m┌──────────────────────────┐
│[35mGardevoir     [[36mSapphire[35m]  │
│[35m              [[34mAmethyst[35m]  │
├──────────────────────────┤[35m
│[36mAbility: [31m      Trace      [35m│
[35m│[34mSpectral Ability:         [35m│
│Star Illusionist          │
├──────────────────────────┤
│[32mDazzling Gleam  Psychic   [35m│
│[32mShadow Ball     Calm Mind [35m│
│[35mBlack Hole[35m                │
└──────────────────────────┘```""", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;30m┌────────────────────────┐
│Lairon        [Gundam]  │
├────────────────────────┤
│[36mAbility:[0m [31m     Rock Head [30m│
├────────────────────────┤
│[0;32mRock Slide    Headbutt  [30m│
│[0;32mIron head     Protect   [30m│
└────────────────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;34m┌────────────────────────────┐
│Primarina       [Melody]    │
├────────────────────────────┤
│[36mAbility: [31m       Liquid voice[34m│
├────────────────────────────┤
│[0;32mDisarming voice Icy wind    [34m│
│[0;32mSparkling Aria  Sing        [34m│
└────────────────────────────┘```        """, inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;36m┌─────────────────────────┐
│Bagon         [Blueberry]│
├─────────────────────────┤
│[36mAbility: [31m     Sheer force[36m│
├─────────────────────────┤
│[0;32mDragon claw   Crunch     [36m│
│[0;32mZen headbutt  Headbutt   [36m│
└─────────────────────────┘```        """, inline=True)
        embed.add_field(name="", value="""```ansi
[1;35m┌──────────────────────────────────────────────────────────────────┐
│                          Theme                            │
└──────────────────────────────────────────────────────────────────┘```
<https://youtu.be/WjpVUq7S0qY>""", inline=False)
        embed.set_footer(text="")        
        await ctx.send(embed=embed)