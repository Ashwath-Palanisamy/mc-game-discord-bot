import discord
from discord.ext import commands
import random
import time

description = """An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    assert bot.user is not None
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def joined(ctx, member: discord.Member):
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def greatest_captain(ctx):
    await ctx.send(f"The Greatest captain is always <@1014804950167080960>")

# player choices
class options(discord.ui.View):

    @discord.ui.button(label='Pickaxes', style=discord.ButtonStyle.primary, custom_id="pickaxe_btn", emoji='⛏️')
    async def pickaxes(self, interaction: discord.Interaction, button: discord.ui.Button):
        #values for displaying
        global player
        global bot_hp

        #embed message
        embed = discord.Embed(
            color=discord.Color.green(),
            title='Choose your pickaxe',
            description=f'''Choose your pickaxe to damage the enemy \n Current HP : <@{interaction.user.id}> HP is {player} 
            and Bot's HP is {bot_hp}''',
        )
        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')

        #show pickaxe_options to player
        view = PickaxeOptionsView()
        await interaction.response.send_message(embed=embed, view=view)


    @discord.ui.button(label="Wood", style=discord.ButtonStyle.primary, custom_id="roll_btn")
    async def roll_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        result = random.randint(1, 6)
        await interaction.response.send_message(f"You rolled a {result} 🎲")

    @discord.ui.button(label="Show Captain", style=discord.ButtonStyle.secondary, custom_id="captain_btn")
    async def captain_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("The Greatest captain is always <@1014804950167080960>")

#player options - pickaxes
class PickaxeOptionsView(discord.ui.View):

    #wooden
    @discord.ui.button(label='Wooden Pickaxe', style=discord.ButtonStyle.primary, custom_id='wooden_pickaxe_btn')
    async def wooden_pickaxe(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        global bot_hp
        bot_hp -= 2

        embed = discord.Embed(
            color=discord.Color.green(),
            title='You chose Wooden Pickaxe!',
            description="You decreased the bot's health by 2!",
        )

        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)

    #stone
    @discord.ui.button(label='Stone Pickaxe', style=discord.ButtonStyle.primary, custom_id='stone_pickaxe_btn')
    async def stone_pickaxe(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        global bot_hp
        bot_hp -= 2

        embed = discord.Embed(
            color=discord.Color.green(),
            title='You chose Stone Pickaxe!',
            description="You decreased the bot's health by 2!",
        )

        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)

    #iron
    @discord.ui.button(label='Iron Pickaxe', style=discord.ButtonStyle.primary, custom_id='iron_pickaxe_btn')
    async def iron_pickaxe(self, interaction: discord.Interaction, button: discord.ui.Button):
        global bot_hp
        bot_hp -= 3
        embed = discord.Embed(
            color=discord.Color.green(),
            title='You chose Wooden Pickaxe!',
            description="You decreased the bot's health by 3!",
        )
        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)

    #gold
    @discord.ui.button(label='Gold Pickaxe', style=discord.ButtonStyle.primary, custom_id='gold_pickaxe_btn')
    async def gold_pickaxe(self, interaction: discord.Interaction, button: discord.ui.Button):
    
        global bot_hp
        bot_hp -= 2
        embed = discord.Embed(
            color=discord.Color.green(),
            title='You chose Wooden Pickaxe!',
            description="You decreased the bot's health by 2!",
        )
        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)

    #diamond
    @discord.ui.button(label='Diamond Pickaxe', style=discord.ButtonStyle.primary, custom_id='diamond_pickaxe_btn')
    async def diamond_pickaxe(self, interaction: discord.Interaction, button: discord.ui.Button):
    
        global bot_hp
        bot_hp -= 5
        embed = discord.Embed(
            color=discord.Color.green(),
            title='You chose Wooden Pickaxe!',
            description="You decreased the bot's health by 5!",
        )
        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)

    #netherite
    @discord.ui.button(label='Netherite Pickaxe', style=discord.ButtonStyle.primary, custom_id='netherite_pickaxe_btn')
    async def netherite_pickaxe(self, interaction: discord.Interaction, button: discord.ui.Button):
    
        global bot_hp
        bot_hp -= 6
        embed = discord.Embed(
            color=discord.Color.green(),
            title='You chose Wooden Pickaxe!',
            description="You decreased the bot's health by 6!",
        )
        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)

        
#HPcount for players and bots
player=20
bot_hp=20

@bot.command()
async def start(ctx):
    #embed section
    embed = discord.Embed(
        title='Welcome to the Game!',
        description=f''' <@{ctx.message.author.id}> HP is {player} and My hp is {bot_hp} \n
                    Click the button to play''',
        color=discord.Color.green(),
    )

    embed.set_author(name=bot.user.display_name)
    embed.set_footer(text='Made by FriendSMP75 Staff team',icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')

    # response for selecting buttons
    view = options()
    await ctx.send(view=view, embed=embed)

with open('bot.txt') as f:
    a=f.read()
    bot.run(a)
    f.close()
