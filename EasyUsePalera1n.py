# coding: UTF-8
Appname = "EtUPalera1n v1.0"
Developer = "@wakanameko2"
Version= 'version1.0'
SPThanks = 'https://github.com/palera1n/palera1n (Palera1n_Team)'
import tkinter as tk
import webbrowser
import platform
import os
import subprocess
from subprocess import PIPE
import sys
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

ur = platform.uname()
print(ur.system)
print(ur.release)
print(ur.version)
print(ur.processor)
print(Appname)
print(Developer)
print(SPThanks)

if not ur.system == 'Darwin':messagebox.showerror('Attention','Mac以外のPCでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')

#MainWindow
MainWindow = tk.Tk()
MainWindow.geometry('400x200')
MainWindow.resizable(width = False, height = False)
MainWindow.title(Appname)
Menubaa = tk.Menu(MainWindow) 
MainWindow.config(menu=Menubaa)
#窓数制限
DeviceInfoWindow = None

def exitPale():
    exit()

def PPalera1n():
    global DeviceInfoWindow
    if DeviceInfoWindow == None or not DeviceInfoWindow.winfo_exists():
        print('処理を開始します。')
        print("デバイスを検索中...")
        os.system("ideviceinfo > device_info.txt")
        Dinfo = open("device_info.txt", "r")
        fileData = Dinfo.read()
        #Reading Device_Name
        start0 = 'DeviceName: '
        end0 = 'DieID:'
        s0 = str(fileData)
        foundData0 = s0[s0.find(start0)+len(start0):s0.rfind(end0)]
        deviceName = str(foundData0)
        LAST_CONNECTED_IOS_VER = str(deviceName)
        #Reading iOS_Version
        start = 'ProductVersion: '
        end = 'ProductionSOC:'
        s = str(fileData)
        foundData = s[s.find(start)+len(start):s.rfind(end)]
        deviceIOS = str(foundData)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)
        print('デバイス情報を取得しました')
        print(f"{deviceName} {deviceIOS}")
        DeviceInfoWindow = tk.Toplevel()
        DeviceInfoWindow.geometry("300x100")
        DeviceInfoWindow.resizable(width = False, height = False)
        DVIF = tk.Label(DeviceInfoWindow, text = (f"DeviceName: {deviceName}iOS Version: {deviceIOS}"))
        DVIF.pack(expand = True)
        if deviceIOS < '15':
            NOTSUPPORT = tk.Label(DeviceInfoWindow, text = ('このバージョンには対応していません。'))
            NOTSUPPORT.pack(expand = True)
        else:
            pass
        Dinfo.close()
        def CDIW():
            DeviceInfoWindow.destroy()
        CloseDIW = tk.Button(DeviceInfoWindow, text = ('Close'), command = CDIW, width = 9)
        CloseDIW.pack(expand = True)

def SetupPalera1n():
    print('処理を開始します。')
    proc = subprocess.run("git clone --recursive https://github.com/palera1n/palera1n && cd palera1n", shell=True, stdout=PIPE, stderr=PIPE, text=True)
    Palera1nInst = proc.stdout
    print(Palera1nInst)
    print('処理が終了しました。')

def UninstPalera1n():
    print('処理を開始します。')
    proc = subprocess.run("cd Palera1n", shell=True, stdout=PIPE, stderr=PIPE, text=True)
    proc = subprocess.run("rm -rf palera1n", shell=True, stdout=PIPE, stderr=PIPE, text=True)
    Palera1nUnst = proc.stdout
    print(Palera1nUnst)
    print('処理が終了しました。')

def JBNow():
    print('処理を開始します。')
    print("デバイスを検索中...")
    os.system("ideviceinfo > device_info.txt")
    Dinfo = open("device_info.txt", "r")
    fileData = Dinfo.read()
    print('デバイス情報を取得しました')
    print(fileData)
    proc = subprocess.run("palera1n.sh")
    pass

def openGHP():
    webbrowser.open('https://github.com/palera1n/palera1n')

def openGHU():
    webbrowser.open('https://github.com/wakanameko/Easy-to-Use-Palera1n')

def About():
    pass

def insthb():
    print('処理を開始します。')
    #proc = subprocess.run("/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"",shell=True, stdout=PIPE, stderr=PIPE, text=True)
    #HBInst = proc.stdout
    #print(HBInst)
    print('処理が完了しました。')

def instpy3():
    pass

def instpyimg4():
    print('処理を開始します。')
    proc = subprocess.run("python3 -m pip install pyimg4", shell=True, stdout=PIPE, stderr=PIPE, text=True)
    Pyimg4Inst = proc.stdout
    print(Pyimg4Inst)
    print('処理が終了しました。')

menu_file = tk.Menu(MainWindow)
Menubaa.add_cascade(label='EtUPalera1n', menu=menu_file)
menu_file.add_command(label='Connect_iDevice', command=PPalera1n)
menu_file.add_separator()  
menu_file.add_command(label='SetupPalera1n', command=SetupPalera1n)
menu_file.add_command(label='UninstallPalera1n', command=UninstPalera1n) 
menu_file.add_separator() 
menu_file.add_command(label='Jailbreak_Now', command=JBNow)
menu_file.add_separator() 
menu_file.add_command(label='exit', command=exitPale)

menu_py = tk.Menu(MainWindow)
Menubaa.add_cascade(label='Installers', menu=menu_py)
menu_py.add_command(label='Homebrew', command=insthb)
menu_py.add_command(label='Python3(3.11.0)', command=instpy3)
menu_py.add_command(label='Pyimg4', command=instpyimg4)

menu_GitHub = tk.Menu(MainWindow)
Menubaa.add_cascade(label='GitHub', menu=menu_GitHub)
menu_GitHub.add_command(label='Palera1n', command=openGHP)
menu_GitHub.add_command(label='EtUPalera1n', command=openGHU)

menu_about = tk.Menu(MainWindow)
Menubaa.add_cascade(label='about', menu=menu_about)
menu_about.add_command(label='about', command=About)
menu_about.add_command(label=Version)

button_pair = tk.Button(MainWindow, text = "Connect_iDevice", command = PPalera1n, width = 9)
button_setupp = tk.Button(MainWindow, text = "Setup_Palera1n", command = SetupPalera1n, width = 9)
button_jbnow = tk.Button(MainWindow, text = "Jailbreak_Now", command = JBNow, width = 9)
button_openGH = tk.Button(MainWindow, text = "GitHub(Palera1n)", command = openGHP, width = 9)
Label_wlcm = tk.Label(MainWindow, text = 'Welcome to Easy to Use Palera1n!', font = ("normal", 18, "bold"))
Label_inst = tk.Label(MainWindow, text = 'オプションを選択してください。')
#Layout
Label_wlcm.pack()
button_pair.pack(expand = True)
button_setupp.pack(expand = True)
button_jbnow.pack(expand = True)
button_openGH.pack(expand = True)
Label_inst.pack()

MainWindow.mainloop()