# Config file for tgclean

# Class for a chat group
class ChatGroup:
  def __init__(self, chatlist, delete_before_days):
    assert type(chatlist) is list;
    assert type(delete_before_days) is int;
    self.chatlist = chatlist;
    self.delete_before_days = delete_before_days;
  chatlist = [];
  delete_before_days = 0;

# API id and hash obtained during setup
tg_api_id = 12345;
tg_api_hash = "abcd";

# List of chats for a group

listA = [
  "https://t.me/joinchat/abcdef",
  -12345
];

listB = [
  "@abcdef"
];

# List of GroupChat targets
# Taking lists as first argument and days to not delete as second

targets = [
  ChatGroup(listA, 14),
  ChatGroup(listB, 2)
]
