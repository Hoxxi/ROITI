"""
You have the following function:
def loop(times):
for i in range(times):
if i == 10:
break
Make it so the break condition can be dynamically defined. You can change anything you want in the code.

"""

def loop(times, break_state):
    for i in range(times):
        if break_state(i):
            break


"""
When the function is set like this, the user can give any king of break condition. 
This replaces the hardcoded if i == 10 condition
For example lambda function:
loop(20, lambda x: x == 10)
"""