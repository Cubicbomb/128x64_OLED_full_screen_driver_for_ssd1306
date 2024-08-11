def _display_128x64(oled, num):
    code = 0x00
    byte_data =data[num]#读取utf8编码为num的点阵编码
    for t in range(0, 16):
        for y in range(0, 64):#y是行数
            a = bin(byte_data[y+64*t]).replace('0b', '')
            while len(a) < 8:
                a = '0' + a
            for x in range(0, 8):
                oled.pixel(x + 8*t, y, int(a[x]))
#Copyright (c) 2024 Cubicbomb
#我写的就是一坨垃圾
#问题一堆，有待解决