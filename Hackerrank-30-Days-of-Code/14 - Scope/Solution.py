class Difference:
    def __init__(self, a):
        self.__elements = a
        

    # Add your code here   
    def computeDifference(self):
        diff = []

        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                d = abs(self.__elements[i] - self.__elements[j])                # with one element i deducting each element j 
                diff.append(d)


        self.maximumDifference= max(diff)
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
