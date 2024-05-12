#Projekt na cwiczenia z IZS
#Srednie ruchome (Moving Averages):
#>Proste >Wazone   >Eksponencjalne
#>Simple >Weighted >Exponential 
#Do poprawnego dzialania programu wymagane sa biblioteki: 
#>matplotlib >xlwt

import matplotlib.pyplot as plt
from os import system, name 
from time import sleep 
import random
from xlwt import Workbook
x = 0
k = 1
a = 1
b = 1
wb = Workbook()
def main():
    clear()
    print('Projekt IZS')
    print('1.Manualnie')
    print('2.Losowo')
    print('3.Zakoncz')
    op = int(input('Wybierz opcje: '))
    clear()
    if op == 1:
        x = int(input('Wpisz ile danych: '))
        xt = [0]*x
        i = 0
        while i < x:
            xt[i] = int(input())
            i += 1
        clear()
        k = float(input('Wpisz wartosc k =  '))
        clear()
        a = float(input('Wpisz wspolczynnik a =  '))
        clear()
        b = float(input('Wpisz wspolczynnik b =  '))
        clear()
        alfa = float(input('Wpisz wspolczynnik α =  '))
        clear()
        i = 3
        #SMA
        xst = [0]*(x+1)
        xst[0] = 0
        xst[1] = 0
        xst[2] = 0
        Ys = [0]*(x+1)
        Ys[0] = 0
        Ys[1] = 0
        Ys[2] = 0
        #WMA
        xwt = [0]*(x+1)
        xwt[0] = 0
        xwt[1] = 0
        xwt[2] = 0
        Yw = [0]*(x+1)
        Yw[0] = 0
        Yw[1] = 0
        Yw[2] = 0
        #EMA
        xet = [0]*(x+1)
        xet[0] = 0
        xet[1] = 0
        xet[2] = 0
        Ye = [0]*(x+1)
        Ye[0] = 0
        Ye[1] = 0
        Ye[2] = 0
        while i < (x):
            xst[i] = ((xt[i-3] + xt[i-2] + xt[i-1])/3)
            Ys[i] = ((xt[i]-xst[i])/xt[i])
            if Ys[i] < 0:
                Ys[i] = -Ys[i]
            else:
                pass
            xwt[i] = ((xt[i-3] + a*xt[i-2] + b*xt[i-1])/3)
            Yw[i] = ((xt[i]-xwt[i])/xt[i])
            if Yw[i] < 0:
                Yw[i] = -Yw[i]
            else:
                pass
            xet[i] = (alfa*xt[i-1] + (1-alfa)*xet[i-1])
            Ye[i] = ((xt[i]-xet[i])/xt[i])
            if Ye[i] < 0:
                Ye[i] = -Ye[i]
            else:
                pass  
            i += 1
        #SMA
        xst[i] = ((xst[i-2] + xst[i-1])/2)
        Ys[i] = ((Ys[i-2] + Ys[i-1]) / 2)
        #WMA
        xwt[i] = ((xwt[i-2] + xwt[i-1])/2)
        Yw[i] = ((Yw[i-2] + Yw[i-1]) / 2)
        #EMA
        xet[i] = ((xet[i-1] + xet[i-2])/2)
        Ye[i] = ((Ye[i-2] + Ye[i-1]) / 2)
        
        Lp = [0] * (x+1)
        j = 0
        while j < (x+1):
            Lp[j] = (j+1)
            j += 1
        j = 0
        XT = [0]*x
        while j < (x):
            XT[j] = (j+1)
            j += 1
        i = 0
        print('     Xt         SMA            Ψs           WMA           Ψw           EMA           Ψe')
        while i < (x):
            print('|   ',xt[i],'   |   ',"%.2f" % xst[i],'   |   ',"%.2f" % Ys[i],'   |   ',"%.2f" % xwt[i],'   |   ',"%.2f" % Yw[i],'   |   ',"%.2f" % xet[i],'   |   ',"%.2f" % Ye[i],'   |   ')
            i += 1
        print('       ','   |   ',"%.2f" % xst[i],'   |   ',"%.2f" % Ys[i],'   |   ',"%.2f" % xwt[i],'   |   ',"%.2f" % Yw[i],'   |   ',"%.2f" % xet[i],'   |   ',"%.2f" % Ye[i],'   |   ')
        i = 0
        plt.plot(XT,xt,label='Xt')
        plt.plot(Lp,xst,label='SMA')
        plt.plot(Lp,xwt,label='WMA')
        plt.plot(Lp,xet,label='EMA')
        plt.xlabel('Lp')
        plt.ylabel('Wartosc')
        plt.title('Srednie Ruchome:')
        plt.legend()
        plt.show()
        print('Export do Excel?(T/N): ')
        xcl = input()
        if xcl == 'T':
            sheet = wb.add_sheet('Sheet')
            sheet.write(0,0,'Lp')
            sheet.write(0,1,'Xt')
            sheet.write(0,2,'SMA')
            sheet.write(0,3,'Ψs')
            sheet.write(0,4,'WMA')
            sheet.write(0,5,'Ψw')
            sheet.write(0,6,'EMA')
            sheet.write(0,7,'Ψe')
            while i < (x+1):
                sheet.write((i+1),0,Lp[i])
                i += 1
            i = 0
            while i < (x):
                sheet.write((i+1),1,xt[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),2,xst[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),3,Ys[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),4,xwt[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),5,Yw[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),6,xet[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),7,Ye[i])
                i += 1
            i = 0
            wb.save('IZS.xls')
            clear()
        else:
            exit()
    elif op == 2:
        x = int(input('Wpisz ile danych: '))
        xt = [0]*x
        clear()
        k = float(input('Wpisz wartość k =  '))
        clear()
        a = float(input('Wpisz wspolczynnik a =  '))
        clear()
        b = float(input('Wpisz wspolczynnik b =  '))
        clear()
        alfa = float(input('Wpisz wspolczynnik α =  '))
        clear()
        i = 0
        while i < x:
            xt[i] = random.randint(1,101)
            i += 1
        sleep(2)
        i = 3
        #SMA
        xst = [0]*(x+1)
        xst[0] = 0
        xst[1] = 0
        xst[2] = 0
        Ys = [0]*(x+1)
        Ys[0] = 0
        Ys[1] = 0
        Ys[2] = 0
        #WMA
        xwt = [0]*(x+1)
        xwt[0] = 0
        xwt[1] = 0
        xwt[2] = 0
        Yw = [0]*(x+1)
        Yw[0] = 0
        Yw[1] = 0
        Yw[2] = 0
        #EMA
        xet = [0]*(x+1)
        xet[0] = 0
        xet[1] = 0
        xet[2] = 0
        Ye = [0]*(x+1)
        Ye[0] = 0
        Ye[1] = 0
        Ye[2] = 0
        while i < (x):
            xst[i] = ((xt[i-3] + xt[i-2] + xt[i-1])/3)
            Ys[i] = ((xt[i]-xst[i])/xt[i])
            if Ys[i] < 0:
                Ys[i] = -Ys[i]
            else:
                pass
            xwt[i] = ((xt[i-3] + a*xt[i-2] + b*xt[i-1])/3)
            Yw[i] = ((xt[i]-xwt[i])/xt[i])
            if Yw[i] < 0:
                Yw[i] = -Yw[i]
            else:
                pass
            xet[i] = (alfa*xt[i-1] + (1-alfa)*xet[i-1])
            Ye[i] = ((xt[i]-xet[i])/xt[i])
            if Ye[i] < 0:
                Ye[i] = -Ye[i]
            else:
                pass  
            i += 1
        #SMA
        xst[i] = ((xst[i-2] + xst[i-1])/2)
        Ys[i] = ((Ys[i-2] + Ys[i-1]) / 2)
        #WMA
        xwt[i] = ((xwt[i-2] + xwt[i-1])/2)
        Yw[i] = ((Yw[i-2] + Yw[i-1]) / 2)
        #EMA
        xet[i] = ((xet[i-1] + xet[i-2])/2)
        Ye[i] = ((Ye[i-2] + Ye[i-1]) / 2)
        
        Lp = [0] * (x+1)
        j = 0
        while j < (x+1):
            Lp[j] = (j+1)
            j += 1
        j = 0
        XT = [0]*x
        while j < (x):
            XT[j] = (j+1)
            j += 1
        i = 0
        print('     Xt         SMA            Ψs           WMA           Ψw           EMA           Ψe')
        while i < (x):
            print('|   ',xt[i],'   |   ',"%.2f" % xst[i],'   |   ',"%.2f" % Ys[i],'   |   ',"%.2f" % xwt[i],'   |   ',"%.2f" % Yw[i],'   |   ',"%.2f" % xet[i],'   |   ',"%.2f" % Ye[i],'   |   ')
            i += 1
        print('       ','   |   ',"%.2f" % xst[i],'   |   ',"%.2f" % Ys[i],'   |   ',"%.2f" % xwt[i],'   |   ',"%.2f" % Yw[i],'   |   ',"%.2f" % xet[i],'   |   ',"%.2f" % Ye[i],'   |   ')
        i = 0
        plt.plot(XT,xt,label='Xt')
        plt.plot(Lp,xst,label='SMA')
        plt.plot(Lp,xwt,label='WMA')
        plt.plot(Lp,xet,label='EMA')
        plt.xlabel('Lp')
        plt.ylabel('Wartosc')
        plt.title('Srednie Ruchome:')
        plt.legend()
        plt.show()
        print('Export do Excel?(T/N): ')
        xcl = input()
        if xcl == 'T':
            sheet = wb.add_sheet('Sheet')
            sheet.write(0,0,'Lp')
            sheet.write(0,1,'Xt')
            sheet.write(0,2,'SMA')
            sheet.write(0,3,'Ψs')
            sheet.write(0,4,'WMA')
            sheet.write(0,5,'Ψw')
            sheet.write(0,6,'EMA')
            sheet.write(0,7,'Ψe')
            while i < (x+1):
                sheet.write((i+1),0,Lp[i])
                i += 1
            i = 0
            while i < (x):
                sheet.write((i+1),1,xt[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),2,xst[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),3,Ys[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),4,xwt[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),5,Yw[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),6,xet[i])
                i += 1
            i = 0
            while i < (x+1):
                sheet.write((i+1),7,Ye[i])
                i += 1
            i = 0
            wb.save('IZS.xls')
            clear()

        else:
            exit()
    elif op == 3:
        exit()
    else:
        print('blad')
        sleep(2)
        clear()

def clear(): 
    #windows 
    if name == 'nt': 
        _ = system('cls') 
    #mac and linux 
    else: 
        _ = system('clear') 

main()
