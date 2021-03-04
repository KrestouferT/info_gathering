import nmap
import time

nm_scan = nmap.PortScanner()

print('''

  _ __  _ __ ___   __ _ _ __  _ __   ___ _ __
 | '_ \| '_ ` _ \ / _` | '_ \| '_ \ / _ \ '__|
 | | | | | | | | | (_| | |_) | |_) |  __/ |
 |_| |_|_| |_| |_|\__,_| .__/| .__/ \___|_|
                       | |   | |
                       |_|   |_|              
                       
        ''')
print('-------------------------------------------------------')

ip_addr = input('Please enter the IP address you want to scan: ')
print('\nRunning ... ')
nm_scanner = nm_scan.scan(ip_addr, '80', arguments='-O')
host_is_up = "The host is: " + nm_scanner['scan'][ip_addr]['status']['state'] + ".\n"
port_open = "The port 80 is: " + nm_scanner['scan'][ip_addr]['tcp'][80]['state'] + ".\n"
method_scan = "The method of scanning is: " + nm_scanner['scan'][ip_addr]['tcp'][80]['reason'] + ".\n"
guessed_os = "There is %s percent chance that the host is running %s" % (
    nm_scanner['scan'][ip_addr]['osmatch'][0]['accuracy'], nm_scanner['scan'][ip_addr]['osmatch'][0]['name']) + ".\n"

with open("%s.txt" % ip_addr, 'w') as f:
    f.write(host_is_up + port_open + method_scan + guessed_os)
    f.write("\nReport generated" + time.strftime("%Y-%m-%d_%H:%M:%S CET", time.localtime()))

print("\nFinished ... report generated")
