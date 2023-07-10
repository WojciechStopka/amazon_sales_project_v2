import matplotlib.pyplot as plt
import seaborn as sns


def corr_chart(data):
	sns.heatmap(data.corr(method='pearson', numeric_only=True), annot=True)
	plt.show()
