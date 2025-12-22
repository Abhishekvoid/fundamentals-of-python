

def fetch_sales(total_sales):

    return(f"this much sales this month {total_sales}")

def filter_valid_orders():
    
    return(f"this is the the fildterd data")

def summarize_data():
   sales = fetch_sales(12345678)
   order = filter_valid_orders()
   return(f"summary is: sales{sales}, order{order}")

def generate_report():
    
    summary = summarize_data()
    
    print("this is summary of the data:")
    
    print(f"summary: {summary}")

generate_report()