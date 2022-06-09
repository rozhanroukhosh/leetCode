def combinationSum(candidates, target):
        sumDic = {}
        finalist = []
        candidates = sorted(candidates)
        def helpMe(sumDic, target):
            for key in sumDic:
                for j in range(len(candidates)):
                    addup = sumDic[key]+ candidates[j]
                    
                    if addup>target:
                        continue 
                    newKey = tuple(sorted((*key, candidates[j])))
                    print(newKey)
                    if newKey not in sumDic:
                        sumDic[newKey]= addup
                        if addup == target:
                            finalist.append([x for x in newKey])
            print("wtf")               
            helpMe(sumDic, target)
            
                    
                        
                    
        
        for i in range(len(candidates)):
            sumDic[(candidates[i],)] = candidates[i]
            helpMe(sumDic, target)
        return finalist
combinationSum([2,3,6,7], 7)