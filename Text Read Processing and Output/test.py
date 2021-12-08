from math import radians, cos, sin, asin, sqrt


temp = ""

listTrack = 0

endFlag = True
count = 0
lineNo = 1
startBlock = 0
endBlock = 0

cid = []
clabel = []
ccountry = []
clatitude = []
clongitude = []

node_id = []
node_label = []
node_country = []
node_latitude = []
node_longitude = []

distance_from_cn = []




def iterate(filex, line=1):
    count = 0
    for f in filex:
        count += 1
        if count != line:
            continue
        else:

            tempv = f.lstrip()
            tempv = tempv.rstrip()
            filex.seek(0)
            return tempv
            break



def checkBlock(i, j,filec):
    checkCount = 0
    for x in range(i + 1, j):
        temp = iterate(filec, x)
        if temp[0:2] == "id":
            checkCount += 1
        if temp[0:5] == "label":
            checkCount += 1
        if temp[0:7] == "Country":
            checkCount += 1
        if temp[0:9] == "Longitude":
            checkCount += 1
        if temp[0:8] == "Latitude":
            checkCount += 1

    if checkCount == 5:
        print("Checked Suceess")
        checkCount = 0
        for x in range(i + 1, j):
            temp1 = iterate(filec, x)
            if temp1[0:2] == "id":
                node_id.append(temp1[3:])

            if temp1[0:5] == "label":
                node_label.append(temp1[6:].replace('"', ''))

            if temp1[0:7] == "Country":
                node_country.append(temp1[8:].replace('"', ''))

            if temp1[0:9] == "Longitude":
                node_longitude.append(temp1[10:].replace(' ', ''))

            if temp1[0:8] == "Latitude":
                node_latitude.append(temp1[9:].replace(' ', ''))
    else:
        print("Checked Faild")


# Central block

def checkCentralBlock(i, j,filec):
    checkCount = 0
    for x in range(i + 1, j):
        temp = iterate(filec, x)
        if temp[0:2] == "id":
            checkCount += 1
        if temp[0:5] == "label":
            checkCount += 1
        if temp[0:7] == "Country":
            checkCount += 1
        if temp[0:9] == "Longitude":
            checkCount += 1
        if temp[0:8] == "Latitude":
            checkCount += 1

    if checkCount == 5:
        print("Central Checked Suceess")
        checkCount = 0
        for x in range(i + 1, j):
            temp1 = iterate(filec, x)
            if temp1[0:2] == "id":
                cid.append(temp1[3:])
                node_id.append(temp1[3:])

            if temp1[0:5] == "label":
                clabel.append(temp1[6:].replace('"', ''))
                node_label.append(temp1[6:].replace('"', ''))

            if temp1[0:7] == "Country":
                ccountry.append(temp1[8:].replace('"', ''))
                node_country.append(temp1[8:].replace('"', ''))

            if temp1[0:9] == "Longitude":
                clongitude.append(temp1[10:].replace(' ', ''))
                node_longitude.append(temp1[10:].replace(' ', ''))

            if temp1[0:8] == "Latitude":
                clatitude.append(temp1[9:].replace(' ', ''))
                node_latitude.append(temp1[9:].replace(' ', ''))

    else:
        print("Central Checked Faild")


def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)

def dist_cal(flat, flon, tlat, tlon):
    if flat==' ':
        distance_from_cn.append(" ")
        return
    flat = float(flat)
    flon = float(flon)
    tlat = float(tlat)
    tlon = float(tlon)

    dist = distance(flat, tlat, flon, tlon)
    dist = round(dist,3)
    distance_from_cn.append(dist)

    # try:
    #     dist = mt.sqrt(((tlat - flat) ** 2) + ((tlon - flon) ** 2))
    #     distance_from_cn.append(dist)
    # except:
    #     print("central coordinate may be equal to node coordinate")
    #     exit()


#########################################################################
############################### DATA BASE ###############################
#########################################################################

file = open("data_base.txt", 'r')

while endFlag:
    temp = iterate(file, lineNo)
    if temp == "node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkBlock(startBlock, endBlock,file)

    if temp == "central_node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkCentralBlock(startBlock, endBlock,file)

    lineNo += 1
    if iterate(file, lineNo - 1) == iterate(file, lineNo):
        break

# LL = len(node_id)
# lengthRecord.append(LL)


file.close()

listLength = len(node_id)
for i in range(listLength):
    dist_cal(node_latitude[i], node_longitude[i], clatitude[0], clongitude[0])

listTrack = listLength

print("\n\nMain central Node\n", cid, "\n", clabel, "\n", ccountry, "\n", clatitude, "\n", clongitude, "\n\n")

