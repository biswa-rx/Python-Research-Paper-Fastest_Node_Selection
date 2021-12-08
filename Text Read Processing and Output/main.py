import xlsxwriter
import os
import test
from time import sleep


idname = test.node_id
label = test.node_label
Country = test.node_country
Longitude = test.node_longitude
Latitude = test.node_latitude
FinalDistance = test.distance_from_cn


#print(FinalDistance)
# idname = [1, 2, 3, 4, 5]
# label = ["tanmay", "biswa", "om", "Sachin", "Surya"]
# Country = ["india", "india", "nepal", "bhutan", "india"]
# Longitude = [75.236, 52.421, 58.369, 12.458, 75.123]
# Latitude = [45.256, 58.236, 75.214, 52.856, 12.458]
# FinalDistance = [1, 2, 3, 4, 5, 6]

if os.path.exists("First.xlsx"):
    os.remove("First.xlsx")

wb = xlsxwriter.Workbook('First.xlsx')
bold = wb.add_format({'bold': True})

ws = wb.add_worksheet('Main data base')
wse = wb.add_worksheet('East')
wsw = wb.add_worksheet('West')
wsn = wb.add_worksheet('North')
wss = wb.add_worksheet('South')



ws.write('A1', 'ID Name')
ws.write('B1', 'Lable')
ws.write('C1', 'Country')
ws.write('D1', 'Latitude (° N)')
ws.write('E1', 'Longitude (° S)')
ws.write('F1', 'Distance from Central Node (K.M)')

wse.write('A1', 'ID Name')
wse.write('B1', 'Lable')
wse.write('C1', 'Country')
wse.write('D1', 'Latitude (° N)')
wse.write('E1', 'Longitude (° S)')
wse.write('F1', 'Distance from Central Node (K.M)')

wsw.write('A1', 'ID Name')
wsw.write('B1', 'Lable')
wsw.write('C1', 'Country')
wsw.write('D1', 'Latitude (° N)')
wsw.write('E1', 'Longitude (° S)')
wsw.write('F1', 'Distance from Central Node (K.M)')

wsn.write('A1', 'ID Name')
wsn.write('B1', 'Lable')
wsn.write('C1', 'Country')
wsn.write('D1', 'Latitude (° N)')
wsn.write('E1', 'Longitude (° S)')
wsn.write('F1', 'Distance from Central Node (K.M)')

wss.write('A1', 'ID Name')
wss.write('B1', 'Lable')
wss.write('C1', 'Country')
wss.write('D1', 'Latitude (° N)')
wss.write('E1', 'Longitude (° S)')
wss.write('F1', 'Distance from Central Node (K.M)')

size = len(Country)
size = size + 1
b = 1
flag = 0
record = 0
a = ' '

for i in range(b, size):
    # print(a, idname[i - 1])

    if idname[i - 1].isspace():
        flag += 1
        record = i
        i += 1

    if flag == 0:
        a = "A" + str(i + 1 - record)
        ws.write(a, idname[(i - 1)])
        if idname[(i - 1)] == '0':
            ws.write(a, idname[(i - 1)],bold)

    elif flag == 1:
        a = "A" + str(i + 1 - record)
        wse.write(a, idname[(i - 1)])
        if idname[(i - 1)] == '0':
            wse.write(a, idname[(i - 1)],bold)

    elif flag == 2:
        a = "A" + str(i + 1 - record)
        wsw.write(a, idname[(i - 1)])
        if idname[(i - 1)] == '0':
            wsw.write(a, idname[(i - 1)],bold)

    elif flag == 3:
        a = "A" + str(i + 1 - record)
        wsn.write(a, idname[(i - 1)])
        if idname[(i - 1)] == '0':
            wsn.write(a, idname[(i - 1)],bold)

    elif flag == 4:
        a = "A" + str(i + 1 - record)
        wss.write(a, idname[(i - 1)])
        if idname[(i - 1)] == '0':
            wss.write(a, idname[(i - 1)],bold)

