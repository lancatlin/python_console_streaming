from threading import Thread
import time

def example(times):
	for i in range(times):
		print(i)
		time.sleep(1)

thread = Thread(target=example, args=(5,))

thread.start()	# 啟動 Thread

time.sleep(2)
print("This is printed in main thread")

thread.join()