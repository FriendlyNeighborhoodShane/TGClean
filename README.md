# TGClean
A Telegram cleaning python script

Based on work by theel0ja
Modification by FriendlyNeighborhoodShane

A userbot script that deletes all messages in a group older than a specified time.

Requires setting up as described [here](https://docs.pyrogram.org/).

## Installation

```

> apt install clang python

> pip3 install pyrogram[fast]

```

Then setup config.ini according to pyrogram docs (bot won't work, this script is for a userbot).

Open tgclean.py and set targets array to the chats you wish to purge. Also set delete\_before\_days to a comfortable amount .

## Usage

```

> python ./tgclean.py

```

The first time you run it, it will ask you to login with your phone number and verification code. After that, your sessions will be stored in the TGClean.session file.
