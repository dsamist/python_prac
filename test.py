from datetime import datetime

wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    print('Still waiting!')

print(f'We are at {wait_until} seconds!')