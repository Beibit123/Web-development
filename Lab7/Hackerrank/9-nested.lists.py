if __name__ == '__main__':
    d={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name]=score
    scores = d.values()
    sort_scores = sorted(list(set(scores))) 
    second_min = sort_scores[1]
    names = []
    for key,value in d.items(): 
        if value==second_min: 
            names.append(key)
    names = sorted(names)
    for name in names: 
        print (name)
        
        
