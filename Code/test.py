from ftplib import FTP


# FTP server details
ftp_host = '192.168.43.2'
ftp_port = 2221
ftp_user = 'admin'
ftp_password = 'admin'

#Connect to FTP server
ftp = FTP()
ftp.connect(ftp_host, ftp_port)
ftp.login(ftp_user, ftp_password)


with open('signal_1.txt', 'wb') as file:
    ftp.retrbinary('RETR ' + 'signal_1.txt' , file.write)
with open('signal_1.txt', 'r') as signal1:
    signal_1_density = signal1.read()

with open('signal_2.txt', 'wb') as file2:
    ftp.retrbinary('RETR ' + 'signal_2.txt' , file2.write)
with open('signal_2.txt', 'r') as signal2:
    signal_2_density = signal2.read()

with open('signal_3.txt', 'wb') as file3:
    ftp.retrbinary('RETR ' + 'signal_3.txt' , file3.write)
with open('signal_3.txt', 'r') as signal3:
    signal_3_density = signal3.read()


