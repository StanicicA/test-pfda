#We can add any list, the code will calcuate the average of the sum 

ages = [10, 20, 30, 40]

def calculateAverage (list):
    sum = 0;
    for i in list:
        sum = sum + i
    return sum 

print (calculateAverage(ages))

#if we want to calculate the average divided by the number of the items in the list:
#This code is used to calculate anything, list is a general name

def calculateAverage (list):
    sum = 0;
    for i in list:
        sum = sum + i
    return sum/len (list)

print (calculateAverage(ages))
