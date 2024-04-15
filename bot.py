from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from cogs import minecraft


class Stevey:
    def __init__(self):
        """ Get bot token and set the command prefix to use the bot in Discord. """
        self.token = getenv('DISCORD_BOT_TOKEN')

        # Add cogs to our bot:
        self.cogs = [
            {'name': 'Minecraft', 'obj': minecraft.Minecraft, 'active': True},
        ]

        # Here we chose 's:' to call our bot in Discord. Feel free to change this to your liking.
        self.bot = commands.Bot(command_prefix='s:', case_insensitive=True)
        self.add_events()
        self.init_cogs()

    def init_cogs(self):
        """ Loop through all cogs in our list and add them to our Bot """
        for cog in self.cogs:
            self.bot.add_cog(cog['obj'](self.bot))

    def add_events(self):
        """ Add on_ready() event to bot. We can add more events here in future if required. """
        self.bot.event(self.on_ready)

    async def on_ready(self):
        """ Print output to terminal once bot has successfully connected to Discord """
        print(f'{self.bot.user.name} has connected to Discord!')

    def start_bot(self):
        """ Start our bot with our TOKEN """
        self.bot.run(self.token)


if __name__ == '__main__':
    # Load our secret environment variables
    load_dotenv('.env')

    # Initialize our bot
    s = Stevey()

    # Start our bot
    print("Starting bot(Stevey)")
    s.start_bot()
