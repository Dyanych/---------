def fizzBuzz(n):
    for i in range(1,n+1):
        print( _ if (_ := (i%3 == 0) * 'Fizz' + (i%5 == 0) * 'Buzz') else i, end=(i%n != 0)*', ')

n =150 #Check from 1 to n
fizzBuzz(n)