#Label ws swicher

b = 1
flag = 0
record = 0
a = ' '

for i in range(b, size):
    #print(a, idname[i - 1])

    if idname[i - 1].isspace():
        flag += 1
        record = i
        i += 1

    if flag == 0:
        a = "B" + str(i + 1 - record)
        ws.write(a, label[(i - 1)])
        if idname[(i - 1)] == '0':
            ws.write(a, label[(i - 1)], bold)

    elif flag == 1:
        a = "B" + str(i + 1 - record)
        wse.write(a, label[(i - 1)])
        if idname[(i - 1)] == '0':
            wse.write(a, label[(i - 1)], bold)

    elif flag == 2:
        a = "B" + str(i + 1 - record)
        wsw.write(a, label[(i - 1)])
        if idname[(i - 1)] == '0':
            wsw.write(a, label[(i - 1)], bold)

    elif flag == 3:
        a = "B" + str(i + 1 - record)
        wsn.write(a, label[(i - 1)])
        if idname[(i - 1)] == '0':
            wsn.write(a, label[(i - 1)], bold)

    elif flag == 4:
        a = "B" + str(i + 1 - record)
        wss.write(a, label[(i - 1)])
        if idname[(i - 1)] == '0':
            wss.write(a, label[(i - 1)], bold)


#Country ws swicher

b = 1
flag = 0
record = 0
a = ' '

for i in range(b, size):
    #print(a, idname[i - 1])

    if idname[i - 1].isspace():
        flag += 1
        record = i
        i += 1

    if flag == 0:
        a = "C" + str(i + 1 - record)
        ws.write(a, Country[(i - 1)])
        if idname[(i - 1)] == '0':
            ws.write(a, Country[(i - 1)], bold)

    elif flag == 1:
        a = "C" + str(i + 1 - record)
        wse.write(a, Country[(i - 1)])
        if idname[(i - 1)] == '0':
            wse.write(a, Country[(i - 1)], bold)

    elif flag == 2:
        a = "C" + str(i + 1 - record)
        wsw.write(a, Country[(i - 1)])
        if idname[(i - 1)] == '0':
            wsw.write(a, Country[(i - 1)], bold)

    elif flag == 3:
        a = "C" + str(i + 1 - record)
        wsn.write(a, Country[(i - 1)])
        if idname[(i - 1)] == '0':
            wsn.write(a, Country[(i - 1)], bold)

    elif flag == 4:
        a = "C" + str(i + 1 - record)
        wss.write(a, Country[(i - 1)])
        if idname[(i - 1)] == '0':
            wss.write(a, Country[(i - 1)], bold)


# Latitude ws swicher

b = 1
flag = 0
record = 0
a = ' '

