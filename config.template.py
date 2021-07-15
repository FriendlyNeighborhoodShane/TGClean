# Config file for tgclean

# Class for a chat group
class ChatGroup:
  def __init__(self, chatlist, delete_before_days, message):
    assert type(chatlist) is list;
    assert type(delete_before_days) is int;
    assert type(message) is bool;
    self.chatlist = chatlist;
    self.delete_before_days = delete_before_days;
    self.message = message;
  chatlist = [];
  delete_before_days = 0;
  message = True;

# API id and hash obtained during setup
tg_api_id = 12345;
tg_api_hash = "abcd";

# List of chats for a group

listA = [
  "https://t.me/joinchat/abcdef",
  -12345,
];

listB = [
  "@abcdef",
];

# List of GroupChat targets
# Taking lists as first argument
# Days to not delete as second
# Whether to send a result message as the third

targets = [
  ChatGroup(listA, 14, True),
  ChatGroup(listB, 2, False),
];
