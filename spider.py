from urllib import parse
from urllib import request
import json
import numpy as np


url='https://www.chebada.com/busList/GetBusSchedules'
# des='南京'
# arr='盱眙'
# years='2018'
# months='2'
# days='14'
des = input("请输入出发站：")
arr=input('请输入到达站：')
years=input('请输入出发年：')
months=input('请输入出发月：')
days=input('请输入出发日：')

post_data={}
post_data['departure']=des
post_data['destination']=arr
post_data['departureDate']=years+'-'+months+'-'+days

res=request.urlopen(url,data=bytes(parse.urlencode(post_data),encoding='utf-8'))
data=res.read().decode()
new_data=json.loads(data)
new_data=new_data['body']['scheduleList']
f=open('che.txt','w')
for i in new_data:
    tim=i.get('dptTime')
    tic=i.get('ticketLeft')
    dess=i.get('departure')
    arrs=i.get('destination')
    price=i.get('ticketPrice')
    print('发车时间:%s\t出发站:%s\t 到达站:%s \t余票:%s\t价格:%s\t'%(tim,dess,arrs,tic,price))
    f.write(str(i)+'\n')
f.close()

