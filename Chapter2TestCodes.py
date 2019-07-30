#chapter 2
#and evaluates true if both are true
print(True and True)
print(True and False)
print(False and False)
print(False and True)
#Or evaluates true if either of the two is true
print(True or True)
print(True or False)
print(False or True)
print(False or False)
#not operator evaluates the oppsite Boolean value
print(not True)
print(not False)
#mixed
print( (4<5) and (5<6) )
print( (4<5) and (9<6) )
#blocks
password = input()
if password == 'Shivani':
    print('Welcome Aboard')
else:
    print('Access denied')
#while loop statements
inbox = 0
while inbox < 5:
    print('Inbox')
    inbox = inbox + 1
    
#import
import random
for x in range(5):
    print(random.randint(1,10))
    
#infiniteloop
while True:
    print('Hello World')
    
