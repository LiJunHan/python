import wx
from view.view import jiamijiemi

def encryption(event):  # 定义打开文件事件
    path = path_text.GetValue()
    e = jiamijiemi(path)
    e.encrytext()

def ciptolotion(event):
    path = path_text.GetValue()
    c = jiamijiemi(path)
    c.ciptolotext()




app = wx.App()
frame = wx.Frame(None, title="加密解密程序", pos=(350, 170), size=(500, 400))

path_text = wx.TextCtrl(frame, pos=(5, 5), size=(350, 24))
open_button = wx.Button(frame, label="加密", pos=(370, 5), size=(50, 24))
open_button.Bind(wx.EVT_BUTTON, encryption)  # 绑定打开文件事件到open_button按钮上

save_button = wx.Button(frame, label="解密", pos=(430, 5), size=(50, 24))
save_button.Bind(wx.EVT_BUTTON, ciptolotion)

content_text = wx.TextCtrl(frame, pos=(5, 39), size=(475, 300), style=wx.TE_MULTILINE)
content_text.write("\n\n\n\n使用说明：将你需要加密的文件路径填入上方的路径框中，点击加密即可加密文件，可以多次加密，点击解密即可解密文件。\n"
                   "\n\n注意：该程序目前只能加密txt文件。\n\n 该加密程序的密钥文件存在视图层的静态文件中。")
#  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行

frame.Show()
app.MainLoop()
# C:\Users\86155\Desktop\code\cryptology\view\static\a.txt