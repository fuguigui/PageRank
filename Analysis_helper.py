import re
def topN(n,dict_to_order):
    after=sorted(dict_to_order.items(), key=lambda e: e[1],reverse=True)
    topn=list()
    num=n
    if len(after)<n:
        num=len(after)
    for i in range(num):
        topn.append(after[i])
    return topn
def compareDiff(fst,sec):
    penalty=50
    fst_dict=dict(fst)
    sec_dict=dict(sec)
    sum=0
    #
    # p1 = r"(?<=').+?(?=')"
    # pattern1 = re.compile(p1)

    print fst

    for fst_key in fst_dict.keys():
        re_fst_key='\''+fst_key+'\''
        fst_idx=fst.index(re_fst_key)

        print re_fst_key

        if fst_key in sec_dict.keys():
            sec_idx=sec.index(re_fst_key)
            sum=sum+abs(fst_idx-sec_idx)
        else:
            sum=sum+penalty
    return sum
