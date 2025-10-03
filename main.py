import discord
from discord.ext import commands
import random
from discord import app_commands

description = """An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)

#when bot online
@bot.event
async def on_ready():
    await bot.tree.sync()
    assert bot.user is not None
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

#member join checking
@bot.command()
async def joined(ctx, member: discord.Member):
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

#setting mod role so who can use moderation command
mod_roles = {}  # key: guild.id, value: role.id

#settings group
settings = app_commands.Group(name="settings", description="Config the bot")

@settings.command(name='set-mod-role', description='Set mod role to specify which role can use this bot [Only server owner can run it]')
async def set_mod_role(interaction: discord.Interaction, role: discord.Role):
    global mod_roles
    try:
        owner = interaction.guild.owner.id
        if interaction.user.id == owner:
            mod_roles[interaction.guild.id] = role.id
            await interaction.response.send_message(f"<@&{role.id}> is set as mod role")
        else:
            await interaction.response.send_message("You are not server owner!")
    except Exception as e:
        await interaction.response.send_message('Provide the role')

#show mod role
@settings.command(name='show-mod-role',description='Shows the current mod role',)
async def show_mod_role(interaction: discord.Interaction):
    role_id = mod_roles.get(interaction.guild.id)
    if role_id:
        await interaction.response.send_message(f'Current Moderator role is <@&{role_id}>')
    else:
        await interaction.response.send_message("No mod role set for this server.")

#adding the group
bot.tree.add_command(settings)

#if invoked without subcommand/help
@bot.tree.command()
async def setting(interaction: discord.Interaction):
    await interaction.response.send_message("Choose The category: Set_admin_role, show_admin_role")

# a easter egg?
@bot.tree.command(name='captain')
async def greatest_captain(interaction:discord.Interaction):
    await interaction.response.send_message(f"The Greatest captain is always <@1014804950167080960>")


@bot.tree.command(name='kick',description='Kick the member from the server')
async def kick(interaction: discord.Interaction,member: discord.Member,reason: str):

    success_embed=discord.Embed(
        title="Member Kicked",
        type='video',
        description=f"Member {member.mention} has been kick by {interaction.user}\n**Reason:** {reason}",
        color=discord.Color.green()
    )

    role_id = mod_roles.get(interaction.guild.id)

    if role_id is not None: 
        try:
            mod_role = interaction.guild.get_role(role_id)
            if mod_role in interaction.user.roles:
                await member.kick(reason=reason)
                await interaction.response.send_message(f"{member.mention} has been kicked!",embed=success_embed)
            else:
                await interaction.response.send_message(f"You do not have Moderator role to use this bot!")
        except:
            await interaction.response.send_message(f"My role is too below to kick {member.mention} or you don't have permission to kick {member.mention}")
    else:
        await interaction.response.send_message("Ask server owner to set mod role first!")


# ---------- START OF DISCONTINUED SECTION ------------
#bot choices
class bot_turn(discord.ui.View):
    
    async def choose(self, channel):

        option=random.randint(1,2)
        weapon=random.randint(1,2)

        opt=['Pickaxe','Sword','Axe']
        wpt=['Wooden','Stone','Iron','Gold','Diamond','Netherite']

        if option == 1:
            if (weapon ==1) or (weapon==2):
                await channel.send("HAAAAA")
        else:
            await channel.send('idk')
        


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
            description=f"""You decreased the bot's health by 2!\n Current HP: <@{interaction.user.id}> HP is {player} Bot's HP is {bot_hp}""",
        )

        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)
        

        botturn = bot_turn()
        await botturn.choose(interaction.channel)

    #stone
    @discord.ui.button(label='Stone Pickaxe', style=discord.ButtonStyle.primary, custom_id='stone_pickaxe_btn')
    async def stone_pickaxe(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        global bot_hp
        bot_hp -= 2

        embed = discord.Embed(
            color=discord.Color.green(),
            title='You chose Stone Pickaxe!',
            description=f"""You decreased the bot's health by 2!\n Current HP: <@{interaction.user.id}> HP is {player} Bot's HP is {bot_hp}""",
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
            title='You chose Iron Pickaxe!',
            description=f"""You decreased the bot's health by 3!\n Current HP: <@{interaction.user.id}> HP is {player} Bot's HP is {bot_hp}""",
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
            title='You chose Gold Pickaxe!',
            description=f"""You decreased the bot's health by 2!\n Current HP: <@{interaction.user.id}> HP is {player} Bot's HP is {bot_hp}""",
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
            title='You chose Diamond Pickaxe!',
            description=f"""You decreased the bot's health by 5!\n Current HP: <@{interaction.user.id}> HP is {player} Bot's HP is {bot_hp}""",
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
            title='You chose Netherite Pickaxe!',
            description=f"""You decreased the bot's health by 6!\n Current HP: <@{interaction.user.id}> HP is {player} Bot's HP is {bot_hp}""",
        )
        embed.set_footer(text='Made by FriendSMP75 Staff team', icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')
        await interaction.response.send_message(embed=embed)


#HPcount for players and bots
player=20
bot_hp=20

@bot.command()
async def start(ctx):
    player=20
    bot_hp=20
    #embed section
    embed = discord.Embed(
        title='Welcome to the Game!',
        description=f''' <@{ctx.message.author.id}> HP is {player} and My hp is {bot_hp} \n
                    Click the button to play''',
        color=discord.Color.green(),
    )

    embed.set_author(name='Discontinued')
    embed.set_footer(text='Made by FriendSMP75 Staff team',icon_url='https://i.ibb.co/Jw8DHv8Q/servercurrent.jpg')

    # response for selecting buttons
    view = options()
    await ctx.send(view=view, embed=embed)
#------------------ END OF DISCONTINUED SECTION -----------------------

#reading bot token
with open('bot.txt') as f:
    a=f.read()
    bot.run(a)
    f.close()
