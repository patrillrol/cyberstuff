with open('hosts.txt', 'w') as file:
    for i in range(1, 255):
        ip_address = f'192.168.0.{i}'
        file.write(ip_address + '\n')

print('Hosts list generated and saved to hosts.txt')
