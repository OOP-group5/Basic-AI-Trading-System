#region imports
from AlgorithmImports import *
from clr import AddReference
AddReference("System")
AddReference("QuantConnect.Algorithm")
AddReference("QuantConnect.Common")

from System import *
from QuantConnect import *
from QuantConnect.Algorithm import *

from universe import BigTechUniverseSelectionModel
from alpha import GaussianNaiveBayesAlphaModel
from visualization import StrategyVisualizer

class GaussianNaiveBayesClassificationAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 10, 1)
        self.SetEndDate(2020, 10, 13)
        self.SetCash(1000000)
        
        self.SetUniverseSelection(BigTechUniverseSelectionModel())
        self.UniverseSettings.Resolution = Resolution.Daily
        
        self.SetAlpha(GaussianNaiveBayesAlphaModel())
        
        self.SetPortfolioConstruction(InsightWeightingPortfolioConstructionModel())
        
        self.SetExecution(ImmediateExecutionModel())
        
        self.SetRiskManagement(NullRiskManagementModel())
        
        self.strategy_visualizer = StrategyVisualizer()
        

    def OnData(self, data):
        equity_value = self.Portfolio.TotalPortfolioValue
        self.strategy_visualizer.plot_equity_curve(equity_value)
        

    def OnOrderEvent(self, orderEvent):
        equity_value = self.Portfolio.TotalPortfolioValue
        self.strategy_visualizer.plot_equity_curve(equity_value)
