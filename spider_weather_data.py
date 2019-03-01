#-*- coding:utf-8 -*-
import requests
import json
from scrapy.selector import Selector
import datetime
import uuid
import logging
import logging.handlers
import cx_Oracle
import time
#def spider_weather(logger,conn):
def spider_weather(conn):
	timenow_formal = datetime.datetime.now()
	year_now = str(timenow_formal)[:4]
	month_now = str(timenow_formal)[5:7]
	day_now = str(timenow_formal)[8:10]
	hour_now = str(timenow_formal)[11:13]
	str_time = year_now+'-'+month_now+'-'+day_now+' '+hour_now+':00:00'
	time_now_total = datetime.datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
	time_last_day = time_now_total-datetime.timedelta(days=1)
	year_last_day = str(time_last_day)[:4]
	month_last_day = str(time_last_day)[5:7]
	day_last_day = str(time_last_day)[8:10]
	
	time_last_1 = time_now_total-datetime.timedelta(hours=1)
	last_1 = str(time_last_1)[:4]+str(time_last_1)[5:7]+str(time_last_1)[8:10]+str(time_last_1)[11:13]
	time_last_2 = time_now_total-datetime.timedelta(hours=2)
	last_2 = str(time_last_2)[:4]+str(time_last_2)[5:7]+str(time_last_2)[8:10]+str(time_last_2)[11:13]
	time_last_3 = time_now_total-datetime.timedelta(hours=3)
	last_3 = str(time_last_3)[:4]+str(time_last_3)[5:7]+str(time_last_3)[8:10]+str(time_last_3)[11:13]
	time_last_4 = time_now_total-datetime.timedelta(hours=4)
	last_4 = str(time_last_4)[:4]+str(time_last_4)[5:7]+str(time_last_4)[8:10]+str(time_last_4)[11:13]
	time_last_5 = time_now_total-datetime.timedelta(hours=5)
	last_5 = str(time_last_5)[:4]+str(time_last_5)[5:7]+str(time_last_5)[8:10]+str(time_last_5)[11:13]
	time_last_6 = time_now_total-datetime.timedelta(hours=6)
	last_6 = str(time_last_6)[:4]+str(time_last_6)[5:7]+str(time_last_6)[8:10]+str(time_last_6)[11:13]
	time_last_7 = time_now_total-datetime.timedelta(hours=7)
	last_7 = str(time_last_7)[:4]+str(time_last_7)[5:7]+str(time_last_7)[8:10]+str(time_last_7)[11:13]
	time_last_8 = time_now_total-datetime.timedelta(hours=8)
	last_8 =  str(time_last_8)[:4]+str(time_last_8)[5:7]+str(time_last_8)[8:10]+str(time_last_8)[11:13]
	time_last_9 = time_now_total-datetime.timedelta(hours=9)
	last_9 = str(time_last_9)[:4]+str(time_last_9)[5:7]+str(time_last_9)[8:10]+str(time_last_9)[11:13]
	time_last_10 = time_now_total-datetime.timedelta(hours=10)
	last_10 = str(time_last_10)[:4]+str(time_last_10)[5:7]+str(time_last_10)[8:10]+str(time_last_10)[11:13]
	time_last_11 = time_now_total-datetime.timedelta(hours=11)
	last_11 = str(time_last_11)[:4]+str(time_last_11)[5:7]+str(time_last_11)[8:10]+str(time_last_11)[11:13]
	time_last_12 = time_now_total-datetime.timedelta(hours=12)
	last_12 = str(time_last_12)[:4]+str(time_last_12)[5:7]+str(time_last_12)[8:10]+str(time_last_12)[11:13]
	time_last_13 = time_now_total-datetime.timedelta(hours=13)
	last_13 = str(time_last_13)[:4]+str(time_last_13)[5:7]+str(time_last_13)[8:10]+str(time_last_13)[11:13]
	time_last_14 = time_now_total-datetime.timedelta(hours=14)
	last_14 = str(time_last_14)[:4]+str(time_last_14)[5:7]+str(time_last_14)[8:10]+str(time_last_14)[11:13]
	time_last_15 = time_now_total-datetime.timedelta(hours=15)
	last_15 = str(time_last_15)[:4]+str(time_last_15)[5:7]+str(time_last_15)[8:10]+str(time_last_15)[11:13]
	time_array = [{'time_':time_last_1,'time_str':last_1},{'time_':time_last_2,'time_str':last_2},
	{'time_':time_last_3,'time_str':last_3},{'time_':time_last_4,'time_str':last_4},
	{'time_':time_last_5,'time_str':last_5},{'time_':time_last_6,'time_str':last_6},
	{'time_':time_last_7,'time_str':last_7},{'time_':time_last_8,'time_str':last_8},
	{'time_':time_last_9,'time_str':last_9},{'time_':time_last_10,'time_str':last_10},
	{'time_':time_last_11,'time_str':last_11},{'time_':time_last_12,'time_str':last_12},
	{'time_':time_last_13,'time_str':last_13},{'time_':time_last_14,'time_str':last_14},
	{'time_':time_last_15,'time_str':last_15}]
	total_time_last_day = year_last_day+'-'+month_last_day+'-'+day_last_day+'%'+'20'+hour_now+':00:00'
	total_time = year_now+'-'+month_now+'-'+day_now+'%'+'20'+hour_now+':00:00'
	url = 'http://weather.sxmb.gov.cn/map/mainmap.aspx?stime='+total_time_last_day+'&etime='+total_time+'&sname=铜川'
	#url = ('http://weather.sxmb.gov.cn/map/mainmap.aspx?stime=2019-02-17%2010:00:00&etime=2019-02-18%2010:00:00&sname=铜川')
	response = requests.get(url = url,verify=False)
	totalstring = str(Selector(text=response.text).xpath('//script/text()').extract())
	number1 = totalstring.find('var rJson = ')
	number2 = totalstring.find('}] }];')
	json_result=  json.loads(totalstring[number1+12:number2+5])
	total_json = json_result[0]['DS']
	
	for i in range(len(total_json)):
		for j in range(len(time_array)):
			time_cur = time_array[j]['time_']
			time_cur_str = time_array[j]['time_str']
			timenow_formal_1 = datetime.datetime.now()
			timenow = timenow_formal_1.strftime("%Y-%m-%d %H:%M:%S")
			if total_json[i]['Station_Name'] == '宜君'.decode('utf8'):
				TEM_yj = 'TEM'+time_cur_str
				PRE_1h_yj = 'PRE_1h'+time_cur_str
				PRS_yj = 'PRS'+time_cur_str
				WIN_D_Avg_2mi_yj = 'WIN_D_Avg_2mi'+time_cur_str
				WIN_S_Avg_2mi_yj = 'WIN_S_Avg_2mi'+time_cur_str
				GST_yj = 'GST'+time_cur_str
				RHU_yj = 'RHU'+time_cur_str
				
				sql1 = "INSERT INTO CG_QX_QXXSSJ (STATIONID,OBSERVTIME,INSERTTIME,WD2M,WS2M,TT,RH,PP,R1H,DW,UUID)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s')"\
				%('53945',time_cur,timenow,total_json[i][WIN_D_Avg_2mi_yj],total_json[i][WIN_S_Avg_2mi_yj],total_json[i][TEM_yj],total_json[i][RHU_yj],total_json[i][PRS_yj],total_json[i][PRE_1h_yj],total_json[i][GST_yj],str(uuid.uuid4()))
				cursor.execute(sql1)
				conn.commit()
				
			elif total_json[i]['Station_Name'] == '铜川'.decode('utf8'):
				TEM_tc = 'TEM'+time_cur_str
				PRE_1h_tc = 'PRE_1h'+time_cur_str
				PRS_tc = 'PRS'+time_cur_str
				WIN_D_Avg_2mi_tc = 'WIN_D_Avg_2mi'+time_cur_str
				WIN_S_Avg_2mi_tc = 'WIN_S_Avg_2mi'+time_cur_str
				GST_tc = 'GST'+time_cur_str
				RHU_tc = 'RHU'+time_cur_str
				sql2 = "INSERT INTO CG_QX_QXXSSJ (STATIONID,OBSERVTIME,INSERTTIME,WD2M,WS2M,TT,RH,PP,R1H,DW,UUID)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s')"\
				%('53947',time_cur,timenow,total_json[i][WIN_D_Avg_2mi_tc],total_json[i][WIN_S_Avg_2mi_tc],total_json[i][TEM_tc],total_json[i][RHU_tc],total_json[i][PRS_tc],total_json[i][PRE_1h_tc],total_json[i][GST_tc],str(uuid.uuid4()))
				cursor.execute(sql2)
				conn.commit()
			elif total_json[i]['Station_Name'] == '耀州'.decode('utf8'):
				TEM_yz = 'TEM'+time_cur_str
				PRE_1h_yz = 'PRE_1h'+time_cur_str
				PRS_yz = 'PRS'+time_cur_str
				WIN_D_Avg_2mi_yz = 'WIN_D_Avg_2mi'+time_cur_str
				WIN_S_Avg_2mi_yz = 'WIN_S_Avg_2mi'+time_cur_str
				GST_yz = 'GST'+time_cur_str
				RHU_yz = 'RHU'+time_cur_str
				sql3 = "INSERT INTO CG_QX_QXXSSJ (STATIONID,OBSERVTIME,INSERTTIME,WD2M,WS2M,TT,RH,PP,R1H,DW,UUID)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s')"\
				%('57037',time_cur,timenow,total_json[i][WIN_D_Avg_2mi_yz],total_json[i][WIN_S_Avg_2mi_yz],total_json[i][TEM_yz],total_json[i][RHU_yz],total_json[i][PRS_yz],total_json[i][PRE_1h_yz],total_json[i][GST_yz],str(uuid.uuid4()))
				cursor.execute(sql3)
				conn.commit()
for kk in range(9999999):
	#module_path = '/usr/txjson/'
	module_path = 'F:/tongchuan_spider'
	LOG_FILE = module_path+'/spider2.log'
	handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024*1024, backupCount = 5) # 实例化handler 
	fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
	formatter = logging.Formatter(fmt)   # 实例化formatter
	handler.setFormatter(formatter)      # 为handler添加formatter
	logger = logging.getLogger('logging')
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	json_url1 = module_path+'json_air1.json'
	text1 = open(json_url1,'w')
	conn = cx_Oracle.connect('tchbdc_new/tchbdc_new@172.18.0.104/orcl')
	cursor = conn.cursor()
	try:
		spider_weather(conn)
		#logger.info('spider1没错 成功')
	except:
		time.sleep(10)
		logger.error('spider有错 失败',exc_info=1)
	text1.close()
	conn.close()
	handler.close()
	time.sleep(1800)
