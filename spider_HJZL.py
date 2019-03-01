#-*- coding:utf-8 -*-
from __future__ import division
from scrapy.selector import Selector
import cx_Oracle
import datetime
import urllib2  
import uuid  
import time
import json
import logging
import logging.handlers
import requests
#加入了所有区域
def spider3(conn):
	area_name_array = ['铜川市'.decode('utf8'),'王益区'.decode('utf8'),'印台区'.decode('utf8'),'耀州区'.decode('utf8'),'宜君县'.decode('utf8'),'铜川新区'.decode('utf8')]
	for each_name in area_name_array:
		try:
			sql_select1 = "select UUID,SZXZQ from CG_HJZL_DQZDXX where ZDMC = '%s'"%(each_name)
			cursor.execute(sql_select1)
			results_select1 = cursor.fetchall()
			uuid_area = results_select1[0][0]
			area_code_origin = results_select1[0][1]
			area_code = area_code_origin[:6]
			url = 'http://113.140.66.226:8024/sxAQIWeb/ashx/getCity_7DayAQI.ashx?cityName='+area_code
			response = requests.get(url = url,verify=False)
			json_result =  json.loads(response.text)
			timenow_formal = datetime.datetime.now()
			timenow_afterwards = timenow_formal.strftime("%Y-%m-%d %H:%M:%S")
			year = timenow_afterwards[:4]
			for each_result in json_result:
				if each_result['QUALITY'] == 'I':
					QUALITY_id = '95646F517C03404191A1D975A8C663AE'
				elif each_result['QUALITY'] == 'II':
					QUALITY_id = '2c9385fe3f887442013f88b961e6004b'
				elif each_result['QUALITY'] == 'III':
					QUALITY_id = '2c9385fe3f996311013f99f75f180031'
				elif each_result['QUALITY'] == 'IV':
					QUALITY_id = '2c9385fe3f996311013f99f7e2c00035'
				elif each_result['QUALITY'] == 'V':
					QUALITY_id = '2c9385fe3f996311013f99f87c2c0039'
				elif each_result['QUALITY'] == 'VI':
					QUALITY_id = '2c9385fe3f996311013f99f91413003d'
				else:
					QUALITY_id = ''
				
				pjsj = year+'-'+each_result['TIMEPOINT']+' 00:00:00'
				
				sql1 = "INSERT INTO CG_HJZL_KQAQIRPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,ZDMC,ZDUUID,SZXZQ,GMT_CREATE)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'))"\
				%(str(uuid.uuid4()),pjsj,each_result['AQI'],each_result['PRIMARYPOLLUTANT'],QUALITY_id,each_name,uuid_area,area_code_origin.decode('utf8'),timenow_afterwards)
				try:
					cursor.execute(sql1)
					conn.commit()
				except:
					1 == 1
		except:
			1 == 1
'''
#之前的抓aqi日数据的，现在已经不用
def spider3(conn):
	url = 'http://113.140.66.226:8024/sxAQIWeb/ashx/getCity_7DayAQI.ashx?cityName=610200'
	response = requests.get(url = url,verify=False)
	json_result =  json.loads(response.text)
	timenow_formal = datetime.datetime.now()
	timenow_afterwards = timenow_formal.strftime("%Y-%m-%d %H:%M:%S")
	year = timenow_afterwards[:4]
	for each_result in json_result:
		if each_result['QUALITY'] == 'I':
			QUALITY_id = '95646F517C03404191A1D975A8C663AE'
		elif each_result['QUALITY'] == 'II':
			QUALITY_id = '2c9385fe3f887442013f88b961e6004b'
		elif each_result['QUALITY'] == 'III':
			QUALITY_id = '2c9385fe3f996311013f99f75f180031'
		elif each_result['QUALITY'] == 'IV':
			QUALITY_id = '2c9385fe3f996311013f99f7e2c00035'
		elif each_result['QUALITY'] == 'V':
			QUALITY_id = '2c9385fe3f996311013f99f87c2c0039'
		elif each_result['QUALITY'] == 'VI':
			QUALITY_id = '2c9385fe3f996311013f99f91413003d'
		else:
			QUALITY_id = ''
		pjsj = year+'-'+each_result['TIMEPOINT']+' 00:00:00'
		sql1 = "INSERT INTO CG_HJZL_KQAQIRPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,ZDMC,ZDUUID,SZXZQ,GMT_CREATE)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'))"\
		%(str(uuid.uuid4()),pjsj,each_result['AQI'],each_result['PRIMARYPOLLUTANT'],QUALITY_id,'铜川市'.decode('utf8'),'fccbb851829b425d89174f2db6b0d999','610200000000'.decode('utf8'),timenow_afterwards)
		cursor.execute(sql1)
		conn.commit()'''
