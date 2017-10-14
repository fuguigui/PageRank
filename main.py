from Analysis_helper import *
from train_model import *
import os
itr=500
error=0.00001
read_path='E:\\learning\\WebDataMining\\hw\\aan\\release\\2014\\'

Model = TrainModel(itr, error)
Model.read_data(read_path)

author_topn=list()
paper_topn=list()
venue_topn=list()
topn=10

i=0
for alpha in range(6,10,1):
    # create the folder to save the result
    dir_name="alpha_"+str(alpha)+"\\"
    print read_path, dir_name
    print "alpha = %d" %alpha
    isExists=os.path.exists(read_path+dir_name)
    if not isExists:
        os.makedirs(read_path+dir_name)

    # train the model and get the result
    author, paper, venue = Model.run(alpha/10.,dir_name)

    # get the top n of the results
    author_topn.append(topN(topn,author))
    paper_topn.append(topN(topn,paper))
    venue_topn.append(topN(topn,venue))
    i=i+1

# save the top n results and analyze the L1 distance
# create the report files
isExists=os.path.exists(read_path+"report\\")
if not isExists:
    os.makedirs(read_path+"report\\")
author_report=open(read_path+'report\\author_topn_report.txt','w')
paper_report=open(read_path+'report\\paper_topn_report.txt','w')
venue_report=open(read_path+'report\\venue_topn_report.txt','w')

author_error=0
paper_error=0
venue_error=0
alpha=0.6
for i in range(len(author_topn)):
    author_report.write("when alpha=%f, the top %d are \n"%(alpha,topn))
    for j in range(len(author_topn[i])):
        print author_topn[i][j]
        author_report.write(str(author_topn[i][j]))
        author_report.write('\n')
        print "temp"
    author_report.write('\n')

    paper_report.write("when alpha=%f, the top %d are \n"%(alpha,topn))
    for j in range(len(paper_topn[i])):
        paper_report.write(str(paper_topn[i][j]))
        paper_report.write('\n')
    paper_report.write('\n')

    venue_report.write("when alpha=%f, the top %d are \n"%(alpha,topn))
    for j in range(len(venue_topn[i])):
        venue_report.write(str(venue_topn[i][j]))
        venue_report.write('\n')
    venue_report.write('\n')
    alpha=alpha+0.1
    #
    # 这部分在涉及dict和list相互转换和查找方面还有点问题，先不用
    # if i!=0:
    #     author_error=author_error+compareDiff(author_topn[i-1],author_topn[i])
    #     paper_error=paper_error+compareDiff(paper_topn[i-1],paper_topn[i])
    #     venue_error=venue_error+compareDiff(venue_topn[i-1],venue_topn[i])
#
# print "the L1 distance of the results of top %d of author is %d" %(topn, author_error)
# print "the L1 distance of the results of top %d of paper is %d" %(topn, paper_error)
# print "the L1 distance of the results of top %d of venue is %d" %(topn, venue_error)




