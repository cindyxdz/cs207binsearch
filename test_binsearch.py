from binsearch import binary_search
from pytest import raises
import numbers
import numpy as np

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
    
def test_does_not_exist_middle():
    assert binary_search([1,2,6],5) == -1        

def test_string_list_exist():
    assert binary_search(['apple','banana','cherry','peach'],'peach')

def test_string_list_not_exist():
    assert binary_search(['apple','banana','cherry','peach'],'donuts')     
    
def test_not_an_array():
    with raises(TypeError):
        binary_search(2, 2)

def test_list_na():
    assert isinstance(binary_search([1,np.nan,2], 2),int)
        
def test_needle_na():
    assert isinstance(binary_search([1,2,4], np.nan), int)
        
def test_both_na():
    assert isinstance(binary_search([1,np.nan,2], np.nan),int)
        
def test_list_infty():
    assert binary_search([1,2,np.inf], 1) == 0
    
def test_needle_infty():
    assert binary_search([1,2,3], np.inf) == -1

def test_both_infty():
    assert binary_search([1,2,np.inf], np.inf) == 2
    
def test_multiple_element():   
    assert isinstance(binary_search([1,2,2,3,4,4,5],2), int)
    
def test_left_greater_than_right():
    assert binary_search([2,3,5], 3, 3, 2) == -1
        
def test_left_equal_right_exist():
    assert binary_search([1,2,3,4,5],4,3,3) == 3

def test_not_exist_in_range_but_in_list():
    assert binary_search([1,2,3,4,5],5,3,3) == -1

def test_left_smaller_than_right_exist():
    assert binary_search([1,2,3,4,5],5,1,4) == 4

def test_left_smaller_than_right_not_exist():
    assert binary_search([1,2,3,4,5],5,1,3) == -1