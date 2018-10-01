import boto3
import string
from chalice import Chalice
app = Chalice(app_name='mychaliceapp2')

@app.route('/battleship/fired/{positionFiredAt}')

#function to evaluate if incoming missile is hit or miss
def HitOrMiss(positionFiredAt):
    # to do validate if this is a valid one, given the existing board
    #never trust the input
    s3 = boto3.resource('s3')
    obj = s3.Object("battleship-ship-positions", "battleship_boardsize_game1.txt")
    boardsize = int(obj.get()['Body'].read().decode('utf-8'))
    if boardsize > 26:
        return {"boardsize invalid"}
    
    #to do: error handling for Not A Number
    #print(boardsize)
    
    #split input into two, first two characters only
    #positionFiredAt="p8"
    #print (len(positionFiredAt))
    if 0 < len(positionFiredAt) < 4:
        FirstCharacter = positionFiredAt[0]
        FirstCharacter = FirstCharacter.upper()
        SecondCharacter = int(positionFiredAt[1:2])
     #   print (FirstCharacter, SecondCharacter)
        
        #compare
        if not (FirstCharacter <= string.ascii_uppercase[boardsize] \
                and (SecondCharacter <= boardsize or SecondCharacter < 27)):
                #print ("Invalid input for target")
                return{"Invalid input for target"}
       # else:
                #print("input valid")
        #        return("Invalid input for target")
        
    else:
        #print ("not valid")
        return{"Invalid input for target, too long"}
    # get the list of targetareas
    #positionOfShips = ("a1","a2","e6")
   

    obj = s3.Object("battleship-ship-positions", "battleship_positions_game1.txt")
    positionOfShips = obj.get()['Body'].read().decode('utf-8')
    #print (positionOfShips)
            
    #evaluate
    if positionFiredAt in positionOfShips:
        return{"Hit", positionFiredAt}
    elif positionFiredAt != positionOfShips:
        return{"Miss", positionFiredAt}
    else:
        return{"Error"}
    