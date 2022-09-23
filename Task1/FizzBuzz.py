for i in range(1,101):
    print( _ if (_ := (i%3 == 0) * 'Fizz' + (i%5 == 0) * 'Buzz') else i, end=(i%100 != 0)*', ')
