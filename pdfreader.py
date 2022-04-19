import os
from datetime import *
import shutil
from tika import parser
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np

dates = {}
week = 0 
filenumber = 0 
backslash = "\\"

sundaypay = {}
sundayhours = {}

saturdaypay = {}
saturdayhours = {}

weekpay = {}
weekhours = {}

holidaypay = {}
holidayhours = {}

def finddate():
    global dates, filething, folder   
    #path to folder
    folder = os.listdir(r'C:\Users\your\file\path')
    for file in folder:
        #add the file name onto the path
        filething = str(r'C:\Users\your\file\path' + f'\{file}')
        #get raw data from file
        raw = parser.from_file(filething)
        alldata = raw['content']
        #split the pdf
        alldata = alldata.split()
        #get the 25th line which has the date
        rightline = alldata[25]
        #add the line and file name to array e.g. 04/04/2022: C:file.py
        dates[rightline] = filething    


def orderpdf():
    global dates, ordereddate, folder, filenumber, backslash
    #makes a folder
    try:
        os.mkdir('organisedpdfs')
    except:
        #make it completly remove the folder for the future
        print("organisedpdf folder already exists")

    #sorts list of dates           
    ordereddate = OrderedDict(sorted(dates.items(), key = lambda x:datetime.strptime(x[0], '%d/%m/%Y')))
    #for item in dictionary
    for key, value in ordereddate.items():
        #add 1 to file number so files can be ordered by numbers
        filenumber = int(filenumber)
        filenumber = filenumber + 1
        filenumber = str(filenumber)
        zeroLeading = filenumber.zfill(4)
        #gets the orignal value
        valueold = value
        #replaces where the files in past where from and changes it to new directory
        valuenew = value.replace("files", "organisedpdfs")
        #reverses the new value
        reversednew = valuenew[::-1]
        #finds the index of the last backslash   
        char = reversednew.index(backslash)
        #gets the filename after the .pdf
        removing = reversednew[4:char]
        #reversed the reversed to get it back to normal
        removing = removing[::-1]
        #replaces the filename with a number so it can used earlier in the future
        valuenew = valuenew.replace(removing, str(zeroLeading))
        #copys file into new location
        shutil.copyfile(valueold, valuenew)
    print("files are now ordered and in place")

totalpay = {}
totalhours = {}

locationorganised = os.listdir(r'C:\Users\your\file\path\organised')
def getinfo():
    global sundaypay, week, saturdaypay, saturdayhours, weekpay, weekhours, holidayhours, holidaypay, totalpay, totalhours
    for file in sorted(locationorganised):
        toopenfile = (r'C:\Users\your\file\path\organised' + file)
        raworganised = parser.from_file(toopenfile)
        allData = raworganised['content']
        #split the pdf
        allData = allData.split()\
        #adds to week
        week = week + 1
        saturdayhours[week] = 0
        saturdaypay[week] = 0
        sundayhours[week] = 0
        sundaypay[week] = 0
        weekpay[week] = 0
        weekhours[week] = 0
        holidayhours[week] = 0
        holidaypay[week] = 0
        totalhours[week] = 0 
        totalpay[week] = 0

        #for line in file
        for i in allData: 
            #gets index
            i2 = allData.index(i)
            if i == "Sunday":
                #adds 4 to index which is the location of pay
                sundayPayindex = i2 + 4
                if allData[sundayPayindex] == "Wages":
                    sundaypay[week] = 0
                    totalpay[week] + 0
                    break
                sundaypay[week] = allData[sundayPayindex]
                bruh = allData[sundayPayindex].replace("$", "")
                totalpay[week] = totalpay[week] + float(round(float(bruh), 2))
                sundayHourindex = i2 + 2
                sundayhours[week] = float(allData[sundayHourindex])
                totalhours[week] = totalhours[week] + float(allData[sundayHourindex])
                
            elif i == "Saturday":
                #adds 4 to index which is the location of pay
                saturdayPayindex = i2 + 4
                if allData[saturdayPayindex] == "Wages":
                    saturdaypay[week] = 0
                    totalpay[week] + 0
                    break
                saturdaypay[week] = allData[saturdayPayindex]
                bruh =  allData[saturdayPayindex].replace("$", "")           
                totalpay[week] = totalpay[week] + float(round(float(bruh), 2))
                saturdayHourindex = i2 + 2
                saturdayhours[week] = float(allData[saturdayHourindex])
                totalhours[week] = totalhours[week] + float(allData[saturdayHourindex])
                
            elif i == "W/day":
                #adds 4 to index which is the location of pay
                weekPayindex = i2 + 4
                if allData[weekPayindex] == "Wages":
                    weekpay[week] = 0
                    totalpay[week] + 0
                    break
                weekpay[week] = allData[weekPayindex]
                bruh = allData[weekPayindex].replace("$", "")  
                totalpay[week] = totalpay[week] + float(round(float(bruh), 2))
                weekPayindex = i2 +2
                weekhours[week] = float(allData[weekPayindex])
                totalhours[week] = totalhours[week] + float(allData[weekPayindex])
                
            elif i == "P/Holiday":
                #adds 4 to index which is the location of pay
                holidayPayindex = i2 + 4
                if allData[holidayPayindex] == "Wages":
                    holidaypay[week] = 0
                    totalpay[week] + 0
                    break
                holidaypay[week] = allData[holidayPayindex]
                bruh = allData[holidayPayindex].replace("$", "")
                totalpay[week] = totalpay[week] + float(round(float(bruh), 2))
                holidayPayindex = i2 + 2
                holidayhours[week] = float(allData[holidayPayindex])
                totalhours[week] = totalhours[week] + float(allData[holidayPayindex])
                

