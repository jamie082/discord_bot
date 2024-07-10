from discord.ext import commands
TOKEN = "FIND YOUR TOKEN IN THE BOT TAB IN DISCORD DEVELOPER PORTAL"

# Initialize Bot and Denote the Command Prefix
bot = commands.Bot(command_prefix="!")

# Runs when Bot successfully Connects
@bot.eventasync def on_ready():
print(f'{bot.user}' successfully logged in!')'
      
bot.run(TOKEN)