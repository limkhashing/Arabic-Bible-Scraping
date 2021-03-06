import firebase_admin
import pandas as pd

from firebase_admin import credentials, firestore

cred = credentials.Certificate("../credential.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client(default_app)
al_quran_collection = db.collection(u'al_quran')

# df = pd.read_excel('../data/Quran Database.xlsx')
df = pd.read_csv(r'../data/Quran Database with chapter name.csv')

for index, row in df.iterrows():
    print(row['Chapter'])
    # print(row['Verse'])
    # print(row['Meaning'])
    # print(row['Translation (Yusuf Ali)'])
    # print(row['Chapter Name'])

    document_id = str(row['Chapter']) + "_" + str(row['Verse'])
    data = {
        'chapter': row['Chapter'],
        'chapter_name': row['Chapter Name'],
        'verse': row['Verse'],
        'meaning': row['Meaning'],
        'translation': row['Translation (Yusuf Ali)']
    }

    al_quran_collection.document(document_id).set(data)

print("Done")
