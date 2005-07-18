#!/usr/bin/env python

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
