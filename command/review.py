from discord.ext import commands
import discord.file
import imutils
import cv2

from review import analyze_image


class Review(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="review", description="Review a meme")
    async def review(self, ctx):
        attachments = ctx.message.attachments

        try:
            top_attachment = attachments[0]
            image = analyze_image.load_image(top_attachment.url)
            image = imutils.resize(image, width=250)

            score = analyze_image.get_colourfulness(image)

            if score > 20:
                response = discord.File(open("./response/approved.png", "rb"))
            else:
                response = discord.File(open("./response/rejected.png", "rb"))

            await ctx.send(file=response)
        except Exception as e:
            await ctx.send(e)


def setup(bot):
    bot.add_cog(Review(bot))
