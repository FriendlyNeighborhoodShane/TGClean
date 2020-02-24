# TGClean
A Telegram cleaning python script

Based on work by theel0ja
Modification by FriendlyNeighborhoodShane

A userbot script that deletes all messages in a group older than a specified time.

## Installation

```

> apt install clang python

> pip3 install pyrogram[fast]

```

## Configuration

Open config.py.

Obtain api_id and api_hash as described [here](https://docs.pyrogram.org/). But instead of putting it in config.ini, put them as tg_api_id and tg_api_hash in config.py (in the quotes).

In the targets array, add a ChatGroup object for every chat/days combo you need. The first argument is the list of chats, and the second is the last N days you want to keep messages for. There can be as many ChatGroup objects as you want (long as your computer doesnlt run out of memory :P).

## Usage

```

> python ./tgclean.py

```

The first time you run it, it will ask you to login with your phone number and verification code. After that, your sessions will be stored in the TGClean.session file.
