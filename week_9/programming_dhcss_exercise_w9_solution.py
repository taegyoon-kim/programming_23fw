# -*- coding: utf-8 -*-
"""programming_dhcss_exercise_w9_solution

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1snkQDsnLJZoMW2K17Mtq4GhmQnm-ReDh

Programming for DHCSS Exercises: Week 9. NumPy and Pandas
"""

### Problem 1 ###

### Let's create some example survey data (the index indicates survey id).

import pandas as pd

data = {'age': [25, 30, 35, 40, 45],
        'last_name': ['kim', 'kwon', 'choi', 'han', 'jung']}
df1 = pd.DataFrame(data, index = range(0, 5))
df1.index.name = 'survey_id'

### Problem 1a: Using iloc, select the rows for 'kwon' and 'choi'.

df1.iloc[1:3]
df1.iloc[[1, 2]]

### Problem 1b: Using loc, select the rows from 'choi' to 'jung' (three rows).

df1.loc[2:4]

### Problem 1c: What would the following code lead to? Guess before running.

df1.iloc[0]

### Problem 1d: What would the following code lead to? Guess before running.

df1.loc[0]

### Problem 2 ###

### Let's modify the survey_id a bit.

data = {'age': [25, 30, 35, 40, 45],
        'last_name': ['kim', 'kwon', 'choi', 'han', 'jung']}
df2 = pd.DataFrame(data, index = range(200, 205))
df2.index.name = 'survey_id'

### Problem 2a: Using iloc, select the rows for 'kwon' and 'choi'.

df2.iloc[1:3]
df2.iloc[[1, 2]]

### Problem 2b: Using loc, select the rows from 'choi' to 'jung' (three rows).

df2.loc[202:204]

### Problem 2c: What would the following code lead to? Guess before running.

df2.iloc[0]

### Problem 2d: What would the following code lead to? Guess before running.

df2.loc[0]

### Problem 3 ###

### Let's modify the survey_id once more.

data = {'age': [25, 30, 35, 40, 45],
        'last_name': ['kim', 'kwon', 'choi', 'han', 'jung']}
df3 = pd.DataFrame(data, index = ['a01', 'a02', 'a03', 'a04', 'a08'])
df3.index.name = 'survey_id'

### Problem 3a: Using iloc, select the rows for 'choi'.

df3.iloc[2]

### Problem 3b: Using loc, select the rows from 'choi' to 'jung' (three rows).

df3.loc['a03':'a08']

### Problem 3c: What would the following code lead to? Guess before running.

df3.iloc[0:2]

### Problem 4 ###

### Let's create some example data

book_data = {
    'year': [2018, 2018, 2019, 2019, 2020, 2020],
    'genre': ['Romance', 'Mystery', 'Romance', 'Mystery', 'Romance', 'Mystery'],
    'count_book_produced': [10, 15, 12, 18, 14, 20], # count of books produced in that year
    'count_book_sold': [8, 11, 11, 10, 9, 19] # count of books sold in that year
    }

df_book = pd.DataFrame(book_data)

### Problem 4a: Use the pivot method to put the data in a wide format overviewing the production/sales of books

df_book_wide = df_book.pivot_table(index = 'year', columns = 'genre', values = ['count_book_produced', 'count_book_sold'])

type(df_book_wide)
df_book_wide.index
df_book_wide.columns

### Create another example data

author_data = {
    'author': ['a', 'b'],
    '2019': [1, 0], # books written by the author
    '2020': [2, 1],
    '2021': [1, 3],
    '2022': [1, 0],
    '2023': [1, 0]}
df_author = pd.DataFrame(author_data)

### Problem 4b: Use the melt method to put the data in a long format but exclude the most recent two years (2022, 2023)

df_author_sub = df_author.drop(columns = ['2022', '2023']) # one way
df_author_sub_m = pd.melt(df_author_sub,
                          id_vars = ['author'],
                          var_name = 'year',
                          value_name = 'count_book_written')

df_author_sub_m = pd.melt(df_author_sub, # another way
                          id_vars = ['author'],
                          value_vars = ['2019', '2020', '2021'],
                          var_name = 'year',
                          value_name = 'count_book_written')

### Problem 5 ###

### First, load data sets from the following URLs, using pd.read_csv.

