import wx
import wx.html2
import threading
from app import app  # 确保 'app' 是您 Flask 应用的正确导入路径

# Flask 服务器运行在单独的线程中
def start_flask():
    try:
        app.run(port=5000)
    except Exception as e:
        print(f"无法启动 Flask 服务器: {e}")

# wxPython 应用界面
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(800, 600))
        self.panel = wx.Panel(self)
        self.browser = wx.html2.WebView.New(self.panel)
        if not self.browser:
            print("无法创建 WebView 组件。请检查浏览器引擎是否可用。")
            self.Close()
            return
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.browser, 1, wx.EXPAND)
        self.panel.SetSizer(self.sizer)
        self.browser.LoadURL("http://127.0.0.1:5000")

# wxPython 应用
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "wxPython and Flask")
        frame.Show()
        return True

# 主函数
if __name__ == "__main__":
    try:
        # 启动 Flask 服务器
        threading.Thread(target=start_flask, daemon=True).start()

        # 启动 wxPython 应用
        app = MyApp()
        app.MainLoop()
    except Exception as e:
        print(f"程序运行时出错: {e}")
