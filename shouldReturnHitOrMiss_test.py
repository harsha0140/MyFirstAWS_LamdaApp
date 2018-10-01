# -*- coding: utf-8 -*-

from Battleship_HitMiss import HitOrMiss

#Given that a part of a ships is present at location e6
#When a missile hits target e5
#Then it's reported as hit

def test_Hit():
    
    assert HitOrMiss("e6") == {"Hit", 'e6'}

#Given that no ship is present at location d4
#When a missile hits target d4
#Then it's reported as miss
def test_Miss():
    
    assert HitOrMiss("d4") == {"Miss", 'd4'}
