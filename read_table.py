import pandas as pd


URL = 'https://en.wikipedia.org/wiki/List_of_tallest_buildings'


data = pd.read_html(URL, attrs={'class': 'wikitable sortable'}, header=1)

df = data[0]

df = df.drop('Image', axis=1)
df = df.drop('Notes', axis=1)
df = df.drop('ft', axis=1)

# print(df)



# for i in df.Country:
#     print(i)

# for data in df:
#     print(df[data])
#


# print(df.sort_values(by=['Rank'], ascending=True))
#
# for i in df.Floors:
#     print(i)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#     print(df)

# print(df.Floors.max())
#
# print(df.iloc[df['Floors'].idxmax()])
# print(type(df.iloc[df['Floors'].idxmax()]))
# print(type(df.iloc[df['Floors'].idxmax()].array))
# print(list(df.iloc[df['Year'].idxmin()].array))

print(df.Country.value_counts().idxmax())

# df = df.groupby('Country')['Name'].nunique()
#
# # print(df)
# print(type(df))
# print(df)
# for i in df:
#     print(i)