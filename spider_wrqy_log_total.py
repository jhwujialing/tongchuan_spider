#-*- coding:utf-8 -*-
import cx_Oracle
import logging
import logging.handlers
import uuid
import requests
import json
from scrapy.selector import Selector
import datetime
import time
def spider_zdpwqy(conn,logger):
	sql1 = "select TYPE,NAME,ID,EXTRA from QYXX where TYPE = 'ZDPW'"
	cursor.execute(sql1)
	results = cursor.fetchall()
	for i in range(len(results)):
		qytype = results[i][0]
		qymc = results[i][1]
		qyid = results[i][2]
		extra = results[i][3]
		pollutantid=str(uuid.uuid4())
		l_uuid=pollutantid.split('-')
		pollutantid=''.join(l_uuid)
		url = 'http://113.140.66.227:9777/envinfo_ps/'+extra+'/tocorp?corpid='+qyid+'&areacode='
		try:
			response = requests.get(url = url,verify=False)#,timeout=5
		except:
			logger.error('timeout',exc_info=1)

		qymc = ''
		cym = ''
		zzjgdm = ''
		hylb = ''
		fddbr = ''
		jcbm = ''
		zclx = ''
		qygm = ''
		lxdh = ''
		cz = ''
		lxr = ''
		qydz = ''
		try:
			qymc = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[2]/text()').extract())[0]
		except:
			logger.error('qymc 失败',exc_info=1)
		try:
			cym = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[4]/text()').extract())[0]
		except:
			logger.error('cym 失败',exc_info=1)
		try:
			zzjgdm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[6]/text()').extract())[0]
		except:
			logger.error('zzjgdm 失败',exc_info=1)
		try:
			hylb = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[2]/text()').extract())[0]
		except:
			logger.error('hylb 失败',exc_info=1)

		#qylb = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[3]/text()').extract())[0]
		try:
			fddbr = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[6]/text()').extract())[0]
		except:
			logger.error('fddbr 失败',exc_info=1)
		try:
			jcbm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[2]/text()').extract())[0]
		except:
			logger.error('jcbm 失败',exc_info=1)
		try:
			zclx = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[4]/text()').extract())[0]
		except:
			logger.error('zclx 失败',exc_info=1)
		try:
			qygm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[6]/text()').extract())[0]
		except:
			logger.error('qygm 失败',exc_info=1)
		try:
			lxdh = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[2]/text()').extract())[0]
		except:
			logger.error('lxdh 失败',exc_info=1)
		try:
			cz = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[4]/text()').extract())[0]
		except:
			logger.error('cz 失败',exc_info=1)
		try:
			lxr = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[6]/text()').extract())[0]
		except:
			logger.error('lxr 失败',exc_info=1)
		try:
			qydz = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[5]/td[2]/text()').extract())[0]
		except:
			logger.error('qydz 失败',exc_info=1)
		sql1 = "select PSCODE from PS_BASE_INFO where PSNAME = '%s'"%(qymc)
		
		cursor.execute(sql1)
		results1 = cursor.fetchall()
		pscode = results1[0][0]

		#sqljbxx1 = "INSERT INTO PS_BASE_INFO (PSCODE,PSNAME,CYM,ZZJGDM,HYLB,CORPORATIONNAME,JCBM,ZCLX,QYGM,OFFICEPHONE,FAX,LXR,PSADDRESS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
		#%(pollutantid,qymc,cym,zzjgdm,hylb,fddbr,jcbm,zclx,qygm,lxdh,cz,lxr,qydz)
		#cursor.execute(sqljbxx1)
		#conn.commit()
		total_tr = (str(Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody').extract()).count('tr'))/2
		array_dwmcfq = []
		array_dwmcfs = []

		for j in range(total_tr):
			dwmc = ''
			dwlx = ''
			dwsx = ''
			wd = ''
			jd = ''
			try:
				dwmc = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[1]/text()').extract())[0]
			except:
				logger.error('dwmc 失败',exc_info=1)
			try:
				dwlx = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[2]/text()').extract())[0]
			except:
				logger.error('dwlx 失败',exc_info=1)
			try:
				dwsx = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[3]/text()').extract())[0]
			except:
				logger.error('dwlx 失败',exc_info=1)
			try:
				jd = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[4]/text()').extract())[0]
				
				number1 =  jd.find('°'.decode('utf8'))
				number2 =  jd.find('′'.decode('utf8'))
				number3 =  jd.find('″'.decode('utf8'))
				if number2 == 1:
					jd = 0
				else:
					jd = float(jd[:number1])+float(jd[number1+1:number2])/60+float(jd[number2+1:number3])/3600
				jd = round(jd,3)
			except:
				logger.error('jd 失败',exc_info=1)

			try:
				wd = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[5]/text()').extract())[0]
				
				_number1 =  wd.find('°'.decode('utf8'))
				_number2 =  wd.find('′'.decode('utf8'))
				_number3 =  wd.find('″'.decode('utf8'))
				if _number2 == 1:
					wd = 0
				else:
					wd = float(wd[:_number1])+float(wd[_number1+1:_number2])/60+float(wd[_number2+1:_number3])/3600
				wd = round(wd,3)
				
			except:
				logger.error('wd 失败',exc_info=1)
			if '废气'.decode('utf8') in dwlx:
				pfkid=str(uuid.uuid4())
				l_uuid=pfkid.split('-')
				pfkid=''.join(l_uuid)
				array_dwmcfq.append(dwmc)
				if jd == 0 or wd == 0:
					sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,DWSX)VALUES('%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,dwsx)
				else:
					sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,LONGITUDE,LATITUDE,DWSX)VALUES('%s','%s','%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,jd,wd,dwsx)
				try:
					cursor.execute(sql_gas_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			elif '废水'.decode('utf8') in dwlx or '污水处理厂'.decode('utf8') in dwlx or '河'.decode('utf8') in dwlx:
				array_dwmcfs.append(dwmc)
				pfkid=str(uuid.uuid4())
				l_uuid=pfkid.split('-')
				pfkid=''.join(l_uuid)
				if jd == 0 or wd == 0:
					
					sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,DWSX)VALUES('%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,dwsx)
				else:
					sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,LONGITUDE,LATITUDE,DWSX)VALUES('%s','%s','%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,jd,wd,dwsx)
				try:
					cursor.execute(sql_water_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
					
		total_tr1 = (str(Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]').extract())).count('tr')/2
		
		for k in range(total_tr1):
			
			jcdw = ''
			jcrq = ''
			jcxm = ''
			wrwnd = ''
			pfxz = ''
			dw = ''
			cbbs = ''
			try:
				jcdw = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[1]/text()').extract())[0]
			except:
				logger.error('jcdw 失败',exc_info=1)

			try:
				jcrq = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[2]/text()').extract())[0]
			except:
				logger.error('jcrq 失败',exc_info=1)
			try:
				jcxm = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[3]/text()').extract())[0]
			except:
				logger.error('jcxm 失败',exc_info=1)
			if '颗粒物'.decode('utf8') in jcxm or '烟尘'.decode('utf8') in jcxm or '氮氧化物'.decode('utf8') in jcxm or '二氧化硫'.decode('utf8') in jcxm or '一氧化碳'.decode('utf8') in jcxm or '氯化氢'.decode('utf8') in jcxm or '氧气'.decode('utf8') in jcxm:
				sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME)VALUES('%s','%s','%s')"\
				%(pscode,pfkid,jcdw)
				try:
					cursor.execute(sql_gas_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			elif 'pH' in jcxm or 'PH' in jcxm or '磷'.decode('utf8') in jcxm or ('氮'.decode('utf8') in jcxm and '氮氧化物'.decode('utf8') not in jcxm) or '氨氮'.decode('utf8') in jcxm or '铜'.decode('utf8') in jcxm or '镍'.decode('utf8') in jcxm or '氟'.decode('utf8') in jcxm or '六价铬'.decode('utf8') in jcxm or '三价铬'.decode('utf8') in jcxm or '化学需氧量'.decode('utf8') in jcxm:
				sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME)VALUES('%s','%s','%s')"\
				%(pscode,pfkid,jcdw)
				try:
					cursor.execute(sql_water_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			try:
				wrwnd = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[4]/text()').extract())[0]
			except:
				logger.error('wrwnd 失败',exc_info=1)
			try:
				pfxz = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[5]/text()').extract())[0]
			except:
				logger.error('pfxz 失败',exc_info=1)
			try:
				dw = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[6]/text()').extract())[0]
			except:
				logger.error('dw 失败',exc_info=1)
			try:
				cbbs = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[7]/text()').extract())[0]
			except:
				logger.error('cbbs 失败',exc_info=1)
			
			sql_read1 = "select OUTPUTCODE from PS_GAS_OUTPUT where PSCODE = '%s' and OUTPUTNAME = '%s' and SFZXJC is null"%(pscode,jcdw)
			sql_read2 = "select OUTPUTCODE from PS_WATER_OUTPUT where PSCODE = '%s' and OUTPUTNAME = '%s' and SFZXJC is null"%(pscode,jcdw)
			cursor.execute(sql_read1)
			results_gas = cursor.fetchall()
			cursor.execute(sql_read2)
			results_water = cursor.fetchall()

			try:
				if results_gas:
					outputcode = results_gas[0][0]
					monitortime = datetime.datetime.strptime(jcrq,'%Y-%m-%d %H')
					monitortime = monitortime.strftime("%Y-%m-%d %H:%M:%S")
					wrwnd = wrwnd
					if '颗粒物'.decode('utf8') in jcxm or '烟尘'.decode('utf8') in jcxm:
						try:
							sql_insert_gas1 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,SOOT)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas1)
							conn.commit()
						except:
							sql_update_gas1 = "UPDATE PS_GAS_HOUR_DATA SET SOOT = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas1)
							conn.commit()
					if '氮氧化物'.decode('utf8') in jcxm:
						try:
							sql_insert_gas2 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,NOX)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas2)
							conn.commit()
						except:
							sql_update_gas2 = "UPDATE PS_GAS_HOUR_DATA SET NOX = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas2)
							conn.commit()
					if '二氧化硫'.decode('utf8') in jcxm:
						try:
							sql_insert_gas3 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,SO2)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas3)
							conn.commit()
						except:
							sql_update_gas3 = "UPDATE PS_GAS_HOUR_DATA SET SO2 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas3)
							conn.commit()
					if '一氧化碳'.decode('utf8') in jcxm:
						try:
							sql_insert_gas4 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,CO)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas4)
							conn.commit()
						except:
							sql_update_gas4 = "UPDATE PS_GAS_HOUR_DATA SET CO = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas4)
							conn.commit()
					if '氯化氢'.decode('utf8') in jcxm:
						try:
							sql_insert_gas5 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,HCL)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas5)
							conn.commit()
						except:
							sql_update_gas5 = "UPDATE PS_GAS_HOUR_DATA SET HCL = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas5)
							conn.commit()
					if '氧气'.decode('utf8') in jcxm:
						try:
							sql_insert_gas6 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,O2)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas6)
							conn.commit()
						except:
							sql_update_gas6 = "UPDATE PS_GAS_HOUR_DATA SET O2 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas6)
							conn.commit()

				if results_water:
					outputcode = results_water[0][0]
					monitortime = datetime.datetime.strptime(jcrq,'%Y-%m-%d %H')
					monitortime = monitortime.strftime("%Y-%m-%d %H:%M:%S")
					wrwnd = wrwnd
					if 'pH' in jcxm or 'PH' in jcxm:
						try:
							sql_insert_water1 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,PH)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water1)
							conn.commit()
						except:
							sql_update_water1 = "UPDATE PS_WATER_HOUR_DATA SET PH = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water1)
							conn.commit()
					if '磷'.decode('utf8') in jcxm:
						try:
							sql_insert_water2 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZL)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water2)
							conn.commit()
						except:
							sql_update_water2 = "UPDATE PS_WATER_HOUR_DATA SET ZL = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water2)
							conn.commit()
					if '氮'.decode('utf8') in jcxm and '氨氮'.decode('utf8') not in jcxm:
						try:
							sql_insert_water3 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZD)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water3)
							conn.commit()
						except:
							sql_update_water3 = "UPDATE PS_WATER_HOUR_DATA SET ZD = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water3)
							conn.commit()
					if '氨氮'.decode('utf8') in jcxm:
						try:
							sql_insert_water4 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,NH3)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water4)
							conn.commit()
						except:
							sql_update_water4 = "UPDATE PS_WATER_HOUR_DATA SET NH3 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water4)
							conn.commit()
					if '铜'.decode('utf8') in jcxm:
						try:
							sql_insert_water5 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZT)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water5)
							conn.commit()
						except:
							sql_update_water5 = "UPDATE PS_WATER_HOUR_DATA SET ZT = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water5)
							conn.commit()
					if '镍'.decode('utf8') in jcxm:
						try:
							sql_insert_water6 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZM)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water6)
							conn.commit()
						except:
							sql_update_water6 = "UPDATE PS_WATER_HOUR_DATA SET ZM = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water6)
							conn.commit()
					if '氟'.decode('utf8') in jcxm:
						try:
							sql_insert_water7 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,FLZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water7)
							conn.commit()
						except:
							sql_update_water7 = "UPDATE PS_WATER_HOUR_DATA SET FLZ = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water7)
							conn.commit()
					if '六价铬'.decode('utf8') in jcxm:
						try:
							sql_insert_water8 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,LJG)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water8)
							conn.commit()
						except:
							sql_update_water8 = "UPDATE PS_WATER_HOUR_DATA SET LJG = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water8)
							conn.commit()
					if '三价铬'.decode('utf8') in jcxm:
						try:
							sql_insert_water9 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,SJG)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water9)
							conn.commit()
						except:
							sql_update_water9 = "UPDATE PS_WATER_HOUR_DATA SET SJG = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water9)
							conn.commit()
					if '化学需氧量'.decode('utf8') in jcxm:
						try:
							sql_insert_water10 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,COD)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water10)
							conn.commit()
						except:
							sql_update_water10 = "UPDATE PS_WATER_HOUR_DATA SET COD = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water10)
							conn.commit()
			except:
				logger.error('存小时数据 失败',exc_info=1)
