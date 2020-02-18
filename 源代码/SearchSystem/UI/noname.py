# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import  wx.lib.mixins.listctrl  as  listmix
import time
###########################################################################
## Class MyFrame1
###########################################################################

ID_SEARCH = 200
ID_ABOUT = 201

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.Colour( 3, 131, 135 ))
		self.setupStatusBar()

		#Main menu
		menubar = wx.MenuBar()
		Smenu = wx.Menu()
		Smenu.Append(ID_SEARCH,u'Search(&S)','You can get a home page to find the result of your keywords searching')
		menubar.Append(Smenu,u'File(&F)')
		Amenu = wx.Menu()
		Amenu.Append(ID_SEARCH,u'About(&A)','You can get a page about the whole showing progress')
		menubar.Append(Amenu, u'Help(&H)')

		self.SetMenuBar(menubar)

		wx.EVT_MENU(self, ID_SEARCH, self.OnMenuSearch)
		wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
#		wx.EVT_MENU(self, self.OnCloseWindow)

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		bSizer2.Add( ( 100, 40), 1, 0, 5 )


		self.Paddle_Logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"C:\\Users\\91677\\Desktop\\paddle_Logo.png", wx.BITMAP_TYPE_ANY ),
											wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Paddle_Logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Input_field_1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(430, -1),
										wx.TE_PROCESS_ENTER)
		self.Input_field_1.SetMaxLength( 0 )
		bSizer2.Add( self.Input_field_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Paddle_signal = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0|wx.BORDER_NONE )

		#self.Paddle_signal.SetBitmap( wx.Bitmap( u"C:\\Users\\91677\\Desktop\\paddle_signal.png", wx.BITMAP_TYPE_ANY ) )
		self.Paddle_signal.SetBitmapDisabled( wx.Bitmap( u"C:\\Users\\91677\\Desktop\\paddle_signal02.png", wx.BITMAP_TYPE_ANY ) )
		self.Paddle_signal.SetBitmapPressed( wx.Bitmap( u"C:\\Users\\91677\\Desktop\\paddle_signal.png", wx.BITMAP_TYPE_ANY ) )
		self.Paddle_signal.SetBitmapFocus( wx.Bitmap( u"C:\\Users\\91677\\Desktop\\paddle_signal02.png", wx.BITMAP_TYPE_ANY ) )
		self.Paddle_signal.SetBitmapCurrent( wx.Bitmap( u"C:\\Users\\91677\\Desktop\\paddle_signal.png", wx.BITMAP_TYPE_ANY ) )
		self.Paddle_signal.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.Paddle_signal.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.Paddle_signal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer2.Add( self.Paddle_signal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )



		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.Paddle_signal.Bind( wx.EVT_BUTTON, self.Page_turn_to02 )

	def __del__( self ):
		pass
	# Virtual event handlers, overide them in your derived class
	def Page_turn_to02( self, event ):
		frame01 = MyFrame2(None)
		frame01.m_textCtrl29.ChangeValue(self.Input_field_1.GetValue())
		frame01.Show()
		self.Close()

	def setupStatusBar(self):
		bar = self.CreateStatusBar(1)
		self.SetStatusWidths([-1])
		self.SetStatusText("ready")
	#MenuBar
	def OnMenuSearch(self,event):
		self.SetStatusText("Search")
	def OnMenuAbout(self,event):
		dlg = AboutDialog(None,-1)
		dlg.ShowModal()
		dlg.Destroy()



###########################################################################
## Class MyFrame2
###########################################################################

