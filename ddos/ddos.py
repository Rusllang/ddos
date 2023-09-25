import telnetlib

#host = #4001

f = open('ddos/bebra.txt','r')

com =  f.readlines()

n = len(com)

print(n)


tell = telnetlib.Telnet('172.17.9.151',4001)
print(com[10])
i=0
for i in range(n):
    #tell.write(com[i].encode('utf-8') + b"\n")
    print(com[i])
    tell.write((com[i].replace('\n','') + '\n').encode('utf-8'))
    i+=1   
