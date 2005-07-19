#Boa:Frame:BMainFrame
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
    return BMainFrame(parent)

[wxID_BMAINFRAME, wxID_BMAINFRAMECBOIMAGETYPE, wxID_BMAINFRAMECBOMASTER, 
 wxID_BMAINFRAMECBOTHUMBNAIL, wxID_BMAINFRAMECMDABOUT, wxID_BMAINFRAMECMDEXIT, 
 wxID_BMAINFRAMECMDGENERATE, wxID_BMAINFRAMELBLGALLERYDEST, 
 wxID_BMAINFRAMELBLGALLERYNAME, wxID_BMAINFRAMELBLIMGPL, 
 wxID_BMAINFRAMELBLIMGTYPE, wxID_BMAINFRAMELBLMASTERSIZE, 
 wxID_BMAINFRAMELBLTHUMBNAIL, wxID_BMAINFRAMELBLTITLE, wxID_BMAINFRAMEPNLMAIN, 
 wxID_BMAINFRAMETXTGALLERYDEST, wxID_BMAINFRAMETXTGALLERYNAME, 
 wxID_BMAINFRAMETXTIMGPL, 
] = [wx.NewId() for _init_ctrls in range(18)]

class BMainFrame(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_BMAINFRAME, name='BMainFrame',
              parent=prnt, pos=wx.Point(422, 264), size=wx.Size(458, 325),
              style=wx.DEFAULT_FRAME_STYLE, title=':: xcode-gallery ::')
        self.SetClientSize(wx.Size(450, 291))
        self.Center(wx.BOTH)

        self.pnlMain = wx.Panel(id=wxID_BMAINFRAMEPNLMAIN, name='pnlMain',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(450, 291),
              style=wx.TAB_TRAVERSAL)

        self.lblGalleryname = wx.StaticText(id=wxID_BMAINFRAMELBLGALLERYNAME,
              label='Gallery Name:', name='lblGalleryname', parent=self.pnlMain,
              pos=wx.Point(8, 48), size=wx.Size(67, 13), style=0)

        self.lblGallerydest = wx.StaticText(id=wxID_BMAINFRAMELBLGALLERYDEST,
              label='Gallery destination:', name='lblGallerydest',
              parent=self.pnlMain, pos=wx.Point(8, 80), size=wx.Size(93, 13),
              style=0)

        self.txtGalleryname = wx.TextCtrl(id=wxID_BMAINFRAMETXTGALLERYNAME,
              name='txtGalleryname', parent=self.pnlMain, pos=wx.Point(120, 40),
              size=wx.Size(312, 21), style=0, value='')

        self.txtGallerydest = wx.TextCtrl(id=wxID_BMAINFRAMETXTGALLERYDEST,
              name='txtGallerydest', parent=self.pnlMain, pos=wx.Point(120, 72),
              size=wx.Size(312, 21), style=0, value='')

        self.lblTitle = wx.StaticText(id=wxID_BMAINFRAMELBLTITLE,
              label=':: xcode-gallery ::', name='lblTitle', parent=self.pnlMain,
              pos=wx.Point(160, 8), size=wx.Size(131, 18), style=0)
        self.lblTitle.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.lblThumbnail = wx.StaticText(id=wxID_BMAINFRAMELBLTHUMBNAIL,
              label='Thumbnail size:', name='lblThumbnail', parent=self.pnlMain,
              pos=wx.Point(8, 144), size=wx.Size(73, 13), style=0)

        self.cboThumbnail = wx.ComboBox(choices=[],
              id=wxID_BMAINFRAMECBOTHUMBNAIL, name='cboThumbnail',
              parent=self.pnlMain, pos=wx.Point(120, 136), size=wx.Size(312,
              21), style=0, value='')
        self.cboThumbnail.SetLabel('')

        self.lblImgtype = wx.StaticText(id=wxID_BMAINFRAMELBLIMGTYPE,
              label='Image Type:', name='lblImgtype', parent=self.pnlMain,
              pos=wx.Point(8, 112), size=wx.Size(61, 13), style=0)

        self.cboImagetype = wx.Choice(choices=[],
              id=wxID_BMAINFRAMECBOIMAGETYPE, name='cboImagetype',
              parent=self.pnlMain, pos=wx.Point(120, 104), size=wx.Size(312,
              21), style=0)

        self.lblMastersize = wx.StaticText(id=wxID_BMAINFRAMELBLMASTERSIZE,
              label='Master Size:', name='lblMastersize', parent=self.pnlMain,
              pos=wx.Point(8, 176), size=wx.Size(59, 13), style=0)

        self.cboMaster = wx.ComboBox(choices=[], id=wxID_BMAINFRAMECBOMASTER,
              name='cboMaster', parent=self.pnlMain, pos=wx.Point(120, 168),
              size=wx.Size(312, 21), style=0, value='')
        self.cboMaster.SetLabel('')

        self.lblImgpl = wx.StaticText(id=wxID_BMAINFRAMELBLIMGPL,
              label='Images per line:', name='lblImgpl', parent=self.pnlMain,
              pos=wx.Point(8, 208), size=wx.Size(77, 13), style=0)

        self.txtImgpl = wx.TextCtrl(id=wxID_BMAINFRAMETXTIMGPL, name='txtImgpl',
              parent=self.pnlMain, pos=wx.Point(120, 200), size=wx.Size(312,
              21), style=0, value='')

        self.cmdAbout = wx.Button(id=wxID_BMAINFRAMECMDABOUT,
              label='About xcode-gallery', name='cmdAbout', parent=self.pnlMain,
              pos=wx.Point(8, 240), size=wx.Size(128, 32), style=0)
        self.cmdAbout.Bind(wx.EVT_BUTTON, self.OnCmdAboutButton,
              id=wxID_BMAINFRAMECMDABOUT)

        self.cmdGenerate = wx.Button(id=wxID_BMAINFRAMECMDGENERATE,
              label='Generate Gallery', name='cmdGenerate', parent=self.pnlMain,
              pos=wx.Point(336, 240), size=wx.Size(96, 32), style=0)
        self.cmdGenerate.Bind(wx.EVT_BUTTON, self.OnCmdGenerateButton,
              id=wxID_BMAINFRAMECMDGENERATE)

        self.cmdExit = wx.Button(id=wxID_BMAINFRAMECMDEXIT,
              label='Exit from xcode-gallery', name='cmdExit',
              parent=self.pnlMain, pos=wx.Point(200, 240), size=wx.Size(131,
              32), style=0)
        self.cmdExit.Bind(wx.EVT_BUTTON, self.OnCmdExitButton,
              id=wxID_BMAINFRAMECMDEXIT)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnCmdAboutButton(self, event):
        wx.MessageBox('OnCmdAboutButton, not implemented yet')

    def OnCmdGenerateButton(self, event):
        wx.MessageBox('OnCmdGenerateButton, not implemented yet')

    def OnCmdExitButton(self, event):
        wx.MessageBox('OnCmdExitButton, not implemented yet')
