from  sklearn import tree
if __name__ == '__main__':
    features=[[180,1],[150,0],[177,0],[165,0],[169,1],[160,0]]
    label=["man","woman","man","woman","man","woman"]

    clf=tree.DecisionTreeClassifier()


    clf = clf.fit(features,label)
    s1 = clf.predict([[158,0]])
    s2 =clf.predict([[176,1]])

    print(s1)
    print(s2)
