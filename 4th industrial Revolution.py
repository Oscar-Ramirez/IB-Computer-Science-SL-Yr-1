print("""4th Industrial Revolution

The 4th Industrial revolution is invading a war-torn country


- MENU- 
--------
Please choose one of the options below, and press enter

1) Question & Answer 1
2) Question & Answer 2
3) Question & Answer 3
""")

answer = "empty"
userchoice = input()

while (answer == "empty"):
  answer = "chosen"
  if(userchoice == "1"):
    print("PROMPT 1")
  elif(userchoice == "2"):
    print ("PROMPT 2")
  elif(userchoice == "3"):
    print ("PROMPT 3")
  else:
    print ("INVALID INPUT, please try again")
    answer = "empty"
