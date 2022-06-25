################################################################################
#
# Program: Call Super Anti-Pattern
# 
# Description: An implementation of the Call Super anti-pattern in Python.  See
# the Wikipedia article on the Call Super anti-pattern for more details: 
# https://en.wikipedia.org/wiki/Call_super.  We can fix the call super 
# anti-pattern by using the template method design pattern, see the YouTube 
# Lesson for an example.
#
# YouTube Lesson: https://www.youtube.com/watch?v=BBlaDMqV8ks
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# We wish to generate sales reports and costs reports that have a common 
# report heading.  We use the call super anti-pattern and implement the common 
# report heading in a make_report method of the base class Report, and then 
# *require* the derived classes to call the base class (i.e. super class) method
# to output the common report heading before providing the report body which 
# is unique to the derived class.  The *requirement* for the derived class 
# methods to call the base class method is what makes this an anti-pattern.  We
# might implement the call super anti-pattern in an attempt to refactor code 
# to reduce code duplication (see the commented code below).
#
# We can fix the call super anti-pattern using the template method design 
# pattern.


# The Report base class make_report method handles the generation of the common
# report heading.
class Report:

  def make_report(self):
    print("\n** REPORT HEADING **")
    print("Company: " + self.company)
    print("********************")

# The SalesReport class generates a report that is specifically a "sales 
# report".  It uses the base (super) class method make_report to output the
# report heading in its own make_report method.  The issue is that there is an 
# implicit *requirement* that the class does this.  At the same time, this 
# requirement is not enforced by any language feature.  If we as programmers
# don't call the super/base class make_report method, perhaps because we 
# forget or unaware of the need to, we will have a bug, with no error as a 
# result to indicate that we should not be doing this!
class SalesReport(Report):

  # Set the company and sales member variables when object is instantiated
  def __init__(self,company,sales):
    self.company = company 
    self.sales = sales

  # The make_report method is implicitly required to call the base/super class 
  # make_report method in order to generate the correct report including the 
  # common report heading.
  def make_report(self):
    super().make_report()
    print("Sales: "  + str(self.sales))

# We do the exact same thing as the SalesReport class, only now for a 'costs 
# report', for simplicities sake we keep the reports small and simple but we 
# can imagine more extensive unique report body functionality being implemented
class CostsReport(Report):
  
  def __init__(self,company,costs):
    self.company = company 
    self.costs = costs

  def make_report(self):
    super().make_report()
    print("Costs: "  + str(self.costs))

# Output a sales report using a SalesReport object
sales_report = SalesReport("Google", 20000)
sales_report.make_report()

# Output a costs report using a CostsReport object
costs_report = CostsReport("Amazon", 50000)
costs_report.make_report()

 

#  We might implement the above functionality like this, but we would have 
#  duplicated code in the make_report methods.  We might then try to factor 
#  out this code duplication by using the call super anti-pattern above.  A 
#  better approach would be to use the template method design pattern.
#
#
#  class SalesReport:
#  
#    def __init__(self,company,sales):
#      self.__company = company
#      self.__sales = sales
#
#    def make_report(self):
#      print("\n** REPORT HEADING **")
#      print("Company: " + self.__company)
#      print("********************")
#      print("Sales: "  + str(self.__sales))#
#
#  class CostsReport:
#
#    def __init__(self,company,costs):
#      self.__company = company
#      self.__costs = costs
#
#    def make_report(self):
#      print("\n** REPORT HEADING **")
#      print("Company: " + self.__company)
#      print("********************")
#      print("Costs: "  + str(self.__costs))
#
#
#  sales_report = SalesReport("Google", 20000)
#  sales_report.make_report()
#
#  costs_report = CostsReport("Amazon", 50000)
#  costs_report.make_report()
