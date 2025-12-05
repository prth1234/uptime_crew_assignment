from collections import namedtuple

SaleRecord=namedtuple('SaleRecord',[
    'sale_id',
    'date',
    'product_name',
    'category',
    'quantity',
    'unit_price',
    'region'
])

def get_total_amount(sale):
    return sale.quantity*sale.unit_price

def get_month(sale):
    return sale.date.strftime("%Y-%m")