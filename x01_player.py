#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  x=int(input("enter your thing \n1=rock\n2=paper\n3=scissors"))
  if x==1:
    value=0
  elif x==2:
    value=1
  elif x==3:
    value=2
  return value


if __name__ == "__main__":
  player = playerChoice()
  print(player)
