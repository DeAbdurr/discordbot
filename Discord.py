# Work with Python 3.6
import discord
 
TOKEN = 'Njk3NTg0NzY5OTMxOTM1Nzc0.Xo5bzg.gQHy96Lhwzc0EOT2CoX6HAlVPiM'
 
client = discord.Client()
 
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
 
    if message.content.startswith('!rename me'):
        await message.channel.send(f"We're going to fix that for you {message.author.mention}.")
        await message.author.edit(nick = message.author.name + ' ['+ message.author.top_role.name + ']')
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
client.run(TOKEN)
