from load_csv import load
import matplotlib.pyplot as plt
# matplotlib, seaborn or any lib for Data Visualization and your lib of ex00

def projection_life(df1, df2):
    income_per_person = df1["1900"]
    income_per_person = income_per_person.replace({"k": "e3"}, regex=True).astype(float)
    life_expectancy = df2["1900"]
    life_expectancy = life_expectancy.replace({"k": "e3"}, regex=True).astype(float)
    # print( income_per_person)

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.scatter(income_per_person, life_expectancy)
    plt.show()


def main():
    """

    """
    try:
        df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df2 = load("life_expectancy_years.csv")
        projection_life(df1, df2)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