def spider2(logger,conn):
	area_name_array = ['铜川市'.decode('utf8'),'王益区'.decode('utf8'),'印台区'.decode('utf8'),'耀州区'.decode('utf8'),'宜君县'.decode('utf8'),'铜川新区'.decode('utf8')]
	for each_name in area_name_array:
		try:
			sql_select2 = "select UUID,SZXZQ from CG_HJZL_DQZDXX where ZDMC = '%s'"%(each_name)
			cursor.execute(sql_select2)
			results_select2 = cursor.fetchall()
			uuid_area = results_select2[0][0]
			area_code_origin = results_select2[0][1]
			area_code = area_code_origin[:6]
			timenow_formal = datetime.datetime.now()
			year_now = str(timenow_formal)[:4]
			month_now = str(timenow_formal)[5:7]
			day_now = str(timenow_formal)[8:10]
			hour_now = str(timenow_formal)[11:13]
			str_time = year_now+'-'+month_now+'-'+day_now+' '+hour_now+':00:00'
			time_now_total = datetime.datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
			time_now_total = time_now_total-datetime.timedelta(hours=0)
			time_last1_hour = time_now_total-datetime.timedelta(hours=1)
			time_last2_hour = time_now_total-datetime.timedelta(hours=2)
			
			url0 = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getCity_24AQI.ashx?cityName='+area_code)
			response = requests.get(url = url0,verify=False)
			json_result =  json.loads(response.text)
			url1 = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getDistrict_24IAQI.ashx?cityCode='+area_code)
			response1 = requests.get(url = url1,verify=False)
			json_result1 =  json.loads(response1.text)
			url2 = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getDistrict_24Nd.ashx?cityCode='+area_code)
			response2 = requests.get(url = url2,verify=False)
			json_result2 =  json.loads(response2.text)
			
			station_ID = uuid_area
			station_name = each_name
			 
			pollutantid0 = str(uuid.uuid4())
			pollutantid0 = ''.join((pollutantid0).split('-'))
			pollutantid1 = str(uuid.uuid4())
			pollutantid1 = ''.join((pollutantid1).split('-'))
			pollutantid2 = str(uuid.uuid4())
			pollutantid2 = ''.join((pollutantid2).split('-'))
			PM2_5_0 = ''
			CO_0 = ''
			O3_0 = ''
			NO2_0 = ''
			PM10_0 = ''
			SO2_0 = ''
			TIMEPOINT_0 = ''
			AQI_0 = ''
			QUALITY_0 = ''
			PRIMARYPOLLUTANT_0 = ''
			aqi_so2_0 = ''
			aqi_no2_0 = ''
			aqi_co_0 = ''
			aqi_o3_0 = ''
			aqi_pm10_0 = ''
			aqi_pm25_0 = ''

			PM2_5_1 = ''
			CO_1 = ''
			O3_1 = ''
			NO2_1 = ''
			PM10_1 = ''
			SO2_1 = ''
			TIMEPOINT_1 = ''
			AQI_1 = ''
			QUALITY_1 = ''
			PRIMARYPOLLUTANT_1 = ''
			aqi_so2_1 = ''
			aqi_no2_1 = ''
			aqi_co_1 = ''
			aqi_o3_1 = ''
			aqi_pm10_1 = ''
			aqi_pm25_1 = ''

			PM2_5_2 = ''
			CO_2 = ''
			O3_2 = ''
			NO2_2 = ''
			PM10_2 = ''
			SO2_2 = ''
			TIMEPOINT_2 = ''
			AQI_2 = ''
			QUALITY_2 = ''
			PRIMARYPOLLUTANT_2 = ''
			aqi_so2_2 = ''
			aqi_no2_2 = ''
			aqi_co_2 = ''
			aqi_o3_2 = ''
			aqi_pm10_2 = ''
			aqi_pm25_2 = ''
			for each_result0 in json_result:
				
				time0_total = year_now+'-'+each_result0['TIMEPOINT1']+':00'
				each_time_result0 = datetime.datetime.strptime(time0_total,'%Y-%m-%d %H:%M:%S')
				if time_now_total == each_time_result0:
					AQI_0 = each_result0['AQI']
					QUALITY_0 = each_result0['QUALITY']
					if QUALITY_0 == 'I':
						QUALITY_0 = '95646F517C03404191A1D975A8C663AE'
					elif QUALITY_0 == 'II':
						QUALITY_0 = '2c9385fe3f887442013f88b961e6004b'
					elif QUALITY_0 == 'III':
						QUALITY_0 = '2c9385fe3f996311013f99f75f180031'
					elif QUALITY_0 == 'IV':
						QUALITY_0 = '2c9385fe3f996311013f99f7e2c00035'
					elif QUALITY_0 == 'V':
						QUALITY_0 = '2c9385fe3f996311013f99f87c2c0039'
					elif QUALITY_0 == 'VI':
						QUALITY_0 = '2c9385fe3f996311013f99f91413003d'
					else:
						QUALITY_0 = ''
					PRIMARYPOLLUTANT_0 = each_result0['PRIMARYPOLLUTANT']
				if time_last1_hour == each_time_result0:
					AQI_1 = each_result0['AQI']
					QUALITY_1 = each_result0['QUALITY']
					if QUALITY_1 == 'I':
						QUALITY_1 = '95646F517C03404191A1D975A8C663AE'
					elif QUALITY_1 == 'II':
						QUALITY_1 = '2c9385fe3f887442013f88b961e6004b'
					elif QUALITY_1 == 'III':
						QUALITY_1 = '2c9385fe3f996311013f99f75f180031'
					elif QUALITY_1 == 'IV':
						QUALITY_1 = '2c9385fe3f996311013f99f7e2c00035'
					elif QUALITY_1 == 'V':
						QUALITY_1 = '2c9385fe3f996311013f99f87c2c0039'
					elif QUALITY_1 == 'VI':
						QUALITY_1 = '2c9385fe3f996311013f99f91413003d'
					else:
						QUALITY_1 = ''
					PRIMARYPOLLUTANT_1 = each_result0['PRIMARYPOLLUTANT']
				if time_last2_hour == each_time_result0:
					AQI_2 = each_result0['AQI']
					QUALITY_2 = each_result0['QUALITY']
					if QUALITY_2 == 'I':
						QUALITY_2 = '95646F517C03404191A1D975A8C663AE'
					elif QUALITY_2 == 'II':
						QUALITY_2 = '2c9385fe3f887442013f88b961e6004b'
					elif QUALITY_2 == 'III':
						QUALITY_2 = '2c9385fe3f996311013f99f75f180031'
					elif QUALITY_2 == 'IV':
						QUALITY_2 = '2c9385fe3f996311013f99f7e2c00035'
					elif QUALITY_2 == 'V':
						QUALITY_2 = '2c9385fe3f996311013f99f87c2c0039'
					elif QUALITY_2 == 'VI':
						QUALITY_2 = '2c9385fe3f996311013f99f91413003d'
					else:
						QUALITY_2 = ''
					PRIMARYPOLLUTANT_2 = each_result0['PRIMARYPOLLUTANT']
			for each_result1 in json_result1:
				each_time_result1 = datetime.datetime.strptime(each_result1['TIMEPOINT'],'%Y-%m-%d %H:%M:%S')
				if time_now_total == each_time_result1:
					aqi_so2_0 = each_result1['ISO2']
					aqi_no2_0 = each_result1['INO2']
					aqi_co_0 = each_result1['ICO']
					aqi_o3_0 = each_result1['IO3']
					aqi_pm10_0 = each_result1['IPM10']
					aqi_pm25_0 = each_result1['IPM2_5']
				if time_last1_hour == each_time_result1:
					aqi_so2_1 = each_result1['ISO2']
					aqi_no2_1 = each_result1['INO2']
					aqi_co_1 = each_result1['ICO']
					aqi_o3_1 = each_result1['IO3']
					aqi_pm10_1 = each_result1['IPM10']
					aqi_pm25_1 = each_result1['IPM2_5']
				if time_last2_hour == each_time_result1:
					aqi_so2_2 = each_result1['ISO2']
					aqi_no2_2 = each_result1['INO2']
					aqi_co_2 = each_result1['ICO']
					aqi_o3_2 = each_result1['IO3']
					aqi_pm10_2 = each_result1['IPM10']
					aqi_pm25_2 = each_result1['IPM2_5']
			for each_result2 in json_result2:
				each_time_result2 = datetime.datetime.strptime(each_result2['TIMEPOINT'],'%Y-%m-%d %H:%M:%S')
				
				if time_now_total == each_time_result2:
					PM2_5_0 = each_result2['PM2_5']
					CO_0 = each_result2['CO']
					O3_0 = each_result2['O3']
					NO2_0 = each_result2['NO2']
					PM10_0 = each_result2['PM10']
					SO2_0 = each_result2['SO2']
					TIMEPOINT_0 = time_now_total
					
				if time_last1_hour == each_time_result2:
					PM2_5_1 = each_result2['PM2_5']
					CO_1 = each_result2['CO']
					O3_1 = each_result2['O3']
					NO2_1 =  each_result2['NO2']
					PM10_1 = each_result2['PM10']
					SO2_1 = each_result2['SO2']
					TIMEPOINT_1 = time_last1_hour
				if time_last2_hour == each_time_result2:
					PM2_5_2 = each_result2['PM2_5']
					CO_2 = each_result2['CO']
					O3_2 = each_result2['O3']
					NO2_2 = each_result2['NO2']
					PM10_2 = each_result2['PM10']
					SO2_2 = each_result2['SO2']
					TIMEPOINT_2 = time_last2_hour
			if O3_0 == '—'.decode('utf8'):
				O3_0 = ''
			if SO2_0 == '—'.decode('utf8'):
				SO2_0 = ''
			if NO2_0 == '—'.decode('utf8'):
				NO2_0 = ''
			if PM10_0 == '—'.decode('utf8'):
				PM10_0 = ''
			if PM2_5_0 == '—'.decode('utf8'):
				PM2_5_0 = ''
			if AQI_0 == '—'.decode('utf8'):
				AQI_0 = ''
			if PRIMARYPOLLUTANT_0 == '—'.decode('utf8'):
				PRIMARYPOLLUTANT_0 = ''
			if O3_1 == '—'.decode('utf8'):
				O3_1 = ''
			if SO2_1 == '—'.decode('utf8'):
				SO2_1 = ''
			if NO2_1 == '—'.decode('utf8'):
				NO2_1 = ''
			if PM10_1 == '—'.decode('utf8'):
				PM10_1 = ''
			if PM2_5_1 == '—'.decode('utf8'):
				PM2_5_1 = ''
			if AQI_1 == '—'.decode('utf8'):
				AQI_1 = ''
			if PRIMARYPOLLUTANT_1 == '—'.decode('utf8'):
				PRIMARYPOLLUTANT_1 = ''
			if O3_2 == '—'.decode('utf8'):
				O3_2 = ''
			if SO2_2 == '—'.decode('utf8'):
				SO2_2 = ''
			if NO2_2 == '—'.decode('utf8'):
				NO2_2 = ''
			if PM10_2 == '—'.decode('utf8'):
				PM10_2 = ''
			if PM2_5_2 == '—'.decode('utf8'):
				PM2_5_2 = ''
			if AQI_2 == '—'.decode('utf8'):
				AQI_2 = ''
			if PRIMARYPOLLUTANT_2 == '—'.decode('utf8'):
				PRIMARYPOLLUTANT_2 = ''
			timenow_formal = datetime.datetime.now()
			timenow_afterwards = timenow_formal.strftime("%Y-%m-%d %H:%M:%S")
			sql1 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI,PM10_AQI,PM2D5_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s')"\
			%(pollutantid0,TIMEPOINT_0,AQI_0,PRIMARYPOLLUTANT_0,QUALITY_0,SO2_0,NO2_0,PM10_0,CO_0,O3_0,PM2_5_0,station_name,station_ID,area_code_origin,timenow_afterwards,aqi_so2_0,aqi_no2_0,aqi_co_0,aqi_o3_0,aqi_pm10_0,aqi_pm25_0)
			try:
				cursor.execute(sql1)
				conn.commit()
			except:
				logger.error('已有数据',exc_info=1)
			sql2 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI,PM10_AQI,PM2D5_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s')"\
			%(pollutantid1,TIMEPOINT_1,AQI_1,PRIMARYPOLLUTANT_1,QUALITY_1,SO2_1,NO2_1,PM10_1,CO_1,O3_1,PM2_5_1,station_name,station_ID,area_code_origin,timenow_afterwards,aqi_so2_1,aqi_no2_1,aqi_co_1,aqi_o3_1,aqi_pm10_1,aqi_pm25_1)
			try:
				cursor.execute(sql2)
				conn.commit()
			except:
				logger.error('已有数据',exc_info=1)
			sql3 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI,PM10_AQI,PM2D5_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s')"\
			%(pollutantid2,TIMEPOINT_2,AQI_2,PRIMARYPOLLUTANT_2,QUALITY_2,SO2_2,NO2_2,PM10_2,CO_2,O3_2,PM2_5_2,station_name,station_ID,area_code_origin,timenow_afterwards,aqi_so2_2,aqi_no2_2,aqi_co_2,aqi_o3_2,aqi_pm10_2,aqi_pm25_2)
			try:
				cursor.execute(sql3)
				conn.commit()
			except:
				logger.error('已有数据',exc_info=1)
		except:
			logger.error('错误',exc_info=1)
