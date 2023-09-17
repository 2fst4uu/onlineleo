import discord

# Discord Account-Token
TOKEN = "MTExMjQ0MDY3NTQzOTQ4NDk4OA.G3czAb.btSPhUg2xIZ-7TGU5V4LoPX84AB9P4JZb1bQGQ"
USER = "leo"

# Channel-ID für Interface
SERVICE_ID = 1150226541561786498


# Discord-Client erstellen
client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(SERVICE_ID)
    print(f"connected as {client.user}")
    

# Client mit dem Token starten
client.run(TOKEN)