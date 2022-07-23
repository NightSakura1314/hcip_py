import telnetlib
import time

host="192.168.10.112"
user="admin"
password="1"
port=23

tn = telnetlib.Telnet(host)
tn.read_until(b"Username:")
tn.write(user.encode('ascii')+b"\n")
tn.read_until(b"Password:")
tn.write(password.encode('ascii')+b"\n")
print('已登录交换机'+host)

tn.write(b"sys\n")
tn.write(b"int loopback 1\n")
tn.write(b"ip add 192.168.100.1 24\n")
tn.write(b"quit\n")
tn.write(b"quit\n")
tn.write(b"save\n")
tn.write(b"y\n")
time.sleep(1)
output = tn.read_very_eager().decode('ascii')
print(output)
tn.close()