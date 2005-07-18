#!/usr/bin/env python

import time
import gtk
import gobject
import gtk.glade
import MainWindow

class SplashWindow:
	def __init__(self):
		xml = gtk.glade.XML('glade/splashwindow.glade')

		self.SplashWindow = xml.get_widget('SplashWindow')
		
		self.prgLoading = xml.get_widget('prgLoading')

		self.timer = gobject.timeout_add(25, self.prg_timeout, self)

	def prg_timeout(self, args):
		newval = self.prgLoading.get_fraction() + 0.02
		if newval >= 1.0:
			MainWindow.MainWindow()
			self.destroy(self)
			return False
		else:
			self.prgLoading.set_fraction(newval)
			return True
		

if __name__ == '__main__':
	cls = SplashWindow()
	gtk.main()
			
