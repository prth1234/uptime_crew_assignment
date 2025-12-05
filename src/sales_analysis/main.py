import os
from .csv_reader import read_sales_csv
from .models import get_total_amount
from .analyzer import(
    calculate_total_revenue,
    calculate_average_order_value,
    calculate_quantity_statistics,
    get_category_summaries,
    get_region_summaries,
    get_top_products_by_revenue,
    get_monthly_trends,
    get_products_above_avg_price,
    get_high_value_orders,
    calculate_category_percentages
)

def format_currency(amount):
    return f"${amount:,.2f}"

def print_header(title):
    print()
    print("="*50)
    print(f"  {title}")
    print("="*50)

def run_analysis(csv_path):
    print("Sales Data Analysis")
    print("-"*50)
    print(f"Data source: {csv_path}")
    print("\nLoading data...")

    try:
        sales=read_sales_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: File not found: {csv_path}")
        return
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    print(f"Loaded {len(sales)} sales records")
    print_header("Basic Statistics")
    total_revenue=calculate_total_revenue(sales)
    avg_order=calculate_average_order_value(sales)
    qty_stats=calculate_quantity_statistics(sales)
    print(f"Total Records:       {len(sales)}")
    print(f"Total Revenue:       {format_currency(total_revenue)}")
    print(f"Average Order Value: {format_currency(avg_order)}")
    print(f"Total Quantity Sold: {qty_stats['total']}")


    print_header("Sales by Category")
    categories=get_category_summaries(sales)
    percentages=calculate_category_percentages(sales)
    for cat in categories:
        pct=percentages.get(cat['category'],0)
        print(f"\n  {cat['category']}")
        print(f"    Revenue:    {format_currency(cat['total_revenue'])} ({pct:.1f}%)")
        print(f"    Orders:     {cat['order_count']}")
        print(f"    Avg Order:  {format_currency(cat['avg_order_value'])}")

    print_header("Sales by Region")
    regions=get_region_summaries(sales)
    for region in regions:
        print(f"\n  {region['region']}")
        print(f"    Revenue:    {format_currency(region['total_revenue'])}")
        print(f"    Orders:     {region['order_count']}")
        print(f"    Avg Order:  {format_currency(region['avg_order_value'])}")


    print_header("Top 5 Products by Revenue")
    top_products=get_top_products_by_revenue(sales,n=5)
    for i,(product,revenue) in enumerate(top_products,1):
        print(f"  {i}. {product}: {format_currency(revenue)}")


    print_header("Monthly Sales Trends")
    monthly=get_monthly_trends(sales)
    for month,stats in monthly.items():
        print(f"  {month}: {format_currency(stats['total_revenue'])} ({stats['order_count']} orders)")
    
    
    print_header("Products Above Average Price")
    above_avg=get_products_above_avg_price(sales)
    avg_price=sum(s.unit_price for s in sales)/len(sales) if sales else 0
    print(f"  Average product price: {format_currency(avg_price)}")
    print(f"  Sales with above-avg priced products: {len(above_avg)}")
    print_header("High-Value Orders (>$500)")
    high_value=get_high_value_orders(sales,threshold=500)
    print(f"  Orders over $500: {len(high_value)}")
    
    if high_value:
        high_value_total=sum(get_total_amount(s) for s in high_value)
        print(f"  Combined value: {format_currency(high_value_total)}")
    print()
    print("="*50)
    print("  Analysis Complete")
    print("="*50)

def get_default_csv_path():
    current_dir=os.path.dirname(os.path.abspath(__file__))
    project_root=os.path.dirname(os.path.dirname(current_dir))
    return os.path.join(project_root,"data","sales_data.csv")

def main():
    csv_path=get_default_csv_path()
    run_analysis(csv_path)

if __name__=="__main__":
    main()