"""This module shows an example extension that loads a cog into the bot

this module can be used as a base for other extensions.
"""
from common import logger
from typing import Optional
from disnake import Member
from disnake.ext.commands import slash_command, Bot
from disnake.ext.commands.cog import Cog


class Greetings(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @slash_command()
    async def hello(self, ctx, *, member: Optional[Member] = None):
        """Says hello to you or someone else!"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello {member.name}!")
        else:
            await ctx.send(f"Hello {member.name}!\n*This feels familiar...*")
        self._last_member = member
        logger.info(f"Greeted '{member.name}'")

def setup(bot: Bot):
    bot.add_cog(Greetings(bot))

def teardown(bot: Bot):
    bot.remove_cog(Greetings.__cog_name__)