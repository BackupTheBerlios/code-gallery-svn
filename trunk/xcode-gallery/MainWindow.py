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



#Imports and checks for correct PyGTK version
import os
import gtk
import gtk.glade

class MainWindow:
	# Control variables
	DEBUG=False

	# Used to build the command line
	GALLERYNAME=""
	GALLERYDEST=""
	THUMBNAIL=""
	MASTER=""
	IMGPL=""
	CUSTOMOPTS=""
	
	IMGTYPE="jpg"
	
	
	def __init__(self):
		print """
		\t*** Code Gui - the code-gallery's GUI ***
		Created by Lorenzo Villani aka Arbiter
		
		"""
		xml = gtk.glade.XML('glade/mainwindow.glade')
		xml.signal_autoconnect(self)

		self.txtGalleryname = xml.get_widget('txtGalleryname')
		self.txtDestination = xml.get_widget('txtDestination')
		self.optJPG = xml.get_widget('optJPG')
		self.optPNG = xml.get_widget('optPNG')
		self.txtThumbnail = xml.get_widget('txtThumbnail')
		self.txtMaster = xml.get_widget('txtMaster')
		self.spnImages = xml.get_widget('spnImages')
		self.txtCustopts = xml.get_widget('txtCustopts')

		#self.MainWindow = xml.get_widget('MainWindow')

		#self.MainWindow.show_all()
	
	def on_MainWindow_destroy(self, args):
		gtk.main_quit()
	
	def on_cmdExit_clicked(self, args):
		gtk.main_quit()
	
	def on_cmdAbout_clicked(self, args):
		print('Not implemented yet')
	
	def on_cmdGenerate_clicked(self, args):
		GALLERYNAME = self.txtGalleryname.get_text()
		GALLERYDEST = self.txtDestination.get_text()
		THUMBNAIL = self.txtThumbnail.get_text()
		MASTER = self.txtMaster.get_text()
		IMGPL = self.spnImages.get_text()
		CUSTOMOPTS = self.txtCustopts.get_value()
		
		CMDLINE="code-gallery --gallery-name " + GALLERYNAME + " --dir " + GALLERYDEST + " --thumbnail-size " + THUMBNAIL + " --master-size " + MASTER + " --file-type " + IMGTYPE + " --images-per-line " + IMPL + "--custom-cnv-options " + CUSTOMOPTS
		os.popen(CMDLINE)
		
if __name__ == '__main__':
	cls = MainWindow()
	gtk.main()
