
from chalice import Chalice
app = Chalice(app_name='mychaliceapp')

@app.route('/battleship/fired/{positionFiredAt}')

#function to evaluate if incoming missile is hit or miss
def HitOrMiss(positionFiredAt):
    # to do validate if this is a valid one, given the existing board
    #never trust the input
        
    # get the list of targetareas
    positionOfShips = ("a1","a2","e5")
            
    #evaluate
    if positionFiredAt in positionOfShips:
        return{"Hit"}
    elif positionFiredAt != positionOfShips:
        return{"Miss"}
    else:
        return{"Error"}
    