def removedollar():
    for key, value in sundaypay.items():
        value = str(value)
        if "$" in value:
            value = value.replace("$", "")
            value = float(value)
            sundaypay[key] = round(value)
        else:
            pass
    
    for key, value in saturdaypay.items():
        value = str(value)
        if "$" in value:
            value = value.replace("$", "")
            value = float(value)
            saturdaypay[key] = round(value)
        else:
            pass

    for key, value in weekpay.items():
        value = str(value)
        if "$" in value:
            value = value.replace("$", "")
            value = float(value)
            weekpay[key] = round(value)
        else:
            pass
    
    for key, value in holidaypay.items():
        value = str(value)
        if "$" in value:
            value = value.replace("$", "")
            value = float(value)
            holidaypay[key] = round(value)   
        else:
            pass
    
    for key, value in totalpay.items():
        value = float(value)
        totalpay[key] = round(value)
    
    for key, value in totalhours.items():
        value = float(value)
        totalhours[key] = round(value)

    for key, value in weekhours.items():
        value = float(value)
        weekhours[key] = round(value)

    for key, value in sundayhours.items():
        value = float(value)
        sundayhours[key] = round(value)
    
    for key, value in saturdayhours.items():
        value = float(value)
        saturdayhours[key] = round(value)

def graphing():

    plt.figure(1)
    plt.bar(*zip(*sundaypay.items()), label="Pay")
    plt.bar(*zip(*sundayhours.items()), label='Hours')
    plt.xlabel('Week Number')
    plt.ylabel('Pay(In AUD)')
    plt.title('Sunday Pay')
    plt.yticks([ 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185])
    plt.grid(color='#95a5a6', linestyle='-', linewidth=1, axis='y', alpha=0.5)
    x = np.arange(1, week+1, 1)
    plt.xticks(x)
    plt.legend()

    plt.figure(2)
    plt.bar(*zip(*weekpay.items()), label="Pay")
    plt.bar(*zip(*weekhours.items()), label='Hours')
    plt.xlabel('Week Number')
    plt.ylabel('Pay(In AUD)')
    plt.title('Weekday Pay')
    plt.yticks([ 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205])
    plt.grid(color='#95a5a6', linestyle='-', linewidth=1, axis='y', alpha=0.5)
    x = np.arange(1, week+1, 1)
    plt.xticks(x)
    plt.legend()

    plt.figure(3)
    plt.bar(*zip(*saturdaypay.items()), label="Pay") 
    plt.bar(*zip(*saturdayhours.items()), label='Hours')
    plt.xlabel('Week Number')
    plt.ylabel('Pay(In AUD)')
    plt.title('Saturday Pay')
    plt.yticks([ 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175])
    plt.grid(color='#95a5a6', linestyle='-', linewidth=1, axis='y', alpha=0.5)
    x = np.arange(1, week+1, 1)
    plt.xticks(x)
    plt.legend()

    plt.figure(4)
    plt.bar(*zip(*holidaypay.items()), label="Pay")
    plt.bar(*zip(*holidayhours.items()), label='Hours')
    plt.xlabel('Week Number')
    plt.ylabel('Pay(In AUD)')
    plt.title('Holiday Pay')
    plt.yticks([ 5, 25,  45,  65,  85,  105,  125,  145,  165,  185, 205, 225, 245, 265])
    plt.grid(color='#95a5a6', linestyle='-', linewidth=1, axis='y', alpha=0.5)
    x = np.arange(1, week+1, 1)
    plt.xticks(x)
    plt.legend()

    plt.figure(5)
    plt.bar(*zip(*totalpay.items()), label="Pay")
    plt.bar(*zip(*totalhours.items()), label='Hours')
    plt.xlabel('Week Number')
    plt.ylabel('Pay(In AUD)')
    plt.title('All time Pay')
    plt.yticks([ 50, 100,  150,  200,  250,  300,  350,  400,  450,  500, 550])
    plt.grid(color='#95a5a6', linestyle='-', linewidth=1, axis='y', alpha=0.5)
    x = np.arange(1, week+1, 1)
    plt.xticks(x)
    plt.legend()
    plt.show()
    
    
finddate()
orderpdf()
getinfo()
removedollar()
graphing()

print(f"sundaypay: {sundaypay}")
print(f"saturdaypay: {saturdaypay}")
print(f"sundayhour: {sundayhours}")
print(f"saturday hour: {saturdayhours}")
print(f"weekday hour: {weekhours}")
print(f"weekday pay: {weekpay}")
print(f"holiday pay: {holidaypay}")
print(f"holiday hours: {holidayhours}")
print(f"total pay: {totalpay}")
print(f"total hours: {totalhours}")
