# Module for statistical analysis.
import pandas as pd
import scipy.stats as stats
from typing import Tuple

def anova_oneway(df: pd.DataFrame, group_col: str, value_col: str) -> Tuple[float, float]:
    """
    Performs one-way ANOVA.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        group_col (str): The column to group by (categorical).
        value_col (str): The column to analyze (numerical).

    Returns:
        Tuple[float, float]: (F-statistic, p-value)
    """
    groups = [group[value_col].values for name, group in df.groupby(group_col)]
    f_stat, p_val = stats.f_oneway(*groups)
    return f_stat, p_val