sw = "Gir"
guess = ""
guesscount = 0
guesslimit = 4
out = False


while guess != sw and not (out):
   
   if guesscount < guesslimit:
      guess = input("enter gueess: ")
      guesscount +=1
   else:
      out = True

if out:
  print("you lose")
else:
  print(guesscount)
  print("you win")