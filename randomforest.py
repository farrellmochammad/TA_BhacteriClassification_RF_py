from __future__ import division
from xlrd import open_workbook
import random

#AllVariableStore
value1 = []
value2 = []
value3 = []
value4 = []
value5 = []
value6 = []
value7 = []
value8 = []
valtemp1 = []
valtemp2 = []
valtemp3 = []
valtemp4 = []
valtemp5 = []
valtemp6 = []
valtemp7 = []
valtemp8 = []

wb = open_workbook('dataSetEcoli.xlsx')
#Read File dataSetEcoli.xlsx from file
for s in wb.sheets():
    for i in range(s.nrows):
         value1.append(s.cell(i,1).value)
         value2.append(s.cell(i,2).value)
         value3.append(s.cell(i,3).value)
         value4.append(s.cell(i,4).value)
         value5.append(s.cell(i,5).value)
         value6.append(s.cell(i,6).value)
         value7.append(s.cell(i,7).value)
         value8.append(s.cell(i,8).value)

#Store From Excel to Variable Data
Data = [value1 , value2 , value3 , value4 , value5 , value6 , value7, value8 ]

#To make Index Random
nums = [x for x in range(337)]
random.shuffle(nums)
nums.remove(0)

#make Data swap
for i in range(1,337):
     Data[0][i],Data[0][nums[i-1]] = Data[0][nums[i-1]],Data[0][i]
     Data[1][i], Data[1][nums[i - 1]] = Data[1][nums[i - 1]], Data[1][i]
     Data[2][i], Data[2][nums[i - 1]] = Data[2][nums[i - 1]], Data[2][i]
     Data[3][i], Data[3][nums[i - 1]] = Data[3][nums[i - 1]], Data[3][i]
     Data[4][i], Data[4][nums[i - 1]] = Data[4][nums[i - 1]], Data[4][i]
     Data[5][i], Data[5][nums[i - 1]] = Data[5][nums[i - 1]], Data[5][i]
     Data[6][i], Data[6][nums[i - 1]] = Data[6][nums[i - 1]], Data[6][i]
     Data[7][i], Data[7][nums[i - 1]] = Data[7][nums[i - 1]], Data[7][i]

x = 1
temp = []
subData = []

#Divided Data Into Several Group
while(x!=337):
     if (x % 29 == 0):
          valtemp1 = []
          valtemp2 = []
          valtemp3 = []
          valtemp4 = []
          valtemp5 = []
          valtemp6 = []
          valtemp7 = []
          valtemp8 = []
          valtemp1.append(Data[0][x])
          valtemp2.append(Data[1][x])
          valtemp3.append(Data[2][x])
          valtemp4.append(Data[3][x])
          valtemp5.append(Data[4][x])
          valtemp6.append(Data[5][x])
          valtemp7.append(Data[6][x])
          valtemp8.append(Data[7][x])
     elif(x % 28 == 0):
          valtemp1.append(Data[0][x])
          valtemp2.append(Data[1][x])
          valtemp3.append(Data[2][x])
          valtemp4.append(Data[3][x])
          valtemp5.append(Data[4][x])
          valtemp6.append(Data[5][x])
          valtemp7.append(Data[6][x])
          valtemp8.append(Data[7][x])
          temp = [valtemp1 , valtemp2 , valtemp3 , valtemp4 , valtemp5 , valtemp6 , valtemp7 , valtemp8]
          subData.append(temp)
     else:
          valtemp1.append(Data[0][x])
          valtemp2.append(Data[1][x])
          valtemp3.append(Data[2][x])
          valtemp4.append(Data[3][x])
          valtemp5.append(Data[4][x])
          valtemp6.append(Data[5][x])
          valtemp7.append(Data[6][x])
          valtemp8.append(Data[7][x])
     x += 1









