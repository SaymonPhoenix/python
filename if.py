AGE = int(input ('How old are you? '))          # int, str, float
if (AGE >= 21):
    print ('Vodka')
elif (AGE >= 18) and (AGE < 21):                # and, or, not
    print ('Beer')
else:
    print ('Juice')