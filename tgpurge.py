# TGPurge script
# By theel0ja
# Modification by FriendlyNeighborhoodShane

import time;

from pyrogram import Client;
from pyrogram.errors import ChannelInvalid, InviteHashExpired, PeerIdInvalid, UsernameInvalid, UserNotParticipant;

import config;

print(" ");
print("TGPurge Cleaning Script");

# Create client object with name
print(" ");
print(" - Starting client");
app = Client("TGClean", api_id = config.tg_api_id, api_hash = config.tg_api_hash);
app.start();

print(" ");
print(" - Starting delete routine");

selfid = app.get_me().id;

for target in config.targets:

  print(" ");
  print(" - Deleting messages older than " + str(target.delete_before_days) + " days");
  delete_before = int(time.time() - (target.delete_before_days * 24 * 60 * 60));

  for chat in target.chatlist:

    # Get target's chat ID and title
    try:
      chatobj = app.get_chat(chat);
    except(ChannelInvalid, PeerIdInvalid, UsernameInvalid, ValueError):
      print(" ");
      print(" ! Given value leads to invalid chat " + str(chat));
      continue;
    except(InviteHashExpired):
      print(" ");
      print(" ! Given chat invite has expired " + str(chat));
      continue;

    print(" ");
    print(" - Deleting from chat " + str(chat));
    print("   -- Chat ID: " + str(chatobj.id));
    print("   -- Chat name: " + chatobj.title);

    # Check that we have delete perms
    try:
      memberobj = app.get_chat_member(chatobj.id, "self");
    except(UserNotParticipant):
      print(" ")
      print("   !! The user is not a participant in this chat");
      continue;

    # Create empty array and variables
    messages = [];
    messagecount = 0;
    deleted = 0;

    # Ask for array of messages (oldest to newest) and iterate through it
    for message in app.iter_history(chatobj.id, reverse = True):

      # TG only allows deleting upto 100 messages at once, then delete messages and reset array
      if(messagecount == 100):
        print("     ++ Deleting " + str(messagecount) + " messages at " + str(message.date));
        app.delete_messages(chatobj.id, messages);
        deleted = deleted + messagecount;
        messages = [];
        messagecount = 0;

      # If message is old, add its id to array
      if(delete_before > message.date):
        if(message.from_user is not None and message.from_user.id == selfid):
          messages += [message.message_id];
          messagecount = messagecount + 1;
      else:
        print("     ++ Found a too new message sent at " + str(message.date));
        break;

    # Delete leftover messages
    if(messagecount > 0):
      print("     ++ Deleting "  + str(messagecount) + " messages at end");
      app.delete_messages(chatobj.id, messages);
      deleted = deleted + messagecount;

    print("   -- Done");

print(" ");
print(" - Stopping Client");
app.stop();
