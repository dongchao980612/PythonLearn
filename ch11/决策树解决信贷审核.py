import operator
from math import log

"""
函数说明    
    创建测试数据集
返回值
    dataSet 数据集
    labels  特征标签
"""
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['有稳定收入', '有房产','审核结果']  # 特征值
    return dataSet, labels

"""
函数说明    
    计算给定数据的香农熵
参数
    dataSet 数据集
返回值
    shannonEnt 信息熵
"""
def calShannonEnt(dataSet):  # 计算给定数据集的香农熵
    numEntries = len(dataSet)  # 计算数据集中实例的总数，为计算每个类标签的概率做准备
    labelCounts = {}  # 统计每个类标签出现的次数
    for featVec in dataSet:  # 遍历每一个样本
        currentLabel = featVec[-1]  # 获得当前样本的分类
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0  # 如果该类标签不在统计字典中，则将其收录
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:  # 遍历每一个类标签
        prob = float(labelCounts[key]) / numEntries  # 计算属于该类标签的样本在总体样本中出现的概率
        shannonEnt -= prob * log(prob, 2)  # 熵的计算子公式，对其求和就可以得到熵
    return shannonEnt  # 返回熵

"""
函数说明
    按照给定特征划分数据集
参数
    dataSet 待划分的数据集
    axis    划分数据集的特征
    value   指定的特征的值
返回值
    return  返回划分好了的数据集

"""
def splitDataSet(dataSet, axis, value):
    retDataSet = []  # Python中函数参数传递的是列表的引用，所以需要重新声明新的列表对象，防止修改原始的数据集
    for featVec in dataSet:  # 遍历数据集中每一个元素
        if featVec[axis] == value:  # 如果该样本特征值与指定特征的值相符
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])  # 上一行与这一行将当前样本除axis位以外的特征值抽取出来放入reducedFeatVec中
            retDataSet.append(reducedFeatVec)  # retDataSet存放这些样本列表（每个样本都是一个列表）
    return retDataSet


def chooseBestFeatureToSplit(dataSet):  # 选择最好的数据集划分方式
    """
    1、dataSet必须是一个由列表元素组成的列表 且所有的列表元素都要具有相同的数据长度
    2、dataSet的每个列表元素（样本）的最后一列必须是当前实例的类别标签
    :param dataSet: 要划分的数据集
    :return: 最佳特征的下标
    """
    numFeatures = len(dataSet[0]) - 1  # numFeatures存放了当前数据集包含了多少个特征属性，特征数量 = 样本长度 - 类标签（1）
    baseEntropy = calShannonEnt(dataSet)  # 计算整个样本集的原始香农熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 遍历数据集中的所有特征
        featList = [example[i] for example in dataSet]  # 按顺序将每个样本的第i个特征值取出并生成列表
        uniqueVals = set(featList)  # 去除重复的特征值，从列表中创建集合是Python语言中得到列表中唯一元素值的最快方法
        newEntropy = 0.0  # 新的香农熵初始化
        for value in uniqueVals:  # 遍历当前特征中所有的特征值
            subDataSet = splitDataSet(dataSet, i, value)  # 按当前特征值进行样本集的划分
            prob = len(subDataSet) / float(len(dataSet))  # 求出取到当前特征值的样本占总样本的比例，也就是在总样本下取到该特征值的概率
            newEntropy += prob * calShannonEnt(subDataSet)  # 条件熵的计算子公式，对其所有特征值求和可得到给定特征A的条件下样本集的条件熵
        infoGain = baseEntropy - newEntropy  # newEntropy也就是给定特征A的条件下样本集的条件概率分布的熵对特征A的数学期望，信息增益 = 样本集的原始香农熵 - 当前特征的条件熵
        if (infoGain > bestInfoGain):  # 某特征的信息增益越大，说明该特征具有对样本集更强的分类能力
            bestInfoGain = infoGain
            bestFeature = i  # 记录最佳特征的下标
    return bestFeature


def majorityCnt(classList):
    """
    :param classList: 待检查的样本集
    :return: 出现次数最多的类标签
    """
    classCount = {}  # 存储了每个类标签出现的次数
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0  # 如果类标签不在字典中，就将其收录
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 按照类标签的出现次数进行排序
    return sortedClassCount[0][0]


def createTree(dataSet, labels):  # 创建树的函数代码
    """
    :param dataSet: 样本集
    :param labels: 特征列表
    :return: 创建好的决策树
    """
    classList = [example[-1] for example in dataSet]  # 按顺序获得当前样本集中所有样本的类标签
    if classList.count(classList[0]) == len(classList):  # 如果当前样本的类标签都相同，则直接返回该类标签
        return classList[0]
    if len(dataSet[0]) == 1:  # 如果当前样本集中的样本已经在之前的划分中使用完了所有特征，则返回当前所有样本中占比最大的类标签
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 选择最好的划分特征，bestFeat为特征的下标
    bestFeatLabel = labels[bestFeat]  # 按照下标取出最好的划分特征
    myTree = {bestFeatLabel: {}}  # 使用字典类型存储树的信息
    del (labels[bestFeat])  # 将当前已经划分过的最好特征从特征列表中删除
    featValues = [example[bestFeat] for example in dataSet]  # 获取当前样本集中每个样本的最好划分特征的特征值并生成列表
    uniqueVals = set(featValues)  # 唯一化最好划分特征的特征值
    for value in uniqueVals:  # 遍历最好划分特征的特征值
        subLabels = labels[:]  # 复制已删除最好划分特征的labels列表，作为递归的参数，保证了每次调用createTree()时不改变原始列表的内容
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),
                                                  subLabels)  # 按最好划分特征划分样本集并递归构造子树
    return myTree


def classify(inputTree, featLabels, testVec):  # 使用决策树的分类函数
    firstStr = list(inputTree)[0]  # 获取第一层划分的特征
    secondDict = inputTree[firstStr]  # 获取第二层
    featIndex = featLabels.index(firstStr)  # 找寻特征列表中该特征的下标
    key = testVec[featIndex]  # 获取测试向量中该特征对应的特征值
    valueOfFeat = secondDict[key]  # 获取该特征值下的节点值
    if isinstance(valueOfFeat, dict):  # 节点值是否为字典，也就是是否为子树
        classLabel = classify(valueOfFeat, featLabels, testVec)  # 仍存在，则递归进行决策，将最终的类标签保存在classLabel中
    else:
        classLabel = valueOfFeat  # 不存在，则类标签就是当前节点的值
    return classLabel  # 返回类标签

if __name__ == '__main__':
    dataSet,labels = createDataSet()
    featLabels=[]
    tree = createTree(dataSet,labels,featLabels)
    print(tree)