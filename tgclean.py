# TGClean script
# By theel0ja
# Modification by FriendlyNeighborhoodShane

# Source link for curious people
sauce = "https://github.com/FriendlyNeighborhoodShane/TGClean";

import time;

from pyrogram import Client;

import config;

print(" ");
print("TGClean Cleaning Script");

# Create client object with name
print(" ");
print(" - Starting client");
app = Client("TGClean", api_id = config.tg_api_id, api_hash = config.tg_api_hash);
app.start();

print(" ");
print(" - Starting delete routine");

for target in config.targets:

  print(" ");
  print(" - Deleting messages older than " + str(target.delete_before_days) + " days");
  delete_before = int(time.time() - (target.delete_before_days * 24 * 60 * 60));

  for chat in target.chatlist:

    # Get target's chat ID and title
    id = app.get_chat(chat).id;
    name = app.get_chat(chat).title;

    print(" ");
    print(" - Deleting from chat " + str(chat));
    print("   -- Chat ID: " + str(id));
    print("   -- Chat name: " + name);

    # Create empty array and variables
    messages = [];
    messagecount = 0;
    deleted = 0;

    # Ask for array of messages (oldest to newest) and iterate through it
    for message in app.iter_history(id, reverse = True):

      # TG only allows deleting upto 100 messages at once, then delete messages and reset array
      if(messagecount == 100):
        print("     ++ Deleting " + str(messagecount) + " messages at " + str(message.date));
        app.delete_messages(id, messages);
        deleted = deleted + messagecount;
        messages = [];
        messagecount = 0;

      # If message is old, add its id to array
      if(delete_before > message.date):
        messages += [message.message_id];
        messagecount = messagecount + 1;
      else:
        print("     ++ Found a too new message sent at " + str(message.date));
        break;

    # Delete leftover messages
    if(messagecount > 0):
      print("     ++ Deleting "  + str(messagecount) + " messages at end");
      app.delete_messages(id, messages);
      deleted = deleted + messagecount;

    # Send result
    app.send_message(id, "- - - TGCLEAN REPORT - - -\n\nFinished group purge at: " + str(time.time()) + "\n\nMessages deleted: " + str(deleted) + "\n\nUserbot sauce at: " + sauce, disable_web_page_preview = True);

    print("   -- Done");

print(" ");
print(" - Stopping Client");
app.stop();