class AboutDialog(wx.Dialog):
	def __init__(self,parent,id):
		wx.Dialog.__init__(self,parent,id,'About me',size = (200,200))

		self.sizerl = wx.BoxSizer(wx.VERTICAL)

		self.sizerl.Add(wx.StaticText(self,-1,u"There exit several tips, \n but we still are compeleting them......"),
						0,wx.ALIGN_CENTER_HORIZONTAL|wx.TOP,border = 20)
		self.SetSizer(self.sizerl)

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )


		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		fgSizer2 = wx.FlexGridSizer( 6, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		self.setupStatusBar()

		self.Paddle_Logo = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"C:\\Users\\91677\\Desktop\\paddle_Logo02.png",wx.BITMAP_TYPE_ANY), wx.DefaultPosition,wx.Size(110, 35), 0)
		self.Paddle_Logo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer2.Add( self.Paddle_Logo, 1, 0, 5)


		#fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_textCtrl29 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 560,-1 ), 0 )
		self.m_textCtrl29.SetMaxLength( 0 )
		fgSizer2.Add( self.m_textCtrl29, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 10,10 ), 0 )
		fgSizer2.Add( self.m_button4, 0, wx.ALL, 5 )

		gSizer10 = wx.GridSizer( 8, 2, 10, 500 )

		gSizer10.SetMinSize( wx.Size( 800,350 ) )
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"title_01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		gSizer10.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"4.11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		gSizer10.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"There is something like to be discribe what shows in the screen and maybe there is just a little words can be seen", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticText46.Wrap( -1 )

		self.m_staticText46.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_staticText46.SetMinSize( wx.Size( 540,-1 ) )

		gSizer10.Add( self.m_staticText46, 0, wx.ALL, 5 )


		gSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"title_02", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		gSizer10.Add( self.m_staticText47, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"4.01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		gSizer10.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"There is something like to be discribe what shows in the screen and maybe there is just a little words can be seen", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticText49.Wrap( -1 )

		self.m_staticText49.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_staticText49.SetMinSize( wx.Size( 540,-1 ) )

		gSizer10.Add( self.m_staticText49, 0, wx.ALL, 5 )


		gSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"title_03", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer10.Add( self.m_staticText50, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"3.16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer10.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"There is something like to be discribe what shows in the screen and maybe there is just a little words can be seen", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticText52.Wrap( -1 )

		self.m_staticText52.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_staticText52.SetMinSize( wx.Size( 540,-1 ) )

		gSizer10.Add( self.m_staticText52, 0, wx.ALL, 5 )


		gSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"title_04", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		gSizer10.Add( self.m_staticText53, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"2.81", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		gSizer10.Add( self.m_staticText54, 0, wx.ALL, 5 )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"There is something like to be discribe what shows in the screen and maybe there is just a little words can be seen", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticText55.Wrap( -1 )

		self.m_staticText55.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_staticText55.SetMinSize( wx.Size( 540,-1 ) )

		gSizer10.Add( self.m_staticText55, 0, wx.ALL, 5 )


		gSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( gSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.m_staticText54.Bind(wx.EVT_LEFT_DOWN, self.Page_turn_to03)
		self.m_staticText51.Bind(wx.EVT_LEFT_DOWN, self.Page_turn_to03)
		self.m_staticText48.Bind(wx.EVT_LEFT_DOWN, self.Page_turn_to03)
		self.m_staticText45.Bind(wx.EVT_LEFT_DOWN, self.Page_turn_to03)

		self.Centre( wx.BOTH )

	# Virtual event handlers, overide them in your derived class
	def Page_turn_to03( self, event ):
		frame02 = MyFrame3(None)
		frame02.Show()
	def setupStatusBar(self):
		bar = self.CreateStatusBar(1)
		self.SetStatusWidths([-1])
		self.SetStatusText("ready")

	def __del__( self ):
		pass

###########################################################################
## Class MyFrame01
###########################################################################

class MyFrame01 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		fgSizer2 = wx.FlexGridSizer( 6, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Paddle_Logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"C:\\Users\\91677\\Desktop\\paddle_Logo02.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 110,35 ), 0 )
		self.Paddle_Logo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )


		fgSizer2 = wx.BoxSizer(wx.VERTICAL)
		self.list = TestVirtualList(self)

		fgSizer2.Add(self.Paddle_Logo, 1, 0, 5)
		fgSizer2.Add(self.list, 1, wx.EXPAND)


		self.SetSizer(fgSizer2)
		self.SetAutoLayout(True)

		gSizer10 = wx.GridSizer( 8, 2, 10, 500 )

		gSizer10.SetMinSize( wx.Size( 800,350 ) )

		gSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( gSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def turn( self, event ):
		event.Skip()


class TestVirtualList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(
            self, parent, -1,
            style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.LC_HRULES|wx.LC_VRULES,size = wx.Size( 600,300 )
            )
        self.InsertColumn(0, "Title")
        self.InsertColumn(1, "Description")
        self.InsertColumn(2, "Kappa")
        self.SetColumnWidth(0, 175)
        self.SetColumnWidth(1, 175)
        self.SetColumnWidth(2, 175)

        #self.InsertItem("aaaa")

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 3, 3, 0, 0 )

		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Model_A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		gSizer11.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Model_B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		gSizer11.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Model_C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		gSizer11.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bpButton5 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bpButton6 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bpButton7 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		calculate_01 = wx.BoxSizer( wx.VERTICAL )

		self.ACC_01 = wx.StaticText( self, wx.ID_ANY, u"4.11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_01.Wrap( -1 )

		calculate_01.Add( self.ACC_01, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Relevance_01 = wx.StaticText( self, wx.ID_ANY, u"98.2%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_01.Wrap( -1 )

		calculate_01.Add( self.Relevance_01, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer11.Add( calculate_01, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		calculate_02 = wx.BoxSizer( wx.VERTICAL )

		self.ACC_02 = wx.StaticText( self, wx.ID_ANY, u"4.01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_02.Wrap( -1 )

		calculate_02.Add( self.ACC_02, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Relevance_02 = wx.StaticText( self, wx.ID_ANY, u"100%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_02.Wrap( -1 )

		calculate_02.Add( self.Relevance_02, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer11.Add( calculate_02, 1, wx.EXPAND, 5 )

		calculate_03 = wx.BoxSizer( wx.VERTICAL )

		self.ACC_03 = wx.StaticText( self, wx.ID_ANY, u"3.98", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_03.Wrap( -1 )

		calculate_03.Add( self.ACC_03, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Relevance_03 = wx.StaticText( self, wx.ID_ANY, u"0.02%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_03.Wrap( -1 )

		calculate_03.Add( self.Relevance_03, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer11.Add( calculate_03, 1, wx.EXPAND, 5 )


		bSizer9.Add( gSizer11, 1, wx.EXPAND, 5 )

		self.m_listCtrl5 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,200 ), wx.LC_ICON )
		self.m_listCtrl5.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_listCtrl5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer9.Add( self.m_listCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		bSizer9.Add((0, 0), 1, wx.EXPAND, 5)
		self.SetSizer( bSizer9 )
		self.Layout()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass





