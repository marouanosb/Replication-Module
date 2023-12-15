import time

# 'i' stands for the number of times we want to replicate the experience
# 'j' stands for the number of times we want to repeat the funtion
# 'func' stands for the function we want to replicate
# 'args' is the list of arguments the are passed when calling the function call
def replicate(i, j, func, args):
    outerResults = []
    for x in range(i):
        innerResults = []
        for y in range(j):
            innerResults.append(func(args))
        outerResults.append(innerResults)

    return outerResults