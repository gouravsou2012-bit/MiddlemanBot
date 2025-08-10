import os
import discord
from discord.ext import commands
from keep_alive import keep_alive  # Import the keep_alive module

keep_alive()  # Start the webserver to keep the bot alive on Render

TOKEN = os.getenv('MTQwMjcwNjU5OTcwNDc5MzIxMw.G4KFDN.NQOmbOKD8sJmumBcTlCEYF2vewMyx4w1vpdynw') or "PASTE-YOUR-TOKEN-HERE"

if not TOKEN:
    print("❌ No bot token found! Add it in Replit secrets or paste it directly.")
    exit()

MM_ROLE_NAME = "MM Client"

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

GUILD_ID = 1199399373470179428
guild = discord.Object(id=GUILD_ID)

class ScamView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Join Us 😄", style=discord.ButtonStyle.green)
    async def join_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name=MM_ROLE_NAME)
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("✅ You joined and got the MM Client role!", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ MM Client role not found!", ephemeral=True)

    @discord.ui.button(label="Leave Us 😡", style=discord.ButtonStyle.red)
    async def leave_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("🚫 You chose to leave. You are being banned...", ephemeral=True)
        try:
            await interaction.guild.ban(interaction.user, reason="Chose to leave via ScamView")
        except discord.Forbidden:
            await interaction.followup.send("⚠️ I don't have permission to ban you.", ephemeral=True)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} guild slash commands")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@bot.tree.command(name="ontop", description="Show scam options")
async def ontop(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**Unfortunately, You Have Been Scammed! 💔**\n"
        "**You Are Now Presented With 2 Options:**\n"
        "**Either Join Us 😁 And Scam Or Leave Us 😡 What's It Gonna Be? 🤔**",
        view=ScamView()
    )

@bot.tree.command(name="middleman", description="Explains what a Middleman (MM) is", guild=guild)
async def middleman(interaction: discord.Interaction):
    message = (
        "💼 **Middle Man (MM) Explained**\n"
        "MM means Middle Man — a trusted person who helps two players trade safely by holding both items first, then giving them to the correct players to prevent scams.\n\n"
        "📌 **Example:**\n"
        "1️⃣ Raju gives his Dragon Fruit (Blox Fruits) to the middle man.\n"
        "2️⃣ Ravi pays/gives the Raccoon (Grow a Garden) directly to Raju.\n"
        "3️⃣ The middle man then passes the Dragon Fruit to Ravi.\n\n"
        "Safe trades = Happy players ✅"
    )
    await interaction.response.send_message(message)

if __name__ == "__main__":
    bot.run(TOKEN)
    
