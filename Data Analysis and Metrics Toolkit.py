import math
from math import ceil, floor
import numpy as np 
import statistics as st

def calculate_volume(length, width, height):
    """
    Calculates the volume of a sample given its length, width, and height.
    """
    return round(length * width * height)

def calculate_mean(data):
    """
    Calculates the mean of a list of numbers.
    """
    sorted_data = sorted(data)
    return round(sum(data) / len(data))

def calculate_median(data):
    """
    Calculates the median of a list of numbers.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return round((sorted_data[n//2-1] + sorted_data[n//2]) / 2) # // for interger devision and / for float divition 
    else:
        return round(sorted_data[n//2])

def calculate_standard_deviation(data):
    """
    Calculates the standard deviation of a list of numbers.
    """
    sorted_data = sorted(data)
    mean = round(calculate_mean(data))
    variance = round(sum((x - mean) ** 2 for x in data) / len(data))
    return round(math.sqrt(variance))


def calculate_skewness(data): # 3 * (Mean – Median) / Standard Deviation 
    """
    Calculates the skewness of a list of numbers.
    """
    n = len(data)
    if n < 3:
        return float('nan')
    mean = round(calculate_mean(data))
    median = round(calculate_median(data))
    std_dev = round(calculate_standard_deviation(data))
    skewness = round(3 * (mean - median) / std_dev)
   # skewness = sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std_dev ** 3)
    return skewness

def calculate_corr_coeffnp(sample_P_data, sample_Q_data):
    corr_coef = round(np.corrcoef(sample_P_data, sample_Q_data)[0, 1])

    return corr_coef


def identify_outliers(data):
     sorted_data = sorted(data)
     mean = round(calculate_mean(sorted_data))
     std_dev = round(calculate_standard_deviation(sorted_data))
   #  Outliers = []
  #   for i in range(len(sorted_data)):
  #       if abs(data[i] - mean) > 3 * std_dev:
   #          Outliers.append(data[i])
             
   #  return Outliers

     Lower_bound = round(mean - 3 * std_dev)
     print("Lower_bound: ", Lower_bound)
     Upper_bound = round(mean + 3 * std_dev)
     print("Upper_bound: ", Upper_bound)
   #  threshold = 3 * std
   #  Outliers = [x for x in data if abs(x - mean) > threshold]
     Outliers = [x for x in sorted_data if x < Lower_bound or x > Upper_bound]
    # for x in sorted_data:
         #if x < Lower_bound or x > Upper_bound:
           #  Outliers_list = []
           #  for Outlier in Outliers:
            #     Outliers_list.append(Outlier)
            #     print(Outliers_list)
     return Outliers
 
def identify_outliers_quartiles(data):
     sorted_data = sorted(data)
     Quartile_1 = round(st.median(sorted_data[:ceil(len(sorted_data)/2)]))
     Quartile_3 = round(st.median(sorted_data[ceil(len(sorted_data)/2):]))
     INT_Quartile = round(Quartile_3 - Quartile_1)
     Lower_bound = round(Quartile_1 - 1.5 * INT_Quartile)
     print("Lower_bound_quartile: ", Lower_bound)
     Upper_bound = round(Quartile_3 + 1.5 * INT_Quartile)
     print("Upper_bound_quartile: ", Upper_bound)
     Outliers = [x for x in sorted_data if x < Lower_bound or x > Upper_bound]

     return Outliers
 # Normalizing data sample 
def Normalizing(data):
     Normalizing_List = []
     for x in data:
         x = round((x - min(data)) / (max(data) - min(data)))
         Normalizing_List.append(x)

     return Normalizing_List

def Euclidean_metric(sample_P_data, sample_Q_data):
    if len(sample_P_data) != len(sample_P_data):
        raise ValueError("Lists must be of equal length")
    Sum_p_P_Q = 0.0
    for i in range(len(sample_P_data)):
         Sum_p_P_Q += round((sample_P_data[i] - sample_Q_data[i])**2)
    return round(math.sqrt(Sum_p_P_Q))

def Manhattan_metric(sample_P_data, sample_Q_data):
    if len(sample_P_data) != len(sample_P_data):
        raise ValueError("Lists must be of equal length")
    Sum_p_P_Q = 0.0 
    for i in range(len(sample_P_data)):
        Sum_p_P_Q += round(abs(sample_P_data[i] - sample_Q_data[i]))
    return round(Sum_p_P_Q)

def Maximum_metric(sample_P_data, sample_Q_data):
    if len(sample_P_data) != len(sample_Q_data):
        raise ValueError("Lists must be of equal length")
    p_P_Q_max = 0.0
    #List_p_P_Q = []
    for i in range (len(sample_P_data)):
        p_P_Q = round(abs(sample_P_data[i] - sample_Q_data[i]))
        if p_P_Q > p_P_Q_max:
           p_P_Q_max = p_P_Q
      #  List_p_P_Q.append(p_P_Q)
    return round(p_P_Q_max)

def print_sample_info(sample_num, length, width, height, data):
    """
    Prints information about a sample, including its volume, length, width, height,
    data, length of data, mean, median, and standard deviation.
    """

    volume = calculate_volume(length, width, height)
    mean = calculate_mean(data)
    median = calculate_median(data) # Build in mutable sequence
    std_dev = calculate_standard_deviation(data) 
    skewness = calculate_skewness(data)
    Outliers_by_Sigma_rule = identify_outliers(data)
    Outliers_by_Sigma_quartiles = identify_outliers_quartiles(data)
    Normalizing_data = Normalizing(data)
   # print('corr_coeff: ', corr_coeff)

    print(f"Sample {sample_num}:")
    print(f"  Volume: {volume} cubic units")
    print(f"  Length: {length} units")
    print(f"  Width: {width} units")
    print(f"  Height: {height} units")
    print(f"  Data: {data}")
    print(f"  Length of data: {len(data)}")
    print(f"  Mean: {mean}")
    print(f"  Median: {median}")
    print(f"  Standard deviation: {std_dev}")
    print(f"  Skewness of the sample: {skewness}")
    print(f"  Outliers by Sigma rule: {Outliers_by_Sigma_rule}")
    print(f"  Outliers_by_Sigma_quartiles: {Outliers_by_Sigma_quartiles}")
    print(f"  Normalizing_data: {Normalizing_data}")
   # print(f" Correlation coefficient: {corr_coeff}")
# Sample usage of the functions with two lists of data
sample_P_data = [9, 10, 8, 19, 18, 19, 4, 12, -22] # [50, 10, 8, 19, 18, 19, 4, 12, -22]
#Outliers_by_Sigma_rule = identify_outliers(sample_P_data)
sample_P_length = 2
sample_P_width = 3
sample_P_height = 4

sample_Q_data = [23, 28, 29, 14, 22, 3, 1, 6, -29] 
sample_Q_length = 1
sample_Q_width = 2
sample_Q_height = 2
corr_coeff = calculate_corr_coeffnp(sample_P_data, sample_Q_data)
Euclidean_metric_calculate = Euclidean_metric(sample_P_data, sample_Q_data)
Manhattan_metric_calculate = Manhattan_metric(sample_P_data, sample_Q_data)
Maximum_metric_calculate = Maximum_metric(sample_P_data, sample_Q_data)
#corr_coef = np.corrcoef(sample_P_data, sample_Q_data)[0, 1]
#print('corr_coeff: ', corr_coeff) 

print_sample_info(1, sample_P_length, sample_P_width, sample_P_height, sample_P_data)
print()
print_sample_info(2, sample_Q_length, sample_Q_width, sample_Q_height, sample_Q_data)
print()
print(f" Correlation coefficient: {corr_coeff}")
print(f" Euclidean_metric: {Euclidean_metric_calculate} ")
print(f" Manhattan_metric: {Manhattan_metric_calculate}")
print(f" Maximum_metric: {Maximum_metric_calculate}")
print()

""" 
return (sorted_data[n//2-1] + sorted_data[n//2]) / 2

Sure! This line of code is calculating the median of a list of numbers.

First, the sorted function is called on the input data list to sort the numbers in ascending order. The resulting sorted list is stored in the sorted_data variable.

Next, the length of the sorted data list is calculated using len(sorted_data) and stored in the n variable.

If the length of the sorted data list is even (i.e. n % 2 == 0), then there is no single middle value. Instead, the median is defined as the average of the two middle values. To calculate this average, the indices of the two middle values are n//2-1 and n//2, and the values at these indices are accessed using sorted_data[n//2-1] and sorted_data[n//2]. The sum of these two values is calculated using the + operator, and then this sum is divided by 2 to find the average. This average is returned as the median.

If the length of the sorted data list is odd, then there is a single middle value. In this case, the index of the middle value is n//2, and the value at this index is accessed using sorted_data[n//2]. This value is returned as the median.

Overall, this line of code is using Python's built-in functionality to sort a list of numbers and calculate its median, which is a statistical measure of the "middle" value of the data.
""" 

"""
Skewness is a statistical measure that indicates the degree of asymmetry in the distribution of a dataset. It is a measure of the deviation of the dataset from the normal distribution. In other words, it shows whether the data is skewed to the left or to the right.

Skewness can be positive, negative, or zero. Positive skewness indicates that the tail of the distribution is longer on the right side, while negative skewness indicates that the tail is longer on the left side. Zero skewness indicates that the distribution is perfectly symmetrical.

Skewness can be calculated using various methods, including the Pearson's moment coefficient of skewness and the Bowley's coefficient of skewness. These methods use different formulas to calculate the degree of skewness, but they all aim to measure the same thing: how asymmetrical the distribution is.

Skewness is an important concept in statistics because it can affect the interpretation of the data. For example, if a dataset has a positive skew, the mean will be larger than the median, and the distribution will be pulled towards the right. This can affect the accuracy of certain statistical tests and models. Therefore, it is important to consider skewness when analyzing data.

"""