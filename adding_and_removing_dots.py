from ntpath import join


s = 'test'


def add_dots(s):
    ls = list(s)

    for i in range(len(ls)):

        ls.insert(i * 2, ".")

    ls.remove(ls[0])

    s = ''.join(ls)

    return s

def remove_dots(s):
    ls = list(s)
   
    for i in range(len(ls)):
       
        if ls[i] == '.':
            ls[i] = ""
 
    s = ''.join(ls)
    
    return s

remove_dots("test.")