#!/usr/bin/env python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello") #wx.Frame is top-level window
frame.Show(True)
app.MainLoop()
