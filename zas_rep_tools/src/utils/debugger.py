#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import sys
from kitchen.text.converters import getwriter
import inspect

if platform.uname()[0].lower() !="windows":
    from blessings import Terminal

from nose.plugins.attrib import attr
from cached_property import cached_property

UTF8Writer = getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def p(func, func_name='DEBUGING', c='w', r=False):
	'''
	Functionality: Print-Function for Debigging 
	'''
	if platform.uname()[0].lower() !="windows":
		t = Terminal()
		colores = {'b':'t.bold_on_bright_blue', 'r':'t.bold_on_bright_red', 'g':'t.bold_on_bright_green', 'w':'t.bold_black_on_bright_white', 'm':'t.bold_white_on_bright_magenta', "c":'t.bold_white_on_bright_cyan', "y":'t.bold_white_on_bright_yellow', "b":'t.bold_white_on_bright_black'}
		#colores = {'b':'t.bold_blue', 'r':'t.bold_red', 'g':'t.bold_green', 'w':'t.bold', 'm':'t.bold_magenta'}
		#for st in  inspect.stack():
		#	print st
		#print u"\n\n{start} <{0}>{stop} \n  {1} \n   {start} </{0}>{stop}\n".format(  func_name,  func, t=t, start=eval(colores[c]), stop=t.normal   )
		if r:
			print "\n\n{start} <{0}>{stop}  \n  {1}  \n   {start} </{0}>{stop}\n".format(  func_name,  repr(func), t=t, start=eval(colores[c]), stop=t.normal   )
		else:
			print "\n\n{start} <{0}>{stop}  \n  {1}  \n   {start} </{0}>{stop}\n".format(  func_name,  func, t=t, start=eval(colores[c]), stop=t.normal   )
	else:
		print "p() is not supported for 'Windows'-OS."


def wipd(f):
	'''
	decorator for nose attr.
	'''
	return attr('wipd')(f)

def wipdn(f): # now
    '''
    decorator for nose attr.
    '''
    return attr('wipdn')(f)

def wipdl(f): #later
    '''
    decorator for nose attr.
    '''
    return attr('wipdl')(f)

def wipdo(f): # open
    '''
    decorator for nose attr.
    '''
    return attr('wipdo')(f)

# def cached(timeout=None):
#     def decorator(func):
#         def wrapper(self, *args, **kwargs):
#             value = None
#             key = '_'.join([type(self).__name__, str(self.id) if hasattr(self, 'id') else '', func.__name__])

#             if settings.CACHING_ENABLED:
#                 value = cache.get(key)

#             if value is None:
#                 value = func(self, *args, **kwargs)

#                 if settings.CACHING_ENABLED:
#                     # if timeout=None Django cache reads a global value from settings
#                     cache.set(key, value, timeout=timeout)

#             return value

#         return wrapper

#     return decorator



# def cachedproperty(func):
#     " Used on methods to convert them to methods that replace themselves\
#         with their return value once they are called. "

#     def cache(*args):
#         self = args[0] # Reference to the class who owns the method
#         funcname = func.__name__
#         ret_value = func(self)
#         setattr(self, funcname, ret_value) # Replace the function with its value
#         return ret_value # Return the result of the function

#     return property(cache)


# def p(func):
#     def func_wrapper(name):
#         return "<\n{0}>{1}</{0}\n>".format(func.__name__, func(name))
#     return func_wrapper


# def markup(func):
# 	def func_wrapper(name):
# 		return "<\n{0}>{1}</{0}\n>".format(func.__name__, func(name))
# 	return func_wrapper