for i in range(b, size):
    #print(a, idname[i - 1])

    if idname[i - 1].isspace():
        flag += 1
        record = i
        i += 1

    if flag == 0:
        a = "D" + str(i + 1 - record)
        Latitude[i - 1] = str(Latitude[i - 1])
        ws.write(a, Latitude[(i - 1)])
        if idname[(i - 1)] == '0':
            ws.write(a, Latitude[(i - 1)], bold)

    elif flag == 1:
        a = "D" + str(i + 1 - record)
        Latitude[i - 1] = str(Latitude[i - 1])
        wse.write(a, Latitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wse.write(a, Latitude[(i - 1)], bold)

    elif flag == 2:
        a = "D" + str(i + 1 - record)
        Latitude[i - 1] = str(Latitude[i - 1])
        wsw.write(a, Latitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wsw.write(a, Latitude[(i - 1)], bold)

    elif flag == 3:
        a = "D" + str(i + 1 - record)
        Latitude[i - 1] = str(Latitude[i - 1])
        wsn.write(a, Latitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wsn.write(a, Latitude[(i - 1)], bold)

    elif flag == 4:
        a = "D" + str(i + 1 - record)
        Latitude[i - 1] = str(Latitude[i - 1])
        wss.write(a, Latitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wss.write(a, Latitude[(i - 1)], bold)

# for i in range(b, size):
#     a = "D" + str(i + 1)
#     if Longitude[i - 1] != ' ':
#         Longitude[i - 1] = str(Longitude[i - 1])+"° N"
#     print(a, Longitude[i - 1])
#     ws.write(a, Longitude[i - 1])

# Longitude ws swicher

b = 1
flag = 0
record = 0
a = ' '

for i in range(b, size):
    #print(a, idname[i - 1])

    if idname[i - 1].isspace():
        flag += 1
        record = i
        i += 1

    if flag == 0:
        a = "E" + str(i + 1 - record)
        Longitude[i - 1] = str(Longitude[i - 1])
        ws.write(a, Longitude[(i - 1)])
        if idname[(i - 1)] == '0':
            ws.write(a, Longitude[(i - 1)], bold)

    elif flag == 1:
        a = "E" + str(i + 1 - record)
        Longitude[i - 1] = str(Longitude[i - 1])
        wse.write(a, Longitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wse.write(a, Longitude[(i - 1)], bold)

    elif flag == 2:
        a = "E" + str(i + 1 - record)
        Longitude[i - 1] = str(Longitude[i - 1])
        wsw.write(a, Longitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wsw.write(a, Longitude[(i - 1)], bold)

    elif flag == 3:
        a = "E" + str(i + 1 - record)
        Longitude[i - 1] = str(Longitude[i - 1])
        wsn.write(a, Longitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wsn.write(a, Longitude[(i - 1)], bold)

    elif flag == 4:
        a = "E" + str(i + 1 - record)
        Longitude[i - 1] = str(Longitude[i - 1])
        wss.write(a, Longitude[(i - 1)])
        if idname[(i - 1)] == '0':
            wss.write(a, Longitude[(i - 1)], bold)


# Final distance ws swicher

b = 1
flag = 0
record = 0
a = ' '

for i in range(b, size):
    #print(a, idname[i - 1])

    if idname[i - 1].isspace():
        flag += 1
        record = i
        i += 1

    if flag == 0:
        a = "F" + str(i + 1 - record)
        FinalDistance[i - 1] = str(FinalDistance[i - 1])
        ws.write(a, FinalDistance[(i - 1)])
        if idname[(i - 1)] == '0':
            ws.write(a, FinalDistance[(i - 1)], bold)

    elif flag == 1:
        a = "F" + str(i + 1 - record)
        FinalDistance[i - 1] = str(FinalDistance[i - 1])
        wse.write(a, FinalDistance[(i - 1)])
        if idname[(i - 1)] == '0':
            wse.write(a, FinalDistance[(i - 1)], bold)

    elif flag == 2:
        a = "F" + str(i + 1 - record)
        FinalDistance[i - 1] = str(FinalDistance[i - 1])
        wsw.write(a, FinalDistance[(i - 1)])
        if idname[(i - 1)] == '0':
            wsw.write(a, FinalDistance[(i - 1)], bold)

    elif flag == 3:
        a = "F" + str(i + 1 - record)
        FinalDistance[i - 1] = str(FinalDistance[i - 1])
        wsn.write(a, FinalDistance[(i - 1)])
        if idname[(i - 1)] == '0':
            wsn.write(a, FinalDistance[(i - 1)], bold)

    elif flag == 4:
        a = "F" + str(i + 1 - record)
        FinalDistance[i - 1] = str(FinalDistance[i - 1])
        wss.write(a, FinalDistance[(i - 1)])
        if idname[(i - 1)] == '0':
            wss.write(a, FinalDistance[(i - 1)], bold)

# for i in range(b, size):
#     a = "F" + str(i + 1)
#     if FinalDistance[i - 1] != ' ':
#         FinalDistance[i - 1] = str(FinalDistance[i - 1])+" K.M"
#     print(a, FinalDistance[i - 1])
#     ws.write(a, FinalDistance[i - 1])

wb.close()

print("\n\nExcel file generated...")
sleep(10)
