from mypackage import mymodule

def test_top_n(): 
    """
    
    make sure that top_n works correctly 
    
    """
    assert mymodule.top_n([8,3,2,7,4],3) == [8,7,4], 'incorect'
    assert mymodule.top_n([10,1,12,9,2],2) == [10,12], 'incorect'
    assert mymodule.top_n([1,2,3,4,5],5) == [1,2,3,4,5], 'incorect'


