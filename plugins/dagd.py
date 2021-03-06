# For The-TG-Bot-3.0
# Syntax shorten, unshorten

import os
import requests
import json
from userbot import syntax


@bot.on(command(pattern="shorten (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("Generated {} for {}.".format(response_api, input_str))
    else:
        await event.edit("Error! Please try again later")


@bot.on(command(pattern="unshorten (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith('3'):
        await event.edit("Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"]))
    else:
        await event.edit("Input URL {} returned status_code {}".format(input_str, r.status_code))


syntax.update({
    "dagd": "\
```.shorten <input_link>```\
\nUsage: Create a da.gd link using <input_link>.\
```.unshorten <da.gd link>```\
\nUsage: Unshorten a da.gd link.\
"
})
