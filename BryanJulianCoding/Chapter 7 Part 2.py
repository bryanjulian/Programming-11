x = "This is a sample string"
x = "0123456789"
 
print("x=", x)
 
# Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])
 
# Accessing from the right side
print("x[-1]=", x[-1])
 
# Access 0-5
print("x[:6]=", x[:6])
# Access 6
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

a = "Hi There"
print(len(a))
 
b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

#for character in "This is a test.":
#    print(character)
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
n = int(input("Enter a month number: "))
if n == 1:
    print(months[0:3])
if n == 2:
    print(months[3:6])
if n == 3:
    print(months[6:9])
if n == 4:
    print(months[9:12])
if n == 5:
    print(months[12:15])
if n == 6:
    print(months[15:18])
if n == 7:
    print(months[18:21])
if n == 8:
    print(months[21:24])
if n == 9:
    print(months[24:27])
if n == 10:
    print(months[27:30])
if n == 11:
    print(months[30:33])
if n == 12:
    print(months[33:36])
    
#plain_text = "This is a test. ABC abc"
 
#for c in plain_text:
    #print(c, end=" ")
    
plain_text = "This is a test. ABC abc"
 
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end="")
plain_text = "This is a test. ABC abc"
 
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)
encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"
 
plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)