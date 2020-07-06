
class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
        

c1 = Course("john",[1,2,3,4,5])
print(c1.name)

c2 = Course("Java Web Services",[5,5,5,5])

c3 = Course("this is the third one",[3,4,5,6,7])
print(c3.name)