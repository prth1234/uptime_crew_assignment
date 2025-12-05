import threading
import time
from .buffer import BoundedBuffer

class Consumer(threading.Thread):
    def __init__(self,buffer,destination,name="Consumer",expected_count=None,delay=0.0):
        super().__init__(name=name)
        self._buffer=buffer
        self._destination=destination
        self._expected_count=expected_count
        self._delay=delay
        self._consumed_count=0
        self._stop_requested=False
        self._lock=threading.Lock()
    
    def get_consumed_count(self):
        with self._lock:
            return self._consumed_count
    
    def stop(self):
        with self._lock:
            self._stop_requested=True
    
    def _should_continue(self):
        with self._lock:
            if self._stop_requested:
                return False
            if self._expected_count is not None:
                return self._consumed_count<self._expected_count
            return True
    
    def run(self):
        print(f"[{self.name}] Started")
        while self._should_continue():
            success,item=self._buffer.get(timeout=0.5)
            if not success:
                with self._lock:
                    if self._stop_requested:
                        break
                    if self._expected_count and self._consumed_count>=self._expected_count:
                        break
                continue
            with self._lock:
                self._consumed_count+=1
                self._destination.append(item)
            print(f"[{self.name}] Consumed: {item}")
            if self._delay>0:
                time.sleep(self._delay)
        print(f"[{self.name}] Finished - consumed {self._consumed_count} items")