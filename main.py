print(''' "KBC " ''')
a=input("what is your name?")
print('are you ready "/n" 1.yes"/n" 2.no')
choice=int(input("1,2- "))
game_end = False
while not game_end :
    

    if choice==1:
     print("que.1:who is the devloper of python?")
     print('ans:1.Guido van rossum. \t 2.Ayush tiwari.\n 3.BJARNE stroustrup.\t 4.James gosling.')
     ans=int(input("1,2,3,4- "))
    if ans==1:
        print("correct answer now going for the next question")
        game_end = True
    else :
        
        is_game_on=True
        print("sorry you loose! better luck ")
        break
        game_end = True
      
        #is_game_on=Truez
    
    print("que.2:who is called as THE GOD OF CRICKET?") 
    print('ans:1.SACHIN TENDULKAR.\t 2.VIRAT KOHLI.\n 3.MS.DHONI.\t 4.RAHUL DRAVID ')
    ans=int(input("1,2,3,4- ")) 
    if ans==1:
      print("correct two in a row,keep going")
    else:
     print("sorry you loose:score=1/5")
     break
    print("que.3:what is the capital of india? ")
    print('ans:1.delhi./t 2.bhopal./n 3.ratibad./t 4.nepal.')

    ans=int(input("1,2,3,4-")) 
    if ans==1:
       print("yess!it is correct,good ")
    else:
       print("sorry the answer is wrong.score=2/5")
       break
    print("que.4: who is the father of computer?")
    print('ans:1.donald babbage./t 2.charles babbage./n 3.dugald bromhead./t 4.joseph louise ')
    ans=int(input("1,2,3,4-"))
    if ans==2 :
       print("hurrey! you are an amazing player")
    else :
       print("sorry the answer is incorrect.score=3/5")
       break
    print("que.5:what is the value of pi?")
    print('ans:1.5./t 2.4.17./n 3.3.17./t 4.3.14 ')
    ans=int(input("1,2,3,4-"))
    

    if ans==4:
        
       print("congo! you are a genius,score=5/5")
    else:
       print("better luck next time but you ar a good player,score=4/5")

