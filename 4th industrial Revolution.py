print("""4th Industrial Revolution

The 4th Industrial revolution is invading a war-torn country


- MENU- 
--------
Please choose one of the options below, and press enter

1) Who do you think went to school before that?
2) Why do you think the laws changed?
3) What eects do you think it would have?
4) What are your thoughts in response to this video?
""")

answer = "empty"
userchoice = input()

while (answer == "empty"):
  answer = "chosen"
  if(userchoice == "1"):
    print("People that went to school before this change were kids whose parents had enough money to send them to a school or buy a private tutor. Besides kids I believe adults went to school if they were seeking knowledge for a profession they want to do.")
  elif(userchoice == "2"):
    print ("The laws changedbecause not every kid learned the important skills that were needed for them to start working in the industrial age that the US was in. Since learning was left up to the parents at home not everyone had good access to an education.")
  elif(userchoice == "3"):
    print ("Since this system was implemented to make the youth more used to working it streamlined turning students into potential employees for companies and corporations.")
  elif(userchoice == "4"):
    print ("There are 2 ways that I am seeing this video. A good thing is that robots and AI are taking over parts of manual labor letting people focus on other aspects furthering the progression of humans. Then there is the bad side that these jobs that are now being taken by automation makes manual labor jobs less available to people that need work. This is an issue that probably won’t be prevalent in my lifetime or near the end of my lifetime.")
  else:
    print ("INVALID INPUT, please try again")
    answer = "empty"
