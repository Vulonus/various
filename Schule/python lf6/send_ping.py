from ping3 import ping

def send_ping():
    successful_pings = list()
    for i in range(1,256):
        r = ping('192.168.1.{}'.format(i), unit='ms', timeout=0.1)
        if r != None:
            print('Successfully pinged 192.168.1.{} delay: {}ms'.format(i,r))
            successful_pings.append('192.168.1.{}'.format(i))
        else:
            print('Failed to ping 192.168.1.{}'.format(i))
    print(successful_pings)
    with open('Successful_LAN_pings.txt' , 'w') as f:
        for address in successful_pings:
            f.write(address)
            f.write('\n')