from redbot.core import commands
import discord

class EmbedShop(commands.Cog):
    """Embeds for the Elite Embed Updates"""

#Billionaire: 815958379624529931
#Elite: 815958696982872075
#Legendary: 815958673770807317
#Epic: 815958568418803772
#Rare: 815957842266816522

    @commands.command(name="es_yuuki")
    async def es_yuuki(self, ctx):
        yuuki = ctx.guild.get_member(295275466703503372)
        embed = discord.Embed(color=0x5C4399)
        embed.set_author(name="Yuuki's greatest achievements", url="https://discordapp.com/users/295275466703503372/", icon_url="https://cdn.discordapp.com/attachments/374597952813137931/850344030936236052/G-PFP4.gif")
        embed.set_thumbnail(url=yuuki.avatar_url)
        embed.add_field(name="**5th august 2020**", value="[[link] ](https://discord.com/channels/374596069989810176/698629712481747046/740519465837396029)Played the first 1,000,000,000 credits roulette with Jaymin", inline=False)
        embed.add_field(name="**7th august 2020**", value="[[link] ](https://discord.com/channels/374596069989810176/698629712481747046/741318683460370535)Reached 1,000,000,000 credits becoming the first <@&815958379624529931> ever on the server", inline=False)
        embed.add_field(name="**18th august 2020**", value="[[link] ](https://discord.com/channels/374596069989810176/735808553872392262/745209602265579571)Reached 2,000,000,000 credits", inline=False)
        embed.add_field(name="**21st august 2020**", value="[[link] ](https://discord.com/channels/374596069989810176/735808553872392262/746466988888424621)Had 476 tickets as the season ends (which are worth 2,380,000,000 credits)", inline=False)
        embed.add_field(name="**25th september 2020**", value="[[link] ](https://discord.com/channels/374596069989810176/381338682298466315/759074225209737316)Organized the biggest heist ever seen, with well over 80 players, breaking the bot", inline=False)
        embed.add_field(name="**24th december 2020**", value="[[link] ](https://discord.com/channels/374596069989810176/735808553872392262/791705199751856140)Got 100,000,000 credits on the first day of the season", inline=False)
        embed.add_field(name="**25th january 2021**", value="[[link] ](https://discord.com/channels/374596069989810176/727787873834631200/803306026190241804)Got to 1B credits with the help of numerous community members and got the 1.5M stats item\n"
                                                            "[[link] ](https://discord.com/channels/374596069989810176/735808553872392262/803366302634213407)This day Yuuki killed an immortal, first recorded immortal kill in history\n"
                                                            "[[link] ](https://discord.com/channels/374596069989810176/727787873834631200/803684594246615120)Total credits at the end of the day: 5,442,400,000", inline=False)
        embed.add_field(name="**18th february 2021**", value="[[link] ](https://discord.com/channels/374596069989810176/708402441850323075/812055743368790046)Caught a Greninja-Ash, the rarest pokemon for find in the wild", inline=False)
        embed.add_field(name="**13th june 2021**", value="[[link] ](https://discord.com/channels/374596069989810176/374597952813137931/853616788256063498)Reached 100 rep points", inline=False)
        embed.set_footer(text="")        
        await ctx.send(embed=embed)

    @commands.command(name="es_artcontests")
    async def es_artcontests(self,ctx):
        embed=discord.Embed(title="Legend Art competitions",color=0x5C4399)
        embed.add_field(name="First competition", value="Theme: `digital art`\n[[link]](https://discord.com/channels/374596069989810176/423094817371848716/860714613312847873)\nCommand: `!art1`",inline=False)
        embed.add_field(name="Second competition", value="Theme: `thumbnail`\n[[link]](https://discord.com/channels/374596069989810176/423094817371848716/875936443980214352)\nCommand: `!art2`",inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="es_artcontestwinners1")
    async def es_artcontestwinners1(self, ctx):
        #winners: Prafull Jadhav, Phantom, Yuuki
        winner1 = ctx.guild.get_member(297069502787485696)
        winner2 = ctx.guild.get_member(309150039274422282)
        winner3 = ctx.guild.get_member(295275466703503372)

        img = [
            "https://cdn.discordapp.com/attachments/423094817371848716/860718528029786163/Screenshot_20210703-083350.jpg",
            "https://cdn.discordapp.com/attachments/423094817371848716/860714958432894986/IMG-20210703-WA0000.jpg",
            "https://cdn.discordapp.com/attachments/423094817371848716/860715113555296256/asunaScan.jpg"
        ]
        avatars = [
            winner1.avatar_url,
            winner2.avatar_url,
            winner3.avatar_url
        ]
        winners = [
            "Prafull Jadhav",
            "Phantom",
            "Yuuki"
        ]
        winnersID = [
            winner1.id,
            winner2.id,
            winner3.id
        ]

        embed0 = discord.Embed(title="Legend Art competition winners",color=0x5C4399)
        embed0.add_field(name="Top 3",value=f"**1st place**\n[{winners[0]}](https://discordapp.com/users/{winnersID[0]})\n\n**2nd place**\n[{winners[1]}](https://discordapp.com/users/{winnersID[1]})\n\n**3rd place**\n[{winners[2]}](https://discordapp.com/users/{winnersID[2]})\n\n**[All the partecipants pictures](https://discord.com/channels/374596069989810176/423094817371848716/860714613312847873)**")

        embed1 = discord.Embed(title=winners[0], url=f"https://discordapp.com/users/{winnersID[0]}/", color=0xFFD700)
        embed2 = discord.Embed(title=winners[1], url=f"https://discordapp.com/users/{winnersID[1]}/", color=0xD3D3D3)
        embed3 = discord.Embed(title=winners[2], url=f"https://discordapp.com/users/{winnersID[2]}/", color=0xcd7f32)

        embed1.set_thumbnail(url=avatars[0])
        embed2.set_thumbnail(url=avatars[1])
        embed3.set_thumbnail(url=avatars[2])

        embed1.add_field(name="30 votes",value="Scenery")
        embed2.add_field(name="18 votes",value="Jean\nGenshin Impact")
        embed3.add_field(name="13 votes",value="Asuna\nSword Art Online")

        embed1.set_image(url=img[0])
        embed2.set_image(url=img[1])
        embed3.set_image(url=img[2])

        await ctx.send(embed=embed0)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)

    @commands.command(name="es_artcontestwinners2")
    async def es_artcontestwinners2(self, ctx):
        #winners: Fyn8, Ha§nain, Burning Rocker
        winner1 = ctx.guild.get_member(550785477884510208)
        winner2 = ctx.guild.get_member(809814468422664233)
        winner3 = ctx.guild.get_member(740113949504045097)

        img = [
            "https://cdn.discordapp.com/attachments/423094817371848716/875936637375381555/ks_thumbnail_2.png",
            "https://cdn.discordapp.com/attachments/423094817371848716/875936551761240084/20210806_181622.png",
            "https://cdn.discordapp.com/attachments/423094817371848716/875936610456326154/image0-1.png"
            ]
        avatars = [
            winner1.avatar_url,
            winner2.avatar_url,
            winner3.avatar_url
        ]
        winners = [
            "Fyn8",
            "Ha§nain",
            "Burning Rocker"
        ]
        winnersID = [
            winner1.id,
            winner2.id,
            winner3.id
        ]

        embed0 = discord.Embed(title="Legend Art competition winners",color=0x5C4399)
        embed0.add_field(name="Top 3",value=f"**1st place**\n[{winners[0]}](https://discordapp.com/users/{winnersID[0]})\n\n**2nd place**\n[{winners[1]}](https://discordapp.com/users/{winnersID[1]})\n\n**3rd place**\n[{winners[2]}](https://discordapp.com/users/{winnersID[2]})\n\n**[All the partecipants pictures](https://discord.com/channels/374596069989810176/423094817371848716/875936443980214352)**")

        embed1 = discord.Embed(title=winners[0], url=f"https://discordapp.com/users/{winnersID[0]}/", color=0xFFD700)
        embed2 = discord.Embed(title=winners[1], url=f"https://discordapp.com/users/{winnersID[1]}/", color=0xD3D3D3)
        embed3 = discord.Embed(title=winners[2], url=f"https://discordapp.com/users/{winnersID[2]}/", color=0xcd7f32)

        embed1.set_thumbnail(url=avatars[0])
        embed2.set_thumbnail(url=avatars[1])
        embed3.set_thumbnail(url=avatars[2])

        embed1.add_field(name="30 votes",value="Noobcraft: episode 69 - Raiding bastions like a noob")
        embed2.add_field(name="16 votes",value="Ranked games with Legend family members")
        embed3.add_field(name="14 votes",value="LeGeND Gaming Family")

        embed1.set_image(url=img[0])
        embed2.set_image(url=img[1])
        embed3.set_image(url=img[2])

        await ctx.send(embed=embed0)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        