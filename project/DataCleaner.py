import pandas as pd

# ['name', 'main_category', 'sub_category', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']


data = pd.read_csv("..//data/Amazon-Products.csv")
data = data.drop(columns=['Unnamed: 0'])
pd.set_option('display.max_columns', 9, 'display.width', 2000)

# Dropping NaN values to have complete data to analyze
data.dropna(inplace=True)


# Removing "," and "₹" from columns
data["discount_price"] = data["discount_price"].replace(",", "", regex=True).replace("₹", "", regex=True)
data["actual_price"] = data["actual_price"].replace(",", "", regex=True).replace("₹", "", regex=True)
data["no_of_ratings"] = data["no_of_ratings"].replace(",", "", regex=True)

# Dropping rows where ratings column is equal to "Get"/"FREE" or contains "₹" symbol
data.drop(data[(data.ratings == "Get") | (data.ratings == "FREE") | (data.ratings.str.contains("₹"))].index,
          inplace=True)

# Converting data in "discount_price" and "actual_price" columns into numeric and
data["discount_price"] = pd.to_numeric(data["discount_price"])
data["actual_price"] = pd.to_numeric(data["actual_price"])

# Converting currency of columns into euro
data["discount_price"] = data["discount_price"].apply(lambda value: round((value/90), 2))
data["actual_price"] = data["actual_price"].apply(lambda value: round((value/90), 2))

data["ratings"] = data["ratings"].astype(float)
data["no_of_ratings"] = data["no_of_ratings"].astype(float)




