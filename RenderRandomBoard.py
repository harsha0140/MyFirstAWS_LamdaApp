# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 23:15:04 2018

@author: weij3721
"""
import boto3
from random import randint




def placeship(boardsize, shipname, shiplength):
  
    boardsize = 10
    
    #first ship, battleship, length 5
    shiplength = 5
    xcoordinate = randint(1,(boardsize-shiplength))
    ycoordinate = randint(1,(boardsize-shiplength))
    shipdirection = randint(0,1)
    print(xcoordinate, ycoordinate,shipdirection)
    if shipdirection == 0: #horizontal
        x = 1
        while x <= shiplength:
            shipcoordinates = [xcoordinate, ycoordinate]
            print (shipcoordinates)
            x +=1
            xcoordinate +=1
            shipcoordinates.append( [xcoordinate, ycoordinate])
    else:
        y = 1 #vertical
        while y <= shiplength:
            shipcoordinates = [xcoordinate, ycoordinate]
            print (shipcoordinates)
            y +=1
            ycoordinate +=1
            shipcoordinates.append( [xcoordinate, ycoordinate])
    
     #add illegal coordinates
     #must always be one extra on all sides
     
     #or just check existing positions? might be easier?
     
     #store in s3 bucket
     s3 = boto3.resource('s3')
     object = s3.Object('battleship-ship-positions', 'ship_positions_generated.txt')
     object.put(Body=bytes(str(shipcoordinates), 'utf-8'))
     