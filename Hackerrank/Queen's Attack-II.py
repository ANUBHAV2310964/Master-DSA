def queenAttack(n,k,r_q,c_q,obs):
  if n ==0:
    return 0
    vset=set([tuple(item) for item in obs])
    if (r_q,c_q) in vset:
      return 0
    directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count=0
    for u,v in directions:
      cur=(r_q+u,c_q+v)
      while 1<=cur[0]<=n and 1<=cur[1]<=n and cur not in vset:
        cur=(cur[0]+u,cur[1]+v)
        count+=1
    return count
 n,k=4,0
r_q,c_q=4,4
obs=[]
ans=queensAttack(n,k,r_q,obs)
