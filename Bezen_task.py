'''
MADE BY AAYUSH DESHMUKH
STARTED ON DATE: 18-05-2022, 10:2 PM
BE_ZEN_SCREENING_TASK
Bezen_task.py
'''
#Importing pandas libraray for data analysis and display function from IPython library for displaying resultant dataframe
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

#Dataframe containig the csv file data
df = pd.read_csv("2022_02_08-02_30_31_AM.csv")

#Viwing the first 5 elements of the data
#df.head()

#Knowing more about the data we have
#df.info()
#df.isna().sum()

#Creating 2 separate dataframes: 1. All the rows of the column "price_string" are not null
#                                2. All the rows of the column "price_string" are null
products_with_price = df[df["price_string"].notnull()]
products_without_price = df[df["price_string"].isna()]

#Creating a dataframe where 1. All the rows having null value in the column "price_string" are dropped and
#                           2. The column "price_string" is divided into two columns currency and value
df_preprocess = df.dropna(subset = ["price_string"])
df_preprocess["price_string"] = df_preprocess["price_string"].apply(lambda x: "$"+x if x[0].isdigit() else x)
df_preprocess["currency"] = df_preprocess["price_string"].apply(lambda x: x[0])
df_preprocess["value"] = df_preprocess["price_string"].apply(lambda x: float(x[1:]))
df_preprocess.drop(columns=["price_string", "price_string_unf"], inplace = True)
#df_preprocess.head()

#df_preprocess["price_string"] = df_preprocess["price_string"].astype(dtype = "float", copy = True)
#df_preprocess.info()



#Creating dataframe by grouping values of different columns and counting the number of products with and without price
#Null category values are dropped before counting the values
category_wise = df_preprocess.dropna(subset = ["category"]).loc[: , ["category", "value"]].groupby(["category"]).count()
product_type_wise = df_preprocess.dropna(subset = ["product_type"]).loc[: , ["product_type", "value"]].groupby(["product_type"]).count()
level_1_wise = df_preprocess.dropna(subset = ["level_1"]).loc[: , ["level_1", "value"]].groupby(["level_1"]).count()

products_without_price["price_string"].fillna("0", inplace=True)
category_wise_without = products_without_price.dropna(subset = ["category"]).loc[: , ["category", "price_string"]].groupby(["category"]).count()
product_type_wise_without = products_without_price.dropna(subset = ["product_type"]).loc[: , ["product_type", "price_string"]].groupby(["product_type"]).count()
level_1_wise_without = products_without_price.dropna(subset = ["level_1"]).loc[: , ["level_1", "price_string"]].groupby(["level_1"]).count()


#Calculating the average price for each category and viewing 1st 5 elements
category_average = df_preprocess.loc[: , ["category","value"]].groupby(["category"]).mean()
#category_average.head()


#Operation to validate if all the values are counted
#print(category_wise["value"].sum() + category_wise_without["price_string"].sum())
#print(product_type_wise["value"].sum() + product_type_wise_without["price_string"].sum())
#print(level_1_wise["value"].sum() + level_1_wise_without["price_string"].sum())


#Required output(textual)
print("NUMBER OF PRODUCTS WITH PRICE   :", products_with_price.shape[0])
print("NUMBER OF PRODUCTS WITHOUT PRICE:", products_without_price.shape[0])
print()

print("PRODUCTS HAVING PRICE CATEGORY-WISE:\n")
display(category_wise)
print("PRODUCTS WITHOUT HAVING PRICE CATEGORY-WISE:\n")
display(category_wise_without)

print("PRODUCTS HAVING PRICE PRODUCT-TYPE-WISE:\n")
display(product_type_wise)
print("PRODUCTS WITHOUT HAVING PRICE PRODUCT-TYPE-WISE:\n")
display(product_type_wise_without)

print("PRODUCTS HAVING PRICE LEVEL-1-WISE:\n")
display(level_1_wise)
print("PRODUCTS WITHOUT HAVING PRICE LEVEL-1-WISE:\n")
display(level_1_wise_without)

print("AVERAGE PRICE CATEGORY-WISE:\n")
display(category_average)

#Required output(visual)

products, categories, levels = df.dropna(subset = ["product_type"])["product_type"].unique(), \
    df.dropna(subset = ["category"])["category"].unique(), df.dropna(subset = ["level_1"])["level_1"].unique()

plt.bar(["Products with price", "Products without price"], [products_with_price.shape[0], products_without_price.shape[0]])
plt.xticks(rotation=90)
plt.title("Products with and without price")
plt.show()

plt.bar(category_wise.index.values.tolist(), category_wise["value"])
plt.xticks(rotation=90)
plt.title("Products having price category-wise")
plt.show()

plt.bar(category_wise_without.index.values.tolist(), category_wise_without["price_string"])
plt.xticks(rotation=90)
plt.title("Products not having price category-wise")
plt.show()

plt.bar(product_type_wise.index.values.tolist(), product_type_wise["value"])
plt.xticks(rotation=90)
plt.title("Products having price product-type-wise")
plt.show()

plt.bar(product_type_wise_without.index.values.tolist(), product_type_wise_without["price_string"])
plt.xticks(rotation=90)
plt.title("Products not having price product-type-wise")
plt.show()

plt.bar(level_1_wise.index.values.tolist(), level_1_wise["value"])
plt.xticks(rotation=90)
plt.title("Products having price level-1-wise")
plt.show()

plt.bar(level_1_wise_without.index.values.tolist(), level_1_wise_without["price_string"])
plt.xticks(rotation=90)
plt.title("Products not having price level-1-wise")
plt.show()
# %%
