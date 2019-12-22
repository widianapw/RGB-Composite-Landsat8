# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from rgb import rgb
import self as self
from PIL import Image
import matplotlib.pyplot as plt
import scipy.misc as sm
###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "RGB Composite", pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.Maximize(True)
		# self.m_menubar3 = wx.MenuBar( 0 )
		# self.m_menu3 = wx.Menu()
		# self.m_menuItem1 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Open File"+ u"\t" + u"ctrl+o", wx.EmptyString, wx.ITEM_NORMAL )
		# self.m_menu3.AppendItem( self.m_menuItem1 )
		
		# self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Save"+ u"\t" + u"ctrl+s", wx.EmptyString, wx.ITEM_NORMAL )
		# self.m_menu3.AppendItem( self.m_menuItem2 )
		
		# self.m_menuItem4 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Save As"+ u"\t" + u"ctrl+alt+s", wx.EmptyString, wx.ITEM_NORMAL )
		# self.m_menu3.AppendItem( self.m_menuItem4 )
		
		# self.m_menuItem41 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Quit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		# self.m_menu3.AppendItem( self.m_menuItem41 )
		
		# self.m_menubar3.Append( self.m_menu3, u"File" ) 
		
		# self.m_menu4 = wx.Menu()
		# self.m_menubar3.Append( self.m_menu4, u"Settings" ) 
		
		# self.SetMenuBar( self.m_menubar3 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"RGB Composite", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Masukan Folder Citra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_dirPicker3 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 600,-1 ), wx.DIRP_DEFAULT_STYLE )
		bSizer3.Add( self.m_dirPicker3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Pilih Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		m_choice1Choices = [ u"Pilih Mode RGB",u"4-3-2 (Natural Color)", u"6-5-4 (Vegetation Analysis)", u"7-5-4 (Shortwave Infrared)", u"7-5-3 (Natural With Atmospheric Removal)", u"5-6-4 (Land/Water)", u"5-6-2 (Healty Vegetation)", u"7-6-5 (Atmospheric Penetrarion)", u"6-5-2 (Agriculture)", u"5-4-3 (Color Infrared)", u"7-6-4 (False Color)" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,choices=m_choice1Choices )
		self.m_choice1.SetSelection(0)
		bSizer3.Add( self.m_choice1, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Koordinat Crop (Opsional)" ), wx.HORIZONTAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Koordinat Default" ), wx.HORIZONTAL )
		
		fgSizer31 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText91 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Longitude Start : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		fgSizer31.Add( self.m_staticText91, 1, wx.ALL|wx.EXPAND|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText10 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Not Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer31.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText110 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Longitude End :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText110.Wrap( -1 )
		fgSizer31.Add( self.m_staticText110, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText11 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Not Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer31.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( fgSizer31, 1, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText130 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Latitude Start :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )
		fgSizer4.Add( self.m_staticText130, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Not Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Latitude End :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Not Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Koordinat Crop" ), wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText51 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Longitude Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer1.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Longitude End", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer1.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Latitude Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Latitude End", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer3.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Proses RGB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer3.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		self.m_bitmap2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Save As" ), wx.HORIZONTAL )
		
		self.m_button3 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"PNG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button3.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		sbSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"JPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button4.SetBackgroundColour( wx.Colour( 128, 64, 64 ) )
		
		sbSizer1.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button51 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"TIF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button51.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 64, 0, 128 ) )
		
		sbSizer1.Add( self.m_button51, 0, wx.ALL, 5 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_HELP, wx.ART_HELP_BROWSER ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer3.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer3.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		self.rgb = rgb()
		self.rgb.MyListener(self)
		
		self.m_dirPicker3.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnDirChanged )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.OnChoiceRGB )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnShowResult )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnSavePNG )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnSaveJPG )
		self.m_button51.Bind( wx.EVT_BUTTON, self.OnSaveTIF )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.OnInformationClick )
	
	def __del__( self ):
		pass
	
	select = 0
	progress=None
	# Virtual event handlers, overide them in your derived class
	def OnMenuItemQuit( self, event ):
		event.Skip()
	
	def OnDirChanged( self, event ):
		path = event.GetPath()
		self.rgb.OpenDir(path)
		if self.rgb.isOpenDir:
			self.showMessage("Direktori Folder Berhasil Dimasukkan!")
			self.m_staticText10.SetLabel(str(self.rgb.lonStartDefault))
			self.m_staticText12.SetLabel(str(self.rgb.latStartDefault))
			self.m_staticText11.SetLabel(str(self.rgb.lonEndDefault))
			self.m_staticText13.SetLabel(str(self.rgb.latEndDefault))
			self.Layout()
		else:
			self.showErrorMessage("Tidak Terdapat Band atau Metadata Pada Folder Yang Diinputkan!")
			self.m_dirPicker3.SetPath("")
			self.m_staticText10.SetLabel("Not Set")
			self.m_staticText12.SetLabel("Not Set")
			self.m_staticText11.SetLabel("Not Set")
			self.m_staticText13.SetLabel("Not Set")
		event.Skip()
	
	
	def OnChoiceRGB( self, event ):
		if self.rgb.isOpenDir:
			selection = event.GetSelection()
			print(selection)
			self.rgb.ValidateSelection(selection)
			print(self.rgb.isValidateSelection)
			if selection == 1 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 4, Band 3 atau Band 2 di dalam Folder!")
				self.m_choice1.SetSelection(0)
			
			elif selection == 2 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 6, Band 5 atau Band 4 di dalam Folder!")
				self.m_choice1.SetSelection(0)
			
			elif selection == 3 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 7, Band 5 atau Band 4 di dalam Folder!")
				self.m_choice1.SetSelection(0)

			elif selection == 4 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 7, Band 5 atau Band 3 di dalam Folder!")
				self.m_choice1.SetSelection(0)
			
			elif selection == 5 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 5, Band 6 atau Band 4 di dalam Folder!")
				self.m_choice1.SetSelection(0)

			elif selection == 6 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 5, Band 6 atau Band 2 di dalam Folder!")
				self.m_choice1.SetSelection(0)
			
			elif selection == 7 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 7, Band 6 atau Band 5 di dalam Folder!")
				self.m_choice1.SetSelection(0)
			
			elif selection == 8 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 6, Band 5 atau Band 2 di dalam Folder!")
				self.m_choice1.SetSelection(0)

			elif selection == 9 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 5, Band 4 atau Band 3 di dalam Folder!")
				self.m_choice1.SetSelection(0)
			
			elif selection == 10 and self.rgb.isValidateSelection == False:
				self.showErrorMessage("Tidak Terdapat Band 7, Band 6 atau Band 4 di dalam Folder!")
				self.m_choice1.SetSelection(0)

			elif selection == 0 and self.rgb.isValidateSelection == False:
				print("pilih selection")
			else:
				self.showMessage("Mode RGB Berhasil Dipilih!")

		else:
			self.showErrorMessage("Masukkan Direktori Folder Terlebih Dahulu!")
			self.m_choice1.SetSelection(0)
			
		event.Skip()
	
	
	def OnShowResult( self, event ):
		lonStart = self.m_textCtrl1.GetValue()
		latStart = self.m_textCtrl3.GetValue()
		lonEnd = self.m_textCtrl2.GetValue()
		latEnd = self.m_textCtrl4.GetValue()
		print(lonStart)
		print(latStart)
		print(lonEnd)
		print(latEnd)
		
		if self.rgb.isOpenDir and self.rgb.isValidateSelection:
			self.showProgress()
			percent = 30
			self.progress.Update(percent)
			self.rgb.ProccessRGBCrop(lonStart, lonEnd, latStart, latEnd)
		elif self.rgb.isOpenDir == False:
			self.showErrorMessage("Direktori Folder Belum Terisi !")
		elif self.rgb.isValidateSelection == False:
			self.showErrorMessage("Pilih Mode RGB sebelum melakukan proses !")
		else :
			self.showErrorMessage("Direktori Folder atau Mode RGB Belum Terisi !")
		
		event.Skip()
	
	def showMessage(self, message):
		dialog = wx.MessageDialog(None, message, "Info", wx.OK | wx.ICON_INFORMATION)
		dialog.ShowModal()

	def showErrorMessage(self, message):
		dialog = wx.MessageDialog(None, message, "Error", wx.OK | wx.ICON_ERROR)
		dialog.ShowModal()
	
	def OnSavePNG( self, event ):
		if self.rgb.isRGB == False:
			self.showErrorMessage("Lakukan Proses RGB Terlebih Dahulu!")
		else :
			saveFileDialog = wx.FileDialog(frame, 'Save to PNG', '', '', 'PNG|*.PNG', wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
			if (saveFileDialog.ShowModal() == wx.ID_OK):
				self.showProgressSave()
				percent = 50
				self.progress.Update(percent)
				path = saveFileDialog.GetPath()
				self.rgb.SaveResult(path)
				self.showProgressSave()
				percent = 100
				self.progress.Update(percent)
				self.progress.Destroy()
				self.showMessage("File has been saved!.")
			else:
				self.showErrorMessage("Failed to save file!")
		
		event.Skip()
	
	def OnSaveJPG( self, event ):
		if self.rgb.isRGB == False:
			self.showErrorMessage("Lakukan Proses RGB Terlebih Dahulu!")
		else :
			saveFileDialog = wx.FileDialog(frame, 'Save to JPG', '', '', 'JPG|*.JPG', wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

			if (saveFileDialog.ShowModal() == wx.ID_OK):
				self.showProgressSave()
				percent = 50
				self.progress.Update(percent)
				path = saveFileDialog.GetPath()
				self.rgb.SaveResult(path)
				self.showProgressSave()
				percent = 100
				self.progress.Update(percent)
				self.progress.Destroy()
				self.showMessage("File has been saved!.")

			else:
				self.showErrorMessage("Failed to save file!")
		event.Skip()
	
	def OnSaveTIF( self, event ):
		if self.rgb.isRGB == False:
			self.showErrorMessage("Lakukan Proses RGB Terlebih Dahulu!")
		else :
			saveFileDialog = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*tif)|*.tif', wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
			if (saveFileDialog.ShowModal() == wx.ID_OK):
				self.showProgressSave()
				percent = 50
				self.progress.Update(percent)

				path = saveFileDialog.GetPath()
				self.rgb.SaveResult(path)
				
				self.showProgressSave()
				percent = 100
				self.progress.Update(percent)
				self.progress.Destroy()
				self.showMessage("File has been saved!.")
				
			else:
				self.showErrorMessage("Failed to save file!")
		event.Skip()
	
	def convertToImage(self, array, isfloat):
		if isfloat:
			rgb = array * 255
		else:
			rgb = array / 255
		pilImage = Image.fromarray(rgb).convert('RGB')
		image = wx.EmptyImage(pilImage.size[0], pilImage.size[1])
		image.SetData(pilImage.tobytes())
		H = image.GetHeight()
		W = image.GetWidth()
		newH = 250
		newW = 250
		if (W > H):
			newH = 250 * H / W
		else:
			newW = 250 * W / H
		image = image.Scale(newW, newH)
		return image
	
	def OnRGBFinished(self, result, selection):
		
		percent = 80
		self.progress.Update(percent)
		# sm.toimage(result,cmin=np.percentile(result,2),cmax=np.percentile(rgb,98)).save('RGB.png')
		# plt.imshow(result, interpolation='nearest')
		# plt.savefig('RGB.png', format='png', dpi=300, bbox_inches='tight')
		sm.imsave('RGB.PNG', result)
		# plt.figure(figsize=(3, 3))
		# plt.figure(figsize=(3.841, 7.195), dpi=300)
		# im = plt.imshow(result, interpolation='nearest')
		# plt.colorbar(im)
		# plt.savefig('RGB.PNG',format='PNG', dpi=300, bbox_inches='tight')
		
		percent = 100
		self.progress.Update(percent)
		b4refImage = wx.Bitmap("RGB.PNG", wx.BITMAP_TYPE_ANY)
		W = b4refImage.GetWidth()
		H = b4refImage.GetHeight()
		if W > H:	
			NewW = 400
			NewH = 400 * H / W
		else:
			NewH = 400
			NewW = 400 * W / H
		image = wx.Bitmap.ConvertToImage(b4refImage)
		scaledImage = image.Scale(NewW,NewH,wx.IMAGE_QUALITY_HIGH)
		bitmap = wx.Bitmap(scaledImage)
		# percent = 100
		# self.progress.Update(percent)
		self.progress.Destroy()
		self.m_bitmap2.SetBitmap(wx.Bitmap(bitmap))
		
		self.showMessage("RGB successfuly")
		
		self.select = selection
		frame.Layout()

	def OnInformationClick(self, event):
		#true color
		if self.select == 1:
			self.showMessage("Natural Color\nKombinasi kanal ini akan menghasilkan warna alami (natural color) karena  kombinasi ini akan menampilkan citra yang sama dengan sistem visual manusia")
		elif self.select == 2:
			self.showMessage("Vegetation Analysis\nKombinasi ini digunakan untuk menganalisis tumbuh-tumbuhan.")
		elif self.select == 3:
			self.showMessage("ShortWave Infrared\nMenghasilkan citra dengan kontras yang jelas dan lebih bersih")
		elif self.select == 4:
			self.showMessage("Natural With Atmospheric Removal\nKombinasi  ini  menunjukkan  warna sebenarnya dengan mengurangi kenampakan pada awan.")
		elif self.select ==5:
			self.showMessage("Land/Water\nKombinasi ini sangat cocok digunakan untuk membedakan badan air  dan  daratan.  Dimana  badan  air  ditunjukkan  dengan  warna  gelap.  Sedangkan daratan ditunjukkan dengan warna lebih terang. ")
		elif self.select ==6:
			self.showMessage("Healthy Vegetation\nDigunakan untuk menghasilkan citra yang menampakkan tumbuhan yang sehat. ")
		elif self.select ==7:
			self.showMessage("Atmospheric Penetration\nBerguna untuk memperjelas citra dari ketebalan awan, memperjelas garis pantai, dan tutupan vegetasi. Kombinasi ini dapat memperjelas citra dari gangguan cuaca.  ")
		elif self.select ==8:
			self.showMessage("Agriculture\nDigunakan untuk menghasilkan citra dengan perbedaan tumbuh-tumbuhan yang jelas ditunjukkan dengan warna kehijauan.")
		elif self.select == 9:
			self.showMessage("Color Infrared\nKombinasi  ini  digunakan  untuk  melihat  masa,  kerapatan,  dan  dominasi  vegetasi. Kontras antara dominasi vegetasi akan terlihat dalam infrared, sehingga efektif bagi analisis vegetasi kehutanan atau pertanian skala besar. ")
		elif self.select == 10:
			self.showMessage("False Color\nDigunakan  untuk  menghasilkan  citra  dengan  perbedaan  yang  jelas  pada  daerah perkotaan/urban.")
		else:
			self.showMessage("Lakukan Proses RGB Terlebih Dahulu!")
		event.Skip()
	
	def showProgress(self):
		self.progress = wx.ProgressDialog("RGB Composite in progress", "please wait...", style=wx.PD_SMOOTH|wx.PD_AUTO_HIDE)

	def showProgressSave(self):
		self.progress = wx.ProgressDialog("Saving As Image", "please wait...", style=wx.PD_SMOOTH|wx.PD_AUTO_HIDE)
		
	def destoryProgress(self):
		self.progress.Destroy()

app = wx.App(False)

#create an object of MyFrame2
frame = MyFrame5(None)
#show the frame
frame.Show(True)
#start the application
app.MainLoop()