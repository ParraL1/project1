#Name: Lilliana Parra
#Github username: ParraL1
#Date: 3/30/22
#Description: Importing the statistics module to get median, mode, and mean of grades



#import the statistics module first
import statistics
#student class with two private data members, the name and the grade
class Student:
    def __init__(self,name,grade):
        self.__name = name
        self.__grade = grade
        #get grade method
    def get_grade(self):
        return self.__grade
#basic stats function that takes a parameter of objects for student stuff that returns
#a tuple containing the mean, median,and mode of all grades

def basic_stats(student):
        #list to store grades in
        list_of_grades = []
        for g in student:
            list_of_grades.append(g.get_grade())
#making sure that the spacing of the lines is correct as it changes the whole answer!

            # getting the mean
        mean = statistics.mean(list_of_grades)
            #getting the median
        median = statistics.median(list_of_grades)
            #getting the mode
        mode = statistics.mode(list_of_grades)
        #making sure the numbers are listed in order!
        in_order = (mean, median, mode)
        #returning the list in order
        return in_order