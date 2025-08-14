r = int(input('Enter number of runs: '))

if r % 100 == 0 and r > 300:
    print(f'{r // 100}th Century')  # Displays "4x Century" for 400, "5x Century" for 500, etc.
elif r > 300:
    print('Triple Century')
elif r > 200:
    print('Double Century')
elif r > 100:
    print('Century')
elif r > 50:
    print('Half Century')
else:
    print('No Century')
