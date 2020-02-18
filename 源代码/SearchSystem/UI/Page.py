# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sys

from wx.lib.wordwrap import wordwrap
import wx.lib.agw.ultimatelistctrl as ULC

#求求你注释但别改这代码
#哈哈哈好的我这次注释啦，不改你的代码啦
paddle_signal_path = "./SearchSystem/paddle_signal.png"
BG_path = "./SearchSystem/BG.jpg.png"
timg_path = "./SearchSystem/timg.jpg.png"

#paddle_signal_path = "paddle_signal.png"
#BG_path = "BG.jpg.png"
#timg_path = "timg.jpg.png"

###########################################################################
## Class Page_1
###########################################################################

print("123456780981233124")

class Page_1 ( wx.Frame ):
	Acc_A = 0.68964
	Acc_B = 0.65192
	Acc_C = 0.64851

	Rel_A = 4
	Rel_B = 4
	Rel_C = 4
	txt_query = "query"
	txt_title = "title"
	txt_description = "description"
	final_relevance = "4.00" 

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 1000,650 ), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX )






		###############################
		#######我要设置背景图片了，哎 好难啊
		###############################
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

		self.SetBackgroundColour(wx.Colour(233, 233, 169))
		self.setupStatusBar()


		##################################
		#搜索结果

		self.searchResults = []
		#################################

		

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( paddle_signal_path, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 0,wx.LEFT|wx.TOP, 20 )
		self.m_bitmap1.SetBackgroundColour(wx.Colour(233, 233, 169))



		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.List_Keywords = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,600 ), wx.LC_REPORT|wx.LC_REPORT|wx.LC_HRULES )
		bSizer3.Add( self.List_Keywords, 0, wx.ALL, 15 )
		'''
		##################################
		#多行测试
		self.List_Description = ULC.UltimateListCtrl(self, agwStyle=ULC.ULC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT,size=wx.Size( 700,600 ))
		#self.items = ['list', 'list', 'I want to wrap words and content shold be placed in multiple lines for each item as the window is resized']
        #self.List_Description.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		colWidth = 200
		self.colWidthPad = 5
		#self.List_Description.InsertColumn(0, "test", width=colWidth)
		#for item in self.items[::-1]:
		#	item = wordwrap(item, colWidth - self.colWidthPad, wx.ClientDC(self))
		#	self.List_Description.InsertStringItem(0, item)


		#self.List_Description.Bind(wx.EVT_LIST_COL_DRAGGING, self.onDrag)



		##########################################

		'''
		self.List_Description = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,600 ), wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES )
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

	def OnEraseBack(self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()

		#dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(BG_path)
		dc.DrawBitmap(bmp, 0, 0)

	def onDrag(self, evt):
		col = evt.GetItem().GetColumn()
		width = self.List_Description.GetColumnWidth(col)
		itemCount = self.List_Description.GetItemCount()
		

		for i in range(0, itemCount):
			text = wordwrap(self.searchResults[i][col], width - self.colWidthPad, wx.ClientDC(self))
			self.List_Description.SetStringItem(i, col, text)


###########################################################################
## Class MyFrame3
###########################################################################

class Page_2 ( wx.Frame ):

	def __init__( self, parent ):
		print("1234567")
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CrowdFlower Search Calculate", pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX |wx.STAY_ON_TOP )

		print("12345678098")
		self.SetSizeHints( wx.Size( 800,800 ),wx.Size( 800,800 ) )
		self.SetBackgroundColour(wx.Colour(233, 233, 169))
		self.setupStatusBar()

		self.bSizer9 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 4, 3, 0, 0 )

