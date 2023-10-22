# Radio-Worthy: What Types of Songs Climb the Chart?
The Billboard Hot 100 is a cultural artifact, reflecting the music taste of 
the masses. Because of this, we can explore cultural and musical trends 
throughout the decades.

Specifically, we want to explore what kinds of song climb the chart throughout
the decade. Does the 80s prefer more danceable tracks? Is the 70s more acoustic 
than the 2000s?

We can use clustering techniques to answer this question.

## Project Structure
Currently, there are five directories:
- `/data` - consists our dataset both raw files and generated by our notebooks
- `/data/pkls` - serialized versions of our Python objects
- `/notebooks` - contains the notebooks that do the analysis
- `/scripts` - contains Python scripts not related to analysis
- `/src` - contains Python scripts that aid our investigation

## Datasets
To aid in our investigation, we use [Dhruvil Dave's dataset](https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs/) 
on songs from the Billboard Hot 100, ranging from the year 1958 to 2021.

We have 330 087 observations and six variables in our dataset. The variables and
their description are as follows:
- **date**: date of the chart
- **rank**: rank of the song
- **song**: song title
- **artist**: artist name
- **last-week**: rank of the song in the preceding week
- **peak-rank**: the highest rank that the song historically charted
- **weeks-on-board**: how many weeks the song is charting up to the point of 
    the record (does not have to be consecutive)

However, the chart data alone might not have the most groundbreaking insights. 
We can augment this primary dataset with another to broaden our investigation.

[Yamac Eren's dataset](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks) 
consists of Spotify data of around 600 000 tracks. Like the Billboard Hot 100, 
this dataset can be generated from public data given by Spotify. Specifically, 
it can be gathered through the Spotify API.

It consists of the following important features: 
- **name**: the title of the song
- **duration_ms**: the length of the song in millisecond
- **artists**: an array of artists featured in the song
- **danceability**: "how suitable a track is for dancing based on a combination 
    of musical elements"
- **energy**: "represents a perceptual measure of intensity and activity"
- **loudness**: "overall loudness of a track in decibels"
- **acousticness**: "confidence measure from 0.0 to 1.0 of whether the track 
    is acoustic"
- **valence**: "describing the musical positiveness conveyed by a track"

## Notebooks
To better organize our analysis, I divided the project into different notebooks.

In the current phase, we have the following notebooks:
- **01_data_selection_and_processing**: involves selecting, cleaning and 
    ensuring that all necessary features are ready to be analyzed
- **02_exploratory_data_analysis**: involves sifting through our data to glean 
    initial insights
