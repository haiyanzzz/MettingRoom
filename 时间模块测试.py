#!usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

import time
# print(time.time())
# print(time.strftime("%Y-%m-%d"))

d = (1,"20")
print(d[1],type(d[1]))


#自己创建的一张time表查询时间段
# timelist = models.Time.objects.all()
# l = []
# for i in timelist:
#    l.append(i.timeline.strftime("%H:%M"))