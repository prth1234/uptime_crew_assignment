import unittest
from datetime import date
import sys
import os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','src'))

from sales_analysis.models import SaleRecord,get_total_amount,get_month
from sales_analysis.csv_reader import read_sales_from_string,parse_date
from sales_analysis.analyzer import(
    calculate_total_revenue,
    calculate_average_order_value,
    calculate_quantity_statistics,
    group_sales_by_category,
    get_category_summaries,
    get_top_products_by_revenue,
    get_monthly_trends,
    filter_sales_by_category,
    get_products_above_avg_price,
    get_high_value_orders,
    calculate_category_percentages
)

def make_sale(sale_id="S001",sale_date=None,product="Widget",category="Electronics",quantity=1,price=10.0,region="North"):
    if sale_date is None:
        sale_date=date(2024,1,15)
    return SaleRecord(sale_id,sale_date,product,category,quantity,price,region)

def get_test_sales():
    return[
        make_sale("S001",date(2024,1,10),"Laptop","Electronics",2,999.99,"North"),
        make_sale("S002",date(2024,1,15),"T-Shirt","Clothing",5,25.00,"South"),
        make_sale("S003",date(2024,2,5),"Jeans","Clothing",3,75.00,"West"),
        make_sale("S004",date(2024,2,10),"Monitor","Electronics",2,399.99,"North"),
    ]

CSV_DATA="""sale_id,date,product_name,category,quantity,unit_price,region
S001,2024-01-10,Laptop,Electronics,2,999.99,North
S002,2024-01-15,T-Shirt,Clothing,5,25.00,South
"""


class TestModels(unittest.TestCase):
    def test_total_amount(self):
        sale=make_sale(quantity=3,price=100.0)
        self.assertEqual(get_total_amount(sale),300.0)

    def test_month(self):
        sale=make_sale(sale_date=date(2024,3,15))
        self.assertEqual(get_month(sale),"2024-03")


class TestCSV(unittest.TestCase):
    def test_parse_date(self):
        d=parse_date("2024-03-15")
        self.assertEqual(d,date(2024,3,15))

    def test_read_csv(self):
        records=read_sales_from_string(CSV_DATA)
        self.assertEqual(len(records),2)
        self.assertEqual(records[0].product_name,"Laptop")


class TestAggregations(unittest.TestCase):
    def test_total_revenue(self):
        sales=get_test_sales()
        total=calculate_total_revenue(sales)
        self.assertGreater(total,0)

    def test_average_order(self):
        sales=[make_sale(quantity=1,price=100.0),make_sale(quantity=1,price=200.0)]
        avg=calculate_average_order_value(sales)
        self.assertEqual(avg,150.0)

    def test_quantity_stats(self):
        sales=get_test_sales()
        stats=calculate_quantity_statistics(sales)
        self.assertEqual(stats['total'],2+5+3+2)


class TestGrouping(unittest.TestCase):
    def test_group_by_category(self):
        sales=get_test_sales()
        grouped=group_sales_by_category(sales)
        self.assertIn("Electronics",grouped)
        self.assertIn("Clothing",grouped)

    def test_category_summaries(self):
        sales=get_test_sales()
        summaries=get_category_summaries(sales)
        self.assertEqual(len(summaries),2)


class TestFilters(unittest.TestCase):
    def test_filter_by_category(self):
        sales=get_test_sales()
        result=filter_sales_by_category(sales,"Electronics")
        self.assertEqual(len(result),2)

    def test_above_avg_price(self):
        sales=get_test_sales()
        result=get_products_above_avg_price(sales)
        avg=sum(s.unit_price for s in sales)/len(sales)
        for sale in result:
            self.assertGreater(sale.unit_price,avg)

    def test_high_value_orders(self):
        sales=get_test_sales()
        result=get_high_value_orders(sales,threshold=500)
        for sale in result:
            self.assertGreaterEqual(get_total_amount(sale),500)


class TestAnalytics(unittest.TestCase):
    def test_top_products(self):
        sales=get_test_sales()
        top=get_top_products_by_revenue(sales,n=2)
        self.assertLessEqual(len(top),2)

    def test_monthly_trends(self):
        sales=get_test_sales()
        trends=get_monthly_trends(sales)
        self.assertIn("2024-01",trends)

    def test_category_percentages(self):
        sales=get_test_sales()
        pct=calculate_category_percentages(sales)
        total=sum(pct.values())
        self.assertAlmostEqual(total,100.0,places=1)


if __name__=='__main__':
    unittest.main(verbosity=2)
