#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *
def ply():
  x=int(input("enter your thing \n1=rock\n2=paper\n3=scissors"))
  if x==1:
    value=0
  elif x==2:
    value=1
  elif x==3:
    value=2
  return value
def computerChoice():
  value=r.randint(0,2)
  return value
def playerWins(computer,player):
    x=player-computer
    return x

def playerWins(computer,player):
  x=player-computer
  return x
if __name__ == "__main__":
  player = ply()
  com = computerChoice()
  x=playerWins(com,player)
  if x==-1:
   print("you losse")
  if x==1:
    print("you win")
  if x==0:
    print("we tied")
