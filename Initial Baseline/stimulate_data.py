import numpy as np

# Simulated data generation parameters
num_stocks = 1000  # Number of stocks
max_length = 30  # Maximum length of returns

# Simulate data for technology sector stocks
tech_stocks = []

for _ in range(num_stocks):
    # Generate random returns for each stock
    stock_returns = np.random.normal(0, 0.02, np.random.randint(10, max_length))
    
    # Assign random direction (positive or negative) to each stock
    direction = np.random.choice(["positive", "negative"])
    
    # Create stock dictionary
    stock = {
        "returns": stock_returns.tolist(),
        "direction": direction
    }
    
    tech_stocks.append(stock)
