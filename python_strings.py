

a="hello world"
#outputs the whole comment of a string

print(a)
#outputs the first character of the string
print(a[0])
#outputs the last character of the string
print(a[-1])
#outputs the three last characters of hello 
print(a[2:5])
#outputs the whole comment of the string in lower cas
print(a[:])
#outputs the whole comment of the string in lowercase
print(a[0:])
#outputs the string hello
print(a[:6])
#outputs the last three letters of the string hello
print(a[2:6])
#it  explains what the last three letters are
print("string a[2:5] : ", a[2:5])
#it outputs blank
print("string a[5]:",a[5])
#6 is including while 10 is excluding
print("string a[6:10]:",a[6:10])
a="hello"
b="world"
#outputs concatination of hello world
print(a+b)
#outputs hello five times
print(a*5)
#outputs true
print('h'in a)
#outputs false
print('m'in a)
#outputs true
print('x' not in a)

#STRING BUILT-IN METHODS
x="hello mercy"
y="hello"
#(len(),) lower(), upper()
#capitalize()
#print(len(x))
#outputs  the first comment hello in small leter 
print(y.lower())
#outputs the whole string in caps
print(x.upper())
#outputs the first character h in capital the rest in small
print(x.capitalize())
#output method for replace
txt = "I like praying"

x = txt.replace("praying", "travelling")

print(x) 
#outputs the method for find
txt = "Hello, python is such an interesting program to learn."

x = txt.find("to")

print(x)
#output method for splitting
txt = "welcome to zetech university"

x = txt.split()

print(x)

#output method for title
txt = "Welcome to page"

x = txt.title()
print(x)
#output method for encoding
txt = "My name is mercy"

x = txt.encode()

print(x)