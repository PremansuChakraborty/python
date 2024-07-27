# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime

# 6-12 gm, 12-14 gn, 14-18 gfn, 18-20 ge, 20-5 gn

import time

h=int(time.strftime('%H'))
m=int(time.strftime('%M'))
s=int(time.strftime('%S'))
print(h)
if h>=6 and h<12:
    print("GOOD MORNING")
elif h>=12 and h<14:
    print("GOOD NOON")
elif h>=14 and h<18:
    print("GOOD AFTER NOON") 
elif h>=18 and h<20:
    print("GOOD EVENING")  
else:
    print("GOOD NIGHT")
