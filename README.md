# TGClean
A Telegram cleaning python script

Based on work by theel0ja
Modification by FriendlyNeighborhoodShane

TGClean is a userbot script that deletes all messages in a group older than a specified time as an admin.

TGPurge is a userbot script that deletes all of your messages in a group older than a specified time (does not need admin).

## Installation

```

> apt install python

> pip3 install pyrogram tgcrypto

```

## Configuration

The same configuration file is shared between both the scripts.

Open config.py.

Obtain api_id and api_hash as described [here](https://docs.pyrogram.org/). But instead of putting it in config.ini, put them as tg_api_id and tg_api_hash in config.py (in the quotes).

In the targets array, add a ChatGroup object for every chat/days combo you need. The first argument is the list of chats, the second is the last N days you want to keep messages for, and the third is a boolean for if you want a result message to be sent to the chat. There can be as many ChatGroup objects as you want (long as your computer doesn't run out of memory :P).

## Usage

```
> python ./tgclean.py
```
or
```
> python ./tgpurge.py
```

The first time you run it, it will ask you to login with your phone number and verification code. After that, your sessions will be stored in the TGClean.session file (shared between both scripts).

Alternatively, use login.py to login and create the session without actually cleaning anything.
