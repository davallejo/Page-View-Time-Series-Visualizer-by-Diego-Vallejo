#time_series_visualizer.py
#Autor: Diego Armando Vallejo Vinueza

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df.index, df['value'], color='red', label='Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.legend()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_bar, x='year', y='value', hue='month', ci=None, palette='viridis')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Year-wise Average Page Views on freeCodeCamp Forum (2016-2019)")
    ax.legend(title="Months", loc="upper left", bbox_to_anchor=(1, 1))

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
