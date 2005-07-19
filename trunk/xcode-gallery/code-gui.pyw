#!/usr/bin/env python
#
# PROJECT	: xcode-gallery - Code-Gallery's GUI
# AUTHORS	: Arbiter
#
# COPYRIGHT (C) Copyright 2005 Lorenzo Villani (Arbiter) and contributors
#
###################################################################################
#                                                                                 #
#  LICENSE: See COPYING file which comes with this distribution for more details  #
#                                                                                 #
#  This program is free software; you can redistribute it and/or modify           #
#  it under the terms of the GNU General Public License as published by           #
#  the Free Software Foundation; either version 2 of the License, or              #
#  (at your option) any later version.                                            #
#                                                                                 #
#  This program is distributed in the hope that it will be useful,                #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#  GNU General Public License for more details.                                   #
#                                                                                 #
#  You should have received a copy of the GNU General Public License              #
#  along with this program; if not, write to the Free Software                    #
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA     #
#                                                                                 #
###################################################################################
#
# Last Change by Arbiter on 19/07/2005 @ 10:10
#
# To Devels : 
#             Please, insert comments and output ONLY in ENGLISH!
#             If you are unsure about anything and you want to check it later,
#	      add a comment in this form:
#             
#	      # --<DevelName>-- <Comment>
#             
#	      example:
#
#             # --lavish-- I don't think this is a nice solution...
#
# Arbiter (based upon comment from Lavish)
#
####################################################################################



from utils import *
import sys


# Checks for pygtk presence
try:
	import pygtk
	print_ok('PyGTK found')
except ImportError:
	print_err('PyGTK was not found in your system, please install it')

# Checks for pygtk version
try:
	pygtk.require('2.0')
	print_ok('PyGTK 2.0 or greater found')
except:
	print_err('PyGTK is installed but the version is not 2.0 or greater')

# Checks for pyGTK glade support
try:
	import gtk
	import gtk.glade
	print_ok('PyGTK was compiled with glade support')
except ImportError:
	print_err('PyGTK was not compiled with glade support')

#Psyco support
try:
	import psyco
	psyco.full()
	print_ok('Pysco found, JIT compiling enabled')
except ImportError:
	print_err('Psyco NOT found, JIT compiling disabled')

# Ok, final initialization
if __name__ == '__main__':
	import MainWindow
	startup = MainWindow.MainWindow()
	gtk.main()
