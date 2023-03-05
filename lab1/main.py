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

    svariance = np.std(standardized, axis=0)
    smean = np.mean(standardized, axis=0)

    print("------------------attribute nr", i)
    print("before standarization: ")
    print("variance =", variance)
    print("mean =", mean)
    print("after standarization: ")
    print("variance =", svariance)
    print("mean =", round(smean))

# Format the data from file - convert symbolic values
dt = np.dtype([('col1', np.int32), ('col2', 'U32'), ('col3', 'U32'), ('col4', np.int32),
               ('col5', 'U16'), ('col6', 'U10'), ('col7', np.int32), ('col8', np.int32),
               ('col9', np.float64), ('col10', np.int32), ('col11', np.int32), ('col12', np.int32),
               ('col13', np.float64), ('col14', np.int32)])
churn = np.genfromtxt('Churn_Modelling.csv', delimiter=',', dtype=dt, names=True)

geo = churn['Geography']
geo_map = {'France': 0, 'Spain': 1, 'Germany': 2}
geo_dummy = np.zeros((len(geo), len(geo_map)))
for k, v in geo_map.items():
    geo_dummy[:, v] = np.where(geo == k, 1, 0)

# churn = np.hstack((churn['CreditScore'], geo_dummy, churn['Geography']))
# merged = np.hstack((geo_dummy, churn))
# merged = np.concatenate((geo_dummy, churn), axis=None)
# print(merged[150])
print(geo_dummy.shape)
print(type(churn))
new_churn = []
for i in range(len(churn)):
    temp = list(churn[i])
    temp.insert(0, int(geo_dummy[i, 2]))
    temp.insert(0, int(geo_dummy[i, 1]))
    new_churn.append(tuple(temp))
print(churn[150])
print(geo_dummy[150])
print(new_churn[150])
# print(type(churn))
# print(geo_dummy.shape)