def spider_zdjkqy(conn,logger):
	sql1 = "select TYPE,NAME,ID,EXTRA from QYXX where TYPE = 'ZDJK'"
	cursor.execute(sql1)
	results = cursor.fetchall()
	for i in range(len(results)):
		qytype = results[i][0]
		qymc = results[i][1].decode('gbk')
		qyid = results[i][2]
		extra = results[i][3]
		pollutantid=str(uuid.uuid4())
		l_uuid=pollutantid.split('-')
		pollutantid=''.join(l_uuid)
		
		url = 'http://113.140.66.227:9777/envinfo_ps/publicity/tocorp?'+extra+'&corpname='+qymc+'&areacode=610200'
		
		#url = 'http://113.140.66.227:9777/envinfo_ps/'+extra+'/tocorp?corpid='+qyid+'&areacode='
		try:
			response = requests.get(url = url,verify=False)#,timeout=5
		except:
			logger.error('timeout',exc_info=1)
		
		qymc = ''
		cym = ''
		zzjgdm = ''
		hylb = ''
		fddbr = ''
		jcbm = ''
		zclx = ''
		qygm = ''
		lxdh = ''
		cz = ''
		lxr = ''
		qydz = ''
		try:
			qymc = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[2]/text()').extract())[0]
			
		except:
			logger.error('qymc 失败',exc_info=1)
		
		try:
			cym = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[4]/text()').extract())[0]
		except:
			logger.error('cym 失败',exc_info=1)
		try:
			zzjgdm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[6]/text()').extract())[0]
		except:
			logger.error('zzjgdm 失败',exc_info=1)
		try:
			hylb = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[2]/text()').extract())[0]
		except:
			logger.error('hylb 失败',exc_info=1)

		#qylb = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[3]/text()').extract())[0]
		try:
			fddbr = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[6]/text()').extract())[0]
		except:
			logger.error('fddbr 失败',exc_info=1)
		try:
			jcbm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[2]/text()').extract())[0]
		except:
			logger.error('jcbm 失败',exc_info=1)
		try:
			zclx = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[4]/text()').extract())[0]
		except:
			logger.error('zclx 失败',exc_info=1)
		try:
			qygm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[6]/text()').extract())[0]
		except:
			logger.error('qygm 失败',exc_info=1)
		try:
			lxdh = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[2]/text()').extract())[0]
		except:
			logger.error('lxdh 失败',exc_info=1)
		try:
			cz = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[4]/text()').extract())[0]
		except:
			logger.error('cz 失败',exc_info=1)
		try:
			lxr = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[6]/text()').extract())[0]
		except:
			logger.error('lxr 失败',exc_info=1)
		try:
			qydz = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[5]/td[2]/text()').extract())[0]
		except:
			logger.error('qydz 失败',exc_info=1)
		'''sqljbxx1 = "INSERT INTO PS_BASE_INFO (PSCODE,PSNAME,CYM,ZZJGDM,HYLB,CORPORATIONNAME,JCBM,ZCLX,QYGM,OFFICEPHONE,FAX,LXR,PSADDRESS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
		%(pollutantid,qymc,cym,zzjgdm,hylb,fddbr,jcbm,zclx,qygm,lxdh,cz,lxr,qydz)
		try:
			cursor.execute(sqljbxx1)
			conn.commit()
			print 1
		except:
			print 2'''
		
		sql1 = "select PSCODE from PS_BASE_INFO where PSNAME = '%s'"%(qymc)
		
		cursor.execute(sql1)
		results1 = cursor.fetchall()
		pscode = results1[0][0]


		total_tr = (str(Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody').extract()).count('tr'))/2
		array_dwmcfq = []
		array_dwmcfs = []
		
		for j in range(total_tr):
			dwmc = ''
			dwlx = ''
			dwwz = ''
			pffs = ''
			pfqx = ''
			cywz = ''
			try:
				dwmc = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[1]/text()').extract())[0]
				
			except:
				logger.error('dwmc 失败',exc_info=1)
			try:
				dwlx = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[2]/text()').extract())[0]
			except:
				logger.error('dwlx 失败',exc_info=1)
			try:
				dwwz  = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[3]/text()').extract())[0]
			except:
				logger.error('dwwz 失败',exc_info=1)
			try:
				pffs = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[4]/text()').extract())[0]
			except:
				logger.error('pffs 失败',exc_info=1)
			try:
				pfqx = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[5]/text()').extract())[0]
			except:
				logger.error('pfqx 失败',exc_info=1)
			try:
				cywz = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[5]/text()').extract())[0]
			except:
				logger.error('cywz 失败',exc_info=1)

			if '废气'.decode('utf8') in dwlx:
				pfkid=str(uuid.uuid4())
				l_uuid=pfkid.split('-')
				pfkid=''.join(l_uuid)
				array_dwmcfq.append(dwmc)
				sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,OUTPUTPOSITION,PFFS,PFQX,CYWZ)VALUES('%s','%s','%s','%s','%s','%s','%s')"\
				%(pscode,pfkid,dwmc,dwwz,pffs,pfqx,cywz)
				try:
					cursor.execute(sql_gas_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			elif '废水'.decode('utf8') in dwlx or '污水处理厂'.decode('utf8') in dwlx or '河'.decode('utf8') in dwlx:
				array_dwmcfs.append(dwmc)
				pfkid=str(uuid.uuid4())
				l_uuid=pfkid.split('-')
				pfkid=''.join(l_uuid)
				sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,OUTPUTPOSITION,PFFS,PFQX,CYWZ)VALUES('%s','%s','%s','%s','%s','%s','%s')"\
				%(pscode,pfkid,dwmc,dwwz,pffs,pfqx,cywz)
				try:
					cursor.execute(sql_water_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
		total_tr1 = (str(Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]').extract())).count('tr')/2
		for k in range(total_tr1):
			
			jcdw = ''
			jcrq = ''
			jcxm = ''
			wrwnd = ''
			pfxz = ''
			dw = ''
			cbbs = ''
			zxbz = ''
			pfkid=str(uuid.uuid4())
			l_uuid=pfkid.split('-')
			pfkid=''.join(l_uuid)
			try:

				jcdw = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[1]/text()').extract())[0]
				
			except:
				logger.error('jcdw 失败',exc_info=1)
			try:
				jcrq = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[2]/text()').extract())[0]
			except:
				logger.error('jcrq 失败',exc_info=1)
			try:
				jcxm = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[3]/text()').extract())[0]
			except:
				logger.error('jcxm 失败',exc_info=1)
			if '颗粒物'.decode('utf8') in jcxm or '烟尘'.decode('utf8') in jcxm or '氮氧化物'.decode('utf8') in jcxm or '二氧化硫'.decode('utf8') in jcxm or '一氧化碳'.decode('utf8') in jcxm or '氯化氢'.decode('utf8') in jcxm or '氧气'.decode('utf8') in jcxm:
				sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME)VALUES('%s','%s','%s')"\
				%(pscode,pfkid,jcdw)
				try:
					cursor.execute(sql_gas_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			elif 'pH' in jcxm or 'PH' in jcxm or '磷'.decode('utf8') in jcxm or ('氮'.decode('utf8') in jcxm and '氮氧化物'.decode('utf8') not in jcxm) or '氨氮'.decode('utf8') in jcxm or '铜'.decode('utf8') in jcxm or '镍'.decode('utf8') in jcxm or '氟'.decode('utf8') in jcxm or '六价铬'.decode('utf8') in jcxm or '三价铬'.decode('utf8') in jcxm or '化学需氧量'.decode('utf8') in jcxm:
				sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME)VALUES('%s','%s','%s')"\
				%(pscode,pfkid,jcdw)
				try:
					cursor.execute(sql_water_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			try:
				wrwnd = str((Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[5]').extract()))
				wrwnd_number1 = wrwnd.find('eval(')
				wrwnd_rest = wrwnd[wrwnd_number1+5:]
				wrwnd_number2 = wrwnd_rest.find(')')
				wrwnd = wrwnd_rest[:wrwnd_number2]
			except:
				logger.error('wrwnd 失败',exc_info=1)
			
			try:
				pfxz = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[6]/text()').extract())[0]
			except:
				logger.error('pfxz 失败',exc_info=1)
			try:
				dw = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[7]/text()').extract())[0]
			except:
				logger.error('dw 失败',exc_info=1)
			try:
				cbbs = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[8]/text()').extract())[0]
			except:
				logger.error('cbbs 失败',exc_info=1)
			try:
				zxbz = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[9]/text()').extract())[0]
			except:
				logger.error('cbbs 失败',exc_info=1)
			sql_read1 = "select OUTPUTCODE from PS_GAS_OUTPUT where PSCODE = '%s' and OUTPUTNAME = '%s' and SFZXJC is null"%(pscode,jcdw)
			sql_read2 = "select OUTPUTCODE from PS_WATER_OUTPUT where PSCODE = '%s' and OUTPUTNAME = '%s' and SFZXJC is null"%(pscode,jcdw)
			cursor.execute(sql_read1)
			results_gas = cursor.fetchall()
			cursor.execute(sql_read2)
			results_water = cursor.fetchall()
			try:
				if results_gas:
					outputcode = results_gas[0][0]
					monitortime = datetime.datetime.strptime(jcrq,'%Y-%m-%d %H')
					monitortime = monitortime.strftime("%Y-%m-%d %H:%M:%S")
					wrwnd = wrwnd
					
					if '颗粒物'.decode('utf8') in jcxm or '烟尘'.decode('utf8') in jcxm:
						#print outputcode,monitortime,wrwnd,zxbz
						try:
							sql_insert_gas1 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,SOOT,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_gas1)
							conn.commit()
						except:
							sql_update_gas1 = "UPDATE PS_GAS_HOUR_DATA SET SOOT = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas1)
							conn.commit()
					if '氮氧化物'.decode('utf8') in jcxm:
						try:
							sql_insert_gas2 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,NOX,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_gas2)
							conn.commit()
						except:
							sql_update_gas2 = "UPDATE PS_GAS_HOUR_DATA SET NOX = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas2)
							conn.commit()
					if '二氧化硫'.decode('utf8') in jcxm:
						try:
							sql_insert_gas3 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,SO2,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_gas3)
							conn.commit()
						except:
							sql_update_gas3 = "UPDATE PS_GAS_HOUR_DATA SET SO2 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas3)
							conn.commit()
					if '一氧化碳'.decode('utf8') in jcxm:
						try:
							sql_insert_gas4 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,CO,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_gas4)
							conn.commit()
						except:
							sql_update_gas4 = "UPDATE PS_GAS_HOUR_DATA SET CO = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas4)
							conn.commit()
					if '氯化氢'.decode('utf8') in jcxm:
						try:
							sql_insert_gas5 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,HCL,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_gas5)
							conn.commit()
						except:
							sql_update_gas5 = "UPDATE PS_GAS_HOUR_DATA SET HCL = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas5)
							conn.commit()
					if '氧气'.decode('utf8') in jcxm:
						try:
							sql_insert_gas6 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,O2,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_gas6)
							conn.commit()
						except:
							sql_update_gas6 = "UPDATE PS_GAS_HOUR_DATA SET O2 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas6)
							conn.commit()

				if results_water:
					outputcode = results_water[0][0]
					monitortime = datetime.datetime.strptime(jcrq,'%Y-%m-%d %H')
					monitortime = monitortime.strftime("%Y-%m-%d %H:%M:%S")
					wrwnd = wrwnd
					if 'pH' in jcxm or 'PH' in jcxm:
						try:
							sql_insert_water1 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,PH,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water1)
							conn.commit()
						except:
							sql_update_water1 = "UPDATE PS_WATER_HOUR_DATA SET PH = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water1)
							conn.commit()
					if '磷'.decode('utf8') in jcxm:
						try:
							sql_insert_water2 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZL,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water2)
							conn.commit()
						except:
							sql_update_water2 = "UPDATE PS_WATER_HOUR_DATA SET ZL = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water2)
							conn.commit()
					if '氮'.decode('utf8') in jcxm and '氨氮'.decode('utf8') not in jcxm:
						try:
							sql_insert_water3 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZD,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water3)
							conn.commit()
						except:
							sql_update_water3 = "UPDATE PS_WATER_HOUR_DATA SET ZD = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water3)
							conn.commit()
					if '氨氮'.decode('utf8') in jcxm:
						try:
							sql_insert_water4 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,NH3,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water4)
							conn.commit()
						except:
							sql_update_water4 = "UPDATE PS_WATER_HOUR_DATA SET NH3 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water4)
							conn.commit()
					if '铜'.decode('utf8') in jcxm:
						try:
							sql_insert_water5 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZT,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water5)
							conn.commit()
						except:
							sql_update_water5 = "UPDATE PS_WATER_HOUR_DATA SET ZT = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water5)
							conn.commit()
					if '镍'.decode('utf8') in jcxm:
						try:
							sql_insert_water6 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZM,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water6)
							conn.commit()
						except:
							sql_update_water6 = "UPDATE PS_WATER_HOUR_DATA SET ZM = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water6)
							conn.commit()
					if '氟'.decode('utf8') in jcxm:
						try:
							sql_insert_water7 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,FLZ,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water7)
							conn.commit()
						except:
							sql_update_water7 = "UPDATE PS_WATER_HOUR_DATA SET FLZ = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water7)
							conn.commit()
					if '六价铬'.decode('utf8') in jcxm:
						try:
							sql_insert_water8 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,LJG,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water8)
							conn.commit()
						except:
							sql_update_water8 = "UPDATE PS_WATER_HOUR_DATA SET LJG = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water8)
							conn.commit()
					if '三价铬'.decode('utf8') in jcxm:
						try:
							sql_insert_water9 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,SJG,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water9)
							conn.commit()
						except:
							sql_update_water9 = "UPDATE PS_WATER_HOUR_DATA SET SJG = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water9)
							conn.commit()
					if '化学需氧量'.decode('utf8') in jcxm:
						
						try:
							sql_insert_water10 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,COD,ZXBZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s','%s')"\
							%(outputcode,monitortime,wrwnd,zxbz)
							cursor.execute(sql_insert_water10)
							conn.commit()
						except:
							
							sql_update_water10 = "UPDATE PS_WATER_HOUR_DATA SET COD = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water10)
							conn.commit()
			except:
				logger.error('存储 失败',exc_info=1)

