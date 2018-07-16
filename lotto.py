import random

def number_input():
  print "Welcome to the lottery number generator."
  auth = True
  while auth == True:
    try:
      usernum = int(raw_input("Please enter how many numbers you would like to have: "))
      lottery_gen(usernum)
      auth = False
    except:
      print "Please enter a number."

def lottery_gen(x):
  numberlist = []
  counter = 0
  while counter < x:
    ball = random.randint(1, 45)
    if ball not in numberlist:
      numberlist.append(random.randint(1, 45))
      counter += 1
  print "Here is your list of lottery numbers: " + str(numberlist)

if __name__ == '__main__':
  number_input()