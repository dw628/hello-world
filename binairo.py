#dw20200803 Binairo modified from sudoku.py

import numpy as np

grid = [
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9]
]

# from Brain Games
grid = [
[0,9,0,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,1,9,9,9,9,0,0,9],
[9,9,9,0,0,9,9,9,9,9],
[1,9,9,9,9,9,9,0,9,0],
[9,9,9,9,0,9,0,9,9,0],
[9,9,9,9,9,9,9,9,9,9],
[9,9,1,9,1,9,9,9,0,9],
[9,9,9,9,1,9,9,0,0,9],
[9,9,1,9,9,0,9,9,9,9]
]

grid = [
[9,9,9,9,1,9,0,9,9,9],
[9,1,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,0,0,9],
[9,9,0,9,9,9,9,9,9,9],
[1,9,9,9,0,9,1,9,0,9],
[9,9,9,9,9,9,9,9,9,1],
[9,9,9,9,9,0,0,9,9,1],
[1,0,0,9,9,9,9,9,9,9],
[9,9,9,9,0,0,9,9,0,9],
[9,9,1,9,9,9,1,9,0,9]
]


print(np.matrix(grid))

def find_same_col():   # return True if column with same content is found
    global grid
    for x in range(9) : #from 0 to 8
        found = False
        xi = x + 1
        while xi < 10 and not found:
            yi = 0
            found = True
            while yi < 10:
                # print("compare grid[yi][xi] != grid[yi][x]", grid[yi][xi], grid[yi][x])
                if grid[yi][xi] != grid[yi][x] :
                    found = False
                    break
                yi += 1
            # print("x", x, "xi", xi, "found:", found)
            xi += 1
        if found == True :
            return found
    return found

def find_same_row():   # return True if row with same content is found
    global grid
    for y in range(9) : #from 0 to 8
        found = False
        yi = y + 1
        while yi < 10 and not found:
            xi = 0
            found = True
            while xi < 10:
                # print("compare grid[yi][xi] != grid[y][xi]", grid[yi][xi], grid[y][xi])
                if grid[yi][xi] != grid[y][xi] :
                    found = False
                    break
                xi += 1
            # print("y", y, "yi", yi, "found:", found)
            yi += 1
        if found == True :
            return found
    return found

#
def possible(y,x,n) :
    global grid
    # until 5 zeros and 5 ones in every row and column
    # no more than two of the same number can be next to or under each other
    # rows or cols with exactly the same content are not allowed
    #
    # loop the row
    nc = 0
    for i in range(10) : # 0 to 9
        if grid[y][i] == n :
            nc += 1
            if nc >= 5 :
                return False
    # loop the column
    nc = 0
    for i in range(10) : # 0 to 9
        if grid[i][x] == n :
            nc += 1
            if nc >= 5 :
                return False
    # check adjacent cells in row
    nc_lt = 0
    nc_gt = 0
    nc_mid = 0
    xbeg = max(x - 2, 0)
    xend = min(x + 2, 9) + 1
    for i in range(xbeg, xend) :
         if grid[y][i] == n :
             if i < x :
                 nc_lt += 1
             if i > x :
                 nc_gt += 1
             if i == (x-1) or i == (x+1) :
                 nc_mid += 1
    # print("adj row x y:",x,y, "xbeg:",xbeg, "xend",xend, "nc_lt:",nc_lt, "nc_gt:",nc_gt, "nc_mid:",nc_mid)

    if nc_lt >= 2 or nc_gt >= 2 or nc_mid >= 2 :
        return False

    # check adjacent cells in col
    nc_lt = 0
    nc_gt = 0
    nc_mid = 0
    ybeg = max(y - 2, 0)
    yend = min(y + 2, 9) + 1
    for i in range(ybeg, yend) :
         if grid[i][x] == n :
             if i < y :
                 nc_lt += 1
             if i > y :
                 nc_gt += 1
             if i == (y-1) or i == (y+1) :
                 nc_mid += 1
    # print("adj col x y:",x,y, "xbeg:",xbeg, "xend",xend, "nc_lt:",nc_lt, "nc_gt:",nc_gt, "nc_mid:",nc_mid)
    if nc_lt >= 2 or nc_gt >= 2 or nc_mid >= 2 :
        return False

    return True
#
y = 2
x = 6
n = 0
print('y x n =', y, x, n)
print(possible(y,x,n))
y = 2
x = 6
n = 1
print('y x n =', y, x, n)
print(possible(y,x,n))

#
y = 4
x = 9
n = 0
print('y x n =', y, x, n)
print(possible(y,x,n))
y = 4
x = 9
n = 1
print('y x n =', y, x, n)
print(possible(y,x,n))

#
y = 9
x = 0
n = 0
print('y x n =', y, x, n)
print(possible(y,x,n))
y = 9
x = 0
n = 1
print('y x n =', y, x, n)
print(possible(y,x,n))

sc = 0 # solution count


    
def solve() :
    global sc
    # solc += 1 # solve count
    #print("Enter solve, count =", sc)
    global grid
    for y in range(10) : # 0 to 9
        for x in range(10) :
            if grid[y][x] == 9 :
                for n in range(2) : # 0 to 1
                    if possible(y,x,n) :
                        grid[y][x] = n
                        #print(y,x,n," y x n is possible on sc =", sc, "grid =", grid[y])
                        #input("Continue?")
                        solve()
                        grid[y][x] = 9
                    #else :
                        #
                        #print(y,x,n," y x n is NOT possible on sc =", sc)
                return
    # rows or cols with exactly the same content are not allowed
    # ???
    
    # print result
    sc += 1
    print("Solution #", sc)
    print(np.matrix(grid))
    if find_same_col() :
        print("** Same content in the columns.")
    if find_same_row() :
        print("** Same content in the rows")
    input("More?")
#

solve()
print("No more! Original grid:")
print(np.matrix(grid))
# # """
# # elapsed_time = timeit.timeit(code_to_test, number=1)/100
# # print(elapsed_time)
