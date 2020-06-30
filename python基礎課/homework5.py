import wx
import os

wildcard = "All files (*.*)|*.*"
#"Python source (*.py)|*.py|" \
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

	def __init__(self, parent):
		self.frame = wx.Frame.__init__(self, parent,
									   id=wx.ID_ANY,
									   title=u'記事本',
									   pos=wx.DefaultPosition,
									   size=wx.Size(653, 353),
									   style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		self.m_menubar2 = wx.MenuBar(0)
		self.bar_file = wx.Menu()
		self.function1 = wx.MenuItem(self.bar_file, wx.ID_ANY, u"建立新檔", wx.EmptyString, wx.ITEM_NORMAL)
		self.bar_file.Append(self.function1)

		self.function2 = wx.MenuItem(self.bar_file, wx.ID_ANY, u"開啟舊檔", wx.EmptyString, wx.ITEM_NORMAL)
		self.bar_file.Append(self.function2)

		self.function3 = wx.MenuItem(self.bar_file, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL)
		self.bar_file.Append(self.function3)

		self.function4 = wx.MenuItem(self.bar_file, wx.ID_ANY, u"結束程式", wx.EmptyString, wx.ITEM_NORMAL)
		self.bar_file.Append(self.function4)

		self.m_menubar2.Append(self.bar_file, u"檔案")

		self.bar_about = wx.Menu()
		self.function2_1 = wx.MenuItem(self.bar_about, wx.ID_ANY, u"作者介紹", wx.EmptyString, wx.ITEM_NORMAL)
		self.bar_about.Append(self.function2_1)

		self.m_menubar2.Append(self.bar_about, u"關於")

		self.SetMenuBar(self.m_menubar2)

		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		self.m_richText1 = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
													0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
		bSizer2.Add(self.m_richText1, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer2)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.Bind(wx.EVT_MENU, self.new_file, id=self.function1.GetId())
		self.Bind(wx.EVT_MENU, self.load_file, id=self.function2.GetId())
		self.Bind(wx.EVT_MENU, self.save_file, id=self.function3.GetId())
		self.Bind(wx.EVT_MENU, self.close_window, id=self.function4.GetId())
		self.Bind(wx.EVT_MENU, self.auther_intro, id=self.function2_1.GetId())

		# 自建
		self.currentDirectory = os.getcwd()
		self.frame1 = MyDialog1(parent=None)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def new_file(self, event):
		self.SetTitle(u'記事本')
		self.m_richText1.Clear()

	def load_file(self, event):
		# 需要重跑一個清空頁面
		self.SetTitle(u'記事本')
		self.m_richText1.Clear()
		"""
        Create and show the Open FileDialog
        """
		dlg = wx.FileDialog(self,
							message="Choose a file",
							defaultDir=self.currentDirectory,
							defaultFile="",
							wildcard=wildcard,
							style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
							)
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
			print("You chose the following file(s):")
			for path in paths:
				print(path)
				filename = os.path.basename(path)
				newTitle = f'記事本 - {filename}'
				self.SetTitle(newTitle)
				with open(path, 'r', encoding='utf-8') as f:
					self.m_richText1.WriteText(str(f.read()))
		dlg.Destroy()

	def save_file(self, event):
		dlg = wx.FileDialog(
			self, message="Save file as ...",
			defaultDir=self.currentDirectory,
			defaultFile="", wildcard=wildcard, style=wx.FD_SAVE
		)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			print("You chose the following filename: %s" % path)
			with open(path, 'a', encoding='utf8') as f:
				f.write(self.m_richText1.GetValue())
		dlg.Destroy()

	def close_window(self, event):
		self.Close(True)

	def auther_intro( self, event):
         self.frame1.Show()

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"關於作者", pos = wx.DefaultPosition, size = wx.Size( 246,122 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.label_auther = wx.StaticText( self, wx.ID_ANY, u"作者: 王大明", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_auther.Wrap( -1 )

		bSizer3.Add( self.label_auther, 0, wx.ALL, 5 )

		self.label_email = wx.StaticText( self, wx.ID_ANY, u"信箱: Da-Ming@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_email.Wrap( -1 )

		bSizer3.Add( self.label_email, 0, wx.ALL, 5 )

		self.label_website = wx.StaticText( self, wx.ID_ANY, u"網站: www.DaMingWang.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_website.Wrap( -1 )

		bSizer3.Add( self.label_website, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


if __name__ == '__main__':
	mainwindow = wx.App()

	frame0 = MyFrame1(parent=None)
	frame0.Show()

	mainwindow.MainLoop()