################################################################################
#
# Program: Chain Of Responsibility Design Pattern
# 
# Description: An implementation of the chain-of-responsibility pattern in 
# Python.  See the Wikipedia article on the design pattern for more information:
# https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern.
#
# YouTube Lesson: https://www.youtube.com/watch?v=QOW1IN8i8J8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We create a chain-of-responsibility pattern to implement a 'logger'.  Large 
# software applications will often write log messages during their execution to 
# help trace their behavior at runtime, using log functions throughout the 
# program source code.  Log messages may be written to different destinations, 
# such as files, databases or the console.  We implement a chain of loggers, so 
# that when a log message is written the message can be written to multiple 
# destinations by being passed through the chain of loggers.

# Import the abstract base class module so we can create a 'Logger' interface 
# that defines the interface for 'Handler' objects in the pattern
from abc import ABC, abstractmethod

# The Logger class defines the interface for the 'handlers' in our 
# implementation of the pattern.  We use the template method design pattern 
# with log as the template method and make_entry as a helper method, this way 
# we can define the common logic to pass the message to the next logger in 
# this base class rather than repeating the logic in the derived classes:
# https://en.wikipedia.org/wiki/Template_method_pattern.  We implement it as 
# an abstract base class as we will never actually instantiate a Logger object,
# we will only instantiate derived classes that log messages in specific ways.  
class Logger(ABC): 
  
  # A Logger object is given the next logger object in the chain when it is 
  # instantiated, the last object in the chain will be instantiated with None
  # as its next logger.  The next logger is kept as a member variable.
  def __init__(self, next_logger):
    self.__next_logger = next_logger 
  
  # The make_entry() method is used as a helper method by the log template 
  # method.  This method will carry out the logging functionality for each 
  # specific type of logger.  We make it an abstract method using the 
  # @abstractmethod decorator so that derived classes MUST implement it in 
  # order for them to be able to instantiated themselves.
  @abstractmethod 
  def make_entry(self, message):
    pass
  
  # The log() template method carries out the logging, using the make_entry 
  # helper method to actually output the log message, and then passing the 
  # message on to the next logger in the chain by calling the next logger 
  # member variable's log method.
  def log(self, message):

    self.make_entry(message)

    if (self.__next_logger is None):
      return 
    else:
      self.__next_logger.log(message)

# ConsoleLogger is a derived class of Logger and provides an implementation
# of the make_entry() method that logs the message to a console.
class ConsoleLogger(Logger):

  def make_entry(self, message):
    print("**CONSOLE**: " + message)

# FileLogger is a derived class of Logger and provides an implementation of the 
# make_entry() method that logs the message to a file (to keep this example 
# focused on the design pattern, we just output the message to the console with 
# a prefix to differentiate it from the other types of loggers).
class FileLogger(Logger):

  def make_entry(self, message):
    print("**FILE**: " + message)

# Create a DatabaseLogger using the same technique as the above Loggers
class DatabaseLogger(Logger):

  def make_entry(self, message):
    print("**DATABASE**: " + message)

# Create the chain of objects, with the ConsoleLogger object as the last Logger
# in the chain and the DatabaseLogger object as the first.
console1 = ConsoleLogger(None)
file1 = FileLogger(console1)
database1 = DatabaseLogger(file1)

# When we log a message using the DatabaseLogger object the message will be 
# passed to the FileLogger object and then the ConsoleLogger object too!
database1.log("test")