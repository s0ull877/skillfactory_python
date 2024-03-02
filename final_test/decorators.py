import os

# при достижении 3 неправильных ответов консоль чистится
def counter(fn):
    count = 0
    def wrapper(*args):
        nonlocal count
        
        result = fn(*args)
        count += 1
        if count == 3 or result[-1]: #result[-1] тот самый side_choosen ->
        # счетчик сбрасывается, чтобы не было багов в следующем кОне
            count = 0
            os.system('cls')
        return result
    
    
    return wrapper