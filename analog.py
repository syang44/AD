pre = 0
curr = 1
fibonacci = "1"
fibSeq = "1"
pos = 0

def isPrime(n):
    if n == 0 and n == 1:
        return False

    i = 2

    while(i*i <= n):
        if (n % i == 0): 
            return False
        i +=1
    
    return True


#compute next fibonacci number
def nextFibNum():
    global pre, curr
    next = pre + curr
    pre = curr
    curr = next
    return next


#concatenate fibonacci numbers
def FibSeq():
    global fibonacci
    newNum = str(nextFibNum())
    fibonacci += newNum
    return fibonacci


#splice 10 consecutive digits from Fibonacci sequence
def split():
    res = fibonacci[pos: pos+10: 1]
    return res

#find 10 consecutive digit prime number
def findTenDigitPrime():
    global pos
    res = 0
    prime = False
    
    while(not prime):
        #compute next fibonacci number if there aren't enough digits
        if(len(fibonacci) - pos < 11):
            FibSeq()
            continue
        
        stringNum = split()
        res = int(stringNum)
        prime = isPrime(res)
        pos += 1
    
    return res


#find nth 10-digit prime number in Fibonnaci
def findNthPrime(n):
    i = 1
    res = 0
    while(n > 0):
        res = findTenDigitPrime()
        #print(i, "th: ", res, "\n")
        i += 1
        n -= 1
    
    return res

#match number to corresponding letter
def match(n):
    return chr(ord('a')+n)

def letter(n):
    mod = n % 26
    return match(mod)

#find word corresponding to 10 digit number
def word(n):
    res = ""
    for i in range(0, 10, 2):
        digit = n[i:i+2:1]
        print(digit)
        l = letter(int(digit))
        res += str(l)
    return res

#run each number separately or reset fibonacci
#firstNum = findNthPrime(44722)
secondNum = findNthPrime(53215)
#print(word(str(firstNum)))
print(word(str(secondNum)))