#########################################################################
################################# EAST ##################################
#########################################################################
node_id.append(" ")
node_label.append(" ")
node_country.append(" ")
node_longitude.append(" ")
node_latitude.append(" ")

print("\n\nChecking EAST...")

file = open("east.txt", 'r')

lineNo=1

cid.clear()
clabel.clear()
ccountry.clear()
clatitude.clear()
clongitude.clear()





while endFlag:
    temp = iterate(file, lineNo)
    if temp == "node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkBlock(startBlock, endBlock,file)

    if temp == "central_node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkCentralBlock(startBlock, endBlock,file)

    lineNo += 1
    if iterate(file, lineNo - 1) == iterate(file, lineNo):
        break

# LL = len(node_id)
# lengthRecord.append(LL)

file.close()

listLength = len(node_id)
for i in range(listTrack,listLength):
    dist_cal(node_latitude[i], node_longitude[i], clatitude[0], clongitude[0])

listTrack = listLength

print("\n\nCentralNode of East\n", cid, "\n", clabel, "\n", ccountry, "\n", clatitude, "\n", clongitude, "\n\n")

#########################################################################
################################# WEST ##################################
#########################################################################
node_id.append(" ")
node_label.append(" ")
node_country.append(" ")
node_longitude.append(" ")
node_latitude.append(" ")


print("\n\nChecking WEST...")

file = open("west.txt", 'r')

lineNo=1

cid.clear()
clabel.clear()
ccountry.clear()
clatitude.clear()
clongitude.clear()





while endFlag:
    temp = iterate(file, lineNo)
    if temp == "node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkBlock(startBlock, endBlock,file)

    if temp == "central_node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkCentralBlock(startBlock, endBlock,file)

    lineNo += 1
    if iterate(file, lineNo - 1) == iterate(file, lineNo):
        break

# LL = len(node_id)
# lengthRecord.append(LL)

file.close()

listLength = len(node_id)
for i in range(listTrack,listLength):
    dist_cal(node_latitude[i], node_longitude[i], clatitude[0], clongitude[0])

listTrack = listLength

print("\n\nCentralNode of West\n", cid, "\n", clabel, "\n", ccountry, "\n", clatitude, "\n", clongitude, "\n\n")

#########################################################################
################################ NORTH ##################################
#########################################################################
node_id.append(" ")
node_label.append(" ")
node_country.append(" ")
node_longitude.append(" ")
node_latitude.append(" ")

print("\n\nChecking NORTH...")

file = open("north.txt", 'r')

lineNo=1

cid.clear()
clabel.clear()
ccountry.clear()
clatitude.clear()
clongitude.clear()





while endFlag:
    temp = iterate(file, lineNo)
    if temp == "node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkBlock(startBlock, endBlock,file)

    if temp == "central_node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkCentralBlock(startBlock, endBlock,file)

    lineNo += 1
    if iterate(file, lineNo - 1) == iterate(file, lineNo):
        break


# LL = len(node_id)
# lengthRecord.append(LL)

file.close()

listLength = len(node_id)
for i in range(listTrack,listLength):
    dist_cal(node_latitude[i], node_longitude[i], clatitude[0], clongitude[0])

listTrack = listLength

print("\n\nCentralNode of North\n", cid, "\n", clabel, "\n", ccountry, "\n", clatitude, "\n", clongitude, "\n\n")


#########################################################################
################################ SOUTH ##################################
#########################################################################
node_id.append(" ")
node_label.append(" ")
node_country.append(" ")
node_longitude.append(" ")
node_latitude.append(" ")


print("\n\nChecking SOUTH...")

file = open("south.txt", 'r')

lineNo=1

cid.clear()
clabel.clear()
ccountry.clear()
clatitude.clear()
clongitude.clear()





while endFlag:
    temp = iterate(file, lineNo)
    if temp == "node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkBlock(startBlock, endBlock,file)

    if temp == "central_node [":
        startBlock = lineNo
        while temp != "]":
            temp = iterate(file, lineNo)
            endBlock = lineNo
            lineNo += 1
        lineNo -= 1
        checkCentralBlock(startBlock, endBlock,file)

    lineNo += 1
    if iterate(file, lineNo - 1) == iterate(file, lineNo):
        break


listLength = len(node_id)
for i in range(listTrack,listLength):
    dist_cal(node_latitude[i], node_longitude[i], clatitude[0], clongitude[0])

print("\n\nCentralNode of South\n", cid, "\n", clabel, "\n", ccountry, "\n", clatitude, "\n", clongitude, "\n\n")


print("\n\n\n Detected valid data... \n\n")
print(node_id, "\n", node_label, "\n", node_country, "\n", node_latitude, "\n", node_longitude, "\n\n")

print(distance_from_cn)



file.close()


