import unittest
import threading
import time
import sys
import os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','src'))

from producer_consumer.buffer import BoundedBuffer
from producer_consumer.producer import Producer
from producer_consumer.consumer import Consumer


class TestBuffer(unittest.TestCase):
    def test_create_buffer(self):
        buffer=BoundedBuffer(capacity=5)
        self.assertEqual(buffer.get_capacity(),5)
        self.assertTrue(buffer.is_empty())

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            BoundedBuffer(capacity=0)

    def test_try_put_get(self):
        buffer=BoundedBuffer(capacity=3)
        self.assertTrue(buffer.try_put("a"))
        self.assertTrue(buffer.try_put("b"))
        success,item=buffer.try_get()
        self.assertTrue(success)
        self.assertEqual(item,"a")

    def test_buffer_full(self):
        buffer=BoundedBuffer(capacity=2)
        buffer.try_put("a")
        buffer.try_put("b")
        self.assertTrue(buffer.is_full())
        self.assertFalse(buffer.try_put("c"))

    def test_buffer_empty(self):
        buffer=BoundedBuffer(capacity=3)
        success,_=buffer.try_get()
        self.assertFalse(success)

    def test_fifo_order(self):
        buffer=BoundedBuffer(capacity=3)
        buffer.try_put("first")
        buffer.try_put("second")
        _,item1=buffer.try_get()
        _,item2=buffer.try_get()
        self.assertEqual(item1,"first")
        self.assertEqual(item2,"second")

    def test_reset(self):
        buffer=BoundedBuffer(capacity=3)
        buffer.try_put("a")
        buffer.reset()
        self.assertTrue(buffer.is_empty())


class TestProducerConsumer(unittest.TestCase):
    def test_basic_transfer(self):
        source=["A","B","C"]
        destination=[]
        buffer=BoundedBuffer(capacity=2)
        producer=Producer(buffer,source)
        consumer=Consumer(buffer,destination,expected_count=3)
        producer.start()
        consumer.start()
        producer.join(timeout=5)
        consumer.join(timeout=5)
        self.assertEqual(set(destination),set(source))

    def test_order_preserved(self):
        source=list(range(5))
        destination=[]
        buffer=BoundedBuffer(capacity=3)
        producer=Producer(buffer,source)
        consumer=Consumer(buffer,destination,expected_count=5)
        producer.start()
        consumer.start()
        producer.join(timeout=5)
        consumer.join(timeout=5)
        self.assertEqual(destination,source)

    def test_empty_source(self):
        buffer=BoundedBuffer(capacity=3)
        producer=Producer(buffer,[])
        producer.start()
        producer.join(timeout=2)
        self.assertEqual(producer.get_produced_count(),0)


if __name__=='__main__':
    unittest.main(verbosity=2)