def spider_pwxkzqy(conn,logger):
	qyid = '1'
	
	sql1 = "select TYPE,NAME,ID,EXTRA from QYXX where TYPE = 'PWXKZ'"
	cursor.execute(sql1)
	results = cursor.fetchall()
	for i in range(len(results)):
		qytype = results[i][0]
		qymc = results[i][1].decode('gbk')
		qyid = results[i][2]
		extra = results[i][3]
		pollutantid=str(uuid.uuid4())
		l_uuid=pollutantid.split('-')
		pollutantid=''.join(l_uuid)
		url = 'http://113.140.66.227:9777/envinfo_ps/gjxkzpublicity/tocorp?corpid='+qyid+'&areacode=610200'
		#url = 'http://113.140.66.227:9777/envinfo_ps/publicity/tocorp?corpid=610200000003&wrtype=FQ&devid=177&corpname='+qymc+'&areacode=610200'
		#url = 'http://113.140.66.227:9777/envinfo_ps/'+extra+'/tocorp?corpid='+qyid+'&areacode='
		try:
			response = requests.get(url = url,verify=False)#,timeout=5
		except:
			logger.error('timeout',exc_info=1)

		qymc = ''
		cym = ''
		zzjgdm = ''
		hylb = ''
		fddbr = ''
		jcbm = ''
		zclx = ''
		qygm = ''
		lxdh = ''
		cz = ''
		lxr = ''
		qydz = ''
		try:
			qymc = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[2]/text()').extract())[0]
		except:
			logger.error('qymc 失败',exc_info=1)
		try:
			cym = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[4]/text()').extract())[0]
		except:
			logger.error('cym 失败',exc_info=1)
		try:
			zzjgdm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[1]/td[6]/text()').extract())[0]
		except:
			logger.error('zzjgdm 失败',exc_info=1)
		try:
			hylb = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[2]/text()').extract())[0]
		except:
			logger.error('hylb 失败',exc_info=1)

		#qylb = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[3]/text()').extract())[0]
		try:
			fddbr = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[2]/td[6]/text()').extract())[0]
		except:
			logger.error('fddbr 失败',exc_info=1)
		try:
			jcbm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[2]/text()').extract())[0]
		except:
			logger.error('jcbm 失败',exc_info=1)
		try:
			zclx = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[4]/text()').extract())[0]
		except:
			logger.error('zclx 失败',exc_info=1)
		try:
			qygm = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[3]/td[6]/text()').extract())[0]
		except:
			logger.error('qygm 失败',exc_info=1)
		try:
			lxdh = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[2]/text()').extract())[0]
		except:
			logger.error('lxdh 失败',exc_info=1)
		try:
			cz = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[4]/text()').extract())[0]
		except:
			logger.error('cz 失败',exc_info=1)
		try:
			lxr = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[4]/td[6]/text()').extract())[0]
		except:
			logger.error('lxr 失败',exc_info=1)
		try:
			qydz = (Selector(text=response.text).xpath('//table[@id="comparison"]/tr[5]/td[2]/text()').extract())[0]
		except:
			logger.error('qydz 失败',exc_info=1)
		'''sqljbxx1 = "INSERT INTO PS_BASE_INFO (PSCODE,PSNAME,CYM,ZZJGDM,HYLB,CORPORATIONNAME,JCBM,ZCLX,QYGM,OFFICEPHONE,FAX,LXR,PSADDRESS)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
		%(pollutantid,qymc,cym,zzjgdm,hylb,fddbr,jcbm,zclx,qygm,lxdh,cz,lxr,qydz)
		try:
			cursor.execute(sqljbxx1)
			conn.commit()
			print 1
		except:
			print 2'''
		
		sql1 = "select PSCODE from PS_BASE_INFO where PSNAME = '%s'"%(qymc)
		
		cursor.execute(sql1)
		results1 = cursor.fetchall()
		pscode = results1[0][0]


		total_tr = (str(Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody').extract()).count('tr'))/2
		array_dwmcfq = []
		array_dwmcfs = []

		for j in range(total_tr):
			dwmc = ''
			dwlx = ''
			dwsx = ''
			wd = ''
			jd = ''
			try:
				dwmc = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[1]/text()').extract())[0]
			except:
				logger.error('dwmc 失败',exc_info=1)
			try:
				dwlx = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[2]/text()').extract())[0]
			except:
				logger.error('dwlx 失败',exc_info=1)
			try:
				dwsx = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[3]/text()').extract())[0]
			except:
				logger.error('dwlx 失败',exc_info=1)
			try:
				jd = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[4]/text()').extract())[0]
				
				number1 =  jd.find('°'.decode('utf8'))
				number2 =  jd.find('′'.decode('utf8'))
				number3 =  jd.find('″'.decode('utf8'))
				if number2 == 1:
					jd = 0
				else:
					jd = float(jd[:number1])+float(jd[number1+1:number2])/60+float(jd[number2+1:number3])/3600
				jd = round(jd,3)
			except:
				logger.error('jd 失败',exc_info=1)

			try:
				wd = (Selector(text=response.text).xpath('//div[@id="h1"]/table/tbody/tr['+str(j+1)+']/td[5]/text()').extract())[0]
				
				_number1 =  wd.find('°'.decode('utf8'))
				_number2 =  wd.find('′'.decode('utf8'))
				_number3 =  wd.find('″'.decode('utf8'))
				if _number2 == 1:
					wd = 0
				else:
					wd = float(wd[:_number1])+float(wd[_number1+1:_number2])/60+float(wd[_number2+1:_number3])/3600
				wd = round(wd,3)
				
			except:
				logger.error('wd 失败',exc_info=1)
			if '废气'.decode('utf8') in dwlx:
				pfkid=str(uuid.uuid4())
				l_uuid=pfkid.split('-')
				pfkid=''.join(l_uuid)
				array_dwmcfq.append(dwmc)
				if jd == 0 or wd == 0:
					sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,DWSX)VALUES('%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,dwsx)
				else:
					sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,LONGITUDE,LATITUDE,DWSX)VALUES('%s','%s','%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,jd,wd,dwsx)
				try:
					cursor.execute(sql_gas_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			elif '废水'.decode('utf8') in dwlx or '污水处理厂'.decode('utf8') in dwlx or '河'.decode('utf8') in dwlx:
				array_dwmcfs.append(dwmc)
				pfkid=str(uuid.uuid4())
				l_uuid=pfkid.split('-')
				pfkid=''.join(l_uuid)
				if jd == 0 or wd == 0:
					
					sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,DWSX)VALUES('%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,dwsx)
				else:
					sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME,LONGITUDE,LATITUDE,DWSX)VALUES('%s','%s','%s','%s','%s','%s')"\
					%(pscode,pfkid,dwmc,jd,wd,dwsx)
				try:
					cursor.execute(sql_water_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
		total_tr1 = (str(Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]').extract())).count('tr')/2
		
		for k in range(total_tr1):
			
			jcdw = ''
			jcrq = ''
			jcxm = ''
			wrwnd = ''
			pfxz = ''
			dw = ''
			cbbs = ''

			try:
				jcdw = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[1]/text()').extract())[0]
			except:
				logger.error('jcdw 失败',exc_info=1)

			try:
				jcrq = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[2]/text()').extract())[0]
			except:
				logger.error('jcrq 失败',exc_info=1)
			try:
				jcxm = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[3]/text()').extract())[0]
			except:
				logger.error('jcxm 失败',exc_info=1)
			if '颗粒物'.decode('utf8') in jcxm or '烟尘'.decode('utf8') in jcxm or '氮氧化物'.decode('utf8') in jcxm or '二氧化硫'.decode('utf8') in jcxm or '一氧化碳'.decode('utf8') in jcxm or '氯化氢'.decode('utf8') in jcxm or '氧气'.decode('utf8') in jcxm:
				sql_gas_output = "INSERT INTO PS_GAS_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME)VALUES('%s','%s','%s')"\
				%(pscode,pfkid,jcdw)
				try:
					cursor.execute(sql_gas_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			elif 'pH' in jcxm or 'PH' in jcxm or '磷'.decode('utf8') in jcxm or ('氮'.decode('utf8') in jcxm and '氮氧化物'.decode('utf8') not in jcxm) or '氨氮'.decode('utf8') in jcxm or '铜'.decode('utf8') in jcxm or '镍'.decode('utf8') in jcxm or '氟'.decode('utf8') in jcxm or '六价铬'.decode('utf8') in jcxm or '三价铬'.decode('utf8') in jcxm or '化学需氧量'.decode('utf8') in jcxm:
				sql_water_output = "INSERT INTO PS_WATER_OUTPUT (PSCODE,OUTPUTCODE,OUTPUTNAME)VALUES('%s','%s','%s')"\
				%(pscode,pfkid,jcdw)
				try:
					cursor.execute(sql_water_output)
					conn.commit()
				except:
					logger.error('存 失败',exc_info=1)
			try:
				wrwnd = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[4]/text()').extract())[0]
			except:
				logger.error('wrwnd 失败',exc_info=1)
			try:
				pfxz = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[5]/text()').extract())[0]
			except:
				logger.error('pfxz 失败',exc_info=1)
			try:
				dw = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[6]/text()').extract())[0]
			except:
				logger.error('dw 失败',exc_info=1)
			try:
				cbbs = (Selector(text=response.text).xpath('//tbody[@id="zxjczxsjtbl"]/tr['+str(k+1)+']/td[7]/text()').extract())[0]
			except:
				logger.error('cbbs 失败',exc_info=1)
			sql_read1 = "select OUTPUTCODE from PS_GAS_OUTPUT where PSCODE = '%s' and OUTPUTNAME = '%s' and SFZXJC is null"%(pscode,jcdw)
			sql_read2 = "select OUTPUTCODE from PS_WATER_OUTPUT where PSCODE = '%s' and OUTPUTNAME = '%s' and SFZXJC is null"%(pscode,jcdw)
			cursor.execute(sql_read1)
			results_gas = cursor.fetchall()
			cursor.execute(sql_read2)
			results_water = cursor.fetchall()
			try:
				if results_gas:
					outputcode = results_gas[0][0]
					monitortime = datetime.datetime.strptime(jcrq,'%Y-%m-%d %H')
					monitortime = monitortime.strftime("%Y-%m-%d %H:%M:%S")
					wrwnd = wrwnd
					if '颗粒物'.decode('utf8') in jcxm or '烟尘'.decode('utf8') in jcxm:
						try:
							sql_insert_gas1 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,SOOT)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas1)
							conn.commit()
						except:
							sql_update_gas1 = "UPDATE PS_GAS_HOUR_DATA SET SOOT = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas1)
							conn.commit()
					if '氮氧化物'.decode('utf8') in jcxm:
						try:
							sql_insert_gas2 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,NOX)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas2)
							conn.commit()
						except:
							sql_update_gas2 = "UPDATE PS_GAS_HOUR_DATA SET NOX = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas2)
							conn.commit()
					if '二氧化硫'.decode('utf8') in jcxm:
						try:
							sql_insert_gas3 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,SO2)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas3)
							conn.commit()
						except:
							sql_update_gas3 = "UPDATE PS_GAS_HOUR_DATA SET SO2 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas3)
							conn.commit()
					if '一氧化碳'.decode('utf8') in jcxm:
						try:
							sql_insert_gas4 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,CO)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas4)
							conn.commit()
						except:
							sql_update_gas4 = "UPDATE PS_GAS_HOUR_DATA SET CO = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas4)
							conn.commit()
					if '氯化氢'.decode('utf8') in jcxm:
						try:
							sql_insert_gas5 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,HCL)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas5)
							conn.commit()
						except:
							sql_update_gas5 = "UPDATE PS_GAS_HOUR_DATA SET HCL = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas5)
							conn.commit()
					if '氧气'.decode('utf8') in jcxm:
						try:
							sql_insert_gas6 = "INSERT INTO PS_GAS_HOUR_DATA (OUTPUTCODE,MONITORTIME,O2)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_gas6)
							conn.commit()
						except:
							sql_update_gas6 = "UPDATE PS_GAS_HOUR_DATA SET O2 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_gas6)
							conn.commit()

				if results_water:
					outputcode = results_water[0][0]
					monitortime = datetime.datetime.strptime(jcrq,'%Y-%m-%d %H')
					monitortime = monitortime.strftime("%Y-%m-%d %H:%M:%S")
					wrwnd = wrwnd
					if 'pH' in jcxm or 'PH' in jcxm:
						try:
							sql_insert_water1 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,PH)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water1)
							conn.commit()
						except:
							sql_update_water1 = "UPDATE PS_WATER_HOUR_DATA SET PH = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water1)
							conn.commit()
					if '磷'.decode('utf8') in jcxm:
						try:
							sql_insert_water2 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZL)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water2)
							conn.commit()
						except:
							sql_update_water2 = "UPDATE PS_WATER_HOUR_DATA SET ZL = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water2)
							conn.commit()
					if '氮'.decode('utf8') in jcxm and '氨氮'.decode('utf8') not in jcxm:
						try:
							sql_insert_water3 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZD)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water3)
							conn.commit()
						except:
							sql_update_water3 = "UPDATE PS_WATER_HOUR_DATA SET ZD = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water3)
							conn.commit()
					if '氨氮'.decode('utf8') in jcxm:
						try:
							sql_insert_water4 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,NH3)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water4)
							conn.commit()
						except:
							sql_update_water4 = "UPDATE PS_WATER_HOUR_DATA SET NH3 = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water4)
							conn.commit()
					if '铜'.decode('utf8') in jcxm:
						try:
							sql_insert_water5 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZT)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water5)
							conn.commit()
						except:
							sql_update_water5 = "UPDATE PS_WATER_HOUR_DATA SET ZT = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water5)
							conn.commit()
					if '镍'.decode('utf8') in jcxm:
						try:
							sql_insert_water6 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,ZM)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water6)
							conn.commit()
						except:
							sql_update_water6 = "UPDATE PS_WATER_HOUR_DATA SET ZM = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water6)
							conn.commit()
					if '氟'.decode('utf8') in jcxm:
						try:
							sql_insert_water7 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,FLZ)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water7)
							conn.commit()
						except:
							sql_update_water7 = "UPDATE PS_WATER_HOUR_DATA SET FLZ = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water7)
							conn.commit()
					if '六价铬'.decode('utf8') in jcxm:
						try:
							sql_insert_water8 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,LJG)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water8)
							conn.commit()
						except:
							sql_update_water8 = "UPDATE PS_WATER_HOUR_DATA SET LJG = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water8)
							conn.commit()
					
					if '三价铬'.decode('utf8') in jcxm:
						try:
							sql_insert_water9 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,SJG)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water9)
							conn.commit()
						except:
							sql_update_water9 = "UPDATE PS_WATER_HOUR_DATA SET SJG = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water9)
							conn.commit()
					if '化学需氧量'.decode('utf8') in jcxm:
						try:
							sql_insert_water10 = "INSERT INTO PS_WATER_HOUR_DATA (OUTPUTCODE,MONITORTIME,COD)VALUES('%s',to_date(\'%s\','yyyy-MM-dd HH24:MI:SS'),'%s')"\
							%(outputcode,monitortime,wrwnd)
							cursor.execute(sql_insert_water10)
							conn.commit()
						except:
							sql_update_water10 = "UPDATE PS_WATER_HOUR_DATA SET COD = '%s' where OUTPUTCODE = '%s' and MONITORTIME = to_date(\'%s\','yyyy-MM-dd HH24:MI:SS')"%(wrwnd,outputcode,monitortime)
							cursor.execute(sql_update_water10)
							conn.commit()
			except:
				logger.error('存小时数据 失败',exc_info=1)
				
