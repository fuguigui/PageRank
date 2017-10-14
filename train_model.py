from mutual_map import *
from PageRank import *
import numpy as np


class TrainModel(object):
    def __init__(self,itr,error):
        self.itr=itr
        self.error=error

    def read_data(self,read_path='.\\'):
        #author
        self.author=MapToMatrix(read_path)
        self.author.FileToList('author_ids.txt')
        self.author_len = self.author.getLen()
        self.author_mat = self.author.getMatrix('author_citation_network.txt')
        self.author_init = np.ones(self.author_len)

        # paper
        self.paper = MapToMatrix(read_path)
        self.paper.FileToList('paper_ids.txt')
        self.paper_len = self.paper.getLen()
        self.paper_mat = self.paper.getMatrix('paper_citation_network.txt')
        self.paper_init = np.ones(self.paper_len)

        # venue
        p1 = r"(?<=id\s=\s{).+?(?=})"
        pattern1 = re.compile(p1)
        p2 = r"(?<=venue\s=\s{).+?(?=})"
        pattern2 = re.compile(p2)

        self.venue = MapToMatrix(read_path)
        self.venue.FileToList_Reg('acl-metadata.txt', pattern1, pattern2)
        self.venue_len = self.venue.getLen()
        self.venue_mat = self.venue.SwitchMap('paper_citation_network.txt')
        self.venue_init = np.ones(self.venue_len)

    def run(self, alpha, save_dir=""):
        pg = PageRank(self.itr, self.error, alpha)

        author_resvec = pg.run(self.author_mat, self.author_init, self.author_len)
        self.author.ScoreToName("Author", author_resvec, save_dir+"author_page_rank.txt")
        author_resmap=self.author.getResult()

        paper_resvec = pg.run(self.paper_mat, self.paper_init, self.paper_len)
        self.paper.ScoreToName("self.paper", paper_resvec, save_dir+"paper_page_rank.txt")
        paper_resmap =self.paper.getResult()


        self.venue_resvec = pg.run(self.venue_mat, self.venue_init, self.venue_len)
        self.venue.ScoreToVenue(self.venue_resvec, save_dir+"venue_rank.txt")
        venue_resmap =self.venue.getResult()

        return author_resmap, paper_resmap, venue_resmap



