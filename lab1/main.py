import numpy as np

data = np.loadtxt("australian.txt")

# find available decision classes
# ?

# find size of decision classes
print("size of classes: ", len(data))

# minimal and maximal values for each attribute (2,3,7,10,13,14)
numbers = [2,3,7,10,13,14]
for i in numbers:
    print("max value for a",i," = ", np.max(data[:, i]))
    print("min value for a", i, " = ", np.min(data[:, i]))

# for each attribute detect the number of different available values
for i in range (0,14):
    print("number of different values for a",i," : ", len(np.unique(data[:,i])))

# for each attribute list the set of different, available values
for i in range (0,14):
    print("all the different values for a",i," : ", np.unique(data[:,i]))

# compute standard deviation for each attribute
# in the whole system and separately for each decision class
for i in numbers:
    print("stadard deviation for column",i," :", np.std(data[:,i], 0))

print("-----------------------------------------------------------")
# generate 10% missing values and complete with most common/mean
row = []
for i in range (0,14):
    if i in numbers:
        mean = np.mean(data[:,i],0)
        row.append(mean)
    else:
        unik, counts = np.unique(data[:, i], return_counts=True)
        most = unik[np.argmax(counts)]
        row.append(most)
print("array will be filled with rows: ", row)

print("----------------------------------------------------------")
# normalize attribute values into intervals: ...
intervals = [(-1, 1), (0, 1), (-10, 10)]
for interval in intervals:
    ai, bi = interval
    print("interval: ",ai,bi)
    for a in numbers:
        normalized = (((data[:,a] - np.min(data[:,a])) * (bi - ai))/ (np.max(data[:,a]) - np.min(data[:,a]))) + ai
        print("normalized ",a,": ",normalized)

print("---------------------------------------------------------")
# standarization of attributes of selectred data
data = data.astype(int)
for i in numbers:
    X = data[:,i]
    variance = np.std(X, axis=0)
    mean = np.mean(X, axis=0)
    standardized = (X - mean) / variance

    svariance = np.std(standardized)
    smean = np.mean(standardized)

    print("------------------attribute nr", i)
    print("before standarization: ")
    print("variance =", np.var(data[:,i]))
    print("mean =", np.mean(data[:,i]))
    print("after standarization: ")
    print("variance =", svariance)
    print("mean =", smean)

# Format the data from file - convert symbolic values

