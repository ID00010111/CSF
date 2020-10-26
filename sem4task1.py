#Countdown function
def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)

#Countup function
def countup(n):
  if n >= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n+1)

#Ask user to enter number
if sys.version_info[0] == 3:
  num = input('Enter number: ')
else:
  num = input('Enter number: ')

#Convert string to number
num = int(num)

if num > 0:
#Countdown positive number
  countdown(num)
elif num < 0:
#Countup negative number
  countup(num)
else:
#If input is 0 we can call both functions either countdown or countup in any case it will print Blastoff
  print('Blastoff!')

# Outputs:
# num=3    3 2 1 Blastoff!
# num=-3   -3 -2 -1 Blastoff!
# num=0    Blastoff!