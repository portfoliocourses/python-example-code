################################################################################
#
# Program: Read An INI Config File With ConfigParser
# 
# Description: Example of reading a .ini config file using the configparser 
# module in Python.  A .ini file is an informal but very common format for 
# config files made up of sections containing key/value pairs:
#  https://en.wikipedia.org/wiki/INI_file
#
# YouTube Lesson: https://www.youtube.com/watch?v=DSG6KGF4qJQ  
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Import the ConfigParser and ExtendedInterpolation classes from the 
# configparser module
from configparser import ( 
    ConfigParser,
    ExtendedInterpolation
) 

# Create the ConfigParser object instance, if we pass the optional argument 
# interpolation as an instance of ExtendedInterpolation() then we can parse 
# keys in a config file which reference other keys.
config = ConfigParser(
    interpolation=ExtendedInterpolation()
)

# Use the .read() method to read the config file settings.ini.  If there is a 
# problem with the format of the file, .read() will raise an exception.  In this
# case we will output an error message and exit the program using 'raise 
# SystemExit()'.
try:
    config.read("settings.ini")
except:
    print("settings.ini format error")
    raise SystemExit()

# We can access the config values much like using a dictionary, here we access 
# the log_filename key of the Log section
print( config["Log"]["log_filename"] )

# Access the server key of the Database section
print( config["Database"]["server"] )

# We can use 'in' to check if a key exists in a section
if ("username" in config["Database"]):
    print("username exists")

# We can use .get() to access a value by providing the section and key as string
# arguments.
print( config.get("Database", "password") )

# We can use .sections() to get a list of all the sections in the config file
print( config.sections() )

# We can use .options() to get a list of all the keys in a section
print( config.options("Database") )

# By default the type of the value provided will be a string.  So even though 
# port is an integer, we'll see we get back a string if we use type() to 
# get the type... 
#
# print(type(config["Database"]["port"]))

# We could manually convert the value to an int using int()...
#
# port = int(config["Database"]["port"])
# print(port, type(port))

# If we use .getint() with the section and key strings as arguments, we'll get 
# back the value with type int.  If we use one of the get methods we can supply
# an optional fallback argument, and if the key does not exist in the config 
# file then we'll get back the fallback value instead.
#
port = config.getint("Database", "port", fallback=7)
print(port, type(port))

# There is also a getfloat() method which works much like .getint()!

# The .getboolean() method works like .getint() and .getfloat() as well, though
# notably it will interpret a range of case-insensitive values as true/false, 
# see the settings.ini config file for examples.
if (config.getboolean("Log", "logging_on")):
    print("Logging on...")
else:
    print("Logging off...")

# Because we are using ExtendedInterpolation() we can use values which reference
# other values as done in settings.ini
print(config["Log"]["log_dir"])

# ConfigParser will also support values which reference values in other sections
print(config["Database"]["archive_dir"])