'''
def spider2(logger,conn):
	timenow_formal = datetime.datetime.now()
	year_now = str(timenow_formal)[:4]
	month_now = str(timenow_formal)[5:7]
	day_now = str(timenow_formal)[8:10]
	hour_now = str(timenow_formal)[11:13]
	str_time = year_now+'-'+month_now+'-'+day_now+' '+hour_now+':00:00'
	time_now_total = datetime.datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
	time_now_total = time_now_total-datetime.timedelta(hours=2)
	time_last1_hour = time_now_total-datetime.timedelta(hours=1)
	time_last2_hour = time_now_total-datetime.timedelta(hours=2)
	
	url = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getCity_24AQI.ashx?cityName=610200')
	response = requests.get(url = url,verify=False)
	json_result =  json.loads(response.text)
	url1 = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getDistrict_24IAQI.ashx?cityCode=610200')
	response1 = requests.get(url = url1,verify=False)
	json_result1 =  json.loads(response1.text)
	url2 = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getDistrict_24Nd.ashx?cityCode=610200')
	response2 = requests.get(url = url2,verify=False)
	json_result2 =  json.loads(response2.text)
	station_ID = 'fccbb851829b425d89174f2db6b0d999'
	station_name = '铜川市'.decode('utf8')
	pollutantid0 = str(uuid.uuid4())
	pollutantid0 = ''.join((pollutantid0).split('-'))
	pollutantid1 = str(uuid.uuid4())
	pollutantid1 = ''.join((pollutantid1).split('-'))
	pollutantid2 = str(uuid.uuid4())
	pollutantid2 = ''.join((pollutantid2).split('-'))
	PM2_5_0 = ''
	CO_0 = ''
	O3_0 = ''
	NO2_0 = ''
	PM10_0 = ''
	SO2_0 = ''
	TIMEPOINT_0 = ''
	AQI_0 = ''
	QUALITY_0 = ''
	PRIMARYPOLLUTANT_0 = ''
	aqi_so2_0 = ''
	aqi_no2_0 = ''
	aqi_co_0 = ''
	aqi_o3_0 = ''
	aqi_pm10_0 = ''
	aqi_pm25_0 = ''

	PM2_5_1 = ''
	CO_1 = ''
	O3_1 = ''
	NO2_1 = ''
	PM10_1 = ''
	SO2_1 = ''
	TIMEPOINT_1 = ''
	AQI_1 = ''
	QUALITY_1 = ''
	PRIMARYPOLLUTANT_1 = ''
	aqi_so2_1 = ''
	aqi_no2_1 = ''
	aqi_co_1 = ''
	aqi_o3_1 = ''
	aqi_pm10_1 = ''
	aqi_pm25_1 = ''

	PM2_5_2 = ''
	CO_2 = ''
	O3_2 = ''
	NO2_2 = ''
	PM10_2 = ''
	SO2_2 = ''
	TIMEPOINT_2 = ''
	AQI_2 = ''
	QUALITY_2 = ''
	PRIMARYPOLLUTANT_2 = ''
	aqi_so2_2 = ''
	aqi_no2_2 = ''
	aqi_co_2 = ''
	aqi_o3_2 = ''
	aqi_pm10_2 = ''
	aqi_pm25_2 = ''
	for each_result0 in json_result:
		time0_total = year_now+'-'+each_result0['TIMEPOINT1']+':00'
		each_time_result0 = datetime.datetime.strptime(time0_total,'%Y-%m-%d %H:%M:%S')
		if time_now_total == each_time_result0:
			AQI_0 = each_result0['AQI']
			QUALITY_0 = each_result0['QUALITY']
			if QUALITY_0 == 'I':
				QUALITY_0 = '95646F517C03404191A1D975A8C663AE'
			elif QUALITY_0 == 'II':
				QUALITY_0 = '2c9385fe3f887442013f88b961e6004b'
			elif QUALITY_0 == 'III':
				QUALITY_0 = '2c9385fe3f996311013f99f75f180031'
			elif QUALITY_0 == 'IV':
				QUALITY_0 = '2c9385fe3f996311013f99f7e2c00035'
			elif QUALITY_0 == 'V':
				QUALITY_0 = '2c9385fe3f996311013f99f87c2c0039'
			elif QUALITY_0 == 'VI':
				QUALITY_0 = '2c9385fe3f996311013f99f91413003d'
			else:
				QUALITY_0 = ''
			PRIMARYPOLLUTANT_0 = each_result0['PRIMARYPOLLUTANT']
		if time_last1_hour == each_time_result0:
			AQI_1 = each_result0['AQI']
			QUALITY_1 = each_result0['QUALITY']
			if QUALITY_1 == 'I':
				QUALITY_1 = '95646F517C03404191A1D975A8C663AE'
			elif QUALITY_1 == 'II':
				QUALITY_1 = '2c9385fe3f887442013f88b961e6004b'
			elif QUALITY_1 == 'III':
				QUALITY_1 = '2c9385fe3f996311013f99f75f180031'
			elif QUALITY_1 == 'IV':
				QUALITY_1 = '2c9385fe3f996311013f99f7e2c00035'
			elif QUALITY_1 == 'V':
				QUALITY_1 = '2c9385fe3f996311013f99f87c2c0039'
			elif QUALITY_1 == 'VI':
				QUALITY_1 = '2c9385fe3f996311013f99f91413003d'
			else:
				QUALITY_1 = ''
			PRIMARYPOLLUTANT_1 = each_result0['PRIMARYPOLLUTANT']
		if time_last2_hour == each_time_result0:
			AQI_2 = each_result0['AQI']
			QUALITY_2 = each_result0['QUALITY']
			if QUALITY_2 == 'I':
				QUALITY_2 = '95646F517C03404191A1D975A8C663AE'
			elif QUALITY_2 == 'II':
				QUALITY_2 = '2c9385fe3f887442013f88b961e6004b'
			elif QUALITY_2 == 'III':
				QUALITY_2 = '2c9385fe3f996311013f99f75f180031'
			elif QUALITY_2 == 'IV':
				QUALITY_2 = '2c9385fe3f996311013f99f7e2c00035'
			elif QUALITY_2 == 'V':
				QUALITY_2 = '2c9385fe3f996311013f99f87c2c0039'
			elif QUALITY_2 == 'VI':
				QUALITY_2 = '2c9385fe3f996311013f99f91413003d'
			else:
				QUALITY_2 = ''
			PRIMARYPOLLUTANT_2 = each_result0['PRIMARYPOLLUTANT']
	for each_result1 in json_result1:
		each_time_result1 = datetime.datetime.strptime(each_result1['TIMEPOINT'],'%Y-%m-%d %H:%M:%S')
		if time_now_total == each_time_result1:
			aqi_so2_0 = each_result1['ISO2']
			aqi_no2_0 = each_result1['INO2']
			aqi_co_0 = each_result1['ICO']
			aqi_o3_0 = each_result1['IO3']
			aqi_pm10_0 = each_result1['IPM10']
			aqi_pm25_0 = each_result1['IPM2_5']
		if time_last1_hour == each_time_result1:
			aqi_so2_1 = each_result1['ISO2']
			aqi_no2_1 = each_result1['INO2']
			aqi_co_1 = each_result1['ICO']
			aqi_o3_1 = each_result1['IO3']
			aqi_pm10_1 = each_result1['IPM10']
			aqi_pm25_1 = each_result1['IPM2_5']
		if time_last2_hour == each_time_result1:
			aqi_so2_2 = each_result1['ISO2']
			aqi_no2_2 = each_result1['INO2']
			aqi_co_2 = each_result1['ICO']
			aqi_o3_2 = each_result1['IO3']
			aqi_pm10_2 = each_result1['IPM10']
			aqi_pm25_2 = each_result1['IPM2_5']
	for each_result2 in json_result2:
		each_time_result2 = datetime.datetime.strptime(each_result2['TIMEPOINT'],'%Y-%m-%d %H:%M:%S')
		if time_now_total == each_time_result2:
			PM2_5_0 = each_result2['PM2_5']
			CO_0 = each_result2['CO']
			O3_0 = each_result2['O3']
			NO2_0 = each_result2['NO2']
			PM10_0 = each_result2['PM10']
			SO2_0 = each_result2['SO2']
			TIMEPOINT_0 = time_now_total
		if time_last1_hour == each_time_result2:
			PM2_5_1 = each_result2['PM2_5']
			CO_1 = each_result2['CO']
			O3_1 = each_result2['O3']
			NO2_1 =  each_result2['NO2']
			PM10_1 = each_result2['PM10']
			SO2_1 = each_result2['SO2']
			TIMEPOINT_1 = time_last1_hour
		if time_last2_hour == each_time_result2:
			PM2_5_2 = each_result2['PM2_5']
			CO_2 = each_result2['CO']
			O3_2 = each_result2['O3']
			NO2_2 = each_result2['NO2']
			PM10_2 = each_result2['PM10']
			SO2_2 = each_result2['SO2']
			TIMEPOINT_2 = time_last2_hour
	if O3_0 == '—'.decode('utf8'):
		O3_0 = ''
	if SO2_0 == '—'.decode('utf8'):
		SO2_0 = ''
	if NO2_0 == '—'.decode('utf8'):
		NO2_0 = ''
	if PM10_0 == '—'.decode('utf8'):
		PM10_0 = ''
	if PM2_5_0 == '—'.decode('utf8'):
		PM2_5_0 = ''
	if AQI_0 == '—'.decode('utf8'):
		AQI_0 = ''
	if PRIMARYPOLLUTANT_0 == '—'.decode('utf8'):
		PRIMARYPOLLUTANT_0 = ''
	if O3_1 == '—'.decode('utf8'):
		O3_1 = ''
	if SO2_1 == '—'.decode('utf8'):
		SO2_1 = ''
	if NO2_1 == '—'.decode('utf8'):
		NO2_1 = ''
	if PM10_1 == '—'.decode('utf8'):
		PM10_1 = ''
	if PM2_5_1 == '—'.decode('utf8'):
		PM2_5_1 = ''
	if AQI_1 == '—'.decode('utf8'):
		AQI_1 = ''
	if PRIMARYPOLLUTANT_1 == '—'.decode('utf8'):
		PRIMARYPOLLUTANT_1 = ''
	if O3_2 == '—'.decode('utf8'):
		O3_2 = ''
	if SO2_2 == '—'.decode('utf8'):
		SO2_2 = ''
	if NO2_2 == '—'.decode('utf8'):
		NO2_2 = ''
	if PM10_2 == '—'.decode('utf8'):
		PM10_2 = ''
	if PM2_5_2 == '—'.decode('utf8'):
		PM2_5_2 = ''
	if AQI_2 == '—'.decode('utf8'):
		AQI_2 = ''
	if PRIMARYPOLLUTANT_2 == '—'.decode('utf8'):
		PRIMARYPOLLUTANT_2 = ''
	timenow_formal = datetime.datetime.now()
	timenow_afterwards = timenow_formal.strftime("%Y-%m-%d %H:%M:%S")
	sql1 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI,PM10_AQI,PM2D5_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s')"\
	%(pollutantid0,TIMEPOINT_0,AQI_0,PRIMARYPOLLUTANT_0,QUALITY_0,SO2_0,NO2_0,PM10_0,CO_0,O3_0,PM2_5_0,station_name,station_ID,'610200000000',timenow_afterwards,aqi_so2_0,aqi_no2_0,aqi_co_0,aqi_o3_0,aqi_pm10_0,aqi_pm25_0)
	try:
		cursor.execute(sql1)
		conn.commit()
	except:
		logger.error('已有数据',exc_info=1)
	sql2 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI,PM10_AQI,PM2D5_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s')"\
	%(pollutantid1,TIMEPOINT_1,AQI_1,PRIMARYPOLLUTANT_1,QUALITY_1,SO2_1,NO2_1,PM10_1,CO_1,O3_1,PM2_5_1,station_name,station_ID,'610200000000',timenow_afterwards,aqi_so2_1,aqi_no2_1,aqi_co_1,aqi_o3_1,aqi_pm10_1,aqi_pm25_1)
	try:
		cursor.execute(sql2)
		conn.commit()
	except:
		logger.error('已有数据',exc_info=1)
	sql3 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI,PM10_AQI,PM2D5_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s')"\
	%(pollutantid2,TIMEPOINT_2,AQI_2,PRIMARYPOLLUTANT_2,QUALITY_2,SO2_2,NO2_2,PM10_2,CO_2,O3_2,PM2_5_2,station_name,station_ID,'610200000000',timenow_afterwards,aqi_so2_2,aqi_no2_2,aqi_co_2,aqi_o3_2,aqi_pm10_2,aqi_pm25_2)
	try:
		cursor.execute(sql3)
		conn.commit()
	except:
		logger.error('已有数据',exc_info=1)
'''
def spider1(logger,conn):
	url = ('http://113.140.66.226:8024/sxAQIWeb/ashx/getCityStationConcen.ashx?cityCode=610200')
	response = requests.get(url = url,verify=False)
	json_result=  json.loads(response.text)

	sql = "select UUID,ZDMC from CG_HJZL_DQZDXX where SFZS = '1'"
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
				if QUALITY == 'I':
					QUALITY = '95646F517C03404191A1D975A8C663AE'
				elif QUALITY == 'II':
					QUALITY = '2c9385fe3f887442013f88b961e6004b'
				elif QUALITY == 'III':
					QUALITY = '2c9385fe3f996311013f99f75f180031'
				elif QUALITY == 'IV':
					QUALITY = '2c9385fe3f996311013f99f7e2c00035'
				elif QUALITY == 'V':
					QUALITY = '2c9385fe3f996311013f99f87c2c0039'
				elif QUALITY == 'VI':
					QUALITY = '2c9385fe3f996311013f99f91413003d'
				else:
					QUALITY = ''
				PM10 = json_result[i]['PM10']
				AQI = json_result[i]['AQI']
				PRIMARYPOLLUTANT = json_result[i]['PRIMARYPOLLUTANT']
				TIMEPOINT = json_result[i]['TIMEPOINT']
				SO2 = (json_result[i]['SO2'])
				STATIONCODE = json_result[i]['STATIONCODE']
				O3 = (json_result[i]['O3'])
				NO2 = json_result[i]['NO2']
				
				if O3 == '—'.decode('utf8'):
					O3 = ''
				if SO2 == '—'.decode('utf8'):
					SO2 = ''
				if NO2 == '—'.decode('utf8'):
					NO2 = ''
				if PM10 == '—'.decode('utf8'):
					PM10 = ''
				if PM2_5 == '—'.decode('utf8'):
					PM2_5 = ''
				if AQI == '—'.decode('utf8'):
					AQI = ''
				if PRIMARYPOLLUTANT == '—'.decode('utf8'):
					PRIMARYPOLLUTANT = ''
					
				try:
					SO2 = int(SO2)
				except:
					SO2 = ''
				try:
					O3 = int(O3)
				except:
					O3 = ''
				try:
					NO2 = int(NO2)
				except:
					NO2 = ''
				try:
					CO = float(CO)
				except:
					CO = ''
				array_so2 = []
				array_no2 = []
				array_co = []
				array_o3 = []
				if SO2:
					if 0<SO2<150:
						array_so2 = [0,50,0,150]
					elif 150<SO2<500:
						array_so2 = [50,100,150,500]
					elif 500<SO2<650:
						array_so2 = [100,150,500,650]
					elif 650<SO2<800:
						array_so2 = [150,200,650,800]
				if NO2:
					if 0<NO2<100:
						array_no2 = [0,50,0,100]
					elif 100<NO2<200:
						array_no2 = [50,100,100,200]
					elif 200<NO2<700:
						array_no2 = [100,150,200,700]
					elif 700<NO2<1200:
						array_no2 = [150,200,700,1200]
					elif 1200<NO2<2340:
						array_no2 = [200,300,1200,2340]
					elif 2340<NO2<3090:
						array_no2 = [300,400,2340,3090]
					elif 3090<NO2<3840:
						array_no2 = [400,500,3090,3840]
				if CO:
					if 0<CO<5:
						array_co = [0,50,0,5]
					elif 5<CO<10:
						array_co = [50,100,5,10]
					elif 10<CO<35:
						array_co = [100,150,10,35]
					elif 35<CO<60:
						array_co = [150,200,35,60]
					elif 60<CO<90:
						array_co = [200,300,60,90]
					elif 90<CO<120:
						array_co = [300,400,90,120]
					elif 120<CO<150:
						array_co = [400,500,120,150]
				if O3:
					if 0<O3<160:
						array_o3 = [0,50,0,160]
					elif 160<O3<200:
						array_o3 = [50,100,160,200]
					elif 200<O3<300:
						array_o3 = [100,150,200,300]
					elif 300<O3<400:
						array_o3 = [150,200,300,400]
					elif 400<O3<800:
						array_o3 = [200,300,400,800]
					elif 800<O3<1000:
						array_o3 = [300,400,800,1000]
					elif 1000<O3<1200:
						array_o3 = [400,500,1000,1200]
				if array_so2:
					aqi_so2 = ((array_so2[1]-array_so2[0])/(array_so2[3]-array_so2[2]))*(SO2-array_so2[2])+array_so2[0]
					aqi_so2 = str(aqi_so2)
				else:
					aqi_so2 = ''
				if array_no2:
					aqi_no2 = ((array_no2[1]-array_no2[0])/(array_no2[3]-array_no2[2]))*(NO2-array_no2[2])+array_no2[0]
					aqi_no2 = str(aqi_no2)
				else:
					aqi_no2 = ''
				if array_co:
					aqi_co = ((array_co[1]-array_co[0])/(array_co[3]-array_co[2]))*(CO-array_co[2])+array_co[0]
					aqi_co = str(aqi_co)
				else:
					aqi_co = ''
				if array_o3:
					aqi_o3 = ((array_o3[1]-array_o3[0])/(array_o3[3]-array_o3[2]))*(O3-array_o3[2])+array_o3[0]
					aqi_o3 = str(aqi_o3)
				else:
					aqi_o3 = ''
				SO2 = str(SO2)
				NO2 = str(NO2)
				CO = str(CO)
				O3 = str(O3)
				timenow_formal = datetime.datetime.now()
				timenow_afterwards = timenow_formal.strftime("%Y-%m-%d %H:%M:%S")
				sql_search_xzqh = "select SZXZQ from CG_HJZL_DQZDXX where ZDMC = '%s'"%(results[i1][1].decode('gbk'))
				cursor.execute(sql_search_xzqh)
				results_xzqh = cursor.fetchall()
				
				sql1 = "INSERT INTO CG_HJZL_KQAQIXSPJ (UUID,PJSJ,AQI,SYWRW,KQZSDJID,SO2,NO2,PM10,CO,O3,PM2D5,ZDMC,ZDUUID,SZXZQ,GMT_CREATE,SO2_AQI,NO2_AQI,CO_AQI,O3_AQI)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s','%s','%s')"\
				%(pollutantid,TIMEPOINT,AQI,PRIMARYPOLLUTANT,QUALITY,SO2,NO2,PM10,CO,O3,PM2_5,station_name,station_ID,results_xzqh[0][0],timenow_afterwards,aqi_so2,aqi_no2,aqi_co,aqi_o3)
				try:
					cursor.execute(sql1)
					conn.commit()
				except:
					logger.error('已有数据',exc_info=1)
for kk in range(9999999):
	#module_path = '/usr/txjson/'
	module_path = 'F:/tongchuan_spider'
	LOG_FILE = module_path+'/spider1.log'
	handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024*1024, backupCount = 5) # 实例化handler 
	fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
	formatter = logging.Formatter(fmt)   # 实例化formatter
	handler.setFormatter(formatter)      # 为handler添加formatter
	logger = logging.getLogger('logging')
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	conn = cx_Oracle.connect('tchbdc_new/tchbdc_new@172.18.0.104/orcl')
	cursor = conn.cursor()
	#spider1是所有点的小时数据
	
	try:
		spider1(logger,conn)
		#logger.info('spider1没错 成功')
	except:
		time.sleep(10)
		logger.error('spider1有错 失败',exc_info=1)
	#spider2是铜川总点的小时数据
	
	try:
		spider2(logger,conn)
		#logger.info('spider1没错 成功')
	except:
		time.sleep(10)
		logger.error('spider2有错 失败',exc_info=1)
	#spider3是铜川总点的日数据
	try:
		spider3(conn)
	except:
		time.sleep(10)
		logger.error('spider3有错 失败',exc_info=1)
	conn.close()
	handler.close()
	time.sleep(900)