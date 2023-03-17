from redbot.core import commands
import discord

class CustomEmbeds(commands.Cog):
    """Embeds for Emilia and Alex"""

    @commands.command(name="emilia")
    async def Emilia(self, ctx):
        embed = discord.Embed(color=0x8A42F5)
        embed.add_field(name="", value="""```ansi
[1;35m┌─────────────────────────┐
│      Emilia[35m[[36mEmily[35m]      │
│      [34mTenebria[35m[[34mTene[35m]     │
└─────────────────────────┘``````ansi
[1;33m┌─────────────────────────┐
│     Jolteon[Blitz]      │
├─────────────────────────┤
│     [36mAbility:[31mVolt Absorb[33m │
├────────────╥────────────┤
│[0;32mThunderbolt [1;33m║[0;32m    Bite    [1;33m│
╞════════════╬════════════╡
│[0;32mHelping Hand[1;33m║[0;32m   Agility  [1;33m│
└────────────╨────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;35m┌─────────────────────────────┐
│     [35mGardevoir[[36mSapphire[35m]     │
│     [35m         [[34mAmethyst[35m]     │
├─────────────────────────────┤[35m
│[36m      Ability: [31m  Trace       [35m│
[35m│      [34mSpectral Ability:      [35m│
│      Star Illusionist       │
├──────────────╥──────────────┤
│[32m  Moon Blast  [1;35m║[0;32m    Psychic   [1;35m│
╞══════════════╬══════════════╡
│[32m Shadow Ball  [1;35m║[0;32m   Calm Mind  [1;35m│
╞══════════════╩══════════════╡
│[1;35;40m          Black Hole         [0;1;35m│
└─────────────────────────────┘```""", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;30m┌─────────────────────────┐
│      Lairon[Gundam]     │
├─────────────────────────┤
│     [36mAbility:[31mRock Head   [30m│
├────────────╥────────────┤
│ [0;32mRock Slide [1;30m║[0;32m  Headbutt  [1;30m│
╞════════════╬════════════╡
│ [0;32mIron head  [1;30m║[0;32m   Protect  [1;30m│
└────────────╨────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;34m┌─────────────────────────────┐
│      Primarina[Melody]      │
├─────────────────────────────┤
│        [36mAbility:[31mLiquid voice [34m│
├───────────────╥─────────────┤
│[0;32m  Moon Blast   [1;34m║[0;32m   Icy wind  [1;34m│
╞═══════════════╬═════════════╡
│[0;32mSparkling Aria [1;34m║[0;32m     Sing    [1;34m│
└───────────────╨─────────────┘```        """, inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;36m┌─────────────────────────┐
│       Bagon[Blueberry]  │
├─────────────────────────┤
│     [36mAbility:[31mSheer force [36m│
├────────────╥────────────┤
│[0;32mDragon claw [1;36m║[0;32m   Crunch   [1;36m│
╞════════════╬════════════╡
│[0;32mZen headbutt[1;36m║[0;32m  Headbutt  [1;36m│
└────────────╨────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;37m┌─────────────────────────────┐
│          Absol[Twilight]    │
├─────────────────────────────┤
│        [36mAbility:[31mSuper luck   [37m│
├───────────────╥─────────────┤
│[0;32m  Night Slash  [1;37m║[0;32m    Slash    [1;37m│
╞═══════════════╬═════════════╡
│[0;32m  Sword Dance  [1;37m║[0;32m    Detect   [1;37m│
└───────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;35m┌───────────────────────────────────────────────────────────┐
│                          Themes                           │
└───────────────────────────────────────────────────────────┘```
Emilia's [Theme](https://youtu.be/6lAIQu_1YVU)
Specter's [Theme](https://youtu.be/K0GkcT7ReKs)""", inline=False)
        embed.set_footer(text="")        
        await ctx.send(embed=embed)

    @commands.command(name="monarch")
    async def Monarch(self, ctx):
        embed = discord.Embed(color=0x8A42F5)
        embed.add_field(name="", value="""```ansi
[1;35m┌─────────────────────────┐
│      Emilia[35m[[36mEmily[35m]      │
│    [34mTenebria[35m[[34mTene[35m]       │
└─────────────────────────┘``````ansi
[1;33m┌─────────────────────────┐
│     Jolteon[Blitz]      │
├─────────────────────────┤
│     [36mAbility:[31mVolt Absorb[33m │
├────────────╥────────────┤
│[0;32mThunderbolt [1;33m║[0;32mBite        [1;33m│
╞════════════╬════════════╡
│[0;32mHelping Hand[1;33m║[0;32mAgility     [1;33m│
└────────────╨────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;35m┌─────────────────────────────┐
│     [35mGardevoir[[36mSapphire[35m]     │
│     [35m         [[34mAmethyst[35m]     │
├─────────────────────────────┤[35m
│[36m      Ability: [31m  Trace       [35m│
[35m│      [34mSpectral Ability:      [35m│
│      Star Illusionist       │
├──────────────╥──────────────┤
│[32mMoon Blast    [1;35m║[0;32mPsychic       [1;35m│
╞══════════════╬══════════════╡
│[32mShadow Ball   [1;35m║[0;32mCalm Mind     [1;35m│
╞══════════════╩══════════════╡
│[1;35;40m          Black Hole         [0;1;35m│
└─────────────────────────────┘```""", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;30m┌─────────────────────────┐
│      Lairon[Gundam]     │
├─────────────────────────┤
│     [36mAbility:[31mRock Head   [30m│
├────────────╥────────────┤
│[0;32mRock Slide  [1;30m║[0;32mHeadbutt    [1;30m│
╞════════════╬════════════╡
│[0;32mIron head   [1;30m║[0;32mProtect     [1;30m│
└────────────╨────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;34m┌─────────────────────────────┐
│      Primarina[Melody]      │
├─────────────────────────────┤
│        [36mAbility:[31mLiquid voice [34m│
├───────────────╥─────────────┤
│[0;32mMoon Blast     [1;34m║[0;32mIcy wind     [1;34m│
╞═══════════════╬═════════════╡
│[0;32mSparkling Aria [1;34m║[0;32mSing         [1;34m│
└───────────────╨─────────────┘```        """, inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;36m┌─────────────────────────┐
│       Bagon[Blueberry]  │
├─────────────────────────┤
│     [36mAbility:[31mSheer force [36m│
├────────────╥────────────┤
│[0;32mDragon claw [1;36m║[0;32mCrunch      [1;36m│
╞════════════╬════════════╡
│[0;32mZen headbutt[1;36m║[0;32mHeadbutt    [1;36m│
└────────────╨────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;37m┌─────────────────────────────┐
│          Absol[Twilight]    │
├─────────────────────────────┤
│        [36mAbility:[31mSuper luck   [37m│
├───────────────╥─────────────┤
│[0;32mNight Slash    [1;37m║[0;32mSlash        [1;37m│
╞═══════════════╬═════════════╡
│[0;32mSword Dance    [1;37m║[0;32mDetect       [1;37m│
└───────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;35m┌───────────────────────────────────────────────────────────┐
│                          Themes                           │
└───────────────────────────────────────────────────────────┘```
Emilia's [Theme](https://youtu.be/6lAIQu_1YVU)
Specter's [Theme](https://youtu.be/K0GkcT7ReKs)""", inline=False)
        embed.set_footer(text="")        
        await ctx.send(embed=embed)