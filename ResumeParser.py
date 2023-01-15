''' Importing all the necessary pacakages '''
from pyresparser import ResumeParser
import streamlit as st
import os
import shutil
import nltk

''' Downloading stopword pacakage from Natural Language Toolkit '''
nltk.download('stopwords')

''' Using Streamlit widgets to create the Webpage '''
st.title("Resume Scanner")

link = st.text_input("Enter link")
if(link):
    st.write("Link Submitted Successfully")

Skills = st.multiselect("Skills",["Web Development","Android","Data Analysis","Blockchain","Machine learning"])
Languages = st.multiselect("Languages",["C","C++","Python","Java","JavaScript","SQL","Pearl"])
Frameworks = st.multiselect("Frameworks",["React.js","Angular.js","Node.js","Django","MySQL","Flask","Tensorflow"])

''' Counting the number of files in the specified folder '''
count=0
for i in os.listdir(link):
    count += 1

s = [0]*count
l = [0]*count
f = [0]*count

Submit = st.button("Submit")
files = [f for f in os.listdir(link)]

if(Submit):
    k=0
    for file in files:
        data = ResumeParser(link + "\\" + file).get_extracted_data()
        if not set(data['skills']).isdisjoint(set(Skills)):
            s[k] = 1
        if not set(data['skills']).isdisjoint(set(Languages)):
            l[k] = 1
        if not set(data['skills']).isdisjoint(set(Frameworks)):
            f[k] = 1
        k += 1
        
    j = 0
    ''' Creating Folder named ShortListed in the current Directory to 
        store the shortlisted resumes '''
    os.mkdir("ShortListed")
    for file in files:
        print(file)
        new_path = "ShortListed"
        if(s[j]==1 and l[j]==1 and f[j]==1):
            shutil.move(os.path.join(link,file), new_path)
        if(j==count-1):
            st.write("Resume Shortlisted Successfully")
        j += 1



