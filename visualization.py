#region imports
from AlgorithmImports import *
#endregion
import matplotlib.pyplot as plt

class StrategyVisualizer:
    def __init__(self):
        self.equity_curve = []

    def plot_equity_curve(self, equity_values):
        self.equity_curve = equity_values
        plt.plot(self.equity_curve)
        plt.xlabel("Time")
        plt.ylabel("Equity")
        plt.title("Strategy Equity Curve")
        plt.show()

    def evaluate_strategy(self):
        if len(self.equity_curve) < 2:
            print("Insufficient data to evaluate the strategy.")
        else:
            initial_equity = self.equity_curve[0]
            final_equity = self.equity_curve[-1]
            returns = (final_equity - initial_equity) / initial_equity
            print(f"Strategy Evaluation: Total returns = {returns * 100:.2f}%")
