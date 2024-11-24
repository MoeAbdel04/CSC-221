# File: analysis.py

import pandas as pd
from textblob import TextBlob
from datetime import datetime
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from Excel file and merge with airline lookup."""
    try:
        tweets = pd.read_excel(file_path, sheet_name="Sheet1")
        airline_lookup = pd.read_excel(file_path, sheet_name="Airline Code Lookup")
        tweets = tweets.merge(airline_lookup, on="IATA_CODE", how="left")
        return tweets
    except Exception as e:
        raise Exception(f"Error loading data: {e}")

def add_sentiment(df):
    """Add sentiment column using TextBlob."""
    def analyze_sentiment(text):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0:
            return "positive"
        elif polarity < 0:
            return "negative"
        else:
            return "neutral"
    
    df["sentiment"] = df["text"].apply(analyze_sentiment)
    return df

def add_day_of_week(df):
    """Add day_of_week column based on date_created."""
    try:
        df["day_of_week"] = pd.to_datetime(df["date_created"]).dt.day_name()
    except Exception as e:
        raise Exception(f"Error parsing dates: {e}")
    return df

def summarize_and_plot(df, group_by, column, filename):
    """Summarize data and generate plots."""
    summary = df.groupby(group_by)[column].value_counts(normalize=True).unstack().fillna(0) * 100
    summary.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.title(f"{column.capitalize()} by {group_by.capitalize()}")
    plt.xlabel(group_by.capitalize())
    plt.ylabel("Percentage")
    plt.legend(title=column.capitalize())
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return summary

def save_summary(df, columns, filename):
    """Save summarized data to a CSV file."""
    try:
        df[columns].to_csv(filename, index=False)
    except Exception as e:
        raise Exception(f"Error saving summary: {e}")
