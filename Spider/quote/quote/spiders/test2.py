class Fab(object): 
 
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 
 
    def __iter__(self): 
        return self 
 
    def __next__(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()
 
for n in Fab(5): 
    print(n)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


t='Erving'
i=iter(t)
for i in range(6):
    print(next(i))
print(next(i))
print(next(i))
print(len(t))
