1. Make a new folder and call it _Data_Files (underscore at the beginning).  Put this folder in the same folder 
you run this .py file from, and put all of the archer data files inside it.

2. Run the code.  Two additional folders, with folders inside them, will be created, along with many .txt files.  
If they already exist they will be overwritten.  Note that The .txt files which appear inside the folders inside 
the folder "Score_Sorts" contain only numerical data, with no commas.  Therefore you should able to directly load 
these files via various methods, and plot them, calculate means/deviations/etc, load into numpy arrays, etc.  On the other hand, the 
folders inside the folder "Row_Sorts" -  for instance, a .txt file from the subfolder "Sort_By_Date_Rows", named 
"1__3__2017.txt" - contains a DataFrame object, which contains all scores AND all columns ( ['Grade'], ['Gender'], etc ) 
from tournaments on 1-3-2017.  

3.  You can load in the "Rows" files like you can the "Score" files, but in that case you'll have yourself a 
pandas DataFrame object instead of a column of numbers.  But really this information already exists inside a dictionary,
so loading the rows style .txt files is a bit redundant.  Printing them out is just helpful to understand what is 
happening with the sorting inside the dictionaries; if you look at the lines of code which print to a particular file,
you can see how those DataFrames are being accessed from the dictionaries to print out to those files.  For instance,
If you wanted to access the information in the  "1__3__2017.txt" file, instead of loading the file in you can just 
access the existing dictionary row_sort_by_date_dict using the key 1__3__2017.  Like so:

my_data_subset = row_sort_by_date_dict['1__3__2017']

Or for grade 3 data rows you could say

my_other_data_subset = row_sort_by_grade_dict['Grade_3']

If you want to further parse this data, say, you know want to find the Grade_3 archers who are boys, 
you can use the DataFrame.loc command.  For instance, 

grade_3_boys_scores = my_other_data_subset.loc[my_other_data_subset['Gender'] == 'Boys']

and this should return only those rows where the gender is Boys. 

4.  Note dictionaries contain key, value pairs.  Input a key, get out a matching value.  Dictionaries are unordered, 
so there is no index associated with the (key, value); this mean you cannot iterate through a dictionary with integer
indexing like you can with lists and other things.  There are ways to iterate over dictionaries, for instance with the 
.items() function.  you can say 

for key, value in row_sort_by_score_dict.items():
     print("KEY: ", key)
     print("VALUE: ", value)

but note that while the key will always match the proper value within a single iteration, the key, value pairs will come 
out in any old order since the dictionary doesn't remember what order you put them in.    This is what it means for dictionaries 
to be "unordered".

In some dictionaries, the value will be a list (for instance, score dictionaries), while in others they will be DataFrame objects
(for instance, the rows dictionaries).  If you're unsure you can check with type() function, i.e given our above example we could say.:

type(grade_3_boys_scores)

and it should return something something DataFrame object.  A list object should tell you it's a list, etc. 

5.  DataFrame objects can be accessed much like dictionaries, except instead of a key you input a column in the square brackets.  
For instance, I concatenated the entire data set into one DataFrame called full_df.  In order to access the entire list of scores
and calculate the mean, I used (assuming import numpy as np):  

mean_score_all = np.mean(full_df['Score'])

6. Note that you can access any of my dictionaries in your own script by importing my file. Maybe name my file something better than 
the name I gave it, in hindsight; say, data_sorter.  Then say

import data_sorter

and you should now be able to use the file.object commands, for instance

data_sorter.row_sort_by_grade_dict 

gives you that dictionary.  Assuming your script file is in the same location as the file you're importing.  I think this is also 
true for all objects/variables/etc that my file creates, but this is starting to get outside my expertise so I'm not 100% sure 
if it's that simple.  But I know it works with dictionaries.

7.  Note that the enumerate() command is great for iterating through lists.  Look through the code for examples of how to use this one.