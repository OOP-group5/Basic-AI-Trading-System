import numpy as np
from sklearn.naive_bayes import GaussianNB

def train_gnb_classifiers(stocks):
    max_length = max(len(stock["returns"]) for stock in stocks)
    features = np.array([stock["returns"] + [0] * (max_length - len(stock["returns"])) for stock in stocks])
    labels = np.array([stock["direction"] for stock in stocks])

    gnb = GaussianNB()
    gnb.fit(features, labels)

    return gnb

def main():
    tech_stocks = [
        {
            "returns": [0.01, 0.02, -0.03, 0.01],
            "direction": "positive"
        },
        {
            "returns": [0.02, -0.03, 0.01, 0.02],
            "direction": "positive"
        },
        {
            "returns": [-0.03, 0.01, 0.02, -0.01],
            "direction": "negative"
        },
        {
            "returns": [0.01, 0.02, -0.01, 0.01],
            "direction": "positive"
        },
        {
            "returns": [0.02, -0.01, 0.01],
            "direction": "positive"
        }
    ]

    classifiers = train_gnb_classifiers(tech_stocks)
    # Use the classifiers for prediction or further analysis

main()
