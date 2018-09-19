from numpy import *
import matplotlib.pyplot as plt

def euclDistance (vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))

def initCentroids (dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        centroids[i, :] = dataSet[index, :]
    return centroids


def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        ## for each sample
        for i in xrange(numSamples):
            minDist = 100000.0
            minIndex = 0
            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist = distance
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist ** 2

        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis=0)

    print 'Congratulations, cluster complete!'
    return centroids, clusterAssment

if __name__ == '__main__':

    print('load data...')
    dataSet = []
    fileIn = open('G://unclaimed.txt')
    for line in fileIn.readlines():
        lineArr = line.split(' ')
        a = lineArr[8].split('\n')
        dataSet.append([float(lineArr[0]),float(lineArr[1]),float(lineArr[2]),float(lineArr[3]),float(lineArr[4]),float(lineArr[5]),float(lineArr[6]),float(lineArr[7]),float(a[0])])

    print 'clustering...'
    dataSet = mat(dataSet)
    k = 6
    centroids, clusterAssment = kmeans(dataSet, k)
