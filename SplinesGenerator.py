# SplinesGenerator.py
# Author: Tinli Yarrington
# Date: 3/22/15
# Dates edited: 3/23/15, 3/24/15, 3/25/15, 3/26/15
# Purpose: user inputs number of vertices and values of sides, and program generates bases splines for those graphs
# Notes:
#       - change program so it can take more than three vertices
#       - confirm that splines being generated are bases

'''def turnToInt(sides):
    for side in range(0,len(sides)):
        sides[side] = int(sides[side])

def generateSplines(integerMod, vertices, sides):
    trivialSpline = []
    splines = []

    for side in range(0,vertices-1):
        trivialSpline.append(1)


def main():
    bar = "+" + ("-"*48) + "+"
    print(bar)
    print("|{0:^48}|".format("SPLINES GENERATOR"))
    print(bar)
    print()
    integerMod = eval(input("What is the moduli for this graph?   "))
    vertices = eval(input("How many vertices does your graph have?   "))
    sides = input("What are the values of the sides of your graph? (separate each side with a space)   ")
    sides = sides.split(" ")
    turnToInt(sides)

    generateSplines(integerMod, vertices, sides)

main()'''

import itertools

def main():
    '''
    splines = []

    moduli = eval(input("What moduli are you using for your graph?   "))
    vertices = eval(input("How many vertices does your graph have?   "))
    sides = input("What are the values for the sides of your graph? (please separate each number with a space)   ")
    sides = sides.split(" ")
    
    for side in range(0,len(sides)):
        sides[side] = int(sides[side])

    for vertice in range(0,vertices):
        splines.append([])
        for zero in range(0,vertice):
            splines[vertice].append(0)

    for one in range(0,vertices):
        splines[0].append(1)
    
    print(splines)

    for spline in splines:
        while len(spline) < vertices:
            for vertice in range(len(spline)-1,vertices-1):
                for num in itertools.count(1):
                    if (num - spline[vertice-1])%sides[vertice-1] == 0 and num !=spline[vertice-1] and num%sides[vertice] == 0:
                        spline.append(num)
                        break
    '''
    vertices = 3
    splines = []

 #   moduli = eval(input("What moduli are you using for your graph?   "))
 #   vertices = eval(input("How many vertices does your graph have?   "))
    sides = input("What are the values for the sides of your graph? (please separate each number with a space)   ")
    sides = sides.split(" ")
    
    for side in range(0,len(sides)):
        sides[side] = int(sides[side])

    for vertice in range(0,vertices):
        splines.append([])
        for zero in range(0,vertice):
            splines[vertice].append(0)

    for one in range(0,vertices):
        splines[0].append(1)
    
    print(splines)

    for spline in splines:
        while len(spline) < 3:
            for vertice in range(len(spline),vertices):
                for num in itertools.count(1):
                    if len(spline) == (vertices-1) and num%sides[vertice] == 0 and num%sides[vertice-1] == 0:
                        spline.append(num)
                        break
                    elif (num - spline[vertice-1])%sides[vertice-1] == 0 and num != spline[vertice - 1]:
                        print(spline,len(spline), num)
                        spline.append(num)
                        break
    print(splines)

    '''for num in itertools.count(1):
        if num%sides[0] == 0:
            splines[1].append(num)
            break
    
    for num in itertools.count(1):
        if (num-splines[1][1])%sides[1] == 0 and num%sides[2] == 0:
            splines[1].append(num)
            break

    for num in itertools.count(1):
        if (num-splines[2][1])%sides[1] == 0 and num%sides[2] == 0:
            splines[2].append(num)
            break

    print(splines[0], splines[1], splines[2])

    for vertice in range(0,vertices):
        if splines[1][vertice] >= moduli:
            splines[1][vertice] = splines[1][vertice]%moduli
    for vertice in range(0,vertices):
        if splines[2][vertice] >= moduli:
            splines[2][vertice] = splines[2][vertice]%moduli
    
    print(splines[0], splines[1], splines[2])'''
    
main()
            
