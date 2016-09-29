from binsearch import binary_search
from pytest import raises

def test_zero_element():
    assert binary_search([],1) == -1
    
def test_one_element_exist():
    assert binary_search([1],1) == 0

def test_one_element_not_exist():
    assert binary_search([1],0) == -1

def test_two_element_exist():
    assert binary_search([1,2],1) == 0
    
def test_two_element_not_exist():
    assert binary_search([1,2],3) == -1
        
def test_smaller_than_min():
    assert binary_search([3,5,7],1) == -1      
    
def test_larger_than_max():
    assert binary_search([3,5,7],9) == -1     
    
def test_does_not_exist():
    assert binary_search([1,2,6],5) == -1        

def test_string_list_type_exist():
    assert binary_search(['apple','banana','cherry','peach'],'peach')

def test_mix_list_type_not_exist():
    assert binary_search(['apple','banana','cherry','peach'],'donuts')     
    
def test_not_an_array():
    with raises(TypeError):
        binary_search(2, 2)
        
def test_list_na():

def test_needle_na():
def test_both_na():
def test_list_infty():
def test_needle_infty():
def test_both_infty():
def test_multiple_element():   
    
def test_left_greater_than_right():
    with raises(IndexError):
        binary_search([2,3,5], 3, 3, 2)
        
def test_left_equal_right_exist():
    

def test_left_equal_right_not_exist():

def test_left_smaller_than_right_exist():

def test_left_smaller_than_right_not_exist():

#def test_wrong_needle_type():