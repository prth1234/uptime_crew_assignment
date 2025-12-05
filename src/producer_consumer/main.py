import time
from .buffer import BoundedBuffer
from .producer import Producer
from .consumer import Consumer

def run_demo(num_items=10,buffer_size=3,producer_delay=0.1,consumer_delay=0.15):
    print("="*50)
    print("Producer-Consumer Pattern Demonstration")
    print("="*50)
    print(f"\nConfiguration:")
    print(f"  Items to transfer: {num_items}")
    print(f"  Buffer capacity:   {buffer_size}")
    print(f"  Producer delay:    {producer_delay}s")
    print(f"  Consumer delay:    {consumer_delay}s")

    print()
    source_items=[f"Item_{i+1}"for i in range(num_items)]
    destination=[]
    buffer=BoundedBuffer(capacity=buffer_size)
    producer=Producer(buffer=buffer,source=source_items,delay=producer_delay)
    consumer=Consumer(buffer=buffer,destination=destination,expected_count=num_items,delay=consumer_delay)
    start_time=time.time()


    print("Starting threads...\n")
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    elapsed=time.time()-start_time

    print()
    print("="*50)
    print("Results")
    print("="*50)
    print(f"\nItems produced: {producer.get_produced_count()}")
    print(f"Items consumed: {consumer.get_consumed_count()}")
    print(f"Items in destination: {len(destination)}")
    print(f"Time elapsed: {elapsed:.2f}s")

    if destination==source_items:
        print("\nSUCCESS: All items transferred correctly!")
        print("  Order preserved: Yes")
    elif set(destination)==set(source_items):
        print("\nSUCCESS: All items transferred (order may vary)")
    else:
        print("\nERROR: Mismatch in transferred items!")
        print(f"  Missing: {set(source_items)-set(destination)}")
    print("\nDestination contents:")
    for i,item in enumerate(destination):
        print(f"  [{i+1}] {item}")

def main():
    run_demo(num_items=10,buffer_size=3,producer_delay=0.1,consumer_delay=0.15)

if __name__=="__main__":
    main()