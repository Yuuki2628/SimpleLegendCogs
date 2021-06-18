# Standard Library
import asyncio
import itertools
import random
import discord
import contextlib

# Russian Roulette
from .kill import outputs

# Red
from redbot.core import Config, bank, checks, commands
from redbot.core.errors import BalanceTooHigh


__version__ = "3.1.07"
__author__ = "Redjumpman"


class RussianRoulette(commands.Cog):
    defaults = {
        "MinCost": 100000,
        "Cost": 0,
        "Chamber_Size": 6,
        "Wait_Time": 60,
        "Session": {"Pot": 0, "Players": [], "Active": False},
    }

    def __init__(self):
        self.config = Config.get_conf(self, 5074395004, force_registration=True)
        self.config.register_guild(**self.defaults)

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    @commands.guild_only()
    @commands.command()
    async def russian(self, ctx, bid = 0):
        """Start or join a game of russian roulette.

        The game will not start if no players have joined. That's just
        suicide.

        The maximum number of players in a circle is determined by the
        size of the chamber. For example, a chamber size of 6 means the
        maximum number of players will be 6.
        """
        settings = await self.config.guild(ctx.guild).all()
        if(bid == 0):
            if(settings["Session"]["Pot"] == 0):
                bid = await self.config.guild(ctx.guild).MinCost()
                await self.config.guild(ctx.guild).Cost.set(bid)
            else:
                bid = await self.config.guild(ctx.guild).Cost()
        if await self.game_checks(ctx, settings, bid):
            await self.add_player(ctx, bid)

    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    @commands.command(hidden=True)
    async def rusreset(self, ctx):
        """ONLY USE THIS FOR DEBUGGING PURPOSES"""
        await self.config.guild(ctx.guild).Session.clear()
        await ctx.send("The Russian Roulette session on this server has been cleared.")

    @commands.command()
    async def russianversion(self, ctx):
        """Shows the cog version for RussianRoulette."""
        await ctx.send("You are using russian roulette version {}".format(__version__))

    @commands.group(autohelp=True)
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def setrussian(self, ctx):
        """Russian Roulette Settings group."""
        pass

    @setrussian.command()
    async def chamber(self, ctx, size: int):
        """Sets the chamber size of the gun used. MAX: 12."""
        if not 1 < size <= 12:
            return await ctx.send("Invalid chamber size. Must be in the range of 2 - 12.")
        await self.config.guild(ctx.guild).Chamber_Size.set(size)
        await ctx.send("Chamber size set to {}.".format(size))

    @setrussian.command()
    async def cost(self, ctx, amount: int):
        """Sets the required cost to play."""
        if amount < 0:
            return await ctx.send("You are an idiot.")
        await self.config.guild(ctx.guild).MinCost.set(amount)
        currency = await bank.get_currency_name(ctx.guild)
        await ctx.send("Required cost to play set to {} {}.".format(amount, currency))

    @setrussian.command()
    async def wait(self, ctx, seconds: int):
        """Set the wait time (seconds) before starting the game."""
        if seconds <= 0:
            return await ctx.send("You are an idiot.")
        await self.config.guild(ctx.guild).Wait_Time.set(seconds)
        await ctx.send("The time before a roulette game starts is now {} seconds.".format(seconds))

    async def game_checks(self, ctx, settings, bid):
        if settings["Session"]["Active"]:
            with contextlib.suppress(discord.Forbidden):
                await ctx.author.send("You cannot join or start a game of russian roulette while one is active.")
            return False

        if ctx.author.id in settings["Session"]["Players"]:
            await ctx.send("You are already in the roulette circle.")
            return False

        if len(settings["Session"]["Players"]) == settings["Chamber_Size"]:
            await ctx.send("The roulette circle is full. Wait for this game to finish to join.")
            return False

        async with self.config.guild(ctx.guild).Session.Players() as players:
            num_players = len(players)

        bal = await bank.get_balance(ctx.author)
        mcost = settings["MinCost"]

        if(num_players == 0):
            if bid >= mcost:
                await self.config.guild(ctx.guild).Cost.set(bid)
                price = settings["Cost"]
            else:
                await self.config.guild(ctx.guild).Cost.set(mcost)
                price = settings["Cost"]

        if bal < cost:
            await ctx.send("Insufficient funds! This game requires at least {} credits.".format(settings["Cost"]))
            return False
        if bal < mcost:
            await ctx.send("Insufficient funds! This game requires at least {} credits.".format(settings["MinCost"]))
            return False
        await bank.withdraw_credits(ctx.author, settings["Cost"])
        return True

    async def add_player(self, ctx, cost):
        current_pot = await self.config.guild(ctx.guild).Session.Pot()
        await self.config.guild(ctx.guild).Session.Pot.set(value=(current_pot + cost))

        async with self.config.guild(ctx.guild).Session.Players() as players:
            players.append(ctx.author.id)
            num_players = len(players)

        allowed_mentions = discord.AllowedMentions(roles = True)
        rrole = discord.utils.get(ctx.guild.roles, name="Roulette")
        if(rrole is None):
            rusrole = ""
        else:
            rusrole = rrole.mention

        if num_players == 1:
            wait = await self.config.guild(ctx.guild).Wait_Time()
            await ctx.send(
                f"{rusrole} {ctx.author.mention} is gathering players for a game of russian "
                f"roulette!\nType `{ctx.prefix}rr  or  {ctx.prefix}russian` to enter. "
                f"The round will start in {wait} seconds. "
                f"The bet is set to {cost}", allowed_mentions = allowed_mentions
            )
            await self.config.guild(ctx.guild).Cost.set(cost)
            await asyncio.sleep(wait)
            await self.start_game(ctx)
        else:
            await ctx.send("{} was added to the roulette circle.".format(ctx.author.mention))

    async def start_game(self, ctx):
        await self.config.guild(ctx.guild).Session.Active.set(True)
        data = await self.config.guild(ctx.guild).Session.all()
        players = [ctx.guild.get_member(player) for player in data["Players"]]
        filtered_players = [player for player in players if isinstance(player, discord.Member)]
        if len(filtered_players) < 2:
            try:
                await bank.deposit_credits(ctx.author, data["Pot"])
            except BalanceTooHigh as e:
                await bank.set_balance(ctx.author, e.max_balance)
            await self.reset_game(ctx)
            return await ctx.send("You can't play by youself. That's just like a Decent Lvl 11 guy playing against a LvL 10 with maxed ebarbs, balloon and wizard.\nGame reset and cost refunded.")
        chamber = await self.config.guild(ctx.guild).Chamber_Size()

        counter = 1
        while len(filtered_players) > 1:
            await ctx.send(
                "**Round {}**\n*{} spins the cylinder of the gun "
                "and with a flick of the wrist it locks into "
                "place.*".format(counter, ctx.bot.user.name)
            )
            await asyncio.sleep(3)
            await self.start_round(ctx, chamber, filtered_players)
            counter += 1
        await self.game_teardown(ctx, filtered_players)

    async def start_round(self, ctx, chamber, players):
        position = random.randint(1, chamber)
        while True:
            for turn, player in enumerate(itertools.cycle(players), 1):
                await ctx.send(
                    "{} presses the revolver to their head and slowly squeezes the trigger...".format(player.name)
                )
                await asyncio.sleep(5)
                if turn == position:
                    players.remove(player)
                    msg = "**BANG!** {0} is now dead.\n"
                    msg += random.choice(outputs)
                    await ctx.send(msg.format(player.mention, random.choice(players).name, ctx.guild.owner))
                    await asyncio.sleep(3)
                    break
                else:
                    await ctx.send("**CLICK!** {} passes the gun along.".format(player.name))
                    await asyncio.sleep(3)
            break

    async def game_teardown(self, ctx, players):
        winner = players[0]
        currency = await bank.get_currency_name(ctx.guild)
        total = await self.config.guild(ctx.guild).Session.Pot()
        try:
            await bank.deposit_credits(winner, total)
        except BalanceTooHigh as e:
            await bank.set_balance(winner, e.max_balance)
        await ctx.send(
            "Congratulations {}! You are the last person standing and have "
            "won a total of {} {}.".format(winner.mention, total, currency)
        )
        await self.reset_game(ctx)

    async def reset_game(self, ctx):
        await self.config.guild(ctx.guild).Session.clear()
