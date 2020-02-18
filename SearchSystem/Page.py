# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Main_1 import TTry2

import sys

###########################################################################
## Class Page_1
###########################################################################
global Acc_A,Acc_B,Acc_C,Rel_A,Rel_B,Rel_C

Acc_A = 1.0
Acc_B = 2.0
Acc_C = 3.0
Rel_A = 4.0
Rel_B = 500
Rel_C = 600



bitmap_path = "paddle_signal.png"

class Page_1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 800,511 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.Colour( 255, 255, 225 ))
		self.setupStatusBar()

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( bitmap_path, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap2, 0, wx.ALL, 10 )

		#self.Key_Words_Details = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		#self.Key_Words_Details.Wrap(-1)
		#self.Key_Words_Details = wx.StaticText(self, wx.ID_ANY, u"There exists no key word", wx.DefaultPosition, wx.DefaultSize, 0)
		#bSizer2.Add( self.Key_Words_Details, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )



		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.List_Keywords = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,400 ), wx.LC_REPORT|wx.LC_REPORT|wx.LC_HRULES )
		bSizer3.Add( self.List_Keywords, 0, wx.ALL, 15 )


		self.List_Description = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,400 ), wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES )
		self.List_Description.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer3.Add( self.List_Description, 0, wx.ALL, 20 )

#############################ListCtrl Style########################################


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )



	def __del__( self ):
		pass

	def setupStatusBar(self):
		bar = self.CreateStatusBar(1)
		self.SetStatusWidths([-1])
		self.SetStatusText("Ready")


###########################################################################
## Class MyFrame3
###########################################################################

class Page_2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.Colour( 255, 255, 225 ))
		self.setupStatusBar()

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 4, 3, 0, 0 )

#################这里有三个图形的名字哟！################
		self.Modle_A_Name = wx.StaticText( self, wx.ID_ANY, u"XGBoost Linear Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Modle_A_Name.Wrap( -1 )
		gSizer11.Add( self.Modle_A_Name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Modle_B_Name = wx.StaticText( self, wx.ID_ANY, u"SVR Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Modle_B_Name.Wrap( -1 )
		gSizer11.Add( self.Modle_B_Name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Modle_C_Name = wx.StaticText( self, wx.ID_ANY, u"Random Forest Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Modle_C_Name.Wrap( -1 )
		gSizer11.Add( self.Modle_C_Name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

#################这里有三张模型的图片哟！################
		self.Modle_A_Picture = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(bitmap_path,wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer11.Add(self.Modle_A_Picture, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
		self.Modle_B_Picture = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(bitmap_path,wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer11.Add(self.Modle_B_Picture, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
		self.Modle_C_Picture = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(bitmap_path,wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer11.Add(self.Modle_C_Picture, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
		self.m_bpButton5 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.m_bpButton6 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.m_bpButton7 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		calculate_01 = wx.BoxSizer( wx.VERTICAL )
##################这里有三排Acc和Relevance 哟！################
##A模型
		self.ACC_01 = wx.StaticText( self, wx.ID_ANY, u"Acc: "+str(Acc_A), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_01.Wrap( -1 )
		calculate_01.Add( self.ACC_01, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Relevance_01 = wx.StaticText( self, wx.ID_ANY, u"Relevance: "+str(Rel_A), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_01.Wrap( -1 )
		calculate_01.Add( self.Relevance_01, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		gSizer11.Add( calculate_01, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

##模型B
		calculate_02 = wx.BoxSizer( wx.VERTICAL )
		self.ACC_02 = wx.StaticText( self, wx.ID_ANY, u"Acc: "+str(Acc_B), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_02.Wrap( -1 )
		calculate_02.Add( self.ACC_02, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Relevance_02 = wx.StaticText( self, wx.ID_ANY,u"Relevance: "+str(Rel_B), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_02.Wrap( -1 )
		calculate_02.Add( self.Relevance_02, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		gSizer11.Add( calculate_02, 1, wx.EXPAND, 5 )

##模型C
		calculate_03 = wx.BoxSizer( wx.VERTICAL )
		self.ACC_03 = wx.StaticText( self, wx.ID_ANY, u"Acc: "+str(Acc_C), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_03.Wrap( -1 )
		calculate_03.Add( self.ACC_03, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Relevance_03 = wx.StaticText( self, wx.ID_ANY, u"Relevance: "+str(Rel_C), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_03.Wrap( -1 )
		calculate_03.Add( self.Relevance_03, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		gSizer11.Add( calculate_03, 1, wx.EXPAND, 5 )
		bSizer9.Add(gSizer11, 1, wx.EXPAND, 5)

##############################下面就是计算面板了喔！######################3

		self.m_listCtrl5 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,200 ), wx.LC_REPORT )
		self.m_listCtrl5.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,  wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_listCtrl5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		bSizer9.Add((0, 0), 1, wx.EXPAND, 20)

		bSizer9.Add( self.m_listCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		Cal_Formation = ['weight = softmax(Acc)','weight[1] = 20%','weight[2] = 20%','weight[3] = 20%','weight[4] = 20%','Final grades = ∑weight[i] * relevance[i]']

		self.m_listCtrl5.InsertColumn(0, 'Cal_Formation')
		self.m_listCtrl5.SetColumnWidth(0, 700)
		for key in Cal_Formation:
			index = self.m_listCtrl5.InsertItem(self.m_listCtrl5.GetItemCount(), str(key))

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass
	def setupStatusBar(self):
		bar = self.CreateStatusBar(1)
		self.SetStatusWidths([-1])
		self.SetStatusText("ready")

