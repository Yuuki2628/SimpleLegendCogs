from redbot.core import commands
import discord

from adventure.charsheet import Item, Character
from redbot.core import checks

class Shop(commands.Cog):
    """Buy items"""

#Billionaire: 815958379624529931
#Elite: 815958696982872075
#Legendary: 815958673770807317
#Epic: 815958568418803772
#Rare: 815957842266816522

    @commands.command(name="es_shop")
    async def shop(self, ctx):
        if(ctx.author.id != 295275466703503372):
            return await ctx.send("Only the true bot director shall be allowed to do this")
        embed = discord.Embed(title="LeGeND Shop",color=0x7289DA)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/722551851891032134/853281697411629097/unknown.png")
        embed.add_field(name="__Custom background__", value="Change the picture of your `!profile` background.", inline=False)
        embed.add_field(name="__Emoji Flair__", value="Add/Change an emoji in your nickname. No custom emojis allowed.", inline=False)
        embed.add_field(name="__Custom Command__", value="Have LeGeND Bot say a line of text or perform a command when people type !<a custom word>.", inline=False)
        embed.add_field(name="__Rare__", value="Appear on the top of the members list with an orange color name. Receive more credits in payday.", inline=False)
        embed.add_field(name="__Epic__", value="Appear higher than <@&815957842266816522> and with color Purple. Receive more credits in payday.", inline=False)
        embed.add_field(name="__Legendary__", value="Show you are a true LeGeND and appear higher than <@&815958568418803772> with a private LeGeND Channel. Receive more credits in payday.", inline=False)
        embed.add_field(name="__Elite__", value="Join the most outstanding and limited club and appear higher than <@&815958673770807317> with a private LeGeND Channel.", inline=False)
        embed.add_field(name="__Custom Adventure Boss__", value="Ever wanted to fight yourself or some creature of your choise in adventure? It's your lucky day because now you can challenge anything with the power of this item.", inline=False)
        embed.add_field(name="__Set loot chest__", value="Are you a sets collector? Or are you simply looking for a new set to use in battle? You can buy 10 set chests at a time.", inline=False)
        embed.add_field(name="**__NEW EMBED UPDATE__**", value="Do you want to make your custom commands look unique and special? Look no further, we (I) are proud to introduce the Embed update.\nThere are 2 different embed updates available for purchase:", inline=False)
        embed.add_field(name="Embed update__", value="Turn your command into a simple embed (no links or pictures).", inline=False)
        embed.add_field(name="__Elite Embed update__", value="The simple update isn't enought for you? You can add links, picture and other cool stuff to you embed with this powerful update.\nThe Elite Embed update lets you personalize your embed command almost as you wish.\n||The result will be similar to the shop, the roles or the rules embed.||", inline=False)
        embed.add_field(name="**Items**", value="```\n"
            "Item name          Price   Commands     \n"
            "Emoji flair:        200k   ~            \n"
            "Custom background:  800k   ~            \n"
            "Custom command:     500k   ~            \n"
            "Rare:               1,5M   !buyrare     \n"
            "Epic:               3,5M   !buyepic     \n"
            "Legendary:           10M   !buylegendary\n"
            "Elite:               35M   !buyelite    \n"
           #"-------------------------------------------------"
            "```", inline=False)
        embed.add_field(name="**Legendary Items**", value="```\n"
            "Item name               Price  Elite  \n"
            "Custom adventure boss:    10M     5M  \n"
            "x5 set loot chests:        5M   2.5M  \n"
            "Simple embed update:       5M     1M  \n"
            "Elite embed update:       25M    10M  \n"
           #"-------------------------------------------------"
            "```", inline=False)

        embed.add_field(name="**Note**", value="`M` stands for million/s, `k` stands for thousand/s\n"
                                                "To purchase any item that doesn't have a command specified, dm <@598662722821029888>\n"
                                                "<@&815958379624529931> and <@&815958696982872075> are equivalent regarding shop purchases\n"
                                                "When buying <@&815958696982872075> you will receive a legendary item of choise for free")
        await ctx.send(embed=embed)
    
    @commands.command(name="es_minishop")
    async def minishop(self, ctx):
        embed = discord.Embed(title="LeGeND Shop",color=0x7289DA)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/722551851891032134/853281697411629097/unknown.png")
        embed.add_field(name="**Items**", value="```\n"
            "Item name          Price   Commands     \n"
            "Emoji flair:        200k   ~            \n"
            "Custom background:  800k   ~            \n"
            "Custom command:     500k   ~            \n"
            "Rare:               1,5M   !buyrare     \n"
            "Epic:               3,5M   !buyepic     \n"
            "Legendary:           10M   !buylegendary\n"
            "Elite:               35M   !buyelite    \n"
           #"-------------------------------------------------"
            "```", inline=False)
        embed.add_field(name="**Legendary Items**", value="```\n"
            "Item name          Price  Elite  \n"
            "Custom adv boss:     10M     5M  \n"
            "x5 set loot chests:   4M     2M  \n"
            "Simple embed update:  5M     2M  \n"
            "Elite embed update:  10M    10M  \n"
           #"-------------------------------------------------"
            "```", inline=False)
        embed.add_field(name="Click here to see the full shop", value=f"<#381339305769041922>")
        await ctx.send(embed=embed)

    @commands.group(pass_context=True)
    @commands.guild_only()
    async def buy(self, ctx):
        """Buy an item from the shop"""
        pass

    @buy.command(name="set")
    @commands.guild_only()
    async def add_blacklist(self, ctx, count: int = 1):
        """Buy set loot"""
        user = ctx.author
        userRoles = user.roles
        price = 4000000

        eliter = discord.utils.get(ctx.guild.roles,name="Elite")
        if(eliter in userRoles):
            price = 2000000

        price = price * count
        count = count * 5

        adv = self.get_cog("Adventure")

        async with adv.get_lock(user):
            try:
                c = await Character.from_json(adv.config, user, adv._daily_bonus)
            except Exception as exc:
                log.exception("Error with the new character sheet", exc_info=exc)
            
            # adds set loots
            c.treasure[5] += count

        bal = await bank.get_balance(user)
        await bank.withdraw_credits(user, price)

        return ctx.send(f"You just bought {count} set loot chests for {price}")