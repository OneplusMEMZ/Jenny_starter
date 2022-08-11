#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 
def Form_1_onLoad(uiName):
    pass
def Button_3_onCommand(uiName,widgetName):
    sys.exit()
def Button_9_onCommand(uiName,widgetName):
    os.system(r".\CMCL.exe -account -l -o Jenny_starter_user -s")
    os.system(r".\CMCL.exe -b Jenny_starter")
def Button_17_onCommand(uiName,widgetName):
    import webbrowser
    webbrowser.open("https://github.com/MrShieh-X")
def Button_19_onCommand(uiName,widgetName):
    import webbrowser
    webbrowser.open("https://github.com/OneplusMEMZ")
def Button_20_onCommand(uiName,widgetName):
    import webbrowser
    webbrowser.open("https://gitee.com/MrShiehX")
def Button_26_onCommand(uiName,widgetName):
    import webbrowser
    webbrowser.open("https://jq.qq.com/?_wv=1027&k=9Dm0Bhnm")
def Button_27_onCommand(uiName,widgetName):
    import webbrowser
    webbrowser.open("https://github.com/honghaier-game")

