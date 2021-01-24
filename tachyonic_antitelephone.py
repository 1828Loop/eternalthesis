#speed of light in meters per second
c=299792458

#velocity of the message as a product of the speed of light (c)
message_multiplier=4.4
u=c*message_multiplier

#velocity of inertial frame through space as a product of c
inertial_frame_multiplier=0.99
V=c*inertial_frame_multiplier

#time in seconds the message is recieved after the event of sending
def Ts(u,V,c):
	time=(1-((u*V)/c**2))/((1-(V**2/c**2))**0.5)
	return time

T2 = Ts(u,V,c)
print(T2)
