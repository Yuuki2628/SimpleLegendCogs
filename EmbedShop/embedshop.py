from redbot.core import commands
import discord

class EmbedShop(commands.Cog):
    """Embeds for the Elite Embed Updates"""

    @commands.command(name="es_shop")
    async def es_shop(self, ctx):
        if(ctx.author.id != 295275466703503372):
            return await ctx.send("Only the true bot director shall be allowed to do this")
        embed = discord.Embed(title="LeGeND Shop", description="Note: to purchase any item that doesn't have a command specified, dm <@598662722821029888>")
        embed.add_field(name="__Custom background__", value="Change the picture of your !profile background.\nCost: 800,000 credits", inline=False)
        embed.add_field(name="__Emoji Flair__", value="Add/Change an emoji in your nickname. No custom emojis allowed.\nCost: 200,000 credits", inline=False)
        embed.add_field(name="__Custom Command__", value="Have LeGeND Bot say a line of text or perform a command when people type !<a custom word>.\nCost: 500,000 credits", inline=False)
        embed.add_field(name="__Rare__", value="Appear on the top of the members list with an orange color name. Receive more credits in payday.\nCost: 1,500,000 credits.\nCommand: `!buyrare`", inline=False)
        embed.add_field(name="__Epic__", value="Appear higher than <@&815957842266816522> and with color Purple. Receive more credits in payday.\nCost: 3,500,000 credits.\nCommand: `!buyepic`", inline=False)
        embed.add_field(name="__Legendary__", value="Show you are a true LeGeND and appear higher than <@&815958568418803772> with a private LeGeND Channel. Receive more credits in payday.\nCost: 10,000,000 credits.\nCommand: `!buylegendary`", inline=False)
        embed.add_field(name="__Elite__", value="Join the most outstanding and limited club and appear higher than <@&815958673770807317> with a private LeGeND Channel.\nCost: 35,000,000 credits.\nCommand: `!buyelite`", inline=False)
        embed.add_field(name="__Custom Adventure Boss__", value="Ever wanted to fight yourself or some creature of your choise in adventure? It's your lucky day because now you can challenge anything with the power of this item.\nCost: 8,000,000 credits.\n<@&815958696982872075> or <@&815958379624529931> required.", inline=False)
        embed.add_field(name="__Set loot chest__", value="Are you a sets collector? Or are you simply looking for a new set to use in battle? You can buy a set chest from here.\nCost: 1,000,000 credits.\n<@&815958696982872075> or <@&815958379624529931> required.", inline=False)
        embed.add_field(name="**__NEW EMBED UPDATE__**", value="Do you want to make your custom commands look unique and special? Look no further, we (I) are proud to introduce the Embed update.\nThere are 2 different embed updates available for purchase:", inline=False)
        embed.add_field(name="__Simple Embed update__", value="Your command turns into a simple embed (no links or pictures)\nCost: 5,000,000.\n<@&815958673770807317> or <@&815958379624529931> required.", inline=False)
        embed.add_field(name="__Elite Embed update__", value="The simple update isn't enought for you? You can add links, picture and other cool stuff to you embed with this powerful update.\nThe Elite Embed update lets you personalize your embed command almost as you wish.\n||The result will be similar to the shop embed.||\nCost: 15,000,000.\n<@&815958696982872075> or <@&815958379624529931> required.", inline=False)
        await ctx.send(embed=embed)
        
    @commands.command(name="es_tshop")
    async def es_tshop(self, ctx):
        if(ctx.author.id != 295275466703503372):
            return await ctx.send("Only the true bot director shall be allowed to do this")
        embed = discord.Embed(title="LeGeND Shop", description="Note: to purchase any item that doesn't have a command specified, dm <@598662722821029888>")
        embed.add_field(name="__Custom background__", value="Change the picture of your !profile background.\nCost: 800,000 credits", inline=False)
        embed.add_field(name="__Emoji Flair__", value="Add/Change an emoji in your nickname. No custom emojis allowed.\nCost: 200,000 credits", inline=False)
        embed.add_field(name="__Custom Command__", value="Have LeGeND Bot say a line of text or perform a command when people type !<a custom word>.\nCost: 500,000 credits", inline=False)
        embed.add_field(name="__Rare__", value="Appear on the top of the members list with an orange color name. Receive more credits in payday.\nCost: 1,500,000 credits.\nCommand: `!buyrare`", inline=False)
        embed.add_field(name="__Epic__", value="Appear higher than <@&815957842266816522> and with color Purple. Receive more credits in payday.\nCost: 3,500,000 credits.\nCommand: `!buyepic`", inline=False)
        embed.add_field(name="__Legendary__", value="Show you are a true LeGeND and appear higher than <@&815958568418803772> with a private LeGeND Channel. Receive more credits in payday.\nCost: 10,000,000 credits.\nCommand: `!buylegendary`", inline=False)
        embed.add_field(name="__Elite__", value="Join the most outstanding and limited club and appear higher than <@&815958673770807317> with a private LeGeND Channel.\nCost: 35,000,000 credits.\nCommand: `!buyelite`", inline=False)
        await ctx.send(embed=embed)
        
    @commands.command(name="es_yuuki")
    async def es_yuuki(self, ctx):
        embed = discord.Embed(title="Yuuki's greatest achievements", icon="https://cdn.discordapp.com/avatars/295275466703503372/e1153ef5605d28556064ebd2881fd14b.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/295275466703503372/e1153ef5605d28556064ebd2881fd14b.png?size=4096")
        embed.add_field(name="**5th august 2020**", value="[Played the first 1,000,000,000 credits roulette with Jaymin](https://discord.com/channels/374596069989810176/698629712481747046/740519465837396029)", inline=False)
        embed.add_field(name="**7th august 2020**", value="[Reached 1,000,000,000 credits becoming the first <@&815958379624529931> ever on the server](https://discord.com/channels/374596069989810176/698629712481747046/741318683460370535)", inline=False)
        embed.add_field(name="**18th august 2020**", value="[Reached 2,000,000,000 credits\nGot the Billionaire role](https://discord.com/channels/374596069989810176/735808553872392262/745209602265579571)", inline=False)
        embed.add_field(name="**21st august 2020**", value="[Had 476 tickets as the season ends (2,380,000,000 credits worth)](https://discord.com/channels/374596069989810176/735808553872392262/746466988888424621)", inline=False)
        embed.add_field(name="**25th september 2020**", value="[Organized the biggest heist ever seen, with well over 80 players, breaking the bot](https://discord.com/channels/374596069989810176/381338682298466315/759074225209737316)", inline=False)
        embed.add_field(name="**24th december 2020**", value="[Got 100,000,000 credits on the first day of the season](https://discord.com/channels/374596069989810176/735808553872392262/791705199751856140)", inline=False)
        embed.add_field(name="**25th january 2021**", value="[Got to 1B credits with the help of numerous community members and got the 1.5M stats item](https://discord.com/channels/374596069989810176/727787873834631200/803306026190241804)\n[This day Yuuki killed an immortal, first recorded immortal kill in history](https://discord.com/channels/374596069989810176/735808553872392262/803366302634213407)\n[Total credits at the end of the day: 5,442,400,000](https://discord.com/channels/374596069989810176/727787873834631200/803684594246615120)", inline=False)
        embed.add_field(name="**18th february 2021**", value="[Caught a Greninja-Ash, the rarest pokemon for find in the wild](https://discord.com/channels/374596069989810176/708402441850323075/812055743368790046)", inline=False)
        await ctx.send(embed=embed)
