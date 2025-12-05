from functools import reduce
from .models import get_total_amount,get_month

def calculate_total_revenue(sales):
    if not sales:
        return 0.0
    total=reduce(lambda acc,sale:acc+get_total_amount(sale),sales,0.0)
    return total

def calculate_average_order_value(sales):
    if not sales:
        return 0.0
    total=calculate_total_revenue(sales)
    return total/len(sales)

def calculate_quantity_statistics(sales):
    if not sales:
        return{'min':0,'max':0,'avg':0,'total':0}
    quantities=list(map(lambda s:s.quantity,sales))
    return{
        'min':min(quantities),
        'max':max(quantities),
        'avg':sum(quantities)/len(quantities),
        'total':sum(quantities)
    }

def group_sales_by_category(sales):
    result={}
    for sale in sales:
        if sale.category not in result:
            result[sale.category]=[]
        result[sale.category].append(sale)
    return result

def group_sales_by_region(sales):
    result={}
    for sale in sales:
        if sale.region not in result:
            result[sale.region]=[]
        result[sale.region].append(sale)
    return result

def group_sales_by_month(sales):
    result={}
    for sale in sales:
        month=get_month(sale)
        if month not in result:
            result[month]=[]
        result[month].append(sale)
    return result

def group_sales_by_product(sales):
    result={}
    for sale in sales:
        if sale.product_name not in result:
            result[sale.product_name]=[]
        result[sale.product_name].append(sale)
    return result

def get_category_summaries(sales):
    grouped=group_sales_by_category(sales)
    summaries=[]
    for category,category_sales in grouped.items():
        total_revenue=calculate_total_revenue(category_sales)
        order_count=len(category_sales)
        avg_value=total_revenue/order_count if order_count>0 else 0
        summaries.append({
            'category':category,
            'total_revenue':total_revenue,
            'order_count':order_count,
            'avg_order_value':avg_value
        })
    summaries.sort(key=lambda x:x['total_revenue'],reverse=True)
    return summaries

def get_region_summaries(sales):
    grouped=group_sales_by_region(sales)
    summaries=[]
    for region,region_sales in grouped.items():
        total_revenue=calculate_total_revenue(region_sales)
        order_count=len(region_sales)
        avg_value=total_revenue/order_count if order_count>0 else 0
        summaries.append({
            'region':region,
            'total_revenue':total_revenue,
            'order_count':order_count,
            'avg_order_value':avg_value
        })
    summaries.sort(key=lambda x:x['total_revenue'],reverse=True)
    return summaries

def get_top_products_by_revenue(sales,n=5):
    product_revenue={}
    for sale in sales:
        if sale.product_name not in product_revenue:
            product_revenue[sale.product_name]=0
        product_revenue[sale.product_name]+=get_total_amount(sale)
    sorted_products=sorted(product_revenue.items(),key=lambda x:x[1],reverse=True)
    return sorted_products[:n]

def get_monthly_trends(sales):
    monthly=group_sales_by_month(sales)
    trends={}
    for month,month_sales in sorted(monthly.items()):
        revenue=calculate_total_revenue(month_sales)
        count=len(month_sales)
        trends[month]={
            'total_revenue':revenue,
            'order_count':count,
            'avg_order_value':revenue/count if count>0 else 0
        }
    return trends

def filter_sales_by_category(sales,category):
    filtered=[]
    for sale in sales:
        if sale.category.lower()==category.lower():
            filtered.append(sale)
    return filtered

def filter_sales_by_region(sales,region):
    filtered=[]
    for sale in sales:
        if sale.region.lower()==region.lower():
            filtered.append(sale)
    return filtered

def get_products_above_avg_price(sales):
    if not sales:
        return[]
    total_price=sum(map(lambda s:s.unit_price,sales))
    avg_price=total_price/len(sales)
    filtered=filter(lambda s:s.unit_price>avg_price,sales)
    return list(filtered)

def get_high_value_orders(sales,threshold):
    filtered=[]
    for sale in sales:
        if get_total_amount(sale)>=threshold:
            filtered.append(sale)
    return filtered

def calculate_category_percentages(sales):
    total=calculate_total_revenue(sales)
    if total==0:
        return{}
    grouped=group_sales_by_category(sales)
    percentages={}
    for category,cat_sales in grouped.items():
        cat_revenue=calculate_total_revenue(cat_sales)
        percentages[category]=(cat_revenue/total)*100
    return percentages