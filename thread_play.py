from time import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# start = time()
# milli = [i for i in range(1_000_000_000)]
# sec =  time() - start

count = 0

def count_billion():
    global count
    count += 1

# start = time()
# while count < 1_000_000:
#     count_billion()
#     print(f"{count:,}", end='\r')
# sec =  time() - start

start = time()
with ThreadPoolExecutor(max_workers=500) as executor:
    # futures = [executor.submit(count_billion) for i in range(1_000_000)]
    for i in  range(1_000_000):
        executor.submit(count_billion)
sec =  time() - start
print(count)
print(f"{sec:.2f} sec")