import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from sys import exit
serveurs = ["blue", "orange", "yellow",
            "white", "black", "cyan", "lime", "coral"]
emojis = {"blue":":blue_circle:","orange":":orange_circle:",
        "yellow":":yellow_circle:","white":":white_circle:",
        "black":":black_circle:","cyan":":large_blue_diamond:",
        "lime":":green_circle:","coral":":red_circle:"}

def vote():
    def emoji(a):
        global emojis
        try:
            return emojis[a]
        except KeyError as e:
            print(a)
            raise e

    url = "https://forum.nationsglory.fr/index.php"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    all_b = soup.findAll('b')
    a = []
    for b in all_b:
        a.append(list(filter(lambda x: x != "", "".join(
            [i for i in str(b) if str(i) in "0123456789/"]).split("/"))))
    nb = list(zip(serveurs, a))
    rep = []
    for i in nb:
        rep.append("{} Il y a ***__{}__*** personnes connectés sur ***__{}__*** sur le serveur ***__{}__***. {}".format(
            emoji(i[0]),i[1][0], i[1][1], i[0],
            "(soit une queue de **__{}__** personnes)".format((int(i[1][0]) - int(i[1][1]))) if (int(i[1][0]) > int(i[1][1])) else "(Il n'y a pas de queue. Vas-y fonce !!)"))
    return rep


def to_lower(argument):
    return argument.lower()


client = commands.Bot(command_prefix='+')


@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.command()
async def queue(ctx, *args: to_lower):
    args = " ".join(args)
    print("Une commande +queue {} a été excécuté !".format(args))
    if args in serveurs:
        rep = vote()
        nbr = serveurs.index(args)
        await ctx.send(rep[nbr])
    elif args == "all":
        rep = vote()
        await ctx.send("\n".join(rep))
    elif args == "pink":
        await ctx.send("Je sais pas TwT")
    else:
        rep = 'Veuillez entrer :\n **"+queue *all*"** pour avoir la queue de tout les serveurs\n **"+queue *<le nom du serveur>*"** pour avoir la queue du serveur en question\n'
        await ctx.send(rep)


@client.command()
async def test(ctx, *args: to_lower):
    args = " ".join(args)
    print("Une commande +test {} a été excécuté !".format(args))
    if not args:
        await ctx.send("pas d'arguments")
    else:
        await ctx.send(args)


@client.command()
async def stop(ctx):
    print("une commande +stop a été excécuté")
    await ctx.send("arrêt du bot en cour...")
    exit()

@client.command()
async def invite(ctx):
    print("une commande +invite a été excecuté")
    await ctx.send("Pour m'inviter sur un autre serveur, utilisez ce lien:\nhttps://discordapp.com/oauth2/authorize?client_id=705440030209867877&scope=bot&permissions=3492928")

client.run("")
