################################################################################
#
# Program: Template Method Pattern
# 
# Description: An implementation of the Template Method Design Pattern in 
# Python.  See the Wikipedia article for details on the template method design 
# pattern: https://en.wikipedia.org/wiki/Template_method_pattern.  The template 
# method design pattern is a potential fix to the call super anti-pattern, see 
# the YouTube lesson for an example.
#
# YouTube Lesson: https://www.youtube.com/watch?v=BBlaDMqV8ks
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We wish to generate sales reports and costs reports that have a common 
# report heading.  We use the template method to define the report heading 
# in a base report class, leaving the derived sales and cost report classes 
# to override a helper method that will define the body of the report.


# Import the abstract base class module so we can create an abstract base 
# class and use the abstractmethod decorator to create abstract methods
from abc import ABC, abstractmethod


# Base class Report will define the template method and create an abstract 
# method as a 'helper method' that base classes *must* implement.
class Report(ABC):
  
  # Helper method used to carry out the functionality of the template 
  # method, this method MUST be overridden by the derived classes by design
  @abstractmethod
  def make_report_body(self):
    pass
  
  # Template method that defines "how the algorithm works at a high level" 
  # using helper methods, in this case by defining "how a report works".  The 
  # template method implements how the common report heading works, leaving 
  # the implementation of the report body to the helper method that will be 
  # implemented by the derived classes.
  def make_report(self):
    print("\n** REPORT HEADING **")
    print("Company: " + self.company)
    print("********************")
    self.make_report_body()


# Derived class SalesReport implements sales report functionality specifically,
# overriding the helper method in the base class to do so.
class SalesReport(Report):
  
  # Set the company and sales member variables when object is instantiated
  def __init__(self,company,sales):
    self.company = company 
    self.sales = sales
  
  # Override the helper method as required and supply a definition for how to 
  # create a sales report body
  def make_report_body(self):
    print("Sales: "  + str(self.sales))


# We do the exact same thing as the SalesReport class, only now for a 'costs 
# report', for simplicities sake we keep the reports small and simple but we 
# can imagine more extensive unique report body functionality being implemented
class CostsReport(Report):
  
  def __init__(self,company,costs):
    self.company = company 
    self.costs = costs
  
  # If we try to remove this method from the class, the program will fail as 
  # make_report_body is an abstract method in the base class and thus we MUST 
  # implement it in the derived class.  We are using a language feature to help
  # ensure the implementation is correct.
  def make_report_body(self):
    print("Costs: "  + str(self.costs))

# When we instantiate a SalesReport object and call the make_report() method, it
# is the make_report() template method in the base Report class that will 
# execute, and eventually the make_report_body() helper method implementation in
# the SalesReport derived class will be called to output the report body specific
# to a sales report.
sales_report = SalesReport("Google", 20000)
sales_report.make_report()

# Do the same with a CostsReport object, which will generate a unique cost 
# report with its own helper method implementation
costs_report = CostsReport("Amazon", 50000)
costs_report.make_report()
