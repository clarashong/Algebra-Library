import math

# remainder(num,div) returns the remainder when num is divided by div
def remainder(num, div) :
    return num % div

# gcd(a,b) returns the greatest common divisor of a and b
def gcd (a, b) :
    if (a > b) :
        eea([1,0,a,0],[0,1,b,0])[2]
    else :
        eea([1,0,b,0],[0,1,a,0])[2]

#eea(r1, r2) uses the euclidean algorithm; returns the entire row
def eea (r1, r2) :
    if (r2[2] % r1[2] == 0):
        return r1
    else:
        x = r1[0] - r2[0]
        y = r1[1] - r2[1]
        r = r1[2] % r2[2]
        q = r1[3] // r2[3]
        newRow = [x,y,r,q]
        eea (r2, newRow)

# quadraticFormula solves an equation in the form (ax^2 + bx+ c = 0)
# returns tuple with the 2 possible x values 
def quadraticFormula (a,b,c): 
    result1 = -b - math.sqrt(pow(b) - 4*a*c)
    result2 = -b + math.sqrt(pow(b) - 4*a*c)

    return (result1 / 2*a), (result2/ 2*a)
    
    
