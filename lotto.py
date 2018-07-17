import random

numberlist = set()

def number_input():
  print "Welcome to the lottery number generator."
  auth = True
  while auth == True:
    try:
      usernum = int(raw_input("Please enter how many numbers you would like to have: "))
      lottery_gen(numberlist, usernum)
      auth = False
    except:
      print "Please enter a number."


def lottery_gen(x, y):

  counter = 0
  while counter < y:
    ball = random.randint(1, 45)
    if ball not in x:
      x.add(ball)
      counter += 1
  lotto_ordered = list(x)
  print "Here is your list of lottery numbers: " + str(lotto_ordered)


if __name__ == '__main__':
  number_input()