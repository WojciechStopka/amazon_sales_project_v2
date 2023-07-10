import pandas as pd

# ['name', 'main_category', 'sub_category', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']
EURO_EXCHANGE_RATE = 90


def configure_data(data):
    # Removing Unnamed column
    data = data.drop(columns=['Unnamed: 0'])
    pd.set_option('display.max_columns', 9, 'display.width', 2000)


def drop_data(data):
    # Dropping NaN values to have complete data to analyze
    # Dropping empty rows where ratings column is equal to "Get"/"FREE" or contains "₹" symbol
    data.dropna(inplace=True)
    data.drop(data[(data.ratings == "Get") | (data.ratings == "FREE") | (data.ratings.str.contains("₹"))].index,
              inplace=True)


def replace_symbols(data):
    # Removing "," and "₹" from columns
    data["discount_price"] = data["discount_price"].replace(",", "", regex=True).replace("₹", "", regex=True)
    data["actual_price"] = data["actual_price"].replace(",", "", regex=True).replace("₹", "", regex=True)
    data["no_of_ratings"] = data["no_of_ratings"].replace(",", "", regex=True)


def currency_to_euro(data):
    # Converting currency of "discount_price" and "actual_price" columns into euro and round to 2 places.
    data["discount_price"] = data["discount_price"].apply(lambda value: round((value/EURO_EXCHANGE_RATE), 2))
    data["actual_price"] = data["actual_price"].apply(lambda value: round((value/EURO_EXCHANGE_RATE), 2))


def convert_to_numeric(data):
    # Converting data in "discount_price" and "actual_price" columns into numeric
    data["discount_price"] = pd.to_numeric(data["discount_price"])
    data["actual_price"] = pd.to_numeric(data["actual_price"])
    data["ratings"] = pd.to_numeric(data["ratings"])
    data["no_of_ratings"] = pd.to_numeric(data["no_of_ratings"])




