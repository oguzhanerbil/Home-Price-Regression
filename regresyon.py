import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("Normalized_DataSon.csv")
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
print(data)