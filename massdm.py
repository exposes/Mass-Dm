import discord

saint = discord.Client()

token = "your token here" 

message = "your message here" 

@saint.event
async def on_connect():
  for user in saint.user.friends:
    try:
      await user.send(message)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message {user.name}")


saint.run(token,bot=False)
