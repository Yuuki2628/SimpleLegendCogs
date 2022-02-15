from redbot.core import commands
import discord

from adventure.charsheet import Character
from redbot.core import checks
from redbot.core import bank
from redbot.core.utils.predicates import MessagePredicate

class Shop(commands.Cog):
    """Buy items"""

#Billionaire: 815958379624529931
#Elite:       815958696982872075
#Legendary:   815958673770807317
#Epic:        815958568418803772
#Rare:        815957842266816522

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
            "Item name          Price   Commands      \n"
            "Emoji flair:        200k   ~             \n"
            "Custom background:  800k   ~             \n"
            "Custom command:     500k   ~             \n"
            "Rare:               1,5M   !buy rare     \n"
            "Epic:               3,5M   !buy epic     \n"
            "Legendary:           10M   !buy legendary\n"
            "Elite:               35M   !buy elite    \n"
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
    async def buy_set(self, ctx, count: int = 1):
        """Buy set loot x5 for adventure"""
        if count is None:
            count = 1

        user = ctx.author
        userRoles = user.roles
        price = 4000000

        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")
        if not legendary in userRoles:
            return await ctx.send(f"You need to have bought {legendary.mention} to buy this item")
        
        eliter = discord.utils.get(ctx.guild.roles,name="Elite")
        bilr = discord.utils.get(ctx.guild.roles,name="Billionaire")
        if((eliter in userRoles) or (bilr in userRoles)):
            price = 2000000

        price = price * count
        count = count * 5

        bal = await bank.get_balance(user)
        if bal < price:
            return await ctx.send(f"You don't have enough credits to buy this item\nYou need {price}")
        await bank.withdraw_credits(user, price)

        adv = ctx.bot.get_cog("Adventure")
        async with adv.get_lock(user):
            try:
                c = await Character.from_json(adv.config, user, adv._daily_bonus)
            except Exception as exc:
                log.exception("Error with the new character sheet", exc_info=exc)

            # adds set loots
            c.treasure[5] += count

            await adv.config.user(user).set(await c.to_json(adv.config))

        return await ctx.send(f"You just bought {count} set loot chests for {price}")

    @buy.command(name="boss")
    @commands.guild_only()
    async def buy_boss(self, ctx):
        """Buy a custom boss for adventure"""
        user = ctx.author
        userRoles = user.roles
        price = 10000000

        eliter = discord.utils.get(ctx.guild.roles,name="Elite")
        bilr = discord.utils.get(ctx.guild.roles,name="Billionaire")
        if((eliter in userRoles) or (bilr in userRoles)):
            price = 5000000

        bal = await bank.get_balance(user)
        if bal < price:
            return await ctx.send(f"You don't have enough credits to buy this item\nYou need {price}")

        await ctx.send("If you'd like to cancel at any point write `cancel`")

        await ctx.send("What's the enemy name?\nExample: Yuuki")
        try:
            name = await ctx.bot.wait_for("message", check=MessagePredicate.same_context(user=ctx.author), timeout=90)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled")
        if name is None or name is "cancel" or name is "Cancel":
            return await ctx.send("Cancelled")    

        await ctx.send("What's the enemy main weakness/strength?\nExample: weak to talk, resistant to everything else if possible\nNote: not specifying anything will result in Yuuki deciding for you")
        try:
            stats = await ctx.bot.wait_for("message", check=MessagePredicate.same_context(user=ctx.author), timeout=90)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled")
        if stats is None or stats is "cancel" or stats is "Cancel":
            return await ctx.send("Cancelled")

        await ctx.send("What's the enemy image?\nExample: <https://cdn.discordapp.com/attachments/733451738643824720/943183446212218942/PFP9.png>")
        try:
            img = await ctx.bot.wait_for("message", check=MessagePredicate.same_context(user=ctx.author), timeout=90)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled")
        if img is None or img is "cancel" or img is "Cancel":
            return await ctx.send("Cancelled")
        
        await bank.withdraw_credits(user, price)
        
        yuuki = ctx.guild.get_member(295275466703503372)
        dm_channel = await yuuki.create_dm()
        
        embed=discord.Embed(title="Cboss shop")
        embed.add_field(name="Someone wants to buy a custom boss", value=f"{user.name}#{user.discriminator}", inline=False)
        embed.add_field(name="Name", value=name.content, inline=False)
        embed.add_field(name="Stats", value=stats.content, inline=False)
        embed.add_field(name="Img", value=img.content, inline=False)

        await dm_channel.send(embed=embed)
        return await ctx.send(f"You paid your price of {price} and your request has been forwarded to the one above all")

