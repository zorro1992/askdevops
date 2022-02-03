import psutil

#CPU times
print(psutil.cpu_times())

# Avg CPU load
print(psutil.getloadavg())

# Memory
print(psutil.virtual_memory())

# Swap memory
print(psutil.swap_memory())

# Disk usage
print(psutil.disk_usage('/'))

# Disk IO utilization
print(psutil.disk_io_counters(perdisk=False))

# Temp
print(psutil.sensors_temperatures())