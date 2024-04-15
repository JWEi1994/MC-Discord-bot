from discord.ext import commands
from os import getenv
from mcrcon import MCRcon
from mcstatus import MinecraftServer


class Minecraft(commands.Cog):
    """Minecraft specific commands."""

    def __init__(self, bot):
        self.bot = bot

        # Get our variables
        self.host = getenv('SERVER_IP')
        self.query_port = int(getenv('QUERY_PORT'))
        self.rcon_port = int(getenv('RCON_PORT'))
        self.rcon_pwd = getenv('RCON_PASSWORD')

        # Init our endpoints
        self.query_server = MinecraftServer(self.host, self.query_port)

    @commands.command(name='test_status', brief="Check our Minecraft server status.")
    @commands.has_permissions(administrator=True)
    async def status(self, ctx):
        """ Get server status """
        status = self.query_server.status()
        await ctx.channel.send(f"The server has {status.players.online} players and replied in {status.latency} ms")

    @commands.command(name='msg', brief="Message the server or a player.")
    @commands.has_permissions(administrator=True)
    async def msg(self, ctx, msg=None, player=None):
        """ Message server or a specific player """
        if player is None:
            with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
                mcr.command(f"say {msg}")
                await ctx.channel.send(f"Messaged Minecraft server")
        else:
            with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
                resp = mcr.command(f"tell {player} {msg}")
                await ctx.channel.send(f"Server response: {resp}")

    @commands.command(name='list', brief="List all players on the server.")
    @commands.has_permissions(administrator=True)
    async def list(self, ctx):
        """ List all players on the server """
        with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
            resp = mcr.command("list")
            await ctx.channel.send(f"Server response: {resp}")

    @commands.command(name='kick', brief="Kick a player from the server.")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, player):
        """ Kick a player from the server """
        with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
            resp = mcr.command(f"kick {player}")
            await ctx.channel.send(f"Server response: {resp}")

    @commands.command(name='ban', brief="Ban a player from the server.")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, player):
        """ Ban a player from the server """
        with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
            resp = mcr.command(f"ban {player}")
            await ctx.channel.send(f"Server response: {resp}")

    @commands.command(name='pardon', brief="Pardon a player from the server.")
    @commands.has_permissions(administrator=True)
    async def pardon(self, ctx, player):
        """ Pardon a player from the server """
        with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
            resp = mcr.command(f"pardon {player}")
            await ctx.channel.send(f"Server response: {resp}")

    @commands.command(name='whitelist', brief="Whitelist a player on the server.")
    @commands.has_permissions(administrator=True)
    async def whitelist(self, ctx, player):
        """ Whitelist a player on the server """
        with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
            resp = mcr.command(f"whitelist add {player}")
            await ctx.channel.send(f"Server response: {resp}")
    

    @commands.command(name='remove', brief="Unwhitelist a player on the server.")
    @commands.has_permissions(administrator=True)
    async def unwhitelist(self, ctx, player):
        """ Unwhitelist a player on the server """
        with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
            resp = mcr.command(f"whitelist remove {player}")
            await ctx.channel.send(f"Server response: {resp}")
