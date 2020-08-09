# Title

*Finding The Correlation Between My Movie Preferences And The Corresponding IMDB Ratings*

# Goal

- To see if my likes and dislikes with respect to movies match with the IMDB ratings for those movies. 
- If there is a correlation between the two, I can base my movie choices on the IMDB rating to make sure that I mostly watch the movies that I would enjoy. 
- From what I have casually observed, the movies I tend to like do generally have higher IMDB ratings. But this analysis can be used to confirm or disprove that notion. 

# Approach

# Datasets

# Important lessons and findings

- The entire dataset contained over 7 million rows which consumed more than 400MB of space. Therefore, it was important to explore the data and remove unwanted columns early on to reduce the size of the dataset for easier processing. 
- After cleaning the data by removing missing values and selecting just the years 1990 to 2019, the size of the dataset was still large. So I decided to scale things down by selecting just the years 2005 to 2019. Also, I was most familiar with movies from this timeframe so it inherently made a lot of sense. 
- To start things off, I selected years 2008 and 2009 and started manually labelling whether I liked the movie or not (had to be done manually as it is a personal opinion). While doing this, I realized that there were other categories that I could remove such as *documentaries, short films* and *TV shows* as well as generes such as *sports*. This additional filtering had to be done separately and since I only realized it after labelling several of the movies, it would be a tedious task to include this filtering as part of the initial cleaning of the data. 
- I also realized that just the years 2008 and 2009 only provided a few films that I had watched so I decided to include years 2010 and 2011. So I filtererd the new dataset separately and labelled all the movies. At this point, I realized that all this filtering actually brings the size of the dataset down significantly making the labelling process much quicker. Therefore, I decided to filter and label the dataset for years 2014 to 2019 as well. 
- **To make the process a bit more streamlined, I should have explored the data a bit more at the beginning and selected the appropriate years as well as applied all the additional filtering as part of the cleaning process instead of doing them as separate tasks. However, this is a lesson I learned quickly and finally applied the filtering to the larger range of 2014 to 2019.**
