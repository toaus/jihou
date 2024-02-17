# jihou v1.1
# Copyright 2023-2024 toaus()
import datetime
import time
import threading
import pygame
import os
import sys
import locale
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
pygame.mixer.init()
wav500hz = pygame.mixer.Sound("500hz.wav")
wav1000hz = pygame.mixer.Sound("1000hz.wav")
wav2000hz = pygame.mixer.Sound("2000hz.wav")
#voice
#will
#will = pygame.mixer.Sound("voice/tadaimakara.wav")
#hour
vh0 = pygame.mixer.Sound("voice/h0.wav")
vh1 = pygame.mixer.Sound("voice/h1.wav")
vh2 = pygame.mixer.Sound("voice/h2.wav")
vh3 = pygame.mixer.Sound("voice/h3.wav")
vh4 = pygame.mixer.Sound("voice/h4.wav")
vh5 = pygame.mixer.Sound("voice/h5.wav")
vh6 = pygame.mixer.Sound("voice/h6.wav")
vh7 = pygame.mixer.Sound("voice/h7.wav")
vh8 = pygame.mixer.Sound("voice/h8.wav")
vh9 = pygame.mixer.Sound("voice/h9.wav")
vh10 = pygame.mixer.Sound("voice/h10.wav")
vh11 = pygame.mixer.Sound("voice/h11.wav")
dvh = {}
for hcount in range(12):
	dvh[hcount]= 'vh' + str(hcount)
#dvh = {0:"vh0",1:"vh1",2:"vh2",3:"vh3",4:"vh4",5:"vh5",6:"vh6",7:"vh7",8:"vh8",9:"vh9",10:"vh10",11:"vh11"}
#minute
vm1x10 = pygame.mixer.Sound("voice/m1x10.wav")
vm2x10 = pygame.mixer.Sound("voice/m2x10.wav")
vm3x10 = pygame.mixer.Sound("voice/m3x10.wav")
vm4x10 = pygame.mixer.Sound("voice/m4x10.wav")
vm5x10 = pygame.mixer.Sound("voice/m5x10.wav")
vm1 = pygame.mixer.Sound("voice/m1.wav")
vm2 = pygame.mixer.Sound("voice/m2.wav")
vm3 = pygame.mixer.Sound("voice/m3.wav")
vm4 = pygame.mixer.Sound("voice/m4.wav")
vm5 = pygame.mixer.Sound("voice/m5.wav")
vm6 = pygame.mixer.Sound("voice/m6.wav")
vm7 = pygame.mixer.Sound("voice/m7.wav")
vm8 = pygame.mixer.Sound("voice/m8.wav")
vm9 = pygame.mixer.Sound("voice/m9.wav")
vm10 = pygame.mixer.Sound("voice/m10.wav")
vm20 = pygame.mixer.Sound("voice/m20.wav")
vm30 = pygame.mixer.Sound("voice/m30.wav")
vm40 = pygame.mixer.Sound("voice/m40.wav")
vm50 = pygame.mixer.Sound("voice/m50.wav")
dvmx10 = {'1':"vm1x10",'2':"vm2x10",'3':"vm3x10",'4':"vm4x10",'5':"vm5x10"}
dvm1 = {}
for mcount in range(10):
	dvm1[mcount] = 'vm' + str(mcount)
dvm10 = {1:"vm10",2:"vm20",3:"vm30",4:"vm40",5:"vm50"}
#second
vs0 = pygame.mixer.Sound("voice/s0.wav")
vs10 = pygame.mixer.Sound("voice/s10.wav")
vs20 = pygame.mixer.Sound("voice/s20.wav")
vs30 = pygame.mixer.Sound("voice/s30.wav")
vs40 = pygame.mixer.Sound("voice/s40.wav")
vs50 = pygame.mixer.Sound("voice/s50.wav")
dvs = {0:"vs0", 10:"vs10",20:"vs20",30:"vs30",40:"vs40",50:"vs50"}

