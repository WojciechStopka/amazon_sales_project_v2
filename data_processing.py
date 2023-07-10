import pandas as pd
from project.DataCleaner import (
	configure_data,
	drop_data,
	replace_symbols,
	currency_to_euro,
	convert_to_numeric
)
from project.visualisation.Charts import (
	corr_chart,
)


if __name__ == "__main__":
	data = pd.read_csv("data/Amazon-Products.csv")
	configure_data(data)
	drop_data(data)
	replace_symbols(data)
	convert_to_numeric(data)
	currency_to_euro(data)
	corr_chart(data)

