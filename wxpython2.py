#!/usr/bin/env python
import wx

class MyFrame(wx.Frame):
	""" We derive class of Frame """
#	apa guna self
	def __init__(self,parent,title):
#		assignment title aneh
		wx.Frame.__init__(self, parent, title=title, size=(400,300))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'Small Editor')
app.MainLoop()
