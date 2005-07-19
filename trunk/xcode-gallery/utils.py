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
# Last Change by Arbiter on 19/07/2005 @ 10:15
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

import sys

# We try to import the output module
# witch is not available on all plaform
try:
	import output
	def print_ok(message):
		print(blue('[ ')+green('ok')+blue(' ] ')+message)

	def print_err(message):
		print(blue('[ ')+red('!!')+blue(' ] ')+message)

	def print_warn(message):
		print(blue('[ ')+yellow('**')+blue(' ] ')+message)
except ImportError:
	def print_ok(message):
		print('[ ok ] '+message)
	def print_err(message):
		print('[ !! ] '+message)
	def print_warn(message):
		print('[ ** ] '+message)