#shogo
shogo = pygame.mixer.Sound("voice/shogo.wav")
shogo_time = shogo.get_length()
#ampm
am = pygame.mixer.Sound("voice/am.wav")
pm = pygame.mixer.Sound("voice/pm.wav")
#oshirase
oshirase = pygame.mixer.Sound("voice/oshirase.wav")

#program
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channel1.set_endevent(25)
dt = datetime.datetime.now()
sec1 = dt.second
os.system('cls')
def voice(hour,minute,second):
	pm12 = 0
	time.sleep(2)
	nextsecond = second + 10
	nextminute = minute
	nexthour = hour
	if nextsecond == 60:
		nextminute = minute + 1
		nextsecond = 0
		if nextminute == 60:
			nexthour = hour + 1
			if nexthour == 12:
				pm12 = 1
				nexthour = 0
			elif nexthour == 24:
				nexthour = 0
			nextminute = 0
	#正午は特別扱い
	if pm12 == 1:
		channel1.queue(shogo)
		time.sleep(shogo_time)
		channel1.queue(oshirase)
	else:
		#午前午後の判別
		if nexthour < 12:
			nextampm = 0
		else:
			nextampm = 1
			nexthour = nexthour - 12
		#ボイス生成
		#ただいまから
		# ampm_time = will.get_length()
		# channel1.queue(will)
		# time.sleep(ampm_time+0.01)
		
		# AM/PM
		if nextampm == 0:
			ampm_time = am.get_length()
			channel1.queue(am)
			time.sleep(ampm_time+0.05) #おかしい場合は適宜調整
		elif nextampm == 1:
			ampm_time = pm.get_length()
			channel1.queue(pm)
			time.sleep(ampm_time+0.05) #おかしい場合は適宜調整
		#時
		channel1.queue(eval(dvh[nexthour]))
		hour_time = eval(dvh[nexthour]).get_length()
		time.sleep(hour_time+0.05) #おかしい場合は適宜調整
		#分
		playmin = str(nextminute).zfill(2)
		playmin10 = str(playmin)[-2]
		playmin1 = str(playmin)[-1]
		if playmin10 == '0' and playmin1 == '0': #ちょうど
			pass
		elif playmin10 == '0' and playmin1 != '0': #1~9の場合
			channel1.queue(eval(dvm1[int(playmin1)]))
			min_time1 = eval(dvm1[int(playmin1)]).get_length()
			time.sleep(min_time1+0.05)
		elif playmin10 != '0' and playmin1 == '0': #10の倍数の場合
			channel1.queue(eval(dvm10[int(playmin10)]))
			min_time1 = eval(dvm10[int(playmin10)]).get_length()
			time.sleep(min_time1+0.05)
		else: #それ以外
			channel1.queue(eval(dvmx10[playmin10]))
			min_time1 = eval(dvmx10[playmin10]).get_length()
			time.sleep(min_time1+0.05)
			channel1.queue(eval(dvm1[int(playmin1)]))
			min_time2 = eval(dvm1[int(playmin1)]).get_length()
			time.sleep(min_time2+0.05)
		#秒	
		channel1.queue(eval(dvs[nextsecond]))
		sec_time = eval(dvs[nextsecond]).get_length()
		time.sleep(sec_time)
		#お知らせします
		channel1.queue(oshirase)

try:
	while True:
		dt = datetime.datetime.now()
		hour = dt.hour
		minu = dt.minute
		sec2 = dt.second
		micro = dt.microsecond
		print('\r'+dt.strftime("%Y-%m-%d %a %p %I:%M:%S.%f"), end='') #出力
		#sec1が前、sec2が後
		if sec2 > sec1 or (sec1 - sec2) == 59:
			wav2000hz.play()
			if (sec2 % 10) == 0:
				wav1000hz.play()
				sec1 = sec2
				t_voice = threading.Thread(target=voice,args=(hour,minu,sec1)) #ボイス再生スレッド
				t_voice.start()
			elif sec2 == 27 or sec2 == 28 or sec2 == 29 or sec2 == 57 or sec2 == 58 or sec2 == 59:
				wav500hz.play()
				sec1 = sec2
			else:
				sec1 = sec2
		time.sleep(0.0001)
except KeyboardInterrupt:
	sys.exit(0)
