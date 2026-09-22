import pandas as pd
books = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library.csv") # we've pulled the data and store in a dataframe called books
print(books.head())
customers = pd.read_csv(r"C:\Users\Admin\Desktop\GitFolder\library_customers.csv")
print(customers.head())


customers_cleaned = customers.dropna(how="all") #drop rows containing no customer name
print(customers_cleaned)

print(customers.shape)
print(customers_cleaned.shape)


print(books)
books_cleaned = books.dropna(how="all")
print(books_cleaned)

print(books_cleaned.dtypes)

#books_cleaned =  pd.to_datetime(books['Book checkout'], errors="coerce", dayfirst=True)
print(books_cleaned)
