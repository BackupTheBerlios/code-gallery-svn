#!/usr/bin/env python
#Boa:App:BoaApp
#
# PROJECT	: xcode-gallery
# AUTHORS	: Arbiter
#
# COPYRIGHT (C) Copyright 2005 Lorenzo Villani (Arbiter) and contributors
#
# ##################################################################################
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
# ##################################################################################
#
# Last Change by ARBITER on 19/07/2005 @ 19:20
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
#             # --arbiter-- I don't think this is a nice solution...
#
# Arbiter (based upon lavish's code standards)
#
# ###################################################################################

import wx

from gui import MainFrame

modules ={'AboutDialog': [0, '', 'gui/AboutDialog.py'],
 'BAboutDialog': [0, '', 'gui/base/BAboutDialog.py'],
 'BMainFrame': [1, 'Main frame of Application', 'gui/base/BMainFrame.py'],
 'MainFrame': [0, '', 'gui/MainFrame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = MainFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