for kk in range(9999999):
	module_path = 'F:/tongchuan_spider'
	LOG_FILE = module_path+'/spider3.log'
	handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024*1024, backupCount = 5) # 实例化handler 
	fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
	formatter = logging.Formatter(fmt)   # 实例化formatter
	handler.setFormatter(formatter)      # 为handler添加formatter
	logger = logging.getLogger('logging')
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	conn = cx_Oracle.connect('tchbdc_new/tchbdc_new@172.18.0.104/orcl')
	cursor = conn.cursor()
	#http://113.140.66.227:9777/envinfo_ps/zdypublicity/list
	try:
		spider_zdpwqy(conn,logger)
	except:
		time.sleep(10)
		logger.error('spider_zdpwqy 失败',exc_info=1)
	#http://113.140.66.227:9777/envinfo_ps/publicity/list
	try:
		spider_zdjkqy(conn,logger)
	except:
		time.sleep(10)
		logger.error('spider_zdjkqy 失败',exc_info=1)
	#http://113.140.66.227:9777/envinfo_ps/gjxkzpublicity/list
	try:
		spider_pwxkzqy(conn,logger)
	except:
		time.sleep(10)
		logger.error('spider_pwxkzqy 失败',exc_info=1)
	
	conn.close()
	handler.close()
	#print 123
	time.sleep(900)