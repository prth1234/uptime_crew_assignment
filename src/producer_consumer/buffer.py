import threading
from collections import deque

class BoundedBuffer:
    def __init__(self,capacity):
        if capacity<1:
            raise ValueError("Buffer capacity must be at least 1")
        self._capacity=capacity
        self._buffer=deque()
        self._lock=threading.Lock()
        self._not_full=threading.Condition(self._lock)
        self._not_empty=threading.Condition(self._lock)
        self._shutdown=False
    
    def get_capacity(self):
        return self._capacity
    
    def get_size(self):
        with self._lock:
            return len(self._buffer)
    
    def is_empty(self):
        with self._lock:
            return len(self._buffer)==0
    
    def is_full(self):
        with self._lock:
            return len(self._buffer)>=self._capacity
    
    def put(self,item,timeout=None):
        with self._not_full:
            while len(self._buffer)>=self._capacity and not self._shutdown:
                if not self._not_full.wait(timeout):
                    return False
            if self._shutdown:
                return False
            self._buffer.append(item)
            self._not_empty.notify()
            return True
    
    def get(self,timeout=None):
        with self._not_empty:
            while len(self._buffer)==0 and not self._shutdown:
                if not self._not_empty.wait(timeout):
                    return (False,None)
            if self._shutdown and len(self._buffer)==0:
                return (False,None)
            item=self._buffer.popleft()
            self._not_full.notify()
            return (True,item)
    
    def try_put(self,item):
        with self._lock:
            if len(self._buffer)>=self._capacity:
                return False
            self._buffer.append(item)
            self._not_empty.notify()
            return True
    
    def try_get(self):
        with self._lock:
            if len(self._buffer)==0:
                return (False,None)
            item=self._buffer.popleft()
            self._not_full.notify()
            return (True,item)
    
    def shutdown(self):
        with self._lock:
            self._shutdown=True
            self._not_full.notify_all()
            self._not_empty.notify_all()
    
    def reset(self):
        with self._lock:
            self._buffer.clear()
            self._shutdown=False