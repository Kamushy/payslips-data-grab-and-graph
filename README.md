# Final Product
### MatPlotLib Graphs 
![alt text](https://github.com/Kamushy/Deputy-payslips-data-grab-and-graph/blob/main/Graphs.jpg?raw=true)
### Excel document created without effort
![alt text](https://github.com/Kamushy/Deputy-payslips-data-grab-and-graph/blob/main/Excel%20document.jpg?raw=true)
# How to setup
### Download packets
```ruby
pip install datetime
```
```ruby
pip install tika
```
```ruby
pip install numpy
```
```ruby
pip install matplotlib
```
```ruby
pip install xlsxwriter
```
### Create Folders
- Create a folder called 'files'
- Create a folder called 'organisedpdfs'

### Put paths
- Inside finddate() function
```python
#Keep the r at the start of each path
#add the path of your 'files' folder on line 29 within qoutes
folder = os.listdir(r'C:\Users\your\file\path')

for file in folder:
    #add the path of your 'files' folder on line 32 within qoutes DO NOT REPLACE AFTER THE + 
    filething = str(r'C:\Users\your\file\path' + f'\{file}')
```

- Around getinfo() funciton
```python
#Keep the r at the start of each path
#add the path of your 'organisedpdfs' folder on line 87 within qoutes

def getinfo():
    global sundaypay, week, saturdaypay, saturdayhours, weekpay, weekhours, holidayhours, holidaypay, totalpay, totalhours
    #change this line below
    locationorganised = os.listdir(r'C:\Users\your\file\path\organised')
    for file in sorted(locationorganised)
        #add the path of your 'organisedpdfs' folder on line 89 within qoutes AGAIN please keep the r
        toopenfile = (r'C:\Users\your\file\path\organised' + file)
```
