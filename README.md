# mastodon-pricebot

This is a quick'n'dirty solution to update a Mastodon account with the price of a cryptocurrency.

## How to use it

- clone this repository
- be sure to initialize submodules
- set your PYTHONPATH to include the «thirdparty» directory
- run «create_app_token.py» to generate the app's login token
- run «create_user_token.py» to generate the user's login token (It's not clear ATM but you have to input 3 things: the full instance URL, the email address of the account you'll be tooting from, and the password)
- from now on, running «pricebot.py» will get the latest price of a cryptocurrency from Kraken (this is currently hardcoded to XMR because well, the whole thing is a work in progress)

## What the hell this is horrible

I experiment some weird decisions in this project to see if they would
be viable in practice. For example, I don't rely on
pip/setuptools/whatever, the only form of dependency management you'll
see is the git submodules that are integrated in the repo.

Also, all the logic is currently hardcoded because I wanted the bot to
work for me, but everything will soon™ be configurable, from the
currency you're tracking to the message that gets posted by the bot.

Just wait until I have some time

I swear

Look there's ludum dare 38 this week-end, everything will look nice
and shiny after that

Please

###### Sempai