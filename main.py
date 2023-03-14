#Find an example where g is a Prim Root mod p:prime but not mod p^2
#this means you would have to use g + p as the prim root

#determines if n is prime and returns a boolean
def isPrime(n):
    #edge cases: n <= 1
    if n <= 1: return False

    #iterative approach
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

#returns a list of all prime factors of n
def getPrimeFactors(n):
    #edge cases: n <= 1
    if n <= 1:
        return [1]
    else:
        #divide by first prime encountered until 1
        primeFactors = []
        nCopy = n

        #iterate until nCopy = 1. i.e. there are no more prime factors
        
        i = 2
        while nCopy != 1:

            #iterate from 2 until the first prime factor
            while isPrime(i) and nCopy % i == 0:
                primeFactors.append(i)
                nCopy /= i
                i = 1
            i += 1

        return primeFactors           

#Euler Phi Function
#see: https://en.wikipedia.org/wiki/Euler%27s_totient_function
def eulerPhi(n):

    #handle invalid input
    if n <= 1:
        print('Invalid input for Euler Phi Function - Please enter a Natural Number larger than 1')
        return
    
    #break into all prime factors then multiply all PHI(p) together for p in pfactors
    #recall that PHI(p) = p - 1
    pfactors = getPrimeFactors(n)

    #count all of the same prime number and pair them as lists with the prime and the power it has
    pPairs = []
    prime = pfactors[0]
    pAmt = 1
    index = 1

    if len(pfactors) == 1:
        #only one element so make pPairs that element with 1
        #eg. [[3, 1]]
        pPairs = [[prime, 1]]

    else:
        #loop through entirety of prime factors
        while index != len(pfactors):

            #if there is a new prime then we input the data for the old prime and update this current data
            if pfactors[index] != prime:
                pPairs.append([prime, pAmt])
                pAmt = 1

            #its the same prime so we increment pAmt
            else:
                pAmt += 1

            index += 1

    #ends on a prime that has more than one isntance in pfactors
    if pAmt != 1:
        pPairs.append([prime, pAmt])

    result = 1
    #calculate the result and return it
    for pList in pPairs:
        result *= ((pList[0] ** pList[1]) - (pList[0] ** (pList[1] - 1)))

    return result

#Order of an element m mod n
#calculated by finding the smallest positive integer r s.t. a^r === 1 mod m
def orderMod(m, n):

    #i will be the power that will be iterated until an exit condition is reached
    #exit conditions:
    #   m^i % n mod 1 -> found it
    #   m^i % n mod 0 -> wont ever be found
    #   there is a repeat in the powers being calculated -> wont ever be found
    i = 2
    repeat = m % n
    while (m**i % n != 1) and (repeat != (m**i % n)) and (0 != (m**i % n)):
        i += 1

    #if its got an order return the order. else return -1 since it doesnt have one
    if m**i % n == 1:
        return i
    else:
        return -1

#Determines of g is a primitive root of p or not
def primRootCalc(g, p):
    if orderMod(g, p) == eulerPhi(p):
        return True
    else:
        return False

#Finds and returns all primitive roots for given number as a list
def findPrimRoots(n):

    #finds all primitive roots starting from 2 to n-1
    primRoots = []
    for i in range(2, n):
        if primRootCalc(i, n): primRoots.append(i)

    #print the entire list of primitive roots
    for p in primRoots: print(p)

    return primRoots

#iterate until conditions are met for E.C.
def extraCredit():

    #starting nums
    g = 2
    p = 3

    while not((primRootCalc(g,p)) and (not primRootCalc(g, p**2))):
        print(g, p)
        #iterate through all of g until p
        if g != p - 1:
            g += 1

        else:
            #g = p - 1 and doesnt meet criteria. so we reset g to 2
            g = 2

            #find the next prime
            p += 1
            while not isPrime(p):
                p += 1

    print(primRootCalc(g,p), primRootCalc(g,p**2), primRootCalc(g + p, p**2))


#later add user input
#func: user input grabbing

#findPrimRoots(23)
#extraCredit()