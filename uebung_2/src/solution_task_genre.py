# Lösungsoption #1
def split_to_columns(x, dataframe):
    for genre in x["genre"].split(","):
        if genre in list(dataframe.columns):
            dataframe.at[x.name, genre] = 1
        else:
            dataframe[genre] = 0
            

for index, row in movies_df.iterrows():
    split_to_columns(row, movies_df)

# Lösngsoption #2

genres_df = movies_df['genre'].str.get_dummies(',').replace({0:'no', 1:'yes'})
movies_df = pd.concat([movies_df, genres_df], axis=1)

#Validierung der Lösung
movies_df.head(5)