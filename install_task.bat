@echo off

schtasks /create /tn "BWOverTime" /tr "C:\Python\python.exe C:\speed\measure_speed.py" /sc minute /mo 20
