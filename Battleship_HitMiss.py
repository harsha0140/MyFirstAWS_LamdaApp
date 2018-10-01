import boto3
from chalice import Chalice
app = Chalice(app_name='mychaliceapp2')

@app.route('/battleship/fired/{positionFiredAt}')

#function to evaluate if incoming missile is hit or miss
def HitOrMiss(positionFiredAt):
    # to do validate if this is a valid one, given the existing board
    #never trust the input
    s3 = boto3.resource('s3')
    obj = s3.Object("battleship-ship-positions", "battleship_boardsize_game1.txt")
    boardsize = obj.get()['Body'].read().decode('utf-8')
    print(boardsize)
    
    #split input into two, first two characters only
    positionFiredAt="e4"
    if 0 > len(positionFiredAt) < 3:
        FirstCharacter = positionFiredAt[:1]
        SecondCharacter = positionFiredAt[:2]
        print (FirstCharacter, SecondCharacter)
    else:
        print ("not valid")
        return("Invalid input for target")
    # get the list of targetareas
    #positionOfShips = ("a1","a2","e6")
   

    obj = s3.Object("battleship-ship-positions", "battleship_positions_game1.txt")
    positionOfShips = obj.get()['Body'].read().decode('utf-8')
    print (positionOfShips)
            
    #evaluate
    if positionFiredAt in positionOfShips:
        return{"Hit", positionFiredAt}
    elif positionFiredAt != positionOfShips:
        return{"Miss", positionFiredAt}
    else:
        return{"Error"}
    