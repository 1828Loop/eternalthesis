#speed of light in meters per second
c=299792458

#coordinate of A in meters
xA=1

#coordinate of B in meters
xB=940000000000

#speed of the message as a product of c
u=c*4.4

#speed of the conduit as it moves through space carrying the message as a product of c
V=c*0.99

#time in seconds the message is recieved after the event of sending
def Ts(u,V,c):
	time=(1-((u*V)/c**2))/((1-(V**2/c**2))**0.5)
	return time
'''
def Tf(V,xA,xB,c,u):
	A=(1/(1-V**2*c**2)**0.5)*(((xB-xA)/u)-((V/c**2)*xB))
	B=(1/(1-V**2*c**2)**0.5)*(((xB-xA)/u)-((V/c**2)*xA))
	time=B-A
	return time
'''
'''
#convert seconds to years, days, hours, minutes, seconds
def time(time):
	year = time // (365 * 24 * 3600)
	time = time % (365 * 24 * 3600)
	day = time // (24 * 3600)
	time = time % (24 * 3600)
	hour = time // 3600
	time %= 3600
	minutes = time // 60
	time %= 60
	seconds = time
	print("%dy:%dd:%dh:%dm:%ds" % (year, day, hour, minutes, seconds))
'''
#T1 = Tf(V,xA,xB,c,u).real
T2 = Ts(u,V,c)

#print(T1)
print(T2)