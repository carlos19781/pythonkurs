""" 
Call Stack: Aufrufstapel
"""
def fn():
    print("fn")
    3 / 0

def f():
    fn()
    print("f")

def g():
    try:
        f()
    except ZeroDivisionError as e:
        print("save:", e)
    print("g")


g()


