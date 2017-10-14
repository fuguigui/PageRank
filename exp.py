from mutual_map import *
import re
from Analysis_helper import *
from PageRank import *
import numpy as np

data = open('E:\\learning\\WebDataMining\\hw\\aan\\release\\2014\\venue_test.txt')

# pattern of the venue
p1 = r"(?<=id\s=\s{).+?(?=})"
pattern1 = re.compile(p1)
p2 = r"(?<=venue\s=\s{).+?(?=})"
pattern2 = re.compile(p2)

# venue
venue=MapToMatrix('E:\\learning\\WebDataMining\\hw\\aan\\release\\2014\\')
venue.FileToList_Reg('venue_test.txt', pattern1, pattern2)
venue_len=venue.getLen()
venue_mat=venue.SwitchMap('paper_venue_test.txt')
venue_init=np.ones(venue_len)

pg = PageRank(50, 0.0001, 0.6)
venue_resvec = pg.run(venue_mat, venue_init, venue_len)

venue.ScoreToVenue(venue_resvec, "exp_venue_rank.txt")
venue_resmap =venue.getResult()
venue_topn=topN(3,venue_resmap)

sum_error=compareDiff(venue_topn,venue_topn)
print sum_error
# #
# alpha=0.6
# topn=10
# print "when alpha=%f, the top %d is \n"%(alpha,topn)