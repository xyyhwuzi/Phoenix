import unittest
import wtc
import wx

#---------------------------------------------------------------------------

class fontdlg_Tests(wtc.WidgetTestCase):

    def test_fontdlg1(self):
        data = wx.FontData()
        # on Windows wx.FONTFAMILY_TELETYPE will actually use wx.FONTFAMILY_MODERN
        data.SetInitialFont(wx.FFont(15, wx.FONTFAMILY_MODERN))
        self.assertEqual(data.InitialFont.Family, wx.FONTFAMILY_MODERN)
        
        data.SetInitialFont(wx.FFont(15, wx.FONTFAMILY_SWISS))
        self.assertEqual(data.InitialFont.Family, wx.FONTFAMILY_SWISS)

        dlg = wx.FontDialog(self.frame, data)
        # TODO: find a safe way to test ShowModal on native dialogs
        dlg.Destroy()
        
        
    def test_fontdlg2(self):
        wx.GetFontFromUser
        
#---------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
