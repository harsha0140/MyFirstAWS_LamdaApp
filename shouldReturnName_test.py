# -*- coding: utf-8 -*-
import json
from app import hello_name
    
def test_name():
    assert hello_name("Remko") == {"hello": 'Remko'}
    
def test2_name():    
    response = hello_name("Remko2")
    #response = post_json(client, '/add', {'key': 'value'})
    #assert response.status_code == 200
    assert response == {"hello": 'Remko2'}
