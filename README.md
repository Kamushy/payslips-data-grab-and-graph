# Deputy-payslips-data-grab-and-graph
Get data from your deputy pay slips and turn them into graphs and copyable data

# Deputy-Payslip-Data-Graphing
Get Deputy payslips into graph and printed data.

## How to setup
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
### Create Folders
- Create a folder called 'files'
- Create a folder called 'organisedpdfs'

### Put paths
- Inside finddate() function
```python
#Keep the r
#add the path of your 'files' folder on line 29 within qoutes
folder = os.listdir(r'C:\Users\your\file\path')

for file in folder:
    #add the path of your 'files' folder on line 32 within qoutes DO NOT REPLACE AFTER THE + 
    filething = str(r'C:\Users\your\file\path' + f'\{file}')
```
