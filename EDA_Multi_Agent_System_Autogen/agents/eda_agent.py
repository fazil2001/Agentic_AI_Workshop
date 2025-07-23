import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

class EDAAgent:
    def analyze_data(self, df):
        description = df.describe(include='all').to_markdown()
        plot_path = 'reports/visuals.png'
        sns.pairplot(df.select_dtypes(include='number'))
        plt.savefig(plot_path)
        plt.close()
        return description, plot_path