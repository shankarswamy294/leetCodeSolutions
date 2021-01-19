class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        opted={1:True}
        op=[1]
        kk=k
        n-=1
        while n:
            if op[-1]-k > 0 and op[-1]-k not in opted:
                op.append(op[-1]-k)
            else:
                if k==1:
                    for i in range(1,kk+1):
                        if k==1 and op[-1]+i not in opted:
                            op.append(op[-1]+i)
                            break
                else:
                    op.append(op[-1]+k)
                
            opted[op[-1]]=True
            if k>1:
                k-=1
            n-=1
            
        return op
    
