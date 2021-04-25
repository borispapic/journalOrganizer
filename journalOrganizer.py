import os, shutil, datetime

JOURNAL_PATH= "D:\\PRIV\\Journal"
now = datetime.datetime.now()
monthDict={1:'Januar', 2:'Februar', 3:'Mart', 4:'April', 5:'Maj', 6:'Jun', 7:'Jul', 8:'Avgust', 9:'Septembar', 10:'Oktobar', 11:'Novembar', 12:'Decembar'}
#print(now.month)
#print(monthDict[now.month])
if os.path.exists(f"{JOURNAL_PATH}\\{now.year}\\{now.month}") == False:
    #os.makedirs('C:\\Users\\Boris\\Desktop\\Journal\\{0}\\{1}'.format(now.year,monthDict[now.month]))
    os.makedirs(f"{JOURNAL_PATH}\\{now.year}\\{monthDict[now.month]}")
                
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
for filename in os.listdir(desktop):
    if filename == 'dnevnik.txt':
        newName = str(now.day) + '-' + str(now.month) + '.txt'
        shutil.move(f"{desktop}\\{filename}",f"{JOURNAL_PATH}\\{now.year}\\{monthDict[now.month]}\\{newName}")
