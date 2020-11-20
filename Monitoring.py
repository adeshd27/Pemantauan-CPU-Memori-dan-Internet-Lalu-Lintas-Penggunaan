def ppmonitoring():
	import psutil
	from time import sleep
	
	cpu = psutil.cpu_percent()
	memory = psutil.virtual_memory().percent
	
	rx = psutil.net_io_counters().bytes_sent
	tx = psutil.net_io_counters().bytes_recv
	sleep(1)
	rx_new = psutil.net_io_counters().bytes_sent
	tx_new = psutil.net_io_counters().bytes_recv
	rx = operasi(rx, rx_new)
	tx = operasi(tx, tx_new)
	
	print('''
			MONITORING COMPUTER
				CPU    : {}%
				Memori : {}%
				tx/rx  : {} Kbps/{} Kbps
				
	note : hentikan program dengan ctrl+c
	
	'''.format(cpu, memory, tx, rx))
	
def operasi(old,new):
	new = new - old
	new = (new * 8)/1000
	return new

def monitoring():
	from time import sleep
	
	while (True):
		ppmonitoring()
		sleep(5)
	
try:
	monitoring()
except:
	print("\t Selesai.. Terimakasih")