#################这里有三个图形的名字哟！################
		self.Modle_A_Name = wx.StaticText( self, wx.ID_ANY, u"SVR Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Modle_A_Name.Wrap( -1 )
		gSizer11.Add( self.Modle_A_Name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Modle_B_Name = wx.StaticText( self, wx.ID_ANY, u"Linear Regression Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Modle_B_Name.Wrap( -1 )
		gSizer11.Add( self.Modle_B_Name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Modle_C_Name = wx.StaticText( self, wx.ID_ANY, u"Ridge Regression Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Modle_C_Name.Wrap( -1 )
		gSizer11.Add( self.Modle_C_Name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

#################这里有三张模型的图片哟！################
		self.Modle_A_Picture = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(timg_path,wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer11.Add(self.Modle_A_Picture, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, -30)
		self.Modle_B_Picture = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(timg_path,wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer11.Add(self.Modle_B_Picture, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, -30)
		self.Modle_C_Picture = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(timg_path,wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer11.Add(self.Modle_C_Picture, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, -30)
		self.m_bpButton5 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.m_bpButton6 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.m_bpButton7 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		gSizer11.Add( self.m_bpButton7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		calculate_01 = wx.BoxSizer( wx.VERTICAL )
##################这里有三排Acc和Relevance 哟！################
##A模型
		self.ACC_01 = wx.StaticText( self, wx.ID_ANY, u"Kappa: "+str(Page_1.Acc_A), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_01.Wrap( -1 )
		calculate_01.Add( self.ACC_01, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Relevance_01 = wx.StaticText( self, wx.ID_ANY, u"Relevance: "+str(Page_1.Rel_A), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_01.Wrap( -1 )
		calculate_01.Add( self.Relevance_01, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		gSizer11.Add( calculate_01, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

##模型B
		calculate_02 = wx.BoxSizer( wx.VERTICAL )
		self.ACC_02 = wx.StaticText( self, wx.ID_ANY, u"Kappa: "+str(Page_1.Acc_B), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_02.Wrap( -1 )
		calculate_02.Add( self.ACC_02, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Relevance_02 = wx.StaticText( self, wx.ID_ANY,u"Relevance: "+str(Page_1.Rel_B), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_02.Wrap( -1 )
		calculate_02.Add( self.Relevance_02, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		gSizer11.Add( calculate_02, 1, wx.EXPAND, 5 )

##模型C
		calculate_03 = wx.BoxSizer( wx.VERTICAL )
		self.ACC_03 = wx.StaticText( self, wx.ID_ANY, u"Kappa: "+str(Page_1.Acc_C), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ACC_03.Wrap( -1 )
		calculate_03.Add( self.ACC_03, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.Relevance_03 = wx.StaticText( self, wx.ID_ANY, u"Relevance: "+str(Page_1.Rel_C), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Relevance_03.Wrap( -1 )
		calculate_03.Add( self.Relevance_03, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		gSizer11.Add( calculate_03, 1, wx.EXPAND, 5 )
		self.bSizer9.Add(gSizer11, 1, wx.EXPAND, 5)

##############################下面就是计算面板了喔！######################
		#self.m_listCtrl5 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,200 ), wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES )
		#self.m_listCtrl5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,  wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		#self.m_listCtrl5.SetBackgroundColour( wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR ) )

		#bSizer9.Add( self.m_listCtrl5, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 40 )




	#	Cal_Formation = ['weight = softmax(Acc)','weight[1] = 20%','weight[2] = 20%','weight[3] = 20%','weight[4] = 20%','Final grades = ∑weight[i] * relevance[i]']

	#	self.m_listCtrl5.InsertColumn(0, 'Cal_Formation')
	#	self.m_listCtrl5.SetColumnWidth(0, 700)
	#	for key in Cal_Formation:
	#		index = self.m_listCtrl5.InsertItem(self.m_listCtrl5.GetItemCount(), str(key))

##############################下面尝试新的详情页的内容展示：详情信息 + 计算展示
		'''
		self.Quary_String = "Quary"
		self.Product_Title_String = "Product_Title"
		self.Product_Description_String = "Product_Description"
		self.Relevance_String = "100"
		'''
		self.Quary_String = Page_1.txt_query 
		self.Product_Title_String = Page_1.txt_title 
		self.Product_Description_String = Page_1.txt_description 
		self.Relevance_String = Page_1.final_relevance

		self.information_set()
		#self.Information_Panel()

		self.SetSizer(self.bSizer9)
		self.Layout()
		#self.SetSizerAndFit(self.bSizer9)
		self.Fit()
		self.Centre( wx.BOTH )

	def __del__( self ):
		pass
	def setupStatusBar(self):
		bar = self.CreateStatusBar(1)
		self.SetStatusWidths([-1])
		self.SetStatusText("Ready")

	def information_set(self):
		gSizer3 = wx.GridSizer(6, 7, 0, 0)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		self.Final_Relevance = wx.StaticText(self, wx.ID_ANY, u"Final Relevance：  ", wx.DefaultPosition, wx.DefaultSize,
											 0)
		font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		self.Final_Relevance.SetFont(font)
		self.Final_Relevance.Wrap(-1)

		gSizer3.Add(self.Final_Relevance, 0, wx.ALL, 40)


		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		self.Final_Relevance_Scores = wx.StaticText(self, wx.ID_ANY, u"   "+self.Relevance_String, wx.DefaultPosition,
													wx.DefaultSize, 0)
		self.Final_Relevance_Scores.SetFont(font)
		self.Final_Relevance_Scores.Wrap(-1)

		gSizer3.Add(self.Final_Relevance_Scores, 0, wx.TOP | wx.BOTTOM, 40)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		self.Query = wx.StaticText(self, wx.ID_ANY, u"Query：", wx.DefaultPosition, wx.DefaultSize, 0)
		self.Query.Wrap(-1)

		gSizer3.Add(self.Query, 0, wx.LEFT, 100)
		self.Query_Panel = wx.TextCtrl(self, wx.ID_ANY, self.Quary_String, wx.DefaultPosition, wx.Size(480, 60),
									   style=wx.TE_READONLY | wx.TE_MULTILINE )
		gSizer3.Add(self.Query_Panel, 0, wx.LEFT, 40)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		#gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
	


		self.Product_Title = wx.StaticText(self, wx.ID_ANY, u"Product Title：", wx.DefaultPosition, wx.DefaultSize, 0)
		self.Product_Title.Wrap(-1)

		gSizer3.Add(self.Product_Title, 0, wx.LEFT, 60)#-60

		self.Product_Title_Panel = wx.TextCtrl(self, wx.ID_ANY, self.Product_Title_String, wx.DefaultPosition,
											   wx.Size(480, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)#150,30
		gSizer3.Add(self.Product_Title_Panel, 0, wx.LEFT, 40)#80



		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)
		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		self.Product_Description = wx.StaticText(self, wx.ID_ANY, u"Description：", wx.DefaultPosition,wx.DefaultSize, 0)
		self.Product_Description.SetLabelMarkup(u"Description：")
		self.Product_Description.Wrap(-1)

		gSizer3.Add(self.Product_Description, 0, wx.LEFT, 70)

		self.Product_Description_Panel = wx.TextCtrl(self, wx.ID_ANY, self.Product_Description_String,wx.DefaultPosition, wx.Size(480, 100), style=wx.TE_READONLY | wx.TE_MULTILINE )
		gSizer3.Add(self.Product_Description_Panel, 0, wx.LEFT,40)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		self.bSizer9.Add(gSizer3, 1, wx.EXPAND, 5)





