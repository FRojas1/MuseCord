import discord
from discord.errors import *

from config import Config as confClass


def request_token(_config: confClass):
    print("Please enter the Discord token: ")
    _token = input()
    _config["token"] = _token
    _config.save()
    print("Your token has been saved for future use")
    return _token


if __name__ == '__main__':
    bot = discord.Bot()
    Config = confClass()
    if Config["passing"]:
        try:
            token = Config["token"]
        except KeyError:
            token = request_token(Config)
    else:
        token = request_token(Config)
    try:
        Config["passing"] = True
        Config.save()
        bot.run(token)
    except LoginFailure:
        print("Token is invalid, couldn't login!")
        Config["passing"] = False
        Config.save()
