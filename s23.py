class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    def n(self):
        node=self
        score=0
        while node!=None:
            print(node.val)
            s1=input("answer : ")
            s2=input("t or f : ")
            if s2=="t":
                score+=1
                node=node.left
                print("score = ",score)
                print("----------------------")
            else:
                node=node.right
                print("score = ",score)

            if node==None:
                print("--------finish--------")
q1="q1: 3*7="
q2="q2: 9*2="
q3="q3: 6*4"
q4="q4: 2*0"
q5="q5: 3*8"
q6="q6: 4*10"
q7="q7: 1*5"
node1=Node(q1)
node2=Node(q2)
node3=Node(q3)
node4=Node(q4)
node5=Node(q5)
node6=Node(q6)
node7=Node(q5)
node1.right=node3
node1.left=node2
node2.right=node5
node2.left=node6
node3.left=node5
node4.right=node6
node4.left=node7
node5.left=node6
node1.n()
                
                
