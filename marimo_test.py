import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell
def _(mo):
    mo.md("""
    # Задание 1: Сравнение Marimo и Colab
    """)
    return


@app.cell
def _(pd):
    # Создаем DataFrame
    df = pd.DataFrame({
        "Пассажир": ["Василий", "Иван", "Мария"],
        "Выжил": [1, 0, 1],
        "Класс": [1, 3, 2]
    })
    return (df,)


@app.cell
def _(df):
    # Отображаем таблицу
    df
    return


if __name__ == "__main__":
    app.run()
