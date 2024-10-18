class Names:
    def __init__(self,n):
        self.n=n
        self.x=[]
        for i in range(n):
            name=input("name :")
            self.x.append(name)
        

    def max(self):
        xmax=len(self.x[0])
        for i in range(n):
           if len(self.x[i])>xmax:
               xmax=len(self.x[i])
           else:
               xmax=len(self.x[0])
        return xmax      

    def min(self):
        xmin=len(self.x[0])
        for i in range(n):
           if len(self.x[i])<xmin:
               xmin=len(self.x[i])
           else:
               xmin=len(self.x[0])         
        return xmin       
               
names=Names(int(input("Enter the number of names:")))           
print("The name with maximum length is ",names.max())           
print("The name with minimum length is ",names.min())           
