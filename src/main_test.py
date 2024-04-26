# Import code to test
from main import factorial_iterative as FI, factorial_recurssive as FR

def setup_functions(p_some_test_function):
    # Called before every function
    msg = f"Will now call the test function" + \
    f"{p_some_test_function.__name__}"
    
    print (msg)
# def

def teardown_function(p_some_test_function): 
    msg = f"Finished calling the test function" + \
    f"{p_some_test_function.__name__}"
    
    print (msg)
    
TEST_THIS = 33
def test_our_only_test():
    fr = FR(TEST_THIS)
    fi = FI(TEST_THIS)
    
    # Verefies if the following code is true, panics/throws exception if not
    try:
        assert(fr == fi)
        print("TEST PASSED")
        return True
    except Exception:
        print("TEST FAILED")
        return False