#-*- coding:utf-8 -*-
from __future__ import division
import requests
import json
from scrapy.selector import Selector
import cx_Oracle
import uuid
import datetime
url = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getDistrict_24IAQI.ashx?cityCode=610200')
response = requests.get(url = url,verify=False)
json_result=  json.loads(response.text)
conn = cx_Oracle.connect('tchbdc/tchbdc@172.18.0.104/orcl')
cursor = conn.cursor()
sql = "select UUID,ZDMC from CG_HJZL_DQZDXX"
cursor.execute(sql)
results = cursor.fetchall()
for i1 in range(len(results)):
	for i in range(len(json_result)):
		if results[i1][1].decode('gbk') in json_result[i]['POSITIONNAME']:
			station_name = results[i1][1].decode('gbk')
			pollutantid = str(uuid.uuid4())
			pollutantid = ''.join((pollutantid).split('-'))
			station_ID = results[i1][0]
			PM2_5 = json_result[i]['PM2_5']
			CO = json_result[i]['CO']
			QUALITY = json_result[i]['QUALITY']
			PM10 = json_result[i]['PM10']
			AQI = json_result[i]['AQI']
			PRIMARYPOLLUTANT = json_result[i]['PRIMARYPOLLUTANT']
			TIMEPOINT = json_result[i]['TIMEPOINT']
			SO2 = json_result[i]['SO2']
			STATIONCODE = json_result[i]['STATIONCODE']
			O3 = json_result[i]['O3']
			NO2 = json_result[i]['NO2']
			aqi_so2 = 'novalue'
			aqi_no2 = 'novalue'
			aqi_co = 'novalue'
			aqi_pm10 = 
			aqi_pm25 = 
			timenow_formal = datetime.datetime.now()
			timenow_afterwards = timenow_formal.strftime("%Y-%m-%d %H:%M:%S")
			'''
			sql1 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s')"\
			%(pollutantid,TIMEPOINT,AQI,PRIMARYPOLLUTANT,QUALITY,SO2,NO2,PM10,CO,O3,PM2_5,station_name,station_ID,'铜川市'.decode('utf8'),timenow_afterwards,aqi_so2,aqi_no2,aqi_co,aqi_o3)
			cursor.execute(sql1)
			conn.commit()'''