class Names:
    def __init__(self, n):
      self.n = n
      x = []
      for i in range(n):
        name = input("name: ")
        x.append(name)
      self.x=x  

    def max(self):
      xmax = self.x[0]
      for i in self.x:
        if len(i) > len(xmax):
            xmax = i
      return xmax
                    
    def min(self):
      xmin = self.x[0]
      for i in self.x:
        if len(i) < len(xmin):
            xmin = i
      return xmin
n= Names(int(input("Enter the number of names: ")))
print("The length of the name with maximum length is", n.max())           
print("The length of the name with minimum length is", n.min())
