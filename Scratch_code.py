#%%
import pandas as pd
# %%
df = pd.read_csv("2022_02_08-02_30_31_AM.csv")
# %%
df.head()
# %%
products_with_price = df[df["price_string"].notnull()]
products_without_price = df[df["price_string"].isna()]

products, categories, levels = df["product_type"].unique(), \
    df["category"].unique(), df["level_1"].unique()


#%%
df_preprocess = df.dropna(subset = ["price_string"])
df_preprocess["price_string"] = df_preprocess["price_string"].apply(lambda x: "$"+x if x[0].isdigit() else x)
df_preprocess["currency"] = df_preprocess["price_string"].apply(lambda x: x[0])
df_preprocess["value"] = df_preprocess["price_string"].apply(lambda x: float(x[1:]))
df_preprocess.drop(columns=["price_string", "price_string_unf"], inplace = True)
#df_preprocess["price_string"] = df_preprocess["price_string"].astype(dtype = "float", copy = True)
#%%
category_average = df_preprocess.loc[: , "price_string":"category"].groupby(["category"]).mean()
category_average.head()

# %%
df_preprocess.info()

# %%
df.shape[0]
# %%
#Required output
print("NUMBER OF PRODUCTS WITH PRICE   :", products_with_price.shape[0])
print("NUMBER OF PRODUCTS WITHOUT PRICE:", products_without_price.shape[0])
print("AVERAGE PRICE CATEGORY-WISE:",category_average)
# %%
df_preprocess.info()
# %%
