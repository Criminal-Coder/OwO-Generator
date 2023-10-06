import time
import requests
import random
from data.cogs import start_gen

tokens = [""] # tokens (add more than one token for faster gen)
channelid = ""  # add channel id for msges to be posted
times = 0
print('''

________    ___________________ _______    ____   ____________  
\_____  \  /  _____/\_   _____/ \      \   \   \ /   /\_____  \ 
 /   |   \/   \  ___ |    __)_  /   |   \   \   Y   /  /  ____/ 
/    |    \    \_\  \|        \/    |    \   \     /  /       \ 
\_______  /\______  /_______  /\____|__  /    \___/   \_______ \\


''')


def msg(msg):
  global times
  times += 1

  for token in tokens:
    payload = {"content": msg}
    header = {"authorization": token}
    response = requests.get("https://discord.com/api/users/@me",
                            headers=header)

    if response.status_code == 200:
      data = response.json()
      account_name = f"{data['username']}#{data['discriminator']}"
    else:
      account_name = "**You have not set tokens properly**"
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"
    r = requests.post(url, data=payload, headers=header)
    if r.status_code == 200:
      print(f"#{times} Sent {msg} succesfully in id {account_name}")
    else:
      print(f"Error in sending {msg} in user {account_name}")




if __name__ == "__main__":
  start_gen(tokens)
  while True:

    msg("owo h")
    msg("owo sell all")
    msg("owo cash")
    time.sleep(random.randrange(15, 20))