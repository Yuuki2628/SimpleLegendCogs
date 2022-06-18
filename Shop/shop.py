from redbot.core import commands
import discord

from adventure.charsheet import Character
from redbot.core import checks
from redbot.core import bank
from redbot.core.utils.predicates import MessagePredicate
from redbot.core.utils.chat_formatting import humanize_number

class Shop(commands.Cog):
    """Buy items"""

    def __init__(self):
        self.price = {
            'rare': 1000000, 
            'epic': 4000000, 
            'legendary': 10000000, 
            'champion': 50000000, 
            'custom_boss': 8000000, 
            'set': 5000000, 
            'simple_embed': 2000000, 
            'full_embed': 10000000
        }

    @commands.command(name="es_shop")
    async def shop(self, ctx):
        if(ctx.author.id != 295275466703503372):
            return await ctx.send("Only the true bot director shall be allowed to do this")

        rare = discord.utils.get(ctx.guild.roles,name="Rare")
        epic = discord.utils.get(ctx.guild.roles,name="Epic")
        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")
        champion = discord.utils.get(ctx.guild.roles,name="Champion")
        bil1 = discord.utils.get(ctx.guild.roles,name="OG Billionaire")
        bil2 = discord.utils.get(ctx.guild.roles,name="Billionaire")
        
        embed = discord.Embed(title="LeGeND Shop",color=0x7289DA)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/722551851891032134/853281697411629097/unknown.png")
        embed.add_field(name="__Custom background__", value="Change the picture of your `!profile` background.", inline=False)
        embed.add_field(name="__Emoji Flair__", value="Add/Change an emoji in your nickname. No custom emojis allowed.", inline=False)
        embed.add_field(name="__Custom Command__", value="Have LeGeND Bot say a line of text or perform a command when people type !<a custom word>.", inline=False)
        embed.add_field(name="__Rare__", value="Appear on the top of the members list with an orange color name. Receive more credits in payday.", inline=False)
        embed.add_field(name="__Epic__", value=f"Appear higher than {rare.mention} and with color Purple. Receive more credits in payday.", inline=False)
        embed.add_field(name="__Legendary__", value=f"Show you are a true LeGeND and appear higher than {epic.mention} with a private LeGeND Channel. Receive more credits in payday.", inline=False)
        embed.add_field(name="__Champion__", value=f"Join the most outstanding and limited club and appear higher than {legendary.mention} with a private LeGeND Channel.", inline=False)
        embed.add_field(name="__Custom Adventure Boss__", value=f"Ever wanted to fight yourself or some creature of your choise in adventure? It's your lucky day because now you can challenge anything with the power of this item.", inline=False)
        embed.add_field(name="__Set loot chest__", value=f"Are you a sets collector? Or are you simply looking for a new set to use in battle? You can buy 10 set chests at a time.", inline=False)
        embed.add_field(name="**__NEW EMBED UPDATE__**", value=f"Do you want to make your custom commands look unique and special? Look no further, we (I) are proud to introduce the Embed update.\nThere are 2 different embed updates available for purchase:", inline=False)
        embed.add_field(name="Embed update__", value=f"Turn your command into a simple embed (no links or pictures).", inline=False)
        embed.add_field(name="__Champion Embed update__", value=f"The simple update isn't enought for you? You can add links, picture and other cool stuff to you embed with this powerful update.\nThe Champion Embed update lets you personalize your embed command almost as you wish.\n||The result will be similar to the shop, the roles or the rules embed.||", inline=False)
        embed.add_field(name="**Items**", value="```\n"
            "Item name           Cost   Commands      \n"
            "Emoji flair:        200k   ~             \n"
            "Custom background:  800k   ~             \n"
            "Custom command:     500k   ~             \n"
            "Rare:                 1M   !buy rare     \n"
            "Epic:                 4M   !buy epic     \n"
            "Legendary:           10M   !buy legendary\n"
            "Champion:            50M   !buy champion \n"
           #"-------------------------------------------------"
            "```", inline=False)
        embed.add_field(name="**Legendary Items**", value="```\n"
            "Item name            Cost\n"
            "Custom adv boss:       8M\n"
            "x5 set loot chests:    5M\n"
            "Simple embed update:   2M\n"
            "Champion embed update: 10M\n"
           #"-------------------------------------------------"
            "```", inline=False)

        embed.add_field(name="**Note**", value="`M` stands for million/s, `k` stands for thousand/s\n"
                                                "To purchase any item that doesn't have a command specified, dm <@598662722821029888>.\n"
                                                f"{champion.mention}, {bil1.mention} and {bil2.mention} are equivalent regarding shop purchases.\n"
                                                f"When buying {champion.mention} you will receive a legendary item of choise for free.\n"
                                                f"When buying any Legendary items while having the {champion.mention} role you will receive a 60% discount.")
        await ctx.send(embed=embed)
    
    @commands.command(name="es_minishop")
    async def minishop(self, ctx):
        embed = discord.Embed(title="LeGeND Shop",color=0x7289DA)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/722551851891032134/853281697411629097/unknown.png")
        embed.add_field(name="**Items**", value="```\n"
            "Item name           Cost   Commands      \n"
            "Emoji flair:        200k   ~             \n"
            "Custom background:  800k   ~             \n"
            "Custom command:     500k   ~             \n"
            "Rare:                 1M   !buy rare     \n"
            "Epic:                 4M   !buy epic     \n"
            "Legendary:           10M   !buy legendary\n"
            "Champion:            50M   !buy champion \n"
           #"-------------------------------------------------"
            "```", inline=False)
        embed.add_field(name="**Legendary Items**", value="```\n"
            "Item name            Cost\n"
            "Custom adv boss:       8M\n"
            "x5 set loot chests:    5M\n"
            "Simple embed update:   2M\n"
            "Champion embed update: 10M\n"
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
        currency_name = await bank.get_currency_name(ctx.guild)
        if count is None:
            count = 1

        user = ctx.author
        priceL = self.price["set"]

        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")
        championr = discord.utils.get(ctx.guild.roles,name="Champion")
        bilr1 = discord.utils.get(ctx.guild.roles,name="OG Billionaire")
        bilr2 = discord.utils.get(ctx.guild.roles,name="Billionaire")

        if not ((legendary in user.roles) or (bilr1 in user.roles) or (bilr2 in user.roles)):
            return await ctx.send(f"You need to have bought {legendary.mention} to buy this item")
        
        if((championr in user.roles) or (bilr1 in user.roles) or (bilr2 in user.roles)):
            priceL = int(priceL * 0.4)

        priceL = priceL * count
        count = count * 5

        bal = await bank.get_balance(user)
        if bal < priceL:
            return await ctx.send(f"You don't have enough {currency_name} to buy this item\nYou need {humanize_number(priceL)} {currency_name}")
        await bank.withdraw_credits(user, priceL)

        adv = ctx.bot.get_cog("Adventure")
        async with adv.get_lock(user):
            try:
                c = await Character.from_json(adv.config, user, adv._daily_bonus)
            except Exception as exc:
                log.exception("Error with the new character sheet", exc_info=exc)

            # adds set loots
            c.treasure[5] += count

            await adv.config.user(user).set(await c.to_json(adv.config))
        
        return await ctx.send(f"You just bought {count} set loot chests for {humanize_number(priceL)} {currency_name}")

    @buy.command(name="boss")
    @commands.guild_only()
    async def buy_boss(self, ctx):
        """Buy a custom boss for adventure"""
        currency_name = await bank.get_currency_name(ctx.guild)
        user = ctx.author
        priceL = self.price["custom_boss"]

        championr = discord.utils.get(ctx.guild.roles,name="Champion")
        bilr1 = discord.utils.get(ctx.guild.roles,name="OG Billionaire")
        bilr2 = discord.utils.get(ctx.guild.roles,name="Billionaire")
        if((championr in user.roles) or (bilr1 in user.roles) or (bilr2 in user.roles)):
            priceL = int(priceL * 0.4)

        bal = await bank.get_balance(user)
        if bal < priceL:
            return await ctx.send(f"You don't have enough {currency_name} to buy this item\nYou need {humanize_number(priceL)} {currency_name}")

        await ctx.send("If you'd like to cancel at any point write `cancel`")

        await ctx.send("What's the enemy name?\nExample: Yuuki")
        try:
            name = await ctx.bot.wait_for("message", check=MessagePredicate.same_context(user=ctx.author), timeout=90)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled")
        if name is None or name.content == "cancel" or name.content == "Cancel":
            return await ctx.send("Cancelled")    

        await ctx.send("What's the enemy main weakness/strength?\nExample: weak to talk, resistant to everything else if possible\nNote: not specifying anything will result in Yuuki deciding for you")
        try:
            stats = await ctx.bot.wait_for("message", check=MessagePredicate.same_context(user=ctx.author), timeout=90)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled")
        if stats is None or stats.content == "cancel" or stats.content == "Cancel":
            return await ctx.send("Cancelled")

        await ctx.send("What's the enemy image? Submit a link, sending a whole image will not work\nExample: <https://cdn.discordapp.com/attachments/733451738643824720/943183446212218942/PFP9.png>")
        try:
            img = await ctx.bot.wait_for("message", check=MessagePredicate.same_context(user=ctx.author), timeout=90)
        except asyncio.TimeoutError:
            return await ctx.send("Cancelled")
        if img is None or img.content == "cancel" or img.content == "Cancel":
            return await ctx.send("Cancelled")
        
        await bank.withdraw_credits(user, priceL)
        
        yuuki = ctx.guild.get_member(295275466703503372)
        dm_channel = await yuuki.create_dm()
        
        embed=discord.Embed(title="Cboss shop")
        embed.add_field(name="Someone wants to buy a custom boss", value=f"{user.name}#{user.discriminator}", inline=False)
        embed.add_field(name="Name", value=name.content, inline=False)
        embed.add_field(name="Stats", value=stats.content, inline=False)
        embed.add_field(name="Img", value=img.content, inline=False)

        await dm_channel.send(embed=embed)
        return await ctx.send(f"You paid your price of {humanize_number(priceL)} {currency_name} and your request has been forwarded to the one above all")

    @buy.command(name="rare")
    @commands.guild_only()
    async def buy_rare(self, ctx):
        """Buy the Rare role"""
        currency_name = await bank.get_currency_name(ctx.guild)

        user = ctx.author
        priceL = self.price["rare"]
        bal = await bank.get_balance(user)
        if bal < priceL:
            return await ctx.send(f"You don't have enough {currency_name} to buy this item\nYou need {humanize_number(priceL)} {currency_name}")

        rare = discord.utils.get(ctx.guild.roles,name="Rare")
        if rare in user.roles:
            return await ctx.send("You already have this role!")

        await bank.withdraw_credits(user, priceL)
        await user.add_roles(rare)

        return await ctx.tick()

    @buy.command(name="epic")
    @commands.guild_only()
    async def buy_epic(self, ctx):
        """Buy the Epic role"""
        currency_name = await bank.get_currency_name(ctx.guild)

        user = ctx.author
        priceL = self.price["epic"]
        bal = await bank.get_balance(user)
        if bal < priceL:
            return await ctx.send(f"You don't have enough {currency_name} to buy this item\nYou need {humanize_number(priceL)} {currency_name}")

        rare = discord.utils.get(ctx.guild.roles,name="Rare")
        epic = discord.utils.get(ctx.guild.roles,name="Epic")

        if epic in user.roles:
            return await ctx.send("You already have this role!")
        if not rare in user.roles:
            return await ctx.send(f"You need to have bought the {rare.mention} role first", allowed_mentions = discord.AllowedMentions(roles=False))
        
        await user.add_roles(epic)
        await bank.withdraw_credits(user, priceL)

        return await ctx.tick()

    @buy.command(name="legendary")
    @commands.guild_only()
    async def buy_legendary(self, ctx):
        """Buy the Legendary role"""
        currency_name = await bank.get_currency_name(ctx.guild)

        user = ctx.author
        priceL = self.price["legendary"]
        bal = await bank.get_balance(user)
        if bal < priceL:
            return await ctx.send(f"You don't have enough {currency_name} to buy this item\nYou need {humanize_number(priceL)} {currency_name}")

        epic = discord.utils.get(ctx.guild.roles,name="Epic")
        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")

        if legendary in user.roles:
            return await ctx.send("You already have this role!")
        if not epic in user.roles:
            return await ctx.send(f"You need to have bought the {epic.mention} role first", allowed_mentions = discord.AllowedMentions(roles=False))
        
        await user.add_roles(legendary)
        await bank.withdraw_credits(user, priceL)

        return await ctx.tick()

    @buy.command(name="champion")
    @commands.guild_only()
    async def buy_champion(self, ctx):
        """Buy the Champion role"""
        currency_name = await bank.get_currency_name(ctx.guild)

        user = ctx.author
        priceL = self.price["champion"]
        bal = await bank.get_balance(user)
        if bal < priceL:
            return await ctx.send(f"You don't have enough {currency_name} to buy this item\nYou need {humanize_number(priceL)} {currency_name}")

        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")
        champion = discord.utils.get(ctx.guild.roles,name="Champion")

        if champion in user.roles:
            return await ctx.send("If you want to flex how rich you are you better go somewhere else")
        if not legendary in user.roles:
            return await ctx.send(f"You need to have bought the {legendary.mention} role first", allowed_mentions = discord.AllowedMentions(roles=False))
        
        await user.add_roles(champion)
        await bank.withdraw_credits(user, priceL)

        champion_channel = ctx.bot.get_channel(736789008121593876)
        await champion_channel.send(f"Welcome {user.mention} to the most reserved chat in the server ||probably||\nSince you bought {champion.mention} you deserve a special prize, you'll be awarded with a legendary item of choice from the shop\nBut remember to contact Yuuki to claim it, I heard he's quite inattentive", allowed_mentions = discord.AllowedMentions(roles=False))
        
        return await ctx.tick()

    @buy.command(name="embed")
    @commands.guild_only()
    async def buy_embed(self, ctx, cc_name: str):
        """Buy a simple embed"""
        currency_name = await bank.get_currency_name(ctx.guild)

        user = ctx.author
        priceL = self.price["simple_embed"]
        bal = await bank.get_balance(user)
        if bal < priceL:
            return await ctx.send(f"You don't have enough {currency_name} to buy this item\nYou need {humanize_number(priceL)} {currency_name}")
        
        legendary = discord.utils.get(ctx.guild.roles,name="LeGeNDary")
        championr = discord.utils.get(ctx.guild.roles,name="Champion")
        bilr1 = discord.utils.get(ctx.guild.roles,name="OG Billionaire")
        bilr2 = discord.utils.get(ctx.guild.roles,name="Billionaire")

        if not ((legendary in user.roles) or (championr in user.roles) or (bilr1 in user.roles) or (bilr2 in user.roles)):
            return await ctx.send(f"You need to have bought the {legendary.mention} role first", allowed_mentions = discord.AllowedMentions(roles=False))
        if((championr in user.roles) or (bilr1 in user.roles) or (bilr2 in user.roles)):
            priceL = int(priceL * 0.4)
                
        await bank.withdraw_credits(user, priceL)

        yuuki = ctx.guild.get_member(295275466703503372)
        dm_channel = await yuuki.create_dm()
        
        embed=discord.Embed(title="Simple embed shop")
        embed.add_field(name="Someone wants to buy a simple embed", value=f"{user.name}#{user.discriminator}", inline=False)
        embed.add_field(name="CC", value=cc_name, inline=False)

        await dm_channel.send(embed=embed)
        return await ctx.send(f"You paid your price of {humanize_number(priceL)} {currency_name} and your request has been forwarded to the one above all")
