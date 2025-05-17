# Module for visualizations.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df: pd.DataFrame, column: str, title: str = "") -> None:
    """
    Plots a histogram of a specified column.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        column (str): Column to plot.
        title (str): Plot title.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(title or f"Histogram of {column}")
    plt.show()

def plot_boxplot(df: pd.DataFrame, group_col: str, value_col: str, title: str = "") -> None:
    """
    Plots a boxplot for a value column grouped by a categorical column.

    Args:
        df (pd.DataFrame): DataFrame.
        group_col (str): Column to group by.
        value_col (str): Value column.
        title (str): Plot title.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=group_col, y=value_col, data=df)
    plt.title(title or f"{value_col} by {group_col}")
    plt.show()