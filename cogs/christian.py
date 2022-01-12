from nextcord.ext import commands, tasks
import BibleVerseOfTheDayGetter #is local
import utilities
import nextcord

verse_of_the_day_aliases = ["verse","verseMe","verseday"]
search_aliases = ["search","searchGateway","searchBibleGateway"]
affirmation_aliases = ["affermation","aff"]
add_channel_aliases = ["add_channel", "set_channel","setchannel"]
add_to_dm_aliases = ["adddm"]
remove_from_dm_aliases = ["removedm"]
remove_channel_aliases = []
affirmation_and_verse_aliases = ["dailynow","AffAndVerse"]

class christian(commands.Cog):

    def __init__(self, bot: commands.bot):
        self.bot = bot
        self.printer.start()

    @commands.command(name="verseOfTheDay",aliases = verse_of_the_day_aliases, description = "Get BibleGateway Verse of the Day")
    async def verseOfTheDay(self,ctx: commands.Context):
        embed = nextcord.Embed(title = "Bible Gateway's verse of the day!",colour=0xff0069, url ="https://www.biblegateway.com/")
        feilds = [
            ("Verse of the Day:",BibleVerseOfTheDayGetter.getVerseOfTheDay(),False),
            ]
        utilities.add_fields(embed,feilds)
        await ctx.send(embed=embed)

    @commands.command(name = "searchBible",description= "Search bible gateway")#, aliases=search_aliases)
    async def search(self,ctx:commands.Context):
        opand = ctx.message.content.lower().split() #this splits the message up based on where it has spaces

        output = ""
        for i in range(1,len(opand)):
            output += opand[i] + "+"

        output = output[:-1] #remove final character which is always a + from the line above
        await ctx.channel.send('https://www.biblegateway.com/quicksearch/?quicksearch='+output.strip())

    @commands.command(name="Affirmation",aliases=affirmation_aliases)
    async def affirmation(self,ctx:commands.Context):
        embed = nextcord.Embed(title = "One of God's affirmations for humanity!",colour=0xff0069)
        feilds = [
            ("Affirmation of the Day:",utilities.getAffirmation(), False)
            ]
        utilities.add_fields(embed,feilds)
        await ctx.send(embed=embed)
        
    @commands.command(name = "addToDm", aliases = add_to_dm_aliases)
    async def addToDm(self,ctx:commands.Context):
        channel = await ctx.author.create_dm()
        await channel.send("You have successfully been added as a recipient of God's daily message")
        utilities.appendFile("data/channels.csv",str(channel.id))
    
    @commands.command(name = "RemoveFromDM", aliases = remove_from_dm_aliases)
    async def removeFromDM(self,ctx:commands.Context):
        utilities.removeFromFile(r"data/channels.csv",str(ctx.author.id))
        #await ctx.send("You have successfully been removed as a recipient of God's daily message in your DM's.")

    @commands.command(name = "AddChannel",aliases = add_channel_aliases, description = "Set current channel as a recipient of the verse of the day!")
    async def addChannel(self,ctx:commands.Context):

        utilities.appendFile("data/channels.csv",str(ctx.channel.id))
        await ctx.channel.send("This channel has been successfully set as a reciepient for message of the day.")

    @commands.command(name = "AffirmationAndVerse",aliases = affirmation_and_verse_aliases, description = "This sends you the verse of the day and an uplifting affirmation.")
    async def affirmationAndVerse(self, ctx: commands.Context):
        embed = nextcord.Embed(title = "God's message for you.",colour=0xff0069)
        feilds = [
            ("Verse of the Day:",BibleVerseOfTheDayGetter.getVerseOfTheDay(),False),
            ("Affirmation of the Day:",utilities.getAffirmation(), False)
        ]
        utilities.add_fields(embed,feilds)
        await ctx.send(embed=embed)

    @commands.command(name = "RemoveChannel",aliases = remove_channel_aliases,description = "Remove current channel as a recipient of the verse of the day.")
    async def removeChannel(self,ctx:commands.Context):
        try:
            utilities.removeFromFile("data/channels.csv",str(ctx.channel.id))
            await ctx.channel.send("This channel has been successfully removed as a reciepient for message of the day.")
        except:
            await ctx.channel.send("This channel is not a recipient of VerseOfTheDay.")


    @tasks.loop(hours=24)
    async def printer(self):
        channels = utilities.readFromFile("data/channels.csv") 
        print("Called Successfully")
        for i in channels:
            message_channel = self.bot.get_channel(int(i))
            if message_channel != None:

                embed = nextcord.Embed(title = "God's daily message for you.",colour=0xff0069)

                feilds = [
                    ("Verse of the Day:",BibleVerseOfTheDayGetter.getVerseOfTheDay(),True),
                    ("Affirmation:",utilities.getAffirmation(), False)
                ]
                utilities.add_fields(embed,feilds)

                await message_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=nextcord.Game(name="~help"))
        print(f"Logged in as {self.bot.user}")

    
def setup(bot: commands.Bot):
    bot.add_cog(christian(bot))

