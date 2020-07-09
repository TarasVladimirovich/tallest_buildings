import pandas as pd


URL = 'https://en.wikipedia.org/wiki/List_of_tallest_buildings'


class Reader:

    @staticmethod
    def read_from_url(url):
        """
        Read table to Data_frame and delete useless data
        :param url: URL
        :return: Data_Frame 
        """
        data = pd.read_html(url, attrs={'class': 'wikitable sortable'}, header=1)
        df = data[0]
        df = df.drop('Image', axis=1)
        df = df.drop('Notes', axis=1)
        df = df.drop('ft', axis=1)

        return df


class Buildings:

    def __init__(self, data):
        self.data = data
        self.__oldest_buildings = None
        self.__counties_with_the_largest_number = None
        self.__highest_building = None

    @property
    def highest_building(self):
        if self.__highest_building is None:
            self.__highest_building = list(self.data.iloc[self.data['Floors'].idxmax()].array)
        return self.__highest_building

    @property
    def oldest_buildings(self):
        if self.__oldest_buildings is None:
            self.__oldest_buildings = list(self.data.iloc[self.data['Year'].idxmin()].array)
        return self.__oldest_buildings

    @property
    def counties_with_the_largest_number(self):
        if self.__counties_with_the_largest_number is None:
            self.__counties_with_the_largest_number = self.data.Country.value_counts().idxmax()
        return self.__counties_with_the_largest_number

    def sort(self, column, ascending=False):
        """

        :param column: Choose column to sort
        :param ascending: True or False
        :return: Change original data_frame to sorted
        """
        self.data = self.data.sort_values(by=[column], ascending=ascending)

    def __str__(self):
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
            return str(self.data)


if __name__ == '__main__':

    Reader.read_from_url(URL)

    build = Buildings(Reader.read_from_url(URL))

    print(build.highest_building)
    print(build.oldest_buildings)
    print(build.counties_with_the_largest_number)

    build.sort('Country', ascending=True)
    print(build)