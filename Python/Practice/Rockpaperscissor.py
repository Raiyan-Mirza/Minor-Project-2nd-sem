#ROCK,PAPER SCISSOR GAME
#Can also be done using sets{ }

import random
opt=('ROCK','PAPER','SCISSOR')

print("Heyy!Are you ready for rock,paper scissors game?")
print("----------------------------------------------------------------------------")

    
while True:
     com= random.choice(opt)
     sel1=input("Pick amoung ROCK,PAPER AND SCISSOR: ")
     sel= sel1.upper( )

     print(f"PLAYER:{sel}")
     print(f"COMPUTER:{com}")

     if com == "ROCK" and sel== "SCISSOR":
          print("You Lost")

     elif com == "ROCK" and sel== "PAPER":
          print("You WIN!!")

     elif com == "PAPER" and sel== "SCISSOR":
          print("You WIN!!")

     elif com == "PAPER" and sel== "ROCK":
          print("You Lost")    
    
     elif com == "SCISSOR" and sel== "PAPER":
          print("You Lost")

     elif com == "SCISSOR" and sel== "ROCK":
          print("You WIN!!")

     elif sel =="EXIT":
            print("WELL PLAYED,PLAY AGAIN WITH US.")
            break



     elif com == sel:
            print("PICK AGAIN")
      
        
     else:
             print("INVALID INPUT")
             continue
      

     print("----------------------------------------------------------------------------")










