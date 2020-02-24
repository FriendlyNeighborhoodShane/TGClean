# TG Pyrogram login
# By FriendlyNeighborhoodShane

from pyrogram import Client;
import config;

print(" ");
print("TG Login Script");

print(" ");
print(" - Starting client");
app = Client("TGClean", api_id = config.tg_api_id, api_hash = config.tg_api_hash);
app.start();

print(" ");
print(" - Sending message to self");
app.send_message("self", "- - TG Login Checkin - -");

print(" ");
print(" - Stopping client");
app.stop();
