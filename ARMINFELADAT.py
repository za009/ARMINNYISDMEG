def atlag(list):
    for i in range(0, len(list), 1):
        seged = 0
        ossz = 0
        if(list[i]>90 and list[i]<110):
            ossz = ossz+list[i]
            seged = seged+1
        atlag = ossz/seged
        print("A 90 és 110 közötti sebességű autók átlagsebessége:",round(atlag, 2))
