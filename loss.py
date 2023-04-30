from ping3 import ping
import time

addresses = ['8.8.8.8', '1.1.1.1']

total_pings = 0
failed_pings = 0

loss_detected = False

print("Pinging addresses, please wait...")

start_time = time.time()
while time.time() - start_time < 30:
    for address in addresses:
        try:
            delay = ping(address)
            if delay is None:
                failed_pings += 1
                loss_detected = True
            total_pings += 1
            if loss_detected:
                network_loss = (failed_pings / total_pings) * 100
                print(f'\rCurrent network loss: {network_loss:.2f}%', end='', flush=True)
        except Exception as e:
            print(f"\nAn error occurred while pinging {address}: {str(e)}")

        time.sleep(0.5)

network_loss = (failed_pings / total_pings) * 100

if network_loss == 0.0:
    print('\nCongratulations! No network loss detected.')
else:
    print(f'\nFinal ping statistics: {total_pings} packets transmitted, {total_pings - failed_pings} received, {network_loss:.2f}% packet loss')

input("Press any key to exit...")
