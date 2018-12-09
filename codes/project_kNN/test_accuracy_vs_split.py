import kNN
import matplotlib.pyplot as plt
import numpy as np

number_of_tests = 1000
split_range = np.linspace(0, 1, number_of_tests , endpoint=False)

accuracies = []
error_split_values = []

for split in split_range[1:]:
    try:
        accuracies.append(kNN.main(split))
    except Exception as E:
        print(E)
        error_split_values.append(split)

print("/"*80)
print("does not work for split values: " + str(error_split_values))

plt.plot(split_range[number_of_tests - len(accuracies):], accuracies)
plt.show()