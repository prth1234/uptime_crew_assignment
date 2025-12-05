import csv
import os
from datetime import datetime
from .models import SaleRecord

def parse_date(date_str):
    formats=["%Y-%m-%d","%m/%d/%Y","%d/%m/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(),fmt).date()
        except ValueError:
            continue
            
    raise ValueError(f"Could not parse date: {date_str}")

def read_sales_csv(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")
    records=[]
    with open(filepath,'r',newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)

        for row in reader:
            record=SaleRecord(
                sale_id=row['sale_id'].strip(),
                date=parse_date(row['date']),
                product_name=row['product_name'].strip(),
                category=row['category'].strip(),
                quantity=int(row['quantity']),
                unit_price=float(row['unit_price']),
                region=row['region'].strip()
            )
            records.append(record)

    return records

def read_sales_from_string(csv_content):
    import io
    records=[]
    reader=csv.DictReader(io.StringIO(csv_content))
    for row in reader:
        record=SaleRecord(
            sale_id=row['sale_id'].strip(),
            date=parse_date(row['date']),
            product_name=row['product_name'].strip(),
            category=row['category'].strip(),
            quantity=int(row['quantity']),
            unit_price=float(row['unit_price']),
            region=row['region'].strip()
        )
        records.append(record)
    return records