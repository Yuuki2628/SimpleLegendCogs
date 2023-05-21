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
│[0;32m  Moon Blast  [1;35m║[0;32m    Psychic   [1;35m│
╞══════════════╬══════════════╡
│[0;32m Shadow Ball  [1;35m║[0;32m   Calm Mind  [1;35m│
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
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;35m┌───────────────────────────────────────────────────────────┐
│                          Themes                           │
└───────────────────────────────────────────────────────────┘```
Emilia's [Theme](https://youtu.be/6lAIQu_1YVU)
Specter's [Theme](https://youtu.be/K0GkcT7ReKs)""", inline=False)
        embed.set_footer(text="")
        await ctx.send(embed=embed)

    @commands.command(name="ayaka")
    async def Ayaka(self, ctx):
        embed = discord.Embed(color=0x268BD2)
        embed.add_field(name="", value="""```ansi
[1;34m┌───────────────────────────┐
│         Kamisato          │
│           Ayaka           │
└───────────────────────────┘
┌───────────────────────────┐
│      Aurorus[Amelia]      │
├───────────────────────────┤
│     [36mAbility: [31mSnow Warning [34m│
├─────────────╥─────────────┤
│  [0;32mBlizzard   [1;34m║ [0;32mFreeze Dry  [1;34m│
╞═════════════╬═════════════╡
│ [0;32mEarth Power [1;34m║ [0;32mHidden Power[1;34m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[34m┌───────────────────────────┐
│      [1;35mDitto[[34mDominiel[35m]      [0;34m│
├───────────────────────────┤
│     [1;36mAbility: [31mImposter     [0;34m│
│     [1mSpectral Ability:     [0;34m│
│      [1;36mPerfect copy         [0;34m│
├─────────────╥─────────────┤
│     [1;30m???     [0;34m║     [1;30m???     [0;34m│
╞═════════════╬═════════════╡
│     [1;30m???     [0;34m║     [1;30m???     [0;34m│
╞═════════════╩═════════════╡
│      [1;35mReplica attack       [0;34m│
└───────────────────────────┘```""", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;34m┌───────────────────────────┐
│      Walrein[Olaf]        │
├───────────────────────────┤
│     [36mAbility: [31mOblivious    [34m│
├─────────────╥─────────────┤
│    [0;32mToxic    [1;34m║     [0;32mSurf    [1;34m│
╞═════════════╬═════════════╡
│    [0;32mRoar     [1;34m║   [0;32mProtect   [1;34m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;34m┌───────────────────────────┐
│     Froslass[Crystal]     │
├───────────────────────────┤
│     [36mAbility: [31mSnow Cloak   [34m│
├─────────────╥─────────────┤
│  [0;32mBlizzard   [1;34m║ [0;32mShadow ball [1;34m│
╞═════════════╬═════════════╡
│ [0;32mThunderbolt [1;34m║ [0;32mConfuse Ray [1;34m│
└─────────────╨─────────────┘```        """, inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;34m┌───────────────────────────┐
│      Milotic[Meru]        │
├───────────────────────────┤
│     [36mAbility: [31mMarvel Scale [1;34m│
├─────────────╥─────────────┤
│    [0;32mScald    [1;34m║   [0;32mRecover   [1;34m│
╞═════════════╬═════════════╡
│    [0;32mToxic    [1;34m║   [0;32mIce Beam  [1;34m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[1;34m┌───────────────────────────┐
│      Weavile[Silver]      │
├───────────────────────────┤
│     [36mAbility: [31mPressure     [1;34m│
├─────────────╥─────────────┤
│  [0;32mKnock off  [1;34m║ [0;32mIcicle Crash[1;34m│
╞═════════════╬═════════════╡
│  [0;32mIce shard  [1;34m║   [0;32mPursuit   [1;34m│
└─────────────╨─────────────┘```""", inline=True)
        embed.set_footer(text="")
        await ctx.send(embed=embed)

    @commands.command(name="monarch")
    async def Monarch(self, ctx):
        embed = discord.Embed(color=0xFFFFFF)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────┐
│          [1;34mMonarch          [0;37m│
│           [1m[[34m???[0;37m]           │
└───────────────────────────┘``````ansi
[37m┌───────────────────────────┐
│      [1;35mHisuian Zoroark      [0;37m│
├───────────────────────────┤
│     [1;36mAbility: [30mIllusion     [0;37m│
├─────────────╥─────────────┤
│[1mExtrasensory [0;37m║ [1mShadow Ball [0;37m│
╞═════════════╬═════════════╡
│    [1mSlash    [0;37m║ [1mShadow Claw [0;37m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────┐
│      [1;35mAlolan Nineales      [0;37m│
│           [1m[[35m???[37m]           [0;37m│
├───────────────────────────┤
│    [1;36mAbility: [30mSnow Cloak    [0;37m│
│     [1;34mSpectral Ability:     [0;37m│
│        [1;35mIce Mirror         [0;37m│
├─────────────╥─────────────┤
│ [1mFreeze Dry  [0;37m║  [1mMoon Blast [0;37m│
╞═════════════╬═════════════╡
│    [1mHail     [0;37m║ [1mAurora Veil [0;37m│
╞═════════════╩═════════════╡
│          Ice Age          │
└───────────────────────────┘```""", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────┐
│         [1;35mVolcarona         [0;37m│
├───────────────────────────┤
│     [1;36mAbility: [30mFlame body   [0;37m│
├─────────────╥─────────────┤
│ [1mFiery Dance [0;37m║ [1mQuiver Dance[0;37m│
╞═════════════╬═════════════╡
│  [1mBug Buzz   [0;37m║    [1mRoost    [0;37m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────┐
│         [1;35mAegislash         [0;37m│
├───────────────────────────┤
│  [1;36mAbility: [30mStance Change [0;37m│
├─────────────╥─────────────┤
│[1mKing's Shield[0;37m║   [1m Gyro Ball[0;37m│
╞═════════════╬═════════════╡
│[1m    Toxic    [0;37m║ [1m Shadow Ball[0;37m│
└─────────────╨─────────────┘```        """, inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────┐
│           [1;35mLugia           [0;37m│
├───────────────────────────┤
│     [1;36mAbility: [30mMulticale    [0;37m│
├─────────────╥─────────────┤
│[1mExtrasensory [0;37m║  [1mAeroblast  [0;37m│
╞═════════════╬═════════════╡
│  [1mCalm Mind  [0;37m║   [1mRecover   [0;37m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────┐
│         [1;35mReshiram          [0;37m│
├───────────────────────────┤
│     [1;36mAbility: [30mTurboblaze   [0;37m│
├─────────────╥─────────────┤
│ [1mBlue Flare  [0;37m║ [1mDraco Meteor[0;37m│
╞═════════════╬═════════════╡
│ [1mEarth Power [0;37m║    [1mRoost    [0;37m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[1;32m┌───────────────────────────┐
│         [0;32mRayquaza          [1m│
├───────────────────────────┤
│     [0;36mAbility: [31mAir Lock     [1;32m│
├─────────────╥─────────────┤
│[0;32mDragon Ascent[1m║ [0;32mDragon Dance[1m│
╞═════════════╬═════════════╡
│[0;32mExtreme Speed[1m║[0;32m   Outrage   [1m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────┐
│[1;34;40m         Dragalisk         [0;37m│
├───────────────────────────┤
│     [1;36mAbility: [34;40mDread Space[0;37m  │
├─────────────╥─────────────┤
│[1;30;40m  Void Star  [0;37m║  [1mDark Pulse [0;37m│
╞═════════════╬═════════════╡
│ [1mEarthquake  [0;37m║   [1mOutrage   [0;37m│
└─────────────╨─────────────┘```""", inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="""```ansi
[37m┌───────────────────────────────────────────────────────────┐
│                          [1;34mThemes                           [0;37m│
└───────────────────────────────────────────────────────────┘```
[Amanda](https://youtu.be/EZ_YlKqEQRE)
[Monarch](https://youtu.be/US8JrKjHYvc)
[Dragalisk](https://youtu.be/FMlUKd7DyPk)
[Complete Dragalisk](https://youtu.be/b6WhRKOMUq0)
[Final Phase](https://youtu.be/ocGrewzxOuw)
""", inline=False)
        embed.set_footer(text="")
        await ctx.send(embed=embed)