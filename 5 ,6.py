# بخش پذیری بر اعداد 5 و 6
num =eval(input("Enter your number :"))
if num %5==0 and num %6 ==0 :
    print(" is divisible by 5 and 6 ?" , num %5==0 and num %6 ==0)
if num %5 == 0 or num % 6 == 0 :
    print ("is divisible by 5 or 6 ?" , num %5 == 0 or num % 6 == 0)
if ( num % 5 == 0 or num % 6 == 0 ) and not ( num % 5 == 0 and num % 6 == 0 ) :
    print (" is divisible by 5 or 6, but not both ? " , ( num % 5 == 0 or num % 6 == 0 ) and not ( num % 5 == 0 and num % 6 == 0 ) )