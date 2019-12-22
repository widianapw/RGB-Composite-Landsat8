import glob
import numpy as np
from osgeo import gdal
import scipy.misc as sm
from gdal import GetDriverByName
from pyproj import Proj
import wx
import matplotlib.pyplot as plt

class rgb:
    TAG = "rgb.class"
    in_dir = ""
    isOpenDir = False
    willCroped = False

    isRGB = False
    b4_file = None
    b3_file = None
    b2_file = None

    b5_file = None
    b6_file = None
    b7_file = None
    mtl_file = None

    final_rgb = None
    GlobSelection = 0

    isValidateSelection = False
    cols = 0
    rows = 0
    output_cols = 0
    output_rows = 0
    listener = None
    b2MultiReflectance = ""
    b3MultiReflectance = ""
    b4MultiReflectance = ""
    b5MultiReflectance = ""
    b6MultiReflectance = ""
    b7MultiReflectance = ""

    b2AddReflectance = ""
    b3AddReflectance = ""
    b4AddReflectance = ""
    b5AddReflectance = ""
    b6AddReflectance = ""
    b7AddReflectance = ""

    lonStartCrop = 0
    latStartCrop = 0
    lonEndCrop = 0
    latEndCrop = 0

    lonStartDefault = 0
    latStartDefault = 0
    lonEndDefault = 0
    latEndDefault = 0

    progress = None

    def __init__(self):
        print("RGB instance created")

    def OpenDir(self, path):
        # print(path)
        self.in_dir = path.replace("\\","/") + "/"

        # print(self.in_dir)
        self.b2_file = glob.glob(self.in_dir + '**B2.TIF')
        self.b3_file = glob.glob(self.in_dir + '**B3.TIF')
        self.b4_file = glob.glob(self.in_dir + '**B4.TIF')
        self.b5_file = glob.glob(self.in_dir + '**B5.TIF')
        self.b6_file = glob.glob(self.in_dir + '**B6.TIF')
        self.b7_file = glob.glob(self.in_dir + '**B7.TIF')
        self.mtl_file = glob.glob(self.in_dir + '**MTL.txt')
        print(self.mtl_file)
        if self.mtl_file:
            file = open(self.mtl_file[0], 'r')
            metadata = file.readlines()
            for i in metadata:
                if i.startswith("    CORNER_UL_LON_PRODUCT"):
                    data = i.split()
                    lonStart = data[2]
                    print("Lon start: " + lonStart)
                    self.lonStartDefault = lonStart

                if i.startswith("    CORNER_UR_LAT_PRODUCT"):
                    data = i.split()
                    latStart = data[2]
                    print("Lat Start: " + latStart)
                    self.latStartDefault = latStart

                if i.startswith("    CORNER_UR_LON_PRODUCT"):
                    data = i.split()
                    lonEnd = data[2]
                    print("Lon end: " + lonEnd)
                    self.lonEndDefault = lonEnd

                if i.startswith("    CORNER_LL_LAT_PRODUCT"):
                    data = i.split()
                    latEnd = data[2]
                    print("lat end: " + latEnd)
                    self.latEndDefault = latEnd

                if i.startswith("    REFLECTANCE_MULT_BAND_2"):
                    data = i.split()
                    result = data[2]
                    print("b2MultiReflectance: " + result)
                    self.b2MultiReflectance = result

                if i.startswith("    REFLECTANCE_ADD_BAND_2"):
                    data = i.split()
                    result = data[2]
                    print("b2AddReflectance: " + result)
                    self.b2AddReflectance = result

                if i.startswith("    REFLECTANCE_MULT_BAND_3"):
                    data = i.split()
                    result = data[2]
                    print("b3MultiReflectance: " + result)
                    self.b3MultiReflectance = result

                if i.startswith("    REFLECTANCE_ADD_BAND_3 "):
                    data = i.split()
                    result = data[2]
                    print("b3AddReflectance: " + result)
                    self.b3AddReflectance = result

                if i.startswith("    REFLECTANCE_MULT_BAND_4"):
                    data = i.split()
                    result = data[2]
                    print("b4MultiReflectance: " + result)
                    self.b4MultiReflectance = result

                if i.startswith("    REFLECTANCE_ADD_BAND_4"):
                    data = i.split()
                    result = data[2]
                    print("b4AddReflectance: " + result)
                    self.b4AddReflectance = result

                if i.startswith("    REFLECTANCE_MULT_BAND_5"):
                    data = i.split()
                    result = data[2]
                    print("b5MultiReflectance: " + result)
                    self.b5MultiReflectance = result

                if i.startswith("    REFLECTANCE_ADD_BAND_5"):
                    data = i.split()
                    result = data[2]
                    print("b5AddReflectance: " + result)
                    self.b5AddReflectance = result


                if i.startswith("    REFLECTANCE_MULT_BAND_6"):
                    data = i.split()
                    result = data[2]
                    print("b6MultiReflectance: " + result)
                    self.b6MultiReflectance = result

                if i.startswith("    REFLECTANCE_ADD_BAND_6"):
                    data = i.split()
                    result = data[2]
                    print("b6AddReflectance: " + result)
                    self.b6AddReflectance = result

                if i.startswith("    REFLECTANCE_MULT_BAND_7"):
                    data = i.split()
                    result = data[2]
                    print("b7MultiReflectance: " + result)
                    self.b7MultiReflectance = result

                if i.startswith("    REFLECTANCE_ADD_BAND_7"):
                    data = i.split()
                    result = data[2]
                    print("b7AddReflectance: " + result)
                    self.b7AddReflectance = result        


                if i.startswith("    SUN_ELEVATION"):
                    data = i.split()
                    result = data[2]
                    print("sun elevation: " + result)
                    self.sunElevation = result
        
        if not self.b2_file and not self.b3_file and not self.b4_file and not self.b5_file and not self.b6_file and not self.b7_file or not self.mtl_file:
            self.isOpenDir = False
        else:
            self.isOpenDir = True
        

    def norm(self, band):
        band_min, band_max = band.min(), band.max()
        return ((band - band_min)/(band_max - band_min))

    
    def ProccessRGBCrop(self, lonStart, lonEnd, latStart, latEnd):
        b2MultiReflectance = float(self.b2MultiReflectance)
        b2AddReflectance = float(self.b2AddReflectance)
        b3MultiReflectance = float(self.b3MultiReflectance)
        b3AddReflectance = float(self.b3AddReflectance)
        b4MultiReflectance = float(self.b4MultiReflectance)
        b4AddReflectance = float(self.b4AddReflectance)
        b5MultiReflectance = float(self.b5MultiReflectance)
        b5AddReflectance = float(self.b5AddReflectance)
        b6MultiReflectance = float(self.b6MultiReflectance)
        b6AddReflectance = float(self.b6AddReflectance)
        b7MultiReflectance = float(self.b7MultiReflectance)
        b7AddReflectance = float(self.b7AddReflectance)
        if lonStart == "" and lonEnd == "" and latStart == "" and latEnd == "":
            self.willCroped = False
        else:
            self.willCroped = True

        self.lonStartCrop = lonStart
        self.lonEndCrop = lonEnd
        self.latStartCrop = latStart
        self.latEndCrop = latEnd


        
        if self.GlobSelection == 2 or self.GlobSelection == 5 or self.GlobSelection == 6 or self.GlobSelection == 7 or self.GlobSelection == 8 or self.GlobSelection == 10:
            if self.GlobSelection == 2:
                red_file = self.b6_file
                green_file = self.b5_file
                blue_file = self.b4_file
                red_mult = b6MultiReflectance
                red_add = b6AddReflectance
                green_mult = b5MultiReflectance
                green_add = b5AddReflectance
                blue_mult = b4MultiReflectance
                blue_add = b4AddReflectance

            elif self.GlobSelection == 5:
                red_file = self.b5_file
                green_file = self.b6_file
                blue_file = self.b4_file
                red_mult = b5MultiReflectance
                red_add = b5AddReflectance
                green_mult = b6MultiReflectance
                green_add = b6AddReflectance
                blue_mult = b4MultiReflectance
                blue_add = b4AddReflectance
            
            elif self.GlobSelection == 6:
                red_file = self.b5_file
                green_file = self.b6_file
                blue_file = self.b2_file
                red_mult = b5MultiReflectance
                red_add = b5AddReflectance
                green_mult = b6MultiReflectance
                green_add = b6AddReflectance
                blue_mult = b2MultiReflectance
                blue_add = b2AddReflectance

            elif self.GlobSelection == 7:
                red_file = self.b7_file
                green_file = self.b6_file
                blue_file = self.b5_file
                red_mult = b7MultiReflectance
                red_add = b7AddReflectance
                green_mult = b6MultiReflectance
                green_add = b6AddReflectance
                blue_mult = b5MultiReflectance
                blue_add = b5AddReflectance
            
            elif self.GlobSelection == 8:
                red_file = self.b6_file
                green_file = self.b5_file
                blue_file = self.b2_file
                red_mult = b6MultiReflectance
                red_add = b6AddReflectance
                green_mult = b5MultiReflectance
                green_add = b5AddReflectance
                blue_mult = b2MultiReflectance
                blue_add = b2AddReflectance
            
            elif self.GlobSelection == 9:
                red_file = self.b5_file
                green_file = self.b4_file
                blue_file = self.b3_file
                red_mult = b5MultiReflectance
                red_add = b5AddReflectance
                green_mult = b4MultiReflectance
                green_add = b4AddReflectance
                blue_mult = b3MultiReflectance
                blue_add = b3AddReflectance
            
            elif self.GlobSelection == 10:
                red_file = self.b7_file
                green_file = self.b6_file
                blue_file = self.b4_file
                red_mult = b7MultiReflectance
                red_add = b7AddReflectance
                green_mult = b6MultiReflectance
                green_add = b6AddReflectance
                blue_mult = b4MultiReflectance
                blue_add = b4AddReflectance

            x = self.b6_file
        elif self.GlobSelection == 1 or self.GlobSelection == 3 or self.GlobSelection == 9:
            if self.GlobSelection == 1:
                red_file = self.b4_file
                green_file = self.b3_file
                blue_file = self.b2_file
                red_mult = b4MultiReflectance
                red_add = b4AddReflectance
                green_mult = b3MultiReflectance
                green_add = b3AddReflectance
                blue_mult = b2MultiReflectance
                blue_add = b2AddReflectance
            
            elif self.GlobSelection == 3:
                red_file = self.b7_file
                green_file = self.b5_file
                blue_file = self.b4_file
                red_mult = b7MultiReflectance
                red_add = b7AddReflectance
                green_mult = b5MultiReflectance
                green_add = b5AddReflectance
                blue_mult = b4MultiReflectance
                blue_add = b4AddReflectance

            elif self.GlobSelection == 9:
                red_file = self.b5_file
                green_file = self.b4_file
                blue_file = self.b3_file
                red_mult = b5MultiReflectance
                red_add = b5AddReflectance
                green_mult = b4MultiReflectance
                green_add = b4AddReflectance
                blue_mult = b3MultiReflectance
                blue_add = b3AddReflectance

            x= self.b4_file
        else:
            red_file = self.b7_file
            green_file = self.b5_file
            blue_file = self.b3_file
            red_mult = b7MultiReflectance
            red_add = b7AddReflectance
            green_mult = b5MultiReflectance
            green_add = b5AddReflectance
            blue_mult = b3MultiReflectance
            blue_add = b3AddReflectance
            x = self.b7_file
        print("red",red_file)
        for i in range(len(x)):
            r_link = gdal.Open(red_file[i])
            g_link = gdal.Open(green_file[i])
            b_link = gdal.Open(blue_file[i])
            if self.willCroped:
            # Open each band using gdal
                issue = []
                if self.lonStartCrop < self.lonStartDefault or self.lonStartCrop > self.lonEndDefault:
                    issue.append("Longitude start crop kurang dari limit")
                if self.latStartCrop < self.latStartDefault or self.latStartCrop > self.latEndDefault:
                    issue.append("Latitude start crop kurang dari limit")
                if self.lonEndCrop > self.lonEndDefault or self.lonEndCrop < self.lonStartDefault:
                    issue.append("Longitude end crop melebihi limit")
                if self.latEndCrop > self.latEndDefault or self.latEndCrop < self.latStartDefault:
                    issue.append("Latitude end crop melebihi limit")
                if issue:
                    issueBuf = ""
                    for item in issue:
                        issueBuf += item + "\n"
                        print(issueBuf)
                    issue = []
                    self.listener.showErrorMessage("Crop failed\n\n" + issueBuf) 
                else:
                    self.listener.showProgress()
                    percent = 30
                    self.listener.progress.Update(percent)
                    self.cols = r_link.RasterXSize
                    self.rows = r_link.RasterYSize
                    bands = r_link.RasterCount
                    print("cols: ", self.cols, "\nrows: ", self.rows, "\nbands: ", bands)
                    gt = r_link.GetGeoTransform()
                    x0 = gt[0]
                    y0 = gt[3]
                    pwidth = gt[1]
                    pheight = gt[5]
                    x_end = self.cols * pwidth + x0
                    y_end = self.cols * pheight + y0

                    myProj = Proj("+proj=utm +zone=50, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
                    lon, lat = myProj(x0, y0, inverse=True)
                    x_utm, y_utm = myProj(lon, lat)
                    print("lon: ", lon, "\nlat: ", lat)
                    print("x_utm", x_utm, "\ny_utm", y_utm)

                    x_mulai_crop_utm, y_mulai_crop_utm = myProj(self.lonStartCrop, self.latStartCrop)
                    x_akhir_crop_utm, y_akhir_crop_utm = myProj(self.lonEndCrop, self.latEndCrop)
                    print("x_mulai_crop_utm: ", x_mulai_crop_utm, "\ny_mulai_crop_utm: ", y_mulai_crop_utm, "\nx_akhir_crop_utm: ",
                        x_akhir_crop_utm, "\nx_akhir_crop_utm: ", y_akhir_crop_utm)

                    xoff = int((x_mulai_crop_utm - x0) / pwidth)
                    yoff = int((y_mulai_crop_utm - y0) / pheight)
                    print("xoff: ", xoff, "\nyoff: ", yoff)

                    self.output_cols = int((x_akhir_crop_utm - x_mulai_crop_utm) / pwidth)
                    self.output_rows = int((y_akhir_crop_utm - y_mulai_crop_utm) / pheight)

                    print("output_cols: ", self.output_cols)
                    print("output_rows: ", self.output_rows)

                    band_r = r_link.GetRasterBand(1)
                    band_g = g_link.GetRasterBand(1)
                    band_b = b_link.GetRasterBand(1)

                    cropped_r = band_r.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)
                    cropped_g= band_g.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)
                    cropped_b = band_b.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)
                    print(cropped_r)
                    # call the norm function on each band as array converted to float
                    r = (self.norm(cropped_r.astype(np.float)) * red_mult) + red_add
                    g = (self.norm(cropped_g.astype(np.float)) * green_mult) + green_add
                    b = (self.norm(cropped_b.astype(np.float)) * blue_mult) + blue_add
            
            else :
                self.listener.showProgress()
                percent = 30
                self.listener.progress.Update(percent)
                r = (self.norm(r_link.ReadAsArray().astype(np.float)))
                g = (self.norm(g_link.ReadAsArray().astype(np.float)))
                b = (self.norm(b_link.ReadAsArray().astype(np.float)))
            # Create RGB
            rgb = np.dstack((r,g,b))
            

        self.final_rgb = rgb
        if rgb is not None:
            self.isRGB = True
        else:
            self.isRGB = False
        # rgb_file = "RGB.png"
        # print(rgb_file)
        if self.listener is not None:
            self.listener.OnRGBFinished(rgb, self.GlobSelection)

    
    def ValidateSelection(self, selection):
        
        if selection == 1 : #4-3-2
            if self.b4_file and self.b3_file and self.b2_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False
               
        elif selection == 2: #6-5-4
            if self.b6_file and self.b5_file and self.b4_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False

        elif selection == 3: #7-5-4
            if self.b7_file and self.b5_file and self.b4_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False
        
        elif selection == 4: #7-5-3
            if self.b7_file and self.b5_file and self.b3_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False
               
        elif selection == 5: #5-6-4
            if self.b5_file and self.b6_file and self.b4_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False
        
        elif selection == 6: #5-6-2
            if self.b5_file and self.b6_file and self.b2_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False

        elif selection == 7: #7-6-5
            if self.b7_file and self.b6_file and self.b5_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False
        
        elif selection == 8: #6-5-2
            if self.b6_file and self.b5_file and self.b2_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False
        
        elif selection == 9: #5-4-3
            if self.b5_file and self.b4_file and self.b3_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False
        
        elif selection == 10: #7-6-4
            if self.b7_file and self.b6_file and self.b4_file:
               self.isValidateSelection = True
            else:
                self.isValidateSelection = False

        elif selection==0:
            self.isValidateSelection = False
            
        self.GlobSelection = selection

    def MyListener(self,listener):
        self.listener = listener
    
    def SaveResult(self, path):
        sm.imsave(path, self.final_rgb)
        print ("File created successfully.")
    
class MyListener:
    def OnRGBFinished(self, result, selection):
        print("RGB Finished")

    def showErrorMessage(self, message):
        print("show message error")
    
    def showProgress(self):
        print("show Progress")