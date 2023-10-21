def get_audio_feature_summary(df, audio_feature):
    summary = df.groupby('decade').agg(['mean', 'median', 'std'])
    return summary[audio_feature]
