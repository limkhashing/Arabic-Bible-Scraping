import firebase_admin

from firebase_admin import credentials, firestore
from selenium import webdriver

cred = credentials.Certificate("../credential.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client(default_app)
hadith_collection = db.collection(u'hadith')
narrated_person_collection = db.collection(u'narated_person')

driver = webdriver.Chrome()
driver.get('https://sunnah.com/bukhari/3')
all_hadith = driver.find_element_by_class_name("AllHadith")
all_content_hadith = all_hadith.find_elements_by_class_name("actualHadithContainer")

content_ara_list = []
content_eng_list = []
reference_list = []
in_book_reference_list = []

# 1, 10, 41 no content
i = 51
for content in all_content_hadith[73:76]:
    content_ara = content.find_element_by_class_name("arabic_hadith_full.arabic").text
    content_eng = content.find_element_by_class_name("text_details").text
    reference = content.find_elements_by_tag_name("tr")[0].text.replace('Reference  : ', '')
    in_book_reference = content.find_elements_by_tag_name("tr")[1].text.replace('In-book reference  : ', '')

    print(reference)
    print(in_book_reference)

    content_ara_list.append(content_ara)
    content_eng_list.append(content_eng)
    reference_list.append(reference)
    in_book_reference_list.append(in_book_reference)

    # data = {
    #     # u'narrated_person': [narated_person],
    #     u'content_ara': [content_ara],
    #     u'content_eng': [content_eng],
    #     u'reference': [reference],
    #     u'in_book_reference': [in_book_reference]
    # }
    # hadith_collection.document("chapter "+str(i)).update(data)
    i = i + 1

# data = {
#     # u'narrated_person': [narated_person],
#     u'content_ara': content_ara_list,
#     u'content_eng': content_eng_list,
#     u'reference': reference_list,
#     u'in_book_reference': in_book_reference_list
# }
# hadith_collection.document("chapter 50").update(data)


# all chapters
# all_chapter = all_hadith.find_elements_by_class_name("chapter")
# for chapter in all_chapter:
#     chapter_num = chapter.find_element_by_class_name("echapno").text.replace('(', '').replace(')', '')
#     arabic_chapter = chapter.find_element_by_class_name("arabicchapter.arabic").text
#     english_chapter = chapter.find_element_by_class_name("englishchapter").text.replace('Chapter: ', '')
#
#     hadith_chapter_doc = hadith_collection.document("chapter " + chapter_num)
#     data = {
#         u'chapter_ara': arabic_chapter,
#         u'chapter_eng': english_chapter,
#
#     }
#     hadith_chapter_doc.set(data)


driver.close()