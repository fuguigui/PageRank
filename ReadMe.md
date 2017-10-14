the programme includes:
main: the main function to read data, train the model and analyze the results.
mutual_map: read data from the original file and transfer to vector and matrix required by pagerank algorithm
PageRank: given the largest iteration turns, allowed error range and alpha value, run the pagerank algorithm
train_model: a synthesize of the model training process, from reading data to giving results understandable to readers.
Analysis_helper: help to analyze the result got from model.

The following are functions' details:
------------main--------------
First, given the largest iteration turns and allowed error range, try different alpha value on pagerank and collect the results.
Then, analyze these results, focused on the top n items and compare the differences under different alpha value.

------------mutual_map--------
FileToList(FileToList_Reg):
read from the original file, extract the primitive value name and their id. Save them into a dictionary. Also build a list of id.(FileToList_Reg uses the given patterns to extract the features.)
getMatrix:
save the quotation relationship as a matrix.
SwitchMap:
the same function as getMatrix. But it adds a step to map the paper to the venue and get the venues' quotation relationship.
ScoreToName(ScoreToVenue):
Save the name and its pagerank score in a file. Return the result.(It applies to venue.)
getXXX:
get the value of the corresponding parameter.

-----------PageRank------------
run:
given the largest iteration turns, allowed error range and alpha value , run the algorithm.

-----------train_model----------
a decoration of mutual_map and PageRank.
read_data:
read data from the original file. Use this method can read once but experiment many times.
run:
call PageRank.run, map the result to data understandable to people and save the result.

-----------Analysis_helper-------
help tp analyze the final result.
topN:
get the top N items of the results and save them in a file in order.
compareDiff:
compare the difference of two ordered results. Use L1 distance to compute.

