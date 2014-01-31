#requires https://pypi.python.org/pypi/websocket-client/
import websocket
import json
import os
import getpass
from ChatExchange.SEChatWrapper import *
from BeautifulSoup import *

if "ChatExchangeU" in os.environ:
  username = os.environ["ChatExchangeU"]
else:
  print "Username: "
  username = raw_input()
if "ChatExchangeP" in os.environ:
  password = os.environ["ChatExchangeP"]
else:
  password = getpass.getpass("Password: ")

wrap = SEChatWrapper("SE")
wrap.login(username, password)

url = "https://github.com/Manishearth/ChatExchange-Scripts/blob/master/lazers.py"
prefix = "[ [LAZERS v2](%s) ]" % url


def handlepost(data):
  try:
    a = json.loads(json.loads(data)['data'])
  except:
    return False
  link = BeautifulSoup(a['body']).find('a', {'class': 'question-hyperlink'})
  msg = "http://gaming.stackexchange.com" + link['href']
  print msg
  wrap.sendMessage("35", msg)

if __name__ == "__init__":
  ws = websocket.create_connection("ws://sockets.ny.stackexchange.com/")
  ws.send("41-questions-newest")
  while True:
    a = ws.recv()
    if a is not None and a != "":
      handlepost(a)
