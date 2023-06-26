from multiprocessing import Queue

q = Queue(5)
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())
if not q.full(): # 判断队列是否已满  q.empty() 判断队列是否是空的
    q.put('F',timeout=3)  # put() 如果queue满了则只能等待，除非有“空地” 则添加成功。
else:
    print("队列已满!")

#获取队列的值
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
