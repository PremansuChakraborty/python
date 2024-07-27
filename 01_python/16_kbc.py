# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

question=("1.	Which of the following laws is associated with the heating effect of electric current ?",
      "2.   The value of acceleration due to gravity ‘g’ depends on: 1. Constant of Gravitation ‘G’ 2. Mass of the earth ‘M’ 3. Mass of the falling object ‘m’ 4. Radius of the earth ‘R’ ?",
      "3.	Which element in the periodic table forms maximum number of compounds ?",
      "4.	A body at rest can have ?",
      "5.	A solid metallic hemisphere with radius r is melted and cast into a solid right circular cone with the radius of the base = r. What is the ratio of their curved surface areas ?",
      "6.	How much work is done in moving a charge of 5 C across two points having a potential difference of 16 V ?",
      "7.	Which of the following statements is true ?",
      "8.	Mendeleev could not assign a correct position to which of the following elements in his table ?",
      "9.	The atmospheric pressure at sea level is ........ atm ?",
      "10.	Who demonstrated that objects of different masses would reach the ground together when dropped from the same height ?"
      )
option=("A. Joule's law , B. Ohm's law , C. Faraday's law , D.  Newton's law ",
        "A. a, c, d ,   B. b, c, d ,  C.  a, b, c ,   D.  a, b, d ",
        "A. H,  B.  O,  C.  S , D.  C",
        "A. Speed, B.   Velocity, C.  Momentum, D.   Energy ",
        "A.5/?2, B. 2/?5, C. 3/2 , D. 5/2 ",
        "A. 65 J, B. 45 J, C. 40 J, D. 80 J ",
        "A. Carbon monoxide diffuses from lungs into blood and oxygen diffuses from blood into lungs, B. Carbon dioxide diffuses from lungs into blood and oxygen diffuses from blood into lungs, C. Oxygen diffuses from lungs into blood and carbon dioxide diffuses from blood into lungs, D. Oxygen diffuses from lungs into blood and carbon monoxide diffuses from blood into lungs ",
        "A.Lithium, B. Potassium, C. Hydrogen, D. Helium ",
        "A. 0.001, B. 1, C. 0 , D. 0.1",
        "A.Isaac Newton, B. Archimedes , C. Robert Boyle, D. Galileo Galilei ")

answer=("A","D","D","B","B","D","C","C","B","D")
ammount=0
score=0
print("RULE: ANY WRONG ANSWER QUIT THE GAME")
def input1(index):
    str=input("Enter the correct option: A or B or C or D:\t")
    if answer[index]==str.upper():
        global score
        score = score + 10
        global ammount
        ammount=ammount + 1000*score
        return "CORRECT ANSWER YOUR SCORE and wining ammount: ",score," & ",ammount 
    else:
        global exit
        exit=True
        return "your score and wining ammount: ",score," & ",ammount 


for i in range(0,10):
    print(question[i])
    print(option[i])
    print(input1(i))
    if exit!=True:
     str1=input("do you want to goto next quextion then press: Y\n or to quit the game press any key.")
     if str1.upper()!="Y":
         print("your final score and wining ammount: ",score," & ",ammount)
         break
     print("Next question".center(120,"."))
    else:
        break
    
    