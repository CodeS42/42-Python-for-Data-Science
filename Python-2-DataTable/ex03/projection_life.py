from load_csv import load
import matplotlib.pyplot as plt
# matplotlib, seaborn or any lib for Data Visualization and your lib of ex00

def


def main():
    """

    """
    try:
        df1 = load("population_total.csv")
        aff_pop(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
