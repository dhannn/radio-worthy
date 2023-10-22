""" Scripts for Notebook #2 - Exploratory Data Analysis

This modules contain scripts used for exploring the data.

Programmed by Daniel III Ramos
"""

from pandas import DataFrame

def get_audio_feature_summary(df: DataFrame, audio_feature: str) -> DataFrame:
    """ Gets summary of audio feature per decade

    Gets the summary (mean, median and standard deviation) of the specified 
    audio feature for each decade.

    Args:
        df (`DataFrame`): the `DataFrame` containing the raw data 
        audio_feature (`str`): the specified audio feature to be queried

    Returns:
        `DataFrame`: the `DataFrame` that contains the aggregated summary
            of the audio feature for each decade
    """
    summary = df[['decade', audio_feature]].groupby('decade')\
        .agg(['mean', 'median', 'std'])
    
    return summary[audio_feature]
