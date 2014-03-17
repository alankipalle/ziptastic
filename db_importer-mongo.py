from pymongo import MongoClient
import csv
import sys
import json

class ZipAPIImport():
    def build_database(self, filename):

        # For large CSV files, increase the size
        csv.field_size_limit(sys.maxsize)

        # connect to db
        mc = MongoClient()
        db = mc.ziptastic
        ziptastic_collection = db.ziptastic_codes


        with open(filename, 'rb') as txtdb:
            parseddb = csv.reader(txtdb, delimiter='\t')
            for row in parseddb:
                country = row[0]
                postal_code = row[1]
                city = row[2]
                state = row[3]
                state_short = row[4]
                county = row[5]

                tz = 'n/a'

                if len(row) >= 17:
                    tz = row[17]
                    # print county, postal_code, city, state, state_short, country, tz

                data = {
                        'country': country,
                        'postal_code': postal_code,
                        'city': city,
                        'state': state,
                        'state_short': state_short,
                        'county': county,
                        'timezone': tz
                    }

                ziptastic_collection.insert(data)

        #location = r.hgetall("{0}:{1}".format(the_country, the_zip))

if __name__ == '__main__':
    z = ZipAPIImport()
    z.build_database('allCountries.txt')
