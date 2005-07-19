#Boa:Dialog:BAboutDialog
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

def create(parent):
    return BAboutDialog(parent)

[wxID_BABOUTDIALOG, wxID_BABOUTDIALOGCMDOK, wxID_BABOUTDIALOGIMGLOGO, 
 wxID_BABOUTDIALOGLBLCOPYRIGHT, wxID_BABOUTDIALOGLBLPROGNAME, 
 wxID_BABOUTDIALOGLBLSLOGAN, 
] = [wx.NewId() for _init_ctrls in range(6)]

class BAboutDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_BABOUTDIALOG, name='BAboutDialog',
              parent=prnt, pos=wx.Point(319, 256), size=wx.Size(413, 390),
              style=wx.DEFAULT_DIALOG_STYLE, title=':: About xcode-gallery ::')
        self.SetClientSize(wx.Size(405, 356))

        self.imgLogo = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_BABOUTDIALOGIMGLOGO, name='imgLogo', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(376, 120), style=0)

        self.lblProgname = wx.StaticText(id=wxID_BABOUTDIALOGLBLPROGNAME,
              label='xcode-gallery', name='lblProgname', parent=self,
              pos=wx.Point(160, 152), size=wx.Size(65, 13), style=0)

        self.lblSlogan = wx.StaticText(id=wxID_BABOUTDIALOGLBLSLOGAN,
              label='The definitive code-gallery gui program', name='lblSlogan',
              parent=self, pos=wx.Point(96, 176), size=wx.Size(187, 13),
              style=0)

        self.lblCopyright = wx.StaticText(id=wxID_BABOUTDIALOGLBLCOPYRIGHT,
              label='(C) Copyright 2005 by Lorenzo Villani (Arbiter) and contributors',
              name='lblCopyright', parent=self, pos=wx.Point(48, 208),
              size=wx.Size(303, 13), style=0)

        self.cmdOK = wx.Button(id=wxID_BABOUTDIALOGCMDOK, label='OK',
              name='cmdOK', parent=self, pos=wx.Point(48, 312),
              size=wx.Size(312, 31), style=0)
        self.cmdOK.Bind(wx.EVT_BUTTON, self.OnCmdOKButton,
              id=wxID_BABOUTDIALOGCMDOK)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnCmdOKButton(self, event):
        wx.MessageBox('OnCmdOKButton() need to be implemented')
