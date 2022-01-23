import discord, os, random, shutil
from dotenv import load_dotenv
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import time
load_dotenv()
DISCORD_TOKEN = os.getenv("")
bot = commands.Bot(command_prefix='!')
dir = '/storage/emulated/0/MIUI/Gallery/cloud/owner/horny'

def randpic():
    global dir
    filename = random.choice(os.listdir(dir))
    path = os.path.join(dir, filename)
    return path
def findsize(pa):
    size = os.path.getsize(pa)
    size = size/1024/1024
    return size
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
a = 0
astop = 1

@bot.command(aliases=['уву','ede', 'гуг', 'senko'])
async def uwu(ctx):
	await ctx.channel.send(file=discord.File('uwu.jpg'))
	print('I\'ve just sent a UwU')

@bot.command(aliases=['фурри','агккн', 'cp', 'ср', 'сз', 'scat', 'ысфе'])
async def furry(ctx):
	await ctx.channel.send(file=discord.File('ok.jpg'))
	print('I\'ve just sent a furry')

@bot.command(aliases=['10', 'ten'])
async def decem(ctx):
    await gimme(ctx, 10)

@bot.command(aliases=['100', 'hundred'])
async def yoo(ctx):
    await gimme(ctx, 100)

@bot.command(aliases=['','1', 'horny', 'give', 'дай', 'hentai', 'sex', 'porn', 'хорни', 'хентай', 'гив', 'пиму', 'пиььу', 'рщктн'])
async def gimme(ctx, num = 1):
    global a
    global astop
    i = 0
    astop = 1
    print('*Starting cycle*')
    while i < num:
            if not astop:
                break
            path = randpic()
            size = findsize(path)
            if size > 8:
                print('I cannot send because file size is', size, 'mb')
                shutil.move(path, '/storage/emulated/0/MIUI/Gallery/cloud/owner/url')
            else:
                i += 1
                a = a + 1
                await ctx.channel.send(file=discord.File(path))
                # message_channel = bot.get_channel(753986145158955032)
                # if message_channel == ctx.channel:
                shutil.move(path, '/storage/emulated/0/MIUI/Gallery/cloud/owner/hornywasted')
                print('I have sent a hentai pic right now. It\'s was a', a, 'in this session. File size is', size, 'mb \t|',i,"|" )
    astop = 0

@bot.command(aliases=['cnjg','cnjg\'', 'yamete', 'nomore', 'nohorny'])
async def stop(ctx):
    global astop
    if astop:
        astop = 0
        await ctx.channel.send('As you want...stupid ascetic gay...')
        print('*Stoping doing horny*')
        return
    await ctx.channel.send('I have nothing to stop STFU NIGGA')

@bot.command(aliases=['hh', 'how_many', 'how_much', 'howareyou', 'howhorny'])
async def how_horny(ctx):
    totalFiles = 0
    size = 0
    for base, dirs, files in os.walk('/storage/emulated/0/MIUI/Gallery/cloud/owner/horny'):
        print('Searching in : ',base)
        for Files in files:
            totalFiles += 1
            fp = os.path.join('/storage/emulated/0/MIUI/Gallery/cloud/owner/horny', Files)
            size += os.path.getsize(fp)
    size = size/1024/1024/1024
    await ctx.channel.send("I have "+str(totalFiles)+" hentai pics right now. Files size is "+str(size)+" gb")

@tasks.loop(hours=6)
async def called_once_a_day():
    message_channel = bot.get_channel(774378772647772172)
    print(f"Got channel {message_channel}")
    global a
    global astop
    astop = 1
    i = 0
    now = datetime.now()
    print('*Starting sending scheduled horny* |', now.strftime("%d-%m-%Y %H:%M"), "|")
    then = now + timedelta(hours=6)
    when = timedelta(hours=6)
    while i < 15:
            if not astop:
                break
            path = randpic()
            size = findsize(path)
            if size > 8:
                print('I cannot send because file size is', size, 'mb')
                shutil.move(path, '/storage/emulated/0/MIUI/Gallery/cloud/owner/url')
            else:
                i += 1
                a = a + 1
                await message_channel.send(file=discord.File(path))
                shutil.move(path, '/storage/emulated/0/MIUI/Gallery/cloud/owner/hornywasted')
                print('I have sent a hentai pic right now. It\'s was a', a, 'in this session. File size is', size, 'mb \t|',i,"|")
    then = then.strftime('%H:%M:%S')
    # await countdown(21600)
    print('next horny at ', then)
    astop = 0

async def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}'.format(hours, mins)
        print(timer, end="\r")
        await bot.change_presence(activity=discord.Game(name="next horny in " + timer))
        time.sleep(60)
        t -= 60

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
bot.run('')


