import os, shutil, datetime

now = datetime.datetime.now()
monthDict={1:'Januar', 2:'Februar', 3:'Mart', 4:'April', 5:'Maj', 6:'Jun', 7:'Jul', 8:'Avgust', 9:'Septembar', 10:'Oktobar', 11:'Novembar', 12:'Decembar'}
#print(now.month)
#print(monthDict[now.month])
if now.day == 1:
    os.makedirs('C:\\Users\\Boris\\Desktop\\Journal\\{0}\\{1}'.format(now.year,monthDict[now.month]))
    if now.day == 1 and now.month == 1:
         os.makedirs('C:\\Users\\Boris\\Desktop\\Journal\\{0}'.format(now.year))
                

for filename in os.listdir(r'C:\Users\Boris\Desktop'):
    if filename == 'dnevnik.txt':
        newName = str(now.day) + '-' + str(now.month) + '.txt'
        shutil.move('C:\\Users\\Boris\\Desktop\\{0}'.format(filename),'C:\\Users\\Boris\\Desktop\\Journal\\{0}\\{1}\\{2}'.format(now.year,monthDict[now.month],newName))

