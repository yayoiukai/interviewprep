#Dutch National Flag 
#RGB

# start from random list of three character such as "RGGBGRRGGBGBGR"
# then, it will sort RRRRGGGGGBBBBB" Well,, actually dutch flag is white in the middle
# this one is used green. 
# also this one supposed to be inposition sorting and input is given in array format. 


def swap(colors,i,position):
    temp=colors[position]
    colors[position] = colors[i]
    colors[i] = temp
    return colors 

def sortcolors(colors):
    red = 0 
    blue = len(colors) - 1 
    i = 0 
    while i < blue:
        c = colors[i]
        if c == "B":
            swap(colors,i,blue)
            blue -= 1 
        elif c == "R":
            swap(colors,i,red)
            red += 1 
        else:
            i += 1  # color is G so just advance i index. 

    return colors 




