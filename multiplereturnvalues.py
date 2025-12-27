import statistics
def mean_median_mode(list1):
    return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]

print(mean_median_mode([1,45,5,6,7,7,89,76,56]))
