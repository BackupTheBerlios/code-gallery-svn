#__  _____ ___   __| | ___        __ _  __ _| | | ___ _ __ _   _
#\ \/ / __/ _ \ / _` |/ _ \_____ / _` |/ _` | | |/ _ \ '__| | | |
# >  < (_| (_) | (_| |  __/_____| (_| | (_| | | |  __/ |  | |_| |
#/_/\_\___\___/ \__,_|\___|      \__, |\__,_|_|_|\___|_|   \__, |
#                                |___/                     |___/
# AUTHORS	: Lavish, Arbiter, Pizzak
#
# COPYRIGHT (C) Copyright 2005 Marco Squarcina (Lavish) and contributors
# 
# Xcode-gallery: this module is part of the code-gallery project and is
# currently developed and maintained by Lorenzo Villani (Arbiter)
#    MAIL: arbitermc@gmail.com
#    WEB:  arbitermc.homelinux.org
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
# Last Change by ARBITER on Jun 26, 2005 @ 12:58
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
# Lavish
#
####################################################################################

import gtk
import gtk.glade
from gui import MainWindow

class Main:
	def __init__(self):
		print('Starting...')
		MainWindow.MainWindow()		
		gtk.main()
