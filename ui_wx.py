import wx
from wx.lib.wordwrap import wordwrap
from bracket_checker import balance

class BracketChecker(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(400, 300))
        self.panel = wx.Panel(self, -1)
        self.text = wx.TextCtrl(self.panel, -1, style=wx.TE_MULTILINE)
        self.button_open = wx.Button(self.panel, -1, "Select file")
        self.button_check = wx.Button(self.panel, -1, "Check brackets")
        self.__set_properties()
        self.__do_layout()
        self.__bind_events()
        self.Show(True)

    def __set_properties(self):
        self.SetTitle("Check nesting")
        self.text.SetMinSize((400, 300))
        self.text.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.text, 0, wx.EXPAND, 0)
        sizer_2.Add(self.button_open, 0, 0, 0)
        sizer_2.Add(self.button_check, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        self.panel.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

    def __bind_events(self):
        self.Bind(wx.EVT_BUTTON, self.open_file, self.button_open)
        self.Bind(wx.EVT_BUTTON, self.check_brackets, self.button_check)

    def open_file(self, event):
        filepath = wx.FileSelector("Select file", flags=wx.FD_OPEN)
        if filepath:
            with open(filepath, 'r') as f:
                self.text.Clear()
                self.text.WriteText(f.read())

    def check_brackets(self, event):
        program = self.text.GetValue()
        status = balance(program)
        wx.MessageBox(status, "Check brackets", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App()
    BracketChecker(None, -1, "")
    app.MainLoop()