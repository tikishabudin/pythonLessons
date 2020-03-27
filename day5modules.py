# import helperFunctions
# from helperFunctions import do_this
# import helperFunctions as hf
# from helperFunctions import do_that as dt

# import helpers.helperFunctions as hf
# from helpers.helperFunctions import do_that
# import helpers.helperFunctions

# dothis()
# do_that()
# hf.do_this()
# helperFunctions.do_that()

# from helpers.helperFunctions import do_this as dothat

# dothat()

import helpers.otherHelpers
import helpers.helperFunctions
import worker
import worker.subworker

import flask
import sys

print(sys.version)

helpers.otherHelpers.do_something()
# print(dir(helpers.helperFunctions))