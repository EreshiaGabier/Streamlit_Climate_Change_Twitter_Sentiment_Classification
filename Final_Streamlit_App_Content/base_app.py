"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import nltk
import re
import itertools

# Vectorizer
news_vectorizer = open("resources/tfidf.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")



#st.subheader("Raw Twitter data and label")
#if st.checkbox('Show raw data'): # data is hidden if box is unchecked
#	st.write(raw[['sentiment', 'message']]) # will write the df to the page

	

# The main function where we will build the actual app
def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages
	# st.title("Tweet Classifer")
	# st.subheader("Climate change tweet classification")

	
	# Creating sidebar with selection box -
	options = ["Home","Climate Change Project", "Sentiment Classifier Analysis","Sentiment Prediction","Contact Us"]
	selection = st.sidebar.selectbox("Navigation Pane", options)

	# Building out the "Home" page
	if selection == "Home":
		select = st.sidebar.selectbox("Who we are 🌐",["The Company","Projects","Meet the Team"])
		if select == "The Company":
			st.image("Blue_logo.jpeg",width=450)

			st.subheader("Who We Are")
			st.info("Pro-Clime Solutions is a new leading environmental tachnology company founded in 2022, who specialises in all things Data Science and Machine Learning. We are a proudly African company with facilities in South Africa and Nigeria.  We have a combined experience of 35 years across multiple disciplines from Data Science to Environmental Research. Our compnay's focus is to inform and educate about climate change and provide innovation for Africa.")
			
			st.write("##")# Create space

			st.subheader(" Our Key Values")
			col1, col2, col3 = st.columns(3)
			col1.image ("collaboration.jpg", width=250)
			col1.info('**Collaboration**')
			col2.image("Innovation.jpeg", width=275)
			col2.info('**Innovation**')
			col3.image("efficiency.jpg", width=280)
			col3.info('**Efficiency**')


		if select == "Projects":
			st.image("Blue_logo.jpeg",width=450)

			st.write("##")# Create space
			st.info("**Spain Electricity Shortfall:** Pro-Clime Solution was tasked to model the shortfall between the energy generated by means of fossil fuels and various renewable sources - for the country of Spain")
			st.image("spain_electricity_shortfall.jpeg", width=700)
			
			st.write("##")# Create space
			st.info("**Climate Change and the heat index in Spain:** Pro-Clime Solutions investigated the acute effects of the daily variation in heat index in various parts of Spain.")
			st.image("heat_index.jpeg", width=700)
			
				
	
		if select == "Meet the Team":
			st.image("Blue_logo.jpeg",width=450)
		#1
			col1, col2 = st.columns(2)
			with col1:
				st.image("Ereshia_Gabier.jpg", width=200)
			with col2:
				st.subheader("Ereshia Gabier")
				st.info('Technical Project Manager')
		#2
			col1, col2 = st.columns(2)
			with col1:
				st.image("Jack.jpeg", width=200)
			with col2:
				st.subheader("Ikaneng  Jack Malapile")
				st.info('Lead Data Scientist')
		#3
			col1, col2 = st.columns(2)
			with col1:
				st.image("thando.jpg", width=200)
			with col2:
				st.subheader("Thandolwethu Madondo")
				st.info('Senior Data Scientist')
		#4
			col1, col2 = st.columns(2)
			with col1:
				st.image("Nonso_pix.jpg", width=200)
			with col2:
				st.subheader("Chukwunonso Azih")
				st.info('ML Engineer')
		#5
			col1, col2 = st.columns(2)
			with col1:
				st.image("Oloade.jpeg", width=200)
			with col2:
				st.subheader("Ololade Ogunleye")
				st.info('Senior Business Architect')


	# Building out the "Climate Change Project" page
	if selection == "Climate Change Project":
		st.subheader("Climate Change Sentiment Analysis Project")
		st.info("**_There is no question that climate change is happening; the only arguable point is what part humans are playing in it._** - David Attenborough")
		st.image("climate_change.jpeg",width=700)
		st.info("The effects of Climate Change have been experienced all across the world with long-term shifts in temperatures and weather patterns. This has become a global concern over the last few decades. However, Climate Change is still a divisive topic and has sparked interest by many and has yielded strong opionions on either end of the spectrum. Therefore, analysing sentiments towards Climate Change could aid in informing and educating people. ")
		
		st.write("##")# Create space
		st.subheader("Mission Statement")
		st.info("Our mission at Pro-Clime Solutions is to analyse sentiments about Climate Change from the texts obtained from popular social media platform, Twitter. Our methodology includes Exploratory Data Analysis, Preprocessing and Machine Learning Model predictions. By assessing users' sentiment-spanning multiple demographics and geographic categories, aids in providing beneficial information that could be used for various applications. This is a robust market tool for companies, non-profit organizations or individuals who are interested in the environment. ")
		st.image("Dataset_word.jpeg",width=None)


	# Building out the "Sentiment Classifier Analysis" page
	if selection == "Sentiment Classifier Analysis":
		#st.info("**This application is a Streamlit dashboard used to analyse sentiments about **Climate Change** from tweets.**")
		st.image("climate_change.jpeg",width=700)
		# Number of Tweets
		st.sidebar.subheader("Exploratory Data Analysis of Sentiments 🔍")
		select = st.sidebar.selectbox('Choose Analysis', ['Pie Chart','WordClouds','Frequent Hashtags'])
		#if not st.sidebar.checkbox("Hide", True): 
		st.write("##")# Create space
		st.write("##")# Create space
		if select=='Pie Chart':
			st.header('Pie Chart')
			st.info(' A Pie Chart was created to visually represent the dataset and understand what the dataset entails. ')
			st.title('Climate Change Sentiment Distribution')
			labels = 'Positive', 'News', 'Neutral', 'Negative'
			colors = ['#ff9999','#66b3ff','#95bb72','#ffcc99']
			sizes = [54, 23, 15, 8]
			explode = (0.1, 0, 0, 0)  
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%',
        	shadow=True, startangle=90, colors=colors,radius=1 )
			ax1.axis('equal')
			st.pyplot(fig1)
			st.info("**Observations :** The four labels that make up the list of possible sentiments within this dataset includes Positive, News, Neutral and Negative. The proportion distribution among the labels seen here indicates an imbalance dataset. The majority of the tweets indicate a postive sentiment towards climate change (largest pie slice). The News sentiment follows in distribution size which highlights a great spread of information from news outlets. The Neutral class distribution shows those who are on the fence and require more information to make a decision about climate change. The smallest class distribution proportion are those with Negative sentiments towards climate change. The fact that the negative sentiment is so low helps with curbing misinformation.")	
		

		# WordClouds
		if select == 'WordClouds':
			st.header('WordClouds')
			st.info('**WordClouds were generated to analyse the words surrounding each of the Twitter sentiment classes.** A wordcloud is a collection of words depicted in various sizes. The bigger and bolder the word appears, the more often it is mentioned within its text, thereby relaying its importance.')
			st.write("##")# Create space
			st.write("##")# Create space
			st.title('Positive Sentiment WordCloud')
			st.image('posi_word_no_header.jpeg',width=None)
			st.info('**Observations :** The wordcloud suggests that most positive sentiments include global, warming, climate, change, believe,  real and rt (same sentiment shared amongst people). There are no links or http indicating that data cleaning performed has worked well. The wordcloud suggests there was alot of discussion around scientific genre which includes words such as science, carbon ,research and epa. As this data was collected during the gaining of American election period votes, many tweets were in relation to American politicians and their stance on climate change in exchange for votes.')

			st.write("##")# Create space
			st.write("##")# Create space
			st.title('Negative Sentiment WordCloud')
			st.image('neg_word_no_header.jpeg',width=None)
			st.info('**Observations :** A vast majority of the key words in the negative sentiments are very political and scientific, which indicates a lot of sentiments said by world leaders on the topic of climate change. Trump, a firm anti climate change individual is appearing very significantly, including the terms scientist, made, fake, alarmist which shows either a lot of people not believing that is real, a hunch or because of a lack of scientific evidence to support the claims. There also a lot of words like scam, money, man-made going on indicating one of the reasons they may not really believe climate change or have negative sentiment against it.')

			st.write("##")# Create space
			st.write("##")# Create space
			st.title('Neutral Sentiment WordCloud')
			st.image('neutral_word_no_header.jpeg',width=None)
			st.info('**Observations :** A majority of the neutral words are discussing, engaging and asking about the effects on climate change as seen with words interviewer and scientist. However, the wordcloud also indicates how often Trump made headlines during that period. The mention of penguins pop up often,which indicates they were news worthy due to endangerment because of the effects of climate change. The mention of Leonardo DiCapro indicates that his film called Before The Flood made headlines.')


			st.write("##")# Create space
			st.write("##")# Create space
			st.title('News Sentiment WordCloud')
			st.image ('news_word_no_header.jpeg',width=None)
			st.info('**Observations :** As we can see that the name Trump plays a huge role when it comes to the news sentiment. The Trump administration did not consider Paris Climate Accord (agreement) which made headlines during that time. The wordcloud also introduces a vast majority of issues whereby technical or jargon specific terms such as executive order, policy etc, gets broken and discussed regularly. The word cloud also indicates that majority of the words are well distributed and spoken of almost similarly. Most of that words are not frequently requiring except climate change and global warming. There are a few countries and news outlets mentioned which are in accordance for this wordcloud.')
		
		# Frequent Hashtags
		if select == 'Frequent Hashtags':
			st.header("Frequent Hashtags")
			st.info("Hashtags are popular known functions on the social media platform, Twitter. They are used to index keywords or topics that can be easily accessed by users.")
			st.write("##")# Create space
			st.write("##")# Create space
			st.title('Top 10 Hashtags')
			st.image('tope_10_no_header.jpeg',width=None)
			st.info('**Observations** :  The bar chart highlights the 10 most popular hashtags during that time the dataset was collected. This gives us insights into the context in which people discuss climate change. From there we can see the the top three hashtags are climate, BeforeTheFlood and climatechange. The BeforeTheFlood hashtag gives reference to the film which was release in 2016 and starred Leonard DiCaprio. The film comprises meet ups with scientists, activists and world leaders to discuss the dangers of climate change and possible solutions. During this period the Trump administration played a big role in respect to if America will take a stance in fighting climate change. Therefore, hashtags such ParisAgreement and COP22 was also trending at that time. ')
			st.write("##")# Create space
			st.write("##")# Create space
			st.title('Frequent Hashtags per Sentiment')
			st.image('top10_per_sent.jpeg',width=None)
			st.info(' The plots highlight that the hashtag climate change is seen for all of the four sentiments. Trump and his supporters used the hashtag, MAGA and therefore it is expected to be seen in the negative sentiment category. Topics such as Paris Agreement/Accord and COP22 are also used often in all four sentiments. The negative sentiment introduces the notion of fake news and Climate scam when discussing climate change.')
		
		
	

	# Building out the sentiment predication page
	if selection == "Sentiment Prediction":
		st.info("**This application is a Streamlit dashboard used to analyse sentiments about Climate Change from tweets.**")
		st.image("climate_change.jpeg",width=700)
		st.info("⬅️ Use the sidebar to select Machine Learning Model for sentiment prediction.")

		
		select = st.sidebar.selectbox('Choose Machine Learning Model ⬇️',['Logistic Regression','K-nearest Neighbors (KNN)','Support Vector Classfier (SVC)'])
		# Creating a text box for user input

		tweet_text = st.text_area("Enter Text: ","Type Here")

		if st.button("Classify"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			if select == 'Logistic Regression':
				predictor = joblib.load(open(os.path.join("resources/logistic.pkl"),"rb"))
				prediction = predictor.predict(vect_text)
			if select == 'K-nearest Neighbors (KNN)':
				predictor = joblib.load(open(os.path.join("resources/KNN_model.pkl"),"rb"))
				prediction = predictor.predict(vect_text)
			if select == 'Support Vector Classfier (SVC)':
				predictor = joblib.load(open(os.path.join("resources/SVC_model.pkl"),"rb"))
				prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))
			lst = ['**1:** Positive sentiment about climate change.', '**2:** Factual sentiment based on a legitimate News site.', '**0:** Neutral sentiment about climate change','**-1:**  Negative sentiment about climate change']
			s = ''
			for i in lst:
				s += "- " + i + "\n"
			st.info(s)

			# Explain Models 
			if select == 'Logistic Regression':
				st.info("**What is a Logistic Regression algorithm?** The classification Logistic Regression algorithm is useful in linearly separable data.This model uses a logistic/S-shaped (sigmoid) function to output probabilities and predictions in relation to two maximum values (0 or 1).")

			if select == 'K-nearest Neighbors (KNN)':
				st.info("**What is a K-nearest Neighbors(KNN) algorithm?** The K-nearest Neighbors (KNN) algorithm is said to store all the available cases and classifies new cases based on a similarity measure. The 'K' in the KNN algorithm is the nearest 'neighbor' the value is taken from. For example, if K=1 then the subject is simply assigned to the class of that single nearest neighbor.")

			if select == 'Support Vector Classfier (SVC)':
				st.info('**What is a Support Vector Classifier(SVC) algorithm?** The Support Vector Machine (SVM) is a supervised classification method that separates data using hyperplanes. A hyperplane acts like a decision boundary between the different classes. Each segment will contain only one type of data in that class.')		
	
	
	
	# Building out the "Contact Us" page
	if selection == "Contact Us":
		st.image("Blue_logo.jpeg",width=450)
		st.header(" Get in touch with us 📩 ")
		
		contact_form = """
		<form action="https://formsubmit.co/ereshiagabier@gmail.com" method="POST">
			<input type="hidden" name="_captcha" value="false">
     		<input type="text" name="name" placeholder="Your name"required>
     		<input type="email" name="email" placeholder="Your email"required>
			<textarea name="message" placeholder="Your message here"></textarea>
     		<button type="submit">Send</button>
        </form>
		"""	
		st.markdown(contact_form,unsafe_allow_html=True)

		# Use local CSS file
		def local_css(file_name):
			with open(file_name) as f:
				st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

		local_css("style/style.css") 

	
		st.image("Thank_you.jpeg",width=700)	
		
		

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()
