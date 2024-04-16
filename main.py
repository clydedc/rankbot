import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # A NE PAS CHANGER
intents.message_content = True  # A NE PAS CHANGER 

# ACTIVER TOUT LES ITENTS


bot = commands.Bot(command_prefix='!', intents=intents) # le prefix pas obligée mais le garder

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name}')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        role_id = 123456789789456123  # Remplacez ceci par l'ID du rôle que vous souhaitez attribuer
        role = discord.utils.get(message.guild.roles, id=role_id)
        if role:
            await message.author.add_roles(role)
            await message.channel.send(f"Vous avez reçu le rôle {role.mention}!")
    await bot.process_commands(message)


bot.run('ton token du bot')
