print('......Program Calculate tiles by jarong......')
try:
    tiles = int(input('คุณต้องการปูกระเบื้องกี่แผ่น :  '))
    row = int(input('1 แถวต้องการปูกระเบื้องกี่แผ่น :  ')) # 3 ชิ้นต่อแถว
    color = input('กระเบื้องสีอะไร? [red / gold / white]:')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขจำนวนเต็มเท่านั้น !!!!')
    tiles = int(input('คุณต้องการปูกระเบื้องกี่แผ่น :  '))
    row = int(input('1 แถวต้องการปูกระเบื้องกี่แผ่น :  ')) # 3 ชิ้นต่อแถว
    color = input('กระเบื้องสีอะไร? [red / gold / white]:')

tilescolor = {'red':100,'gold':200,'white':90}
    
print('....Calculate....')
total_row = tiles // row
remain_tiles = tiles % row

#print(total_row,remain_tiles)

buy_more = row - remain_tiles

print(f'มีกระเบื้องทั้้งหมด : {tiles} แผ่น')

print(f'1 แถวปูกระเบื้องได้ : {row} แผ่น')

print('-------คำนวน-------')

print('ต้องปูกระเบื้องทั้งหมด : {} แถว'.format(total_row))
print('เหลือกระเบื้องที่ไม่ได้ปูเต็มแถว : {} แผ่น'.format(remain_tiles))
print('ลูกค้าต้องซื้อกระเบื้องเพิ่ม : {} แผ่น'.format(buy_more))
print('ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม : {} บาท'.format(buy_more * tilescolor[color]))

#ลูกค้าต้องซื้อกระเบื้องเพิ่มกี่แผ่น




