#speed of light in meters per second
c=299792458

#velocity of the message as a product of the speed of light (c)
message_multiplier=4.4
u=c*message_multiplier

#velocity of inertial frame through space as a product of c
inertial_frame_multiplier=0.99
V=c*inertial_frame_multiplier

##TOLMANS THOUGHT EXPERIMENT
#time in seconds the message is recieved after the event of sending
def Ts(u,V,c):
	time=(1-((u*V)/c**2))/((1-(V**2/c**2))**0.5)
	return time
##

#activate thought experiment with variables
T2 = Ts(u,V,c)
#print results (if result is negative - it represents that the message is recieved before it was sent)
print(T2)
