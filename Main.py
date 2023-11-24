import math

def main():
    print (gcd(8, 10))



# remainder(num,div) returns the remainder when num is divided by div
def remainder(num, div) :
    return num % div

# gcd(a,b) returns the greatest common divisor of a and b
def gcd (a, b) :
    if (a < b): 
        return gcd(b,a)
    elif (a % b == 0) :
        return b
    else : 
        return gcd(b, a % b)

#eea(r1, r2) uses the euclidean algorithm; returns the entire row
def eea (r1, r2) :
    r1 = list(r1)
    r2 = list(r2)
    if (r1[2] % r2[2] == 0):
        return r1
    else:
        q = r1[2] // r2[2]
        x = r1[0] - r2[0]*q
        y = r1[1] - r2[1]*q
        r = r1[2] % r2[2]
        newRow = [x,y,r,q]
        return eea (r2, newRow)

# quadraticFormula solves an equation in the form (ax^2 + bx+ c = 0)
# returns tuple with the 2 possible x values 
def quadraticFormula (a,b,c): 
    result1 = -b - math.sqrt(pow(b) - 4*a*c)
    result2 = -b + math.sqrt(pow(b) - 4*a*c)

    return (result1 / 2*a), (result2/ 2*a)

# mean(lon) finds the mean value from a list of numbers
# returns average
def mean (lon) :
    sum = 0
    for n in lon: 
        sum += n
    return sum/len(lon)

# mode(lon) find the mode, or the element with the most occurences, from a list of numbers. 
# 
def mode (lon) : 
    maxCount = 0
    numSet = {}
    dict = {} 
    for n in lon: 
        if (dict.get(n) == None) : 
            dict[n] = 1
        else: 
            dict[n]= dict.get(n) + 1

        if (dict.get(n) == maxCount) : 
            numSet.add(n)
        elif (dict.get(n) > maxCount) : 
            numSet.clear()
            numSet.add(n)
            maxCount = dict.get(n)

# median(lon) calculates the median
# list of numbers -> number
def median (lon) : 
    lon.sort()
    mid = int(len(lon)/2)
    if (len(lon) % 2 == 1) : 
        return lon[mid]
    else : 
        return (lon[mid-1]+lon[mid])/2
    
def hypotenuse(a,b): 
    return (a**2 + b**2) ** 0.5

def distBetweenPoints(p1, p2): 
    deltax = (p2[0] - p1[0])
    deltay = (p2[1] - p1[1])
    return hypotenuse(deltax, deltay)

def solveLDE(a,b,d): 
    if (d % gcd(a,b) != 0) :
        return False
    else: 
        factor = int(d/gcd(a,b))
        result = eea([1,0,a,0],[0,1,b,0])
        return (result[0] * factor, result[1] * factor)

def factorial(x): 
    product = 1
    for i in range (1, x+1): 
        product *= i
    return product

if __name__ == "__main__":
    main()

                


    
    
    
