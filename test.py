from __future__ import division
import time
import datetime
import requests
import json

timenow_formal = datetime.datetime.now()
year_now = str(timenow_formal)[:4]
month_now = str(timenow_formal)[5:7]
day_now = str(timenow_formal)[8:10]
hour_now = str(timenow_formal)[11:13]
str_time = year_now+'-'+month_now+'-'+day_now+' '+hour_now+':00:00'
time_now_total = datetime.datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
time_last1_hour = time_now_total-datetime.timedelta(hours=1)
time_last2_hour = time_now_total-datetime.timedelta(hours=2)


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
aqi_pm10_2 = ''
aqi_pm25_2 = ''
for each_result2 in json_result2:
	each_time_result2 = datetime.datetime.strptime(each_result2['TIMEPOINT'],'%Y-%m-%d %H:%M:%S')
	if time_now_total == each_time_result2:
		PM2_5_0 = each_result2[i]['PM2_5']
		CO_0 = each_result2[i]['CO']
		O3_0 = each_result2[i]['O3']
		NO2_0 = each_result2[i]['NO2']
		PM10_0 = each_result2[i]['PM10']
		SO2_0 = each_result2[i]['SO2']
		TIMEPOINT_0 = time_now_total
	if time_last1_hour == each_time_result2:
		PM2_5_1 = each_result2[i]['PM2_5']
		CO_1 = each_result2[i]['CO']
		O3_1 = each_result2[i]['O3']
		NO2_1 =  each_result2[i]['NO2']
		PM10_1 = each_result2[i]['PM10']
		SO2_1 = each_result2[i]['SO2']
		TIMEPOINT_1 = time_last1_hour
	if time_last2_hour == each_time_result2:
		PM2_5_2 = each_result2[i]['PM2_5']
		CO_2 = each_result2[i]['CO']
		O3_2 = each_result2[i]['O3']
		NO2_2 = each_result2[i]['NO2']
		PM10_2 = each_result2[i]['PM10']
		SO2_2 = each_result2[i]['SO2']
		TIMEPOINT_2 = time_last2_hour

