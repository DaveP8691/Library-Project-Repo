import pandas as pd

books = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library.csv") # we've pulled the data and store in a dataframe called books
print(books.head())
customers = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library_customers.csv")
print(customers.head())

##Test for trailing whitespaces in books dataframe
def clean_titles(df):
    out = df.copy()
    out['Books'] = out['Books'].str.strip()
    return out

count_of_trailing_spaces = books['Books'].str.endswith(" ").sum()
print(f"count of whitespace {count_of_trailing_spaces}")
recount_trailing_spaces = clean_titles(books)['Books'].str.endswith(" ").sum()
print(f"clean_titles")

##missing values test
def test_customer_id_never_missing():
    books = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library.csv").dropna(subset=['Id'])
    n = books['Customer ID'].isna().sum()
    assert n == 0, f"{n} loans have no customers"

try:
    test_customer_id_never_missing()
except AssertionError as e:
    print(e.message)

##Book check out date in the wrong format test
def test_book_checkout_date():
    check_out_date_format = (books["Book checkout"]).dt_type 



assert pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce').notna().all()


try:
     datetime.strptime(str(item), date_format)
except ValueError            
        return False  # Break early on the first bad date string
        return True


 ##Test for incorrect data




 ##Test for duplicates



