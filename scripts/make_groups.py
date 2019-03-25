import numpy as np
import pandas as pd


def make_groups(df, N):
    """Make N random groups."""
    min_num_elements = len(df) // N
    while True:
        group_numbers = pd.Series(
            np.random.choice(
                list(range(N)) * (min_num_elements + 1), len(df), replace=False
            )
        )
        if (group_numbers.value_counts() >= min_num_elements).all():
            break

    df = df.copy()
    df["group"] = group_numbers
    return df


def load_data(path):
    wb = pd.read_excel(path).drop(columns=["Unnamed: 2"])
    wb.columns = wb.iloc[2]
    wb.columns.name = None
    wb = wb.iloc[3:].reset_index(drop=True)
    return wb


if __name__ == "__main__":
    np.random.seed(42)
    wb = load_data("Advanced Python Emails.xlsx")

    for group_id, group in make_groups(wb, 5).groupby("group"):
        assert len(group) >= len(wb) // 5
        print(group, end="\n-----------\n")
