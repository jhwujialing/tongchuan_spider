#-*- coding:utf-8 -*-
from __future__ import division
import requests
import json
from scrapy.selector import Selector
import cx_Oracle
import uuid
import datetime
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
pollutantid = str(uuid.uuid4())
pollutantid = ''.join((pollutantid).split('-'))
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
conn = cx_Oracle.connect('tchbdc/tchbdc@172.18.0.104/orcl')
cursor = conn.cursor()
for each_result0 in json_result:
	time0_total = year_now+'-'+each_result0['TIMEPOINT1']+':00'
	each_time_result0 = datetime.datetime.strptime(time0_total,'%Y-%m-%d %H:%M:%S')
	if time_now_total == each_time_result0:
		AQI_0 = each_result0['AQI']
		QUALITY_0 = each_result0['QUALITY']
		PRIMARYPOLLUTANT_0 = each_result0['PRIMARYPOLLUTANT']
	if time_last1_hour == each_time_result0:
		AQI_1 = each_result0['AQI']
		QUALITY_1 = each_result0['QUALITY']
		PRIMARYPOLLUTANT_1 = each_result0['PRIMARYPOLLUTANT']
	if time_last2_hour == each_time_result0:
		AQI_2 = each_result0['AQI']
		QUALITY_2 = each_result0['QUALITY']
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
timenow_formal = datetime.datetime.now()
timenow_afterwards = timenow_formal.strftime("%Y-%m-%d %H:%M:%S")

print PM2_5_0,CO_0,O3_0,NO2_0,PM10_0,SO2_0,TIMEPOINT_0,AQI_0,QUALITY_0,PRIMARYPOLLUTANT_0,aqi_so2_0,aqi_no2_0,aqi_co_0,aqi_o3_0,aqi_pm10_0,aqi_pm25_0
print PM2_5_1,CO_1,O3_1,NO2_1,PM10_1,SO2_1,TIMEPOINT_1,AQI_1,QUALITY_1,PRIMARYPOLLUTANT_1,aqi_so2_1,aqi_no2_1,aqi_co_1,aqi_o3_1,aqi_pm10_1,aqi_pm25_1
print PM2_5_2,CO_2,O3_2,NO2_2,PM10_2,SO2_2,TIMEPOINT_2,AQI_2,QUALITY_2,PRIMARYPOLLUTANT_2,aqi_so2_2,aqi_no2_2,aqi_co_2,aqi_o3_2,aqi_pm10_2,aqi_pm25_2
conn.close()
'''
selector = Selector(response = response)

content = selector.xpath('//*[@id="1001A"]')
print content'''
