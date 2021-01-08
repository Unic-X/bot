from discord.ext import commands

class errors(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandNotFound):
            pass

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.BotMissingPermissions):
            await ctx.send("I seem to lack some permissions to do dat")
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.NoPrivateMessage):
            await ctx.send("This command doesn't work here lmao ded")

def setup(client):
    client.add_cog(errors(client))