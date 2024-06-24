# A network that learns if we should cate
import csv
# import tensorflow as tf

# from sklearn.model_selection import train_test_split

# read data in from file
with open() as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": 1 if row[4] == "0" else 0
        })

# separate data into training and testing groups
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
x_training, x_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)

#create a neural network
