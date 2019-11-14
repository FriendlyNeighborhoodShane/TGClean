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

Set targets array to the chats you wish to purge. Also set delete\_before\_days to a comfortable amount .

## Usage

```

> python ./tgclean.py

```

The first time you run it, it will ask you to login with your phone number and verification code. After that, your sessions will be stored in the TGClean.session file.
