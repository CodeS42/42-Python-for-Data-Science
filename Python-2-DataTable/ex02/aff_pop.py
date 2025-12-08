from load_csv import load
import matplotlib.pyplot as plt


def filter_data(country, df, years):
    """

    """
    country_data = df[df["country"] == country].drop(columns=["country"])
    country_data = country_data.replace({"k": "e3", "M": "e6"}, regex=True).astype(float)
    country_data = country_data[years]
    country_data = country_data.iloc[0]
    return country_data


def aff_pop(df):
    """

    """
    years = [year for year in df.columns[1:] if 1800 <= int(year) <= 2050]
    france_data = filter_data("France", df, years)
    belgium_data = filter_data("Belgium", df, years)
    
    plt.plot(france_data.index, france_data.values, label="France", color="green")
    plt.plot(belgium_data.index, belgium_data.values, label="Belgium")
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.xticks(years[::40])
    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.legend(loc="lower right")
    plt.show()


def main():
    """

    """
    try:
        df = load("population_total.csv")
        aff_pop(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
