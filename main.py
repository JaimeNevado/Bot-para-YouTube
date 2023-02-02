from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from datetime import datetime, timedelta  
import pyautogui as pg
import time

import os

Mouse = Controller()
keyboard = Controller()

def print_logo():
	print("\n")
	print("██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗    ██╗   ██╗██████╗ ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ ")
	print("╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
	print(" ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗      ██║   ██║██████╔╝██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝")
	print("  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██║   ██║██╔═══╝ ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗")
	print("   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗    ╚██████╔╝██║     ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║")
	print("   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
	print("														    By Jaime Nevado")

def click_in(x, y, wait, speed):
	pg.moveTo(x, y ,speed)
	pg.click()
	time.sleep(wait)

def cmd_letter(letter, wait):
	keyboard.press(Key.cmd)
	keyboard.press(letter)
	time.sleep(wait)
	keyboard.release(Key.cmd)
	keyboard.release(letter)

def main():

	i = 0
	day = 1
	y = 308
	speed = 0.1
	hour_count = 2				#Start hour (08:00h + hour_count)
	total_videos_uploaded = 0	

	#Get how many videos we have to upload
	lst = os.listdir("/Users/jaimenevado/Desktop/Bot-para-YouTube/videos")
	number_files = len(lst) - 1

	print_logo()

	mode = int(input("Select an option: \n1) Default Option (Upload it tomorrow and x3 times a day) \n2)Customize it\n\n"))

	if mode == 1:
		fecha = (datetime.now() + timedelta(day) ).strftime('%d/%m/%Y')		#Default date (tomorrow)
		every_x_hours = 3													#Default time between uploads
		uploads_per_day = 3													#Default uploads per day
	elif mode == 2:
		fecha = input("Select upload date: (dd/mm/yyyy)\n")						#Custom date (dd/mm/yyyy)
		every_x_hours = int(input("Select hours between upload:\n"))			#Custom time between uploads
		uploads_per_day = int(input("Select uploads per day:\n"))				#Custom uploads per day
	else:
		print("Error on the values")
		exit()

	os.system("open http://youtube.com")

	time.sleep(3)

	#Fullscreen chrome
	click_in(114, 48, 3, 0)

	while (total_videos_uploaded < number_files):

		while (i < uploads_per_day and total_videos_uploaded < number_files):

			#Camera button
			click_in(1273, 138, 1, 0)

			#Upload video
			click_in(1184, 185, 2, 0)

			#Select files
			click_in(724, 619, 2, 0)

			#Select video
			click_in(500, y, 1, 0)

			#Open button
			click_in(1067, 664, 5, 0)
			
			#Visibility button
			click_in(1062, 274, 2, 0)

			#Program video button
			click_in(321, 701, 2, 0)

			#Date box button
			click_in(414, 573, 2, 0)

			#Select date text
			cmd_letter('a', 1)

			#Paste date text (Ex: 14/01/2023)
			keyboard.type((datetime.strptime(fecha, '%d/%m/%Y') + timedelta(day) ).strftime('%d/%m/%Y'))
			time.sleep(2)

			#Hour box botton
			click_in(540, 575, 1, 0.2)
			click_in(540, 575, 1, 0.2)

			#Select hour text
			cmd_letter('a', 1)

			time.sleep(1)

			#Hours able to write
			hours = ["08:00","09:00","10:00","11:00","12:00",
					"13:00","14:00","15:00","16:00","17:00",
					"18:00","19:00","20:00","21:00","22:00",
					"23:00","00:00","01:00","02:00","03:00",
					"04:00","05:00","06:00","07:00"]

			#Write an hour inside the array		
			keyboard.type(hours[hour_count])
			hour_count += every_x_hours

			#Upload video button
			click_in(1126, 826, 3, 0.2)

			#Close (END)
			click_in(928, 650, 1, 0.2)

			i += 1
			total_videos_uploaded += 1
			y += 20
			time.sleep(1)
		day += 1
		hour_count = every_x_hours
		i = 0

	print("\n\n")
	print("----------------------------------------")
	print(f"The {total_videos_uploaded} videos has been uploaded succesfully")
	print("----------------------------------------")
	print("\n\n")

if __name__ == '__main__':
	main()