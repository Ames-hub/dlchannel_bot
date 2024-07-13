import lightbulb
import datetime
import hikari
import dotenv
import os

if os.path.exists('secrets.env'):
    dotenv.load_dotenv('secrets.env')

TOKEN = os.environ.get('TOKEN', None)
ADMIN_UUID = os.environ.get('ADMIN_UUID', None)

# Makes sure both are set and persistent.
if TOKEN is None:
    TOKEN = input("Please enter your bot token: ")
    with open('secrets.env', 'w') as f:
        f.write(f"TOKEN={TOKEN}\n")
    print("Token saved to secrets.env")
if ADMIN_UUID is None:
    ADMIN_UUID = int(input("Please enter the discord user id that controls this bot: "))
    with open('secrets.env', 'a') as f:
        f.write(f"ADMIN_UUID={ADMIN_UUID}\n")
    print("User ID saved to secrets.env")

ADMIN_UUID = int(ADMIN_UUID)

bot = lightbulb.BotApp(
    token=TOKEN,
    intents=hikari.Intents.ALL
)

@bot.command
@lightbulb.app_command_permissions(dm_enabled=False)
@lightbulb.command(name="download", description="Download the selected channel's messages and save them to a file.")
@lightbulb.implements(lightbulb.SlashCommand)
async def download(ctx: lightbulb.SlashContext) -> None:
    # Basic af permission check
    if ctx.author.id != ADMIN_UUID:
        return await ctx.respond("You don't have permission to use this command.")

    await ctx.respond("Downloading channel messages...")

    messages = await bot.rest.fetch_messages(
        channel=ctx.channel_id,
        before=datetime.datetime.now(),
    )

    file_dir = f"downloaded/channel-{ctx.channel_id}.txt"
    os.makedirs('downloaded', exist_ok=True)
    with open(file_dir, "w") as f:
        for message in messages:
            f.write(f"{message.author.id} - {message.id} - {message.timestamp}: {message.content}\n")

    await ctx.edit_last_response(content=f"Channel messages downloaded and saved to {file_dir}")

bot.run()
