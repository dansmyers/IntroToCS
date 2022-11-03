# The Victorian Gothic Guide to Data Analytics and Pandas

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Caspar_David_Friedrich_-_Abtei_im_Eichwald_-_Google_Art_Project.jpg/2560px-Caspar_David_Friedrich_-_Abtei_im_Eichwald_-_Google_Art_Project.jpg" width="50%" />

>*The Abby in the Oakwood*, Caspar David Friedrich (1809-10)

## Description

Pandas is a Python framework for data analytics. In this lab, you'll work through three small projects that will illustrate what it can do. Along the way, we'll also learn a little
about Python-based plotting frameworks and review some statistical concepts.

By the end of this lab, you will be familiar with:

- Loading data from a CSV file into a Pandas dataframe.
- Basic dataframe manipulations: Selecting a column, selecting subsets, creating new columns.
- Generating cross tabulations and frequency tables for comparing categorical data.
- Creating bar plots from a frequency table.
- Creating histograms from a dataframe.
- Calculating the mean and five number summary of a dataframe.

At the end of this lab, you'll submit **three Python programs and three PDF plots** to the assignment on Canvas.

The three labs we're going to complete were originally designed by my wife Chelsea for her book,
[*Project-Based R Companion to Introductory Statistics*](https://www.taylorfrancis.com/books/mono/10.1201/9780429292002/project-based-companion-introductory-statistics-chelsea-myers?context=ubx&refId=262ee6fc-50b7-4b79-a116-d508a2270467). She has &ndash; let's call it &ndash; a *fascination* with weird and morbid 19th Century data sets, which is one of her many excellent qualities.

## Get the Data

The three CSV files are posted to Canvas. Download them all, then upload them to your Mimir workspace using the `File ---> Upload` menu.

The three files will upload to your top-level workspace directory. Start by making a subdirectory for this lab and moving the files to it.

```
mkdir CMS_120/Lab_11

cd CMS_120/Lab_11

mv ../../Titanic.csv .

mv ../../Lister.csv .

mv ../../Ohio.csv .
```

The `mv` command moves a file. Here, `..` refers to the parent directory, so the path `../../Titanic.csv` refers to a file named `Titanic.csv` that is two levels up in the
directory hierarchy. The second `.` refers to the current working directory, which will be `CMS_120/Lab_11` in this example. In words, the command takes the file `Titanic.csv`
from two levels up and moves it to the current working directory.

Type `ls` and verify that the three files have appeared in your current directory.

## The *Titanic* Dataset

<img src="http://4.bp.blogspot.com/-B_jEnnLjgI0/U-_r3-pZr6I/AAAAAAAA3lM/UzMzMqlDSsQ/s1600/1977114_10152475439781112_174145227163964287_n.jpg" width="50%" />

In the early hours of April 15, 1912, the "unsinkable" ship *RMS Titanic* sank when it struck an iceberg, killing more than half of the passengers and crew aboard. The `Titanic.csv` dataset contains demographic information for 889 of those passengers as well as a record of whether or not each passenger survived. Our first goal is to explore the functionality of Pandas by opening and modifying the *Titanic* dataset.


### Load the Data Set

Create a new Python file called `titanic.py` and put the following code inside it:

```
"""
Analyze the Titanic data set with Pandas
"""

import pandas as pd
import numpy as np

# Open the Titanic dataset
df = pd.read_csv('Titanic.csv')

# Print the first few lines of the dataframe
#
# Check the names and types of each column
print(df.head())
```

Here is a breakdown of each step:

- The first two lines import the `pandas` module as the alias `pd` and the `numpy` module as `np`. Both of these packages are installed by default on Mimir.

- `numpy` is the "Numerical Python" library and supports working with vectors, matrices, and linear algebra. It's often used together with Pandas.

- The third line uses Pandas' built-in `read_csv` method to pull in the contents of `Titanic.csv`. The result of this operation is a special structure that Pandas calls a ***dataframe***. More about dataframes in a moment.

- The variable name `df` isn't required but is widely used to represent the main dataframe in a project.

- The last line uses `df.head()` to print the beginning of the dataframe.

Run the program and you will see output like this:

```
   Survived  Pclass                                               Name     Sex   Age  Siblings/Spouses_Aboard  Parents/Children_Aboard     Fare
0         0       3                             Mr. Owen Harris Braund    male  22.0                        1                        0   7.2500
1         1       1  Mrs. John Bradley (Florence Briggs Thayer) Cum...  female  38.0                        1                        0  71.2833
2         1       3                              Miss. Laina Heikkinen  female  26.0                        0                        0   7.9250
3         1       1        Mrs. Jacques Heath (Lily May Peel) Futrelle  female  35.0                        1                        0  53.1000
4         0       3                            Mr. William Henry Allen    male  35.0                        0                        0   8.0500
```

### Understanding the Dataframe

A dataframe is, conceptually, a **two-dimensional table** of data values, similar to an Excel spreadsheet.

- Each row in the table is a single item or entity. In this case, each row represents one passenger who sailed on the *Titanic*.
- The columns are the attributes associated with each passenger.
- The headings at the top of the columns are the names of each attribute.
- The left-most column contains a numbering for the rows and isn't part of the actual CSV file; it's been added by Pandas.

The data set has eight fields:

- `Survived`: a 0/1 value indicating whether the passenger survived
- `Pclass`: 1, 2, or 3 indicating whether the passenger was in first, second, or third class
- `Name`
- `Sex`: The string `male` or `female`
- `Age`
- `Siblings/Spouses_Aboard`
- `Parents/Children_Aboard`
- `Fare`: The amount, in 1912 British pounds, paid by the passenger

### Column operations

Most Pandas operations work by selecting values from one or more columns. For example, add the following code to your script to select only the names.

```
names = df['Name']
print(names)
```

You can select multiple columns in one operation by specifying a list of multiple names.

```
name_pclass = df[['Name', 'Pclass']]
print(name_pclass)
```

The syntax for the multi-column operations is a little tricky. The outer pair of square brackets is used to access the dataframe, like a lookup in a dictionary. The inner pair of brackets defines a list of names.

### Selecting a subset

The basic column operations retrieve **all row** of the requested fields. Sometimes you want to select a **subset** of the rows. For example, suppose we wanted to select only
the subset of children from the *Titanic* dataset.

```
children = df[df['Age'] < 18]
print(children.head())
```

There are several things happening here. The inner part of the selection identifies the rows that have `Age < 18`. The outer part selects only those rows from the main dataframe and returns them as a new dataframe called `children`.

Add these lines to your script and run it to verify that the `children` subset contains only passengers with an age less than 18.

How many children are in the dataset? Pandas can automatically count the number of rows in a frame.

```
print(children.count())
```

### Practice

Use the example of the previous section to create a subset containing only the first-class passengers, then count the number of first-class passengers.


### Creating a new column

Sometimes you need to create a new column based on the value of existing columns. For example, many datasets use the 0//1 convention to encode binary attributes because it isn't platform specific. However, it might be helpful to create a new boolean column that expresses whether the passenger survived as `False` or `True` in order to simplify future comparisons. Here is one way to do that.

```
df['Survived_boolean'] = np.where(df['Survived'] == 1, True, False)
print(df.head())
```

The left-hand side creates a new column in the dataframe named `Survived_boolean` by assigning to it. The right-hand side uses `np.where` to quickly convert the 0/1 values in the `Survived` column into booleand. `np.where` takes three arguments:

- A logical test
- A value to output if the test returns `True`
- A value to output if the test returns `False`

In this example, if a passenger has `Survived == 1`, then `Survived_boolean` is set to `True`.

Run your script one more time and you'll see that `Survived_boolean` now appears as a column in the output of `df.head()`.

## Antibiotics

<img src="https://www.listerine.com/sites/listerine_us_2/files/styles/jjbos_adaptive_images_generic-mobile/public/taco-images/listerine_moutwash_products_new_0.jpg?timestamp=1608240595" width="50%" />

### Does use of antiseptics during surgery reduce mortality?

Spoiler alert – **yes**! Though this was actually very controversial at the time. Joseph Lister (the namesake of Listerine), an English surgeon in the late 1800s, pioneered the use of carbolic acid as an antiseptic during surgery after observing that it mitigated the smell of sewage waste used to irrigate farm fields with no apparent harm to the livestock grazing there.  

Mortality data for individuals who had upper or lower limb amputations before and after the discovery of antiseptics are presented in the `Lister.csv` dataset.

### Import the data

Create a new file called `lister.py` and start with the following code.

```
"""
Analyze the Lister data set
"""

import pandas as pd
import numpy as np

# Read the csv file into a dataframe
df = pd.read_csv('Lister.csv')
print(df.head())
```

The output looks like this:

```
   ID  Antiseptic  Limb  Outcome
0   1           0     1        0
1   2           0     1        1
2   3           0     1        0
3   4           0     1        0
4   5           0     1        1
```

The data set contains four fields:

- `ID`: A numerical identifier for each patient.
- `Antiseptic`: Whether the amputation was performed before (0) or after (1) the invention of antiseptics.
- `Limb`: Whether the amputation was performed on a lower (1) or upper (2) limb.
- `Outcome`: Whether the patient died (0) or survived (1).

### Create new columns

Numeric variables are convenient for encoding, but can be hard to interpret. It's **usually** the case that 0 = False and 1 = True, **but you should never assume that** and make sure to check the interpretation of each field before proceeding with your analysis.

Let's make two new columns to map the `Outcome` and `Antiseptic` fields to descriptive strings.

```
df['Outcome_str'] = np.where(df['Outcome'] == 1, 'Survived', 'Did not survive')
df['Antiseptic_use'] = np.where(df['Antiseptic'] == 1, 'Yes', 'No')
```

You can print the entire frame if you want to see both the first and last rows:

```
print(df)
```

Again, re-run the script and verify that the new columns have been created and have appropriate values.

### Frequency tables

How many amputees survived vs. did not survive their operations? The built-in `value_counts` method returns the number of occurences for each distinct value in a data column.

```
print(df['Outcome_str'].value_counts())
```

```
Survived           53
Did not survive    22
```

There were more survivals overall than deaths, but what we really want to know is whether the introduction of antiseptics had an impact on the probability of survival. The `crosstab` method creates tables for comparing the interactions of multiple variables. This line will constuct a crosstab dataframe showing the interaction of `Outcome_str` and `Antiseptic_use`.

```
tab = pd.crosstab(index=df['Antiseptic_use'], columns=df['Outcome_str'], normalize=True) * 100
print(tab)
```

Details:

- `crosstab` is part of Pandas, so the statement starts with `pd`. It's not a method of the dataframe; using `df` would give an error.
- The `index` argument specifies the field to place on the rows of the frequency table.
- The `columns` argument specifies the field for the columns.
- `normalize=True` calculates percentages instead of using raw counts.
- Multiplying by 100 puts the percentages into the range 0-100 for readability.

Here is the output:

```
Outcome_str     Did not survive   Survived
Antiseptic_use                            
No                    21.333333  25.333333
Yes                    8.000000  45.333333
```

The results tell us that, out of the entire data set, 8% of patients fall into the category of `Yes - Did Not Survive`. About 21% fall into `No - Did Not Survive`.

Make one more modification. Setting `normalize='index'` will calculation fractions across the rows rather than over the entire data set.

```
tab = pd.crosstab(index=df['Antiseptic_use'], columns=df['Outcome_str'], normalize='index') * 100
print(tab)
```

The results now clearly illustrate the change in survival rate from incorporating antiseptics. Before their use, about 45% of patients did not survive their amputations; after, only about 15% of patients did not survive.

```
Outcome_str     Did not survive   Survived
Antiseptic_use                            
No                    45.714286  54.285714
Yes                   15.000000  85.000000
```

### Plot

One final part for this section: Let's visualize the results as a bar plot. Pandas includes a built-in plottin library and there are also several frameworks that can be used to create plots in Python.

Pandas' built-in plotting features are implemented on top of a lower-level library called matplotlib. The first thing that we need to do is get access to matplotlib.
Go back up to the **top** of your script and add the following code below the two `import` statements.

```
import matplotlib
matplotlib.use('Agg') # <--- Required for plotting on Mimir
from matplotlib import pyplot as plt
```

Now add the following lines at the bottom of the script.

```
tab.plot(kind='bar', stacked=False)
plt.ylabel('Percent')
plt.ylim([0, 100])
plt.savefig('test.pdf', bbox_inches='tight')
plt.close()
```

Here are the details:

- `tab.plot` creates a plot from the data frame created by `crosstab`. Because we are working on Mimir, we can't directly visualize the plot immediately; instead, we have to save it as a PDF and then download the PDF from Mimir to view the result.

- The next two lines set properties (y-axis label and y-axis range) for the plot.

- `savefig` outputs the plot to a PDF. The optional `bbox_inches='tight'` argument sets the PDF to fit tightly around the figure.

- `plt.close()` closes the plot in memory, which allows the script to proceed and complete.

To see the plot, use your left-hand file browser pane to find your CMS_120/Lab_11 directory. Right-click (or CTRL + click on Mac) on the file and select "Dowload". You can then view the PDF by opening it in your computer's Downloads folder.

## The Civil War


<img src="https://www.history.com/.image/c_fit%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_620/MTU3ODc5MDgzNDc1NzQwMzgz/abraham-lincoln-at-antietam-during-civil-war.jpg" width="50%" />

### Determine the casualty rate for Union Army soldiers in companies from Ohio during the US Civil War.


Approximately 618,000 Union and Confederate soldiers died in battle and from starvation and disease during the single bloodiest conflict in United States history: The Civil War. To put this in perspective, about 400,000 US soldiers perished during the second-most-deadly conflict, World War II. Despite the terrible conditions soldiers faced in the field, remarkably good records about these men, their backgrounds, and their fates have been preserved.  

The `Ohio.csv` dataset contains records from 45 companies from Ohio during the United States Civil War including the number of soldiers in the company, the year the company was formed, details about the demographic make-up of each company as well as the overall mortality and mortality due to injury and illness. We wish to describe the mortality rates for these companies from Ohio during the US Civil War.

### Load the data

Start by creating a new file called `ohio.py`. Put the following code into it:

```
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib
matplotlib.use('Agg') # <--- Required for plotting on Mimir
from matplotlib import pyplot as plt


# Load the Ohio Civil War dataset
df = pd.read_csv('Ohio.csv')
print(df.head())
```

This script will illustrate the use of Seaborn, a second plotting library that is also built on top of matplotlib. Seaborn includes built-in functions for creating common plots with intelligent default styles. Use the following terminal command to install Seaborn:

```
sudo pip install seaborn
```

Here is the output of `head()`:

```
  Company  No_soldiers  Enlist_yr  Death_total  Death_illness  Death_injury  Pct_farmers  Pct_foreign
0    006D          100       1861            5              2             3         5.00        38.00
1    041I          112       1863           11              7             4        59.82        15.18
2    045B          113       1862           34             32             1        79.65         2.65
3    050E           90       1862            5              2             3        68.89         5.56
4    050K           93       1862           14             10             4        61.29        17.20
```

### Visualize the distribution of casualties

The code below uses Seaborn to create a histogram of the `Death_total` field. The `histplot` function creates a histogram. The `bins` argument specifies the number of histogram bins and the `x` argument specifies which data column to aggregate to construct the distribution.

```
# Histogram of casualties
sns.histplot(x='Death_total', data=df, bins=15)

plt.xlabel('Number of casualties')

plt.savefig('hist.pdf', bbox_inches='tight')
plt.close()
```

As before, navigate to the plot in your left-hand file browser and use "Download" to view it.

### Visualize the distribution of the size of the companies

The code below creates a box plot showing the distribution of the size of the companies ([go here if you need a refesher on box plots](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/box-plot-review)).

```
sns.boxplot(y='No_soldiers', data=df)

plt.ylabel('Number of soldiers')
plt.ylim([0, 200])

plt.savefig('box.pdf', bbox_inches='tight')
plt.close()
```

Create the plot and then take a look at it. Do you notice anything interesting?

We see from the circles appearing on the box plot that there is at least one observation on the small side of the distribution and several observations on the large side that are considered outliers.

At this point we should be curious about the very large and very small observations. But what to do? There are two possibilities for what is going on here: 

- The first is that these observations are unusual but correct. There were very large and very small companies in Ohio during this period of the US Civil War. 
- The second possibility is that there is an error in the data or data analysis.

We’ll explore the second case – that the unusual observations are the result of errors – first and then, if we can’t find any errors, we’ll do what we can to confirm that the outliers are correct. When investigating errors, it’s useful to start at the point you noticed the potential error and then work backwards toward the original source of the data to see if you can identify where an error might have been introduced.  

The first thing to consider is that we made an error with our plots or calculations. There are only 45 observations, so you could check the data frame and see that there is one company with 180 soldiers and one with only 10 soldiers. We have not made an error plotting or calculating the summary measures.

The next possibility is that there was an error reading in the data. To check this, open the `Ohio.csv` file and look at the data there. Again, we see Company 78D has 180 soldiers and Company 195B as 10 soldiers, so there is no apparent error in reading the data with Pandas.

Now we must consider a possible error in creating the CSV file. The dataset is taken from this paper:

> C. Lee (1999). "Selective Assignment of Military Positions in the Union Army: Implications for the Impact of the Civil War", Social Science History, Vol. 23, #1, pp 67-97.

[You can find the paper here](https://www.jstor.org/stable/1171541?seq=1#metadata_info_tab_contents). Open it up and navigate to Table 3. Take a moment and find the entry for Companies 78D and 195B. Do you see anything?

We see in Table 3 of the paper that nearly all of the records for "number of soldiers" match, including Company 78D with 180 soldiers. However, if we look at the second page of Table 3, **we see that Company 195B has 100 soldiers, not 10 soldiers**. We have found an error, and we can confidently edit the `Ohio.csv` dataset to change the number of soldiers in Company 195B to 100.

Re-run your program and create the corrected plot.

## Calculate and describe the percent mortality in the 45 Ohio companies.

Although our original question wasn’t phrased this way, we are beginning to see what we are really trying to answer isn’t, "How many casualties were there in these Ohio companies?". Because there was quite a bit of variation in company size, we need to answer the question "What percent of the soldiers in each company died during the war?" This is often true in statistical analyses. The relative frequency (or percent) of an occurrence often tells us more than the raw frequency (or count).

To gain insight into the relative frequency of deaths due to any cause, we can create a new variable by dividing the total number of deaths by the number of soldiers in each company and multiplying by 100%. 

```
# Calculate percent mortality
df['Percent_mortality'] = df['Death_total'] / df['No_soldiers']
print(df.describe())
```

The first line creates a new column by dividing `Death_total` and `No_soldiers`. Pandas is smart enough to vectorize the division operation and apply it across the column
entries. 

`describe()` calculates summary statistics (mean, median, and quartiles) for the data frame. A company from Ohio typically had a casualty rate of about 7%, and 25% of companies lost fewer than a 5% of their men. Only 25% of companies had a casualty rate of more than 14%, but one company lost 30% of its men. Note that the skewed nature of the data makes the median (7%) a better measure of the "typical" casualty rate than the mean (more than 9%).

Finally, let's create one more plot showing the histogram of `Percent_mortality`:

```
sns.histplot(x='Percent_mortality', data=df, bins=15)

plt.xlabel('Number of casualties')
plt.xlim([0, 1.0])

plt.savefig('mortality.pdf', bbox_inches='tight')
plt.close()
```