#Billionaire: 815958379624529931
#Elite:       815958696982872075
#Legendary:   815958673770807317
#Epic:        815958568418803772
#Rare:        815957842266816522

    @buy.command(name="rare")
    @commands.guild_only()
    async def buy_rare(self, ctx):
        """Buy the Rare role"""
        
        user = ctx.author
        price = 1500000
        bal = await bank.get_balance(user)
        if bal < price:
            return await ctx.send(f"You don't have enough credits to buy this item\nYou need {price}")

        rare = discord.utils.get(ctx.guild.roles,name="Rare")
        if rare in user.roles:
            return await ctx.send("You already have this role!")

        await bank.withdraw_credits(user, price)
        await user.add_roles(rare)

        return await ctx.send(f"You just bought the <@815957842266816522> role for {price}", allowed_mentions = discord.AllowedMentions(roles=False))

    @buy.command(name="epic")
    @commands.guild_only()
    async def buy_epic(self, ctx):
        """Buy the Epic role"""
        
        user = ctx.author
        price = 3500000
        bal = await bank.get_balance(user)
        if bal < price:
            return await ctx.send(f"You don't have enough credits to buy this item\nYou need {price}")

        rare = discord.utils.get(ctx.guild.roles,name="Rare")
        epic = discord.utils.get(ctx.guild.roles,name="Epic")

        if epic in user.roles:
            return await ctx.send("You already have this role!")
        if not rare in user.roles:
            return await ctx.send(f"You need to have bought the {rare.mention} role first", allowed_mentions = discord.AllowedMentions(roles=False))
        
        await user.add_roles(epic)
        await bank.withdraw_credits(user, price)
        return await ctx.send(f"You just bought the {epic.mention} role for {price}", allowed_mentions = discord.AllowedMentions(roles=False))

    @buy.command(name="legendary")
    @commands.guild_only()
    async def buy_legendary(self, ctx):
        """Buy the Legendary role"""
        
        user = ctx.author
        price = 10000000
        bal = await bank.get_balance(user)
        if bal < price:
            return await ctx.send(f"You don't have enough credits to buy this item\nYou need {price}")

        epic = discord.utils.get(ctx.guild.roles,name="Epic")
        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")

        if legendary in user.roles:
            return await ctx.send("You already have this role!")
        if not epic in user.roles:
            return await ctx.send(f"You need to have bought the {epic.mention} role first", allowed_mentions = discord.AllowedMentions(roles=False))
        
        await user.add_roles(legendary)
        await bank.withdraw_credits(user, price)
        return await ctx.send(f"You just bought the {legendary.mention} role for {price}", allowed_mentions = discord.AllowedMentions(roles=False))

    @buy.command(name="elite")
    @commands.guild_only()
    async def buy_elite(self, ctx):
        """Buy the Elite role"""
        
        user = ctx.author
        price = 35000000
        bal = await bank.get_balance(user)
        if bal < price:
            return await ctx.send(f"You don't have enough credits to buy this item\nYou need {price}")

        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")
        elite = discord.utils.get(ctx.guild.roles,name="Elite")

        if elite in user.roles:
            return await ctx.send("If you want to flex how rich you are you better go somewhere else")
        if not legendary in user.roles:
            return await ctx.send(f"You need to have bought the {legendary.mention} role first", allowed_mentions = discord.AllowedMentions(roles=False))
        
        await user.add_roles(elite)
        await bank.withdraw_credits(user, price)

        yuuki = ctx.guild.get_member(295275466703503372)
        dm_channel = await yuuki.create_dm()
        
        elite_channel = ctx.bot.get_channel(736789008121593876)

        await elite_channel.send(f"Welcome {user.mention} to the most reserved chat in the server ||probably||\nSince you bought elite you deserver a special prize, you'll be awarded with a legendary item of choice from the shop\nBut remember to contact Yuuki to claim it, I heard he's quite lazy with this stuff")
        await dm_channel.send(f"{user.name}#{user.discriminator} just bought Elite in {user.guild}")
        return await ctx.send(f"You just bought the {elite.mention} role for {price}", allowed_mentions = discord.AllowedMentions(roles=False))
