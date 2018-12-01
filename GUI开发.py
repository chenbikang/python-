import  wx
app = wx.App()
win = wx.Frame(None,title = '我的记事本',size = (410,335))
bt = wx.Button(win,label = "open",pos = (225,5),size = (80,25))
title = wx.TextCtrl(win,pos = (5,5),size = (210,25))
win.Show()
