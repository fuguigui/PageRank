from numpy import *
import re
class MapToMatrix(object):
    def __init__(self,file_cwd):
        self._cwd_=file_cwd
        self.adict={}
        self.keylist=list()
        self.keyset=set()
        self._len_=0
        self.resmap={}

    def FileToList(self, file_name):
        data=open(self._cwd_+file_name)
        for each_line in data:
            splited=re.split(r'\s\s+|\t',each_line.rstrip())
            key=splited[0]
            value=splited[1]

            self.adict[key]=value
            if key not in self.keyset:
                self.keyset.add(key)
                self.keylist.append(key)

        data.close()
        self._len_=self.adict.__len__()

    def FileToList_Reg(self, file_name, pattern1, pattern2):
        key = "paper_id"
        value = "venue"
        update = False
        data=open(self._cwd_+file_name)
        for each_line in data:
            each_line = each_line.rstrip()
            matcher1 = re.search(pattern1, each_line)
            matcher2 = re.search(pattern2, each_line)
            if str(matcher1) != 'None':
                key = matcher1.group(0)
            if str(matcher2) != 'None':
                value = matcher2.group(0)
                update = True
            else:
                update = False
            if update:
                self.adict[key]=value
                if value not in self.keyset:
                    self.keyset.add(value)
                    self.keylist.append(value)

        data.close()
        self._len_=self.keylist.__len__()

    def getMatrix(self,matrix_file):
        matrix=zeros((self._len_,self._len_))

        print "read from file %s to matrix..." %matrix_file

        data = open(self._cwd_ + matrix_file)
        for each_line in data:
            each_line=each_line.strip('\n')
            [incite, outcite] =each_line.split(' ==> ')
            fst_id=self.keylist.index(incite)
            sec_id=self.keylist.index(outcite)
            matrix[fst_id][sec_id]=matrix[fst_id][sec_id] +1

        data.close()

        cnt=matrix.sum(axis=1)
        reg=cnt==0
        cnt=reg+cnt
        result=zeros((self._len_,self._len_))
        for i in range(self._len_):
            result[i]=matrix[i]/cnt[i]
        return result

    def SwitchMap(self,matrix_file):
        matrix = zeros((self._len_, self._len_))

        print "read from file %s to matrix..." % matrix_file

        data = open(self._cwd_ + matrix_file)
        for each_line in data:
            each_line = each_line.strip('\n')
            [incite, outcite] = each_line.split(' ==> ')
            map_fst_obj=self.adict[incite]
            map_sec_obj=self.adict[outcite]

            map_fst_id = self.keylist.index(map_fst_obj)
            map_sec_id = self.keylist.index(map_sec_obj)

            matrix[map_fst_id][map_sec_id]=matrix[map_fst_id][map_sec_id]+1

        data.close()

        cnt = matrix.sum(axis=1)
        reg = cnt == 0
        cnt = reg + cnt
        result = zeros((self._len_, self._len_))
        for i in range(self._len_):
            result[i] = matrix[i] / cnt[i]
        return result


    def ScoreToName(self,name,vec,file_name):

        print "output from score to file %s..."%file_name

        for i in range(len(vec)):
            value=self.adict[self.keylist[i]]
            self.resmap[value]=vec[i]
        fo = open(self._cwd_+file_name, 'w')
        fo.write("There are %d variables\n" % self._len_)
        for value in self.resmap.keys():
            fo.write("%s %s\t%.20f\n" % (name,value, self.resmap[value]))
        fo.close()
        print "Success write in %s" % file_name


    def ScoreToVenue(self,vec,file_name):
        print "output from score to file %s..."%file_name

        for i in range(len(vec)):
            value=self.keylist[i]
            self.resmap[value]=vec[i]
        fo = open(self._cwd_+file_name, 'w')
        fo.write("There are %d variables\n" % self._len_)
        for value in self.resmap.keys():
            fo.write("Venue %s\t%.20f\n" % (value, self.resmap[value]))
        fo.close()
        print "Success write in %s" % file_name

    def getLen(self):
        return self._len_
    def getKeyList(self):
        return self.keylist
    def getResult(self):
        return self.resmap




