""" learning python string"""
#decalse string
astring = "hello"
astring1= "somnath bachal"

print astring
print astring1

a = len(astring)
print a

print astring.index("o")
print astring[1]
print astring[4]

print astring.count("o")

b=astring[0:3]
print b

e = astring1[0:14:2]
print e
print astring1[::-1]

m = astring1.split("h")
print m

n="8"
p=2.5
i=90
u=[1,2,3,"ab"]
print 2*n
print 2 * int(n)
z=type(u)
print z


d="abcd"
k=list(d)
print k
