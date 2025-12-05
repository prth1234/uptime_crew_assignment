import threading
import time
from .buffer import BoundedBuffer

class Producer(threading.Thread):
    def __init__(self,buffer,source,name="Producer",delay=0.0):
        super().__init__(name=name)
        self._buffer=buffer
        self._source=list(source)
        self._delay=delay
        self._produced_count=0
        self._produced_items=[]
        self._stop_requested=False
        self._lock=threading.Lock()
    
    def get_produced_count(self):
        with self._lock:
            return self._produced_count
    
    def get_produced_items(self):
        with self._lock:
            return list(self._produced_items)
    
    def stop(self):
        with self._lock:
            self._stop_requested=True
    
    def run(self):
        print(f"[{self.name}] Started")
        for item in self._source:
            with self._lock:
                if self._stop_requested:
                    print(f"[{self.name}] Stop requested, exiting early")
                    break
            if self._delay>0:
                time.sleep(self._delay)
            success=self._buffer.put(item)
            if not success:
                print(f"[{self.name}] Buffer closed, stopping")
                break
            with self._lock:
                self._produced_count+=1
                self._produced_items.append(item)
            print(f"[{self.name}] Produced: {item}")
        print(f"[{self.name}] Finished - produced {self._produced_count} items")