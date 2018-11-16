import pandas as pd


df = pd.read_csv('GOOGL.csv')
y = list(df['close'].head(30))

# ML Program to find the equation of a linear regression line
# of the form y = mdays + c and predict the y for given days
days = [x for x in range(1, 31)]  # these will be days
# respective stock prices(close)

meandays = sum(days) / 30
meany = sum(y) / 30

numerator = 0
denominator = 0
for i in range(30):
    first = (days[i] - meandays)
    second = (y[i] - meany)
    b = (days[i] - meandays) ** 2
    numerator = numerator + first * second
    denominator = denominator + b
m = numerator / denominator  # Here, m is the slope of the regression line

c = meany - m * meandays  # Here, c is the intercept of the regression line

predday = float(input("Enter any value of days"))

predicted_y = m * predday + c
print(y)
print("The predicted value of y for the given value of days is", predicted_y)
