from time import time, strftime, localtime

today = time()
print(f"Seconds since January 1, 1970: {today:3,.4f} or {today:.2e} in scientific notation")
print(strftime('%b %d %Y', localtime(today)))
