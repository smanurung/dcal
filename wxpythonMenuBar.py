import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self,parent,title=title,size=(500,400))
#		self di bawah ini opsional atau ngga
		self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
		self.CreateStatusBar()
		
		filemenu = wx.Menu()
		
		filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
		filemenu.AppendSeparator()
		filemenu.Append(wx.ID_EXIT,"&Exit","Terminate the program")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File")
		self.SetMenuBar(menuBar)
		self.Show(True)

app = wx.App(True)
frame = MainWindow(None,"Sample Editor")
app.MainLoop()
