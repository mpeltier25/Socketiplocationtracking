import geoip2.database
import socket
#Tell the program where the Geolite database file is
databasedirectory=input("Enter the directory that the Geolite database is located ex. /home/name/Desktop/test folder/GeoLite2-City.mmdb NOTE: this program will print everything out to the screen\n")
reader = geoip2.database.Reader(databasedirectory)
#Tell the program where to read the text file
file_reading=input("Please enter the directory that the csdev01.txt file is located ex. /home/name/Desktop/test folder/csdev01.txt\n")
file=open(file_reading, "r")
#Do a for loop for each line. Had trouble getting the socket part to work with it, but I got the right infornameion below.
for line in file:
    print(line)
    #print(socket.gethostbyname_ex(line) [2])
file.close()
#Close the file, else things get messy.
#Using sockets to determine exact ip, and then reading the various places the people are logging in from, ignoring 10.x.x.x as you specified, the bridgew.edu network is also being ignored since I can't read it from my network.
mysocket=print(socket.gethostbyname_ex("c-75-67-160-236.hsd1.ma.comcast.net")[2])
print("This connection has 1 connections")
response = reader.city('75.67.160.236')
print("This is the country iso code: ", response.country.iso_code)
print("This is the country name: ", response.country.name)
print ("This is the subdivisions most specific name: ", response.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response.city.name)
print ("This is the response postal code: ", response.postal.code)
print ("This is the location latitude: ", response.location.latitude)
print ("This is the location longitude: ", response.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket2=print(socket.gethostbyname_ex('c-24-62-199-228.hsd1.ma.comcast.net')[2])
print("This connection has 13 connections")
response2 = reader.city('24.62.199.228')
print("This is the country iso code: ", response2.country.iso_code)
print("This is the country name: ", response2.country.name)
print ("This is the subdivisions most specific name: ", response2.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response2.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response2.city.name)
print ("This is the response postal code: ", response2.postal.code)
print ("This is the location latitude: ", response2.location.latitude)
print ("This is the location longitude: ", response2.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket3=print(socket.gethostbyname_ex('pool-96-237-160-10.bstnma.fios.verizon.net')[2])
print("This connection has 2 connections")
response3 = reader.city('96.237.160.10')
print("This is the country iso code: ", response3.country.iso_code)
print("This is the country name: ", response3.country.name)
print ("This is the subdivisions most specific name: ", response3.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response3.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response3.city.name)
print ("This is the response postal code: ", response3.postal.code)
print ("This is the location latitude: ", response3.location.latitude)
print ("This is the location longitude: ", response3.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket4=print(socket.gethostbyname_ex('c-75-69-226-190.hsd1.ma.comcast.net')[2])
print("This connection has 4 connections")
response4 = reader.city('75.69.226.190')
print("This is the country iso code: ", response4.country.iso_code)
print("This is the country name: ", response4.country.name)
print ("This is the subdivisions most specific name: ", response4.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response4.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response4.city.name)
print ("This is the response postal code: ", response4.postal.code)
print ("This is the location latitude: ", response4.location.latitude)
print ("This is the location longitude: ", response4.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket5=print(socket.gethostbyname_ex('75.sub-70-215-3.myvzw.com')[2])
print("This connection has 1 connections")
response5 = reader.city('70.215.3.75')
print("This is the country iso code: ", response5.country.iso_code)
print("This is the country name: ", response5.country.name)
print ("This is the subdivisions most specific name: ", response5.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response5.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response5.city.name)
print ("This is the response postal code: ", response5.postal.code)
print ("This is the location latitude: ", response5.location.latitude)
print ("This is the location longitude: ", response5.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket6=print(socket.gethostbyname_ex('c-98-216-57-242.hsd1.ma.comcast.net')[2])
print("This connection has 2 connections")
response6 = reader.city('98.216.57.242')
print("This is the country iso code: ", response6.country.iso_code)
print("This is the country name: ", response6.country.name)
print ("This is the subdivisions most specific name: ", response6.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response6.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response6.city.name)
print ("This is the response postal code: ", response6.postal.code)
print ("This is the location latitude: ", response6.location.latitude)
print ("This is the location longitude: ", response6.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket7=print(socket.gethostbyname_ex('pool-108-20-25-218.bstnma.fios.verizon.net')[2])
print("This connection has 16 connections")
response7 = reader.city('108.20.25.218')
print("This is the country iso code: ", response7.country.iso_code)
print("This is the country name: ", response7.country.name)
print ("This is the subdivisions most specific name: ", response7.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response7.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response7.city.name)
print ("This is the response postal code: ", response7.postal.code)
print ("This is the location latitude: ", response7.location.latitude)
print ("This is the location longitude: ", response7.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket9=print(socket.gethostbyname_ex('50.12.149.153')[2])
print("This connection has 2 connections")
response9 = reader.city('50.12.149.153')
print("This is the country iso code: ", response9.country.iso_code)
print("This is the country name: ", response9.country.name)
print ("This is the subdivisions most specific name: ", response9.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response9.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response9.city.name)
print ("This is the response postal code: ", response9.postal.code)
print ("This is the location latitude: ", response9.location.latitude)
print ("This is the location longitude: ", response9.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket10=print(socket.gethostbyname_ex('c-76-24-113-111.hsd1.ma.comcast.net')[2])
print("This connection has 1 connections")
response10 = reader.city('76.24.113.111')
print("This is the country iso code: ", response10.country.iso_code)
print("This is the country name: ", response10.country.name)
print ("This is the subdivisions most specific name: ", response10.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response10.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response10.city.name)
print ("This is the response postal code: ", response10.postal.code)
print ("This is the location latitude: ", response10.location.latitude)
print ("This is the location longitude: ", response10.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket11=print(socket.gethostbyname_ex('pool-71-162-121-241.bstnma.fios.verizon.net')[2])
print("This connection has 3 connections")
response11 = reader.city('71.162.121.241')
print("This is the country iso code: ", response11.country.iso_code)
print("This is the country name: ", response11.country.name)
print ("This is the subdivisions most specific name: ", response11.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response11.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response11.city.name)
print ("This is the response postal code: ", response11.postal.code)
print ("This is the location latitude: ", response11.location.latitude)
print ("This is the location longitude: ", response11.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket12=print(socket.gethostbyname_ex('mobile-198-228-197-043.mycingular.net')[2])
print("This connection has 3 connections")
response12 = reader.city('198.228.197.43')
print("This is the country iso code: ", response12.country.iso_code)
print("This is the country name: ", response12.country.name)
print ("This is the subdivisions most specific name: ", response12.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response12.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response12.city.name)
print ("This is the response postal code: ", response12.postal.code)
print ("This is the location latitude: ", response12.location.latitude)
print ("This is the location longitude: ", response12.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket14=print(socket.gethostbyname_ex('pool-98-118-115-71.bstnma.fios.verizon.net')[2])
print("This connection has 2 connections")
response14 = reader.city('98.118.115.71')
print("This is the country iso code: ", response14.country.iso_code)
print("This is the country name: ", response14.country.name)
print ("This is the subdivisions most specific name: ", response14.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response14.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response14.city.name)
print ("This is the response postal code: ", response14.postal.code)
print ("This is the location latitude: ", response14.location.latitude)
print ("This is the location longitude: ", response14.location.longitude)
print ("City infornameion complete now moving to next city....")
mysocket15=print(socket.gethostbyname_ex('pool-108-7-190-30.bstnma.fios.verizon.net')[2])
print("This connection has 10 connections")
response15 = reader.city('108.7.190.30')
print("This is the country iso code: ", response15.country.iso_code)
print("This is the country name: ", response15.country.name)
print ("This is the subdivisions most specific name: ", response15.subdivisions.most_specific.name)
print ("This is the subdivisions most specific iso code: ", response15.subdivisions.most_specific.iso_code)
print ("This is the response city name: ", response15.city.name)
print ("This is the response postal code: ", response15.postal.code)
print ("This is the location latitude: ", response15.location.latitude)
print ("This is the location longitude: ", response15.location.longitude)
print ("City infornameion complete now moving to next city.... Program terminated")
