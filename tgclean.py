# TGClean script
# By theel0ja
# Modification by FriendlyNeighborhoodShane

import time
from pyrogram import Client
from pyrogram.errors import FloodWait

# Source link for curious people
sauce = "https://github.com/FriendlyNeighborhoodShane/TGClean"

print("TGClean")
print("Starting up delete routine...")

# Create client object with name
app = Client("TGClean")

# Array of chats to purge
targets = [
  "https://t.me/joinchat/abcdef",
  "@abcdef",
  -123456
]  

# Delete threshhold
delete_before_days = 14
delete_before = int(time.time() - (delete_before_days * 24 * 60 * 60))
print("-- Deleting messages from before " + str(delete_before))

app.start()

for target in targets:

  # Get target's chat ID and title
  id = app.get_chat(target).id
  name = app.get_chat(target).title

  print("-- Deleting from chat " + target)
  print("-- Chat ID: " + str(id))
  print("-- Chat name: " + name)

  # Send warning
  app.send_message(id, "- - - TGCLEANER AUTOMATED MESSAGE - - -\n\nStarting group purge at: " + str(time.time()) + "\n\nUserbot sauce at: " + sauce)

  deleted = 0
  undeleted = 0

  # Ask for array of messages (oldest to newest) and iterate through it
  for message in app.iter_history(id, reverse = True):

    if(delete_before > message.date):
      print("    ++ Deleting message sent at " + str(message.date))
      app.delete_messages(message.chat.id, [message.message_id])
      deleted = deleted + 1
    else:
      print("    ++ Found a too new message sent at " + str(message.date))
      undeleted = undeleted + 1

  # Send result
  app.send_message(id, "- - - TGCLEANER AUTOMATED MESSAGE - - -\n\nFinishing group purge at: " + str(time.time()) + "\n\nUserbot sauce at: " + sauce)
  app.send_message(id, "Messages deleted: " + str(deleted) + "\nMessages not deleted: " + str(undeleted))

  print("-- Done")

app.stop()

