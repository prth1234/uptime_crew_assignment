import csv
import random
from datetime import datetime,timedelta

PRODUCTS={
    'Electronics':[
        ('Laptop Pro',999.99),
        ('Wireless Mouse',49.99),
        ('USB Keyboard',79.99),
        ('Monitor 27inch',349.99),
        ('Bluetooth Speaker',89.99),
        ('Webcam HD',69.99),
        ('Tablet 10inch',449.99),
        ('Smart Watch',199.99),
        ('Wireless Earbuds',129.99),
        ('Power Bank',39.99),
    ],
    'Clothing':[
        ('Cotton T-Shirt',24.99),
        ('Denim Jeans',59.99),
        ('Running Shoes',89.99),
        ('Winter Jacket',149.99),
        ('Casual Hoodie',49.99),
        ('Formal Shirt',44.99),
        ('Sports Shorts',29.99),
        ('Leather Belt',34.99),
        ('Baseball Cap',19.99),
        ('Wool Sweater',79.99),
    ],
    'Home & Garden':[
        ('Coffee Maker',79.99),
        ('Desk Lamp',39.99),
        ('Plant Pot Set',29.99),
        ('Kitchen Scale',24.99),
        ('Vacuum Cleaner',199.99),
        ('Air Purifier',149.99),
        ('Garden Tools',59.99),
        ('Bed Sheets',49.99),
        ('Wall Clock',34.99),
        ('Door Mat',19.99),
    ],
    'Sports':[
        ('Yoga Mat',29.99),
        ('Dumbbells Set',89.99),
        ('Tennis Racket',129.99),
        ('Basketball',34.99),
        ('Soccer Ball',29.99),
        ('Jump Rope',14.99),
        ('Resistance Bands',24.99),
        ('Water Bottle',19.99),
        ('Gym Bag',44.99),
        ('Fitness Tracker',79.99),
    ]
}

REGIONS=['North','South','East','West']

def generate_sales_data(num_records=1000,output_file='data/sales_data.csv'):
    start_date=datetime(2024,1,1)
    end_date=datetime(2024,12,31)
    date_range=(end_date-start_date).days
    records=[]
    for i in range(num_records):
        random_days=random.randint(0,date_range)
        sale_date=start_date+timedelta(days=random_days)
        category=random.choice(list(PRODUCTS.keys()))
        product_name,base_price=random.choice(PRODUCTS[category])
        quantity=random.randint(1,10)
        price_variation=random.uniform(0.9,1.1)
        unit_price=round(base_price*price_variation,2)
        region=random.choice(REGIONS)
        record={
            'sale_id':f'S{i+1:04d}',
            'date':sale_date.strftime('%Y-%m-%d'),
            'product_name':product_name,
            'category':category,
            'quantity':quantity,
            'unit_price':unit_price,
            'region':region
        }
        records.append(record)
    records.sort(key=lambda x:x['date'])
    with open(output_file,'w',newline='',encoding='utf-8') as f:
        fieldnames=['sale_id','date','product_name','category','quantity','unit_price','region']
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"Generated {num_records} sales records to {output_file}")
    print("\nSample records:")
    for record in records[:5]:
        print(f"  {record}")

if __name__=="__main__":
    generate_sales_data(num_records=1000)