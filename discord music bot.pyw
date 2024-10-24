import discord
from discord.ext import commands
import asyncio
import os
import random

# Initilaization

music_path = "C:\\Users\\Admin\\Music\\botmusic"

bot_user_id = 1183782562401882143

token = ""

options = "-vn -b:a 320K -ac 2 -ar 48000"

global volume_adjusted
volume_adjusted = 0.15

# Define a variable to store the voice client
global voice_client
voice_client = None


# Define the intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.voice_states = True

# Create a bot instance with intents
bot = commands.Bot(command_prefix="#", intents=intents)



def return_paths(folder_path):
    
    # Use os.listdir to get a list of all files and directories in the folder
    all_files_and_dirs = os.listdir(folder_path)

    # Filter only the files from the list
    file_paths = [os.path.join(folder_path, item) for item in all_files_and_dirs if os.path.isfile(os.path.join(folder_path, item))]

    # Now, file_paths will contain the paths to all files in the folder
    return file_paths



files_paths = return_paths(music_path)


global random_number
random_number = random.randint(0,len(files_paths))


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    

@bot.event
async def on_voice_state_update(member, before, after):
    
    global voice_client
    global volume_adjusted
    global random_number
    
    
    if member.id != bot_user_id :
        
        if voice_client is not None:
            voice_client.stop()
        

        print(f"in update")  

        # joining a voice channel
        if before.channel is None and after.channel is not None:
            
            print(f"Member User ID: {member.id}")   
            
            random_number += 1
                       
            channel = after.channel
        
            # Check if the bot is not already connected
            if voice_client is None or not voice_client.is_connected(): 
                # Connect to the voice channel
                await channel.connect()
                print(f"Bot connected to voice channel: {channel}")
                        
                

            # Play the predefined audio file
            try:
                source = discord.FFmpegPCMAudio(files_paths[random_number%len(files_paths)],executable="ffmpeg.exe",options=options)
                
                voice_client = member.guild.voice_client
                voice_client.play(discord.PCMVolumeTransformer(source,volume_adjusted))
                

            except FileNotFoundError:
                await channel.send("File not found. Make sure to provide a valid file path.")
                
         
                
        # When i leave a voice channel            
        elif before.channel is not None and after.channel is None:
            # A member left a voice channel
            voice_client = member.guild.voice_client

            if voice_client is not None and voice_client.is_connected():
                # Check the number of members in the voice channel after the member left
                members_in_channel = len(voice_client.channel.members)

                # If there's only one member left (the bot), disconnect the bot
                if members_in_channel == 1:
                    await voice_client.disconnect()
                    print("Bot disconnected from voice channel.")
                
                
                


@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        voice_client.stop()
        await voice_client.disconnect()





@bot.command()
async def next(ctx):

        global voice_client
        global volume_adjusted
        global random_number
        
        if voice_client is not None:
            voice_client.stop()
        
            
        random_number += 1
                     
 
        # Play the predefined audio file
        try:
            source = discord.FFmpegPCMAudio(files_paths[random_number%len(files_paths)],executable="ffmpeg.exe",options=options)
            
            voice_client.play(discord.PCMVolumeTransformer(source,volume_adjusted))
            

        except FileNotFoundError:
            await channel.send("File not found. Make sure to provide a valid file path.")





# Run the bot with your token
bot.run(token)
























