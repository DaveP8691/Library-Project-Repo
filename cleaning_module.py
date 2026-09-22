import pandas as pd
books = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library.csv") # we've pulled the data and store in a dataframe called books
print(books.head())
customers = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library_customers.csv")
print(customers.head())
print(books.shape) # print dimensions of my data frame
count = books.isnull().all().sum() # count empty values in "books"
real = books.dropna(how="any") # if a column is missing a value, drop it and return DF
print(real.shape)
print(real)
books['Id'] # points to the id column in the dataframe
three_books = books['Id'].head(3).tolist() # using key/value pair mapping to identify 3 books from the top of the DF
print(three_books)
print(books.dtypes) # identify the type of datatype the df is using, e.g. Dtype = float64 (float64 is the standard promotion
#pandas will use when given NaN errors, text, etc)
#pd.to_datetime(error=coerce) # coerce is a error hunting tool, which strips the standard process of 'arg'
#"raise error" aware from nan, etc values, so we can perform agg (sum, max, etc) functions on a series/df
silence_the_errors = pd.to_datetime(books['Book checkout'], errors="coerce", dayfirst=True)
print(silence_the_errors.dtype)
print(silence_the_errors.isnull().sum())
print(silence_the_errors.isna().sum())

books = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library.csv") # we've pulled the data and store in a dataframe called books
print(books)
dropped_na = books.dropna(how="all")
dropped_na.shape
#dropped_na.isna.sum()
#books.isna.sum()

filled_value = books.fillna("value") # inplace errors, see value handed back to the col with a new type
#three_books.filled_value.isnull().sum().sum() # 0
#filled_value["Customer"].tolist[-1] # value it ran, it isn't too useful, but it'll showcase the output
filled_value["Books"].toList() # list of remnaining books with value updated
filled_value["Books"].mean() # shows the mean book, similary mode, etc; can be applied here.

#books.duplicated = true false true -> returns true for every row its seen before
dropped_na.duplicated().sum() # agg of the true returns
deduped_dropped_na = dropped_na.drop_duplicates(subset="col") # common func
deduped_dropped_na.shape # inspect
deduped_dropped_na.describe.mean() # console mean

print(books)
print(customers)

print(books.head())
print(customers.head())

books_reformatted = books.(subset = 'book checkout') = pd.to_datetime(books['book checkout']) #want to reformat checkout date to datetime


customers = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library_customers.csv")
print(customers)

customers_cleaned = customers.dropna(how="all")
print(customers_cleaned)