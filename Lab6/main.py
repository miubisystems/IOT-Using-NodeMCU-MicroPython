import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
temp = d.temperature() # eg. 23 (°C)
humid = d.humidity()    # eg. 41 (% RH)
print(temp)
print(humid)
"""
d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature() # eg. 23.6 (°C)
d.humidity()    # eg. 41.3 (% RH)"""