url_1 = "https://raw.githubusercontent.com/taegyoon-kim/programming_dhcss_23fw/main/week_9/policy_citations_example_2002_2018.csv"
url_2 = 'https://raw.githubusercontent.com/taegyoon-kim/programming_dhcss_23fw/main/week_9/policy_citations_example_2019_2021.csv'
url_3 = 'https://raw.githubusercontent.com/taegyoon-kim/programming_dhcss_23fw/main/week_9/tt_ideology.csv'

df1 = pd.read_csv(url_1)
df2 = pd.read_csv(url_2)
df3 = pd.read_csv(url_3)

"""Overview of the datasets
1. **df1** and **df2** are citations data. Each row records a citation from a policy document to another policy document. All citations are from a government organization to a think tank
2. **df1 **is for citations made before or in 2018, and **df2** is for citations made after or in 2019
3. The citing document (the document sending a citation) is indciated with the suffix "_citing", and the cited document (the document receiving a citation) is indicated with the suffix "_cited"
4. For each, we have followig information:
  * policy_document_id: unique id assigned to the document
  * policy_document_type: whether the document is produced by a government organization or a think tank
  * published_on_year: year of publication
  * policy_source_id: string label indicating the institution that produced the document
  * policy_source_title: actual name of the institution that produced the document
  * ref_science_count: the number of references to scientific publications in the document
5. **df3** is for the ideology of think tanks (L: left, R: right, N: neutral)
  * leaning: the ideology column
"""

### Problem 5a: As df1 and df2 contain an identical set of columns for different time periods, put together df1 and df2 (recommend to reset the index).

df = pd.concat([df1, df2], axis = 0).reset_index(drop = True)
min(df['published_on_year_citing'])

### Problem 5b: Subset rows where 1) the citing documents are produced in or after 2003 and 2) are not produced by 'U.S. Government Accountability Office'.

df = df[(df['published_on_year_citing'] >= 2003) & (df['policy_source_title_citing'] != 'U.S. Government Accountability Office')]

len(df)

### Problem 5c: How many citations in total? How many unique government organizations and think tanks? Any missing values? Where, and how many?

len(df)

len(set(df['policy_source_title_citing']))
len(set(df['policy_source_title_cited']))

len(set(df['policy_source_id_citing']))
len(set(df['policy_source_id_cited']))

df.isna().sum()

### Problem 5d: Merge the concatenated data set (containing citations) with df3 (to get the ideology measures for think tanks).

df_idgy = pd.merge(df, df3, how = 'left', left_on = 'policy_source_id_cited', right_on = 'policy_source_id')

### Problem 5e: How many unique the think tanks are their in df3?

len(set(df3['policy_source_id']))
len(set(df3['policy_source_title']))

### Problem 5f: How many of the think tanks in the ideology data set (df3) appear in the merged citation data set (df1 + df2)?

df_4 = pd.merge(df3, df['policy_source_id_cited'], how = 'left', left_on = 'policy_source_id', right_on = 'policy_source_id_cited')
len(set(df_4['policy_source_id_cited'].dropna()))

### Problem 5g: From the merged citation data set, create a data set containing unique think tanks and their ideology measures.

### Hint: one way to do this is to group by think tank (policy_source_title_cited), get the ideology column, and take the first row using the first() method (a DataFrame method).

df_idgy.groupby('policy_source_title_cited')['leaning'].first().dropna().reset_index()

df_idgy.drop_duplicates(subset = 'policy_source_title_cited', keep = 'first')[['policy_source_title_cited', 'leaning']].dropna(subset=['leaning']).reset_index(drop = True)

df_idgy.groupby('leaning')['policy_source_title_cited'].nunique() # this is for counting the number of unique think tanks for each ideology category (note the use of the nunique method)

### Problem 5h: How many scientific references do policy documents from government organizations include over the years, 1) on average and 2) in total?

### Hint: group by published_on_year_citing

print(df_idgy.fillna(0).groupby('published_on_year_citing')['ref_science_count_citing'].agg(['mean', 'sum']).reset_index(drop = False))

### Problem 5i: How did you deal with missing values? Treat NaNs as 0s and run the same code for Problem 5h. Are their any differences?

print(df_idgy.groupby('published_on_year_citing')['ref_science_count_citing'].agg(['mean', 'sum']).reset_index(drop = False))