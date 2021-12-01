### Data Loading

This python code creates a method that calculates the channel type distribution from a YouTube dataset. We need to determine the channel type distribution from the top 1000 entries in the original dataset. To do so, we first establish a separate data frame for the top 1000 entries, then write a function to determine the channel type distribution from that data frame.

## Getting Started

The given code can be copy and used for your dataset.

### Prerequisites

I did this Python Project in Anaconda using Jupiter Notebook. Recommending to install anaconda and python. 


### Installing

Installing Anaconda is a completely straightforward method. We can download the Anaconda executive file online and then run the file and follow the installation steps. 

## Running the tests

Execute all the lines of commands.

Python code:


# 1. Import Python Libraries
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
# 2. Expand the number of columns
```
pd.set_option('max_columns', 500)
```
# 3. Read dataset
```
youtubedata = pd.read_csv('./youtube_dataset.csv')
youtubedata.head()
```
# 4. Bring top 1000 records in a dataframe
```
first_thousand = youtubedata.iloc[:1000,:]
first_thousand
```
# 5. create a function to calculate the distribution of channeltype from the top 1000 records.
```
def dis_fn(df, channeltype):
    print(df.groupby(channeltype)[channeltype].count())
    df[channeltype].value_counts().plot(kind='bar')
dis_fn(first_thousand, 'channeltype')
```
# 6. Load only the top 1000 records of the original 4000 into a separate CSV file.
```
first_thousand.to_csv('Youtubedata-1000.csv')
```
# 7. Print saved first 1000 record in a seperate csv file.
```
df1 = pd.read_csv('./youtubedata-1000.csv')
df1
```
### Break down into end to end tests

Test this code in your system and apply for yoiur dataset.

### And coding style tests

1. This code will create a function to calculate the distribution of the channel type in top 1000 records.
2. Save the top 1000 records into a seperate csv file.


## Deployment

You can deploy this on a live system by using the same code for different datasets for similar purposes.

## Built With

* Python Code: Anaconda

## Contributing

## Versioning

1.0
## Authors

Emmanuel Sebastian

## License

No License (Open)

## Acknowledgments

* Code Used from Durham college- 1202-Functionintro.py
* Inspiration: Prof Omar Al-Trad
 there 👋

<!--
**EmmanuelSebastian/EmmanuelSebastian** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
