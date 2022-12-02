# Developers

<img src = "https://snipboard.io/HdEiXr.jpg" alt="Team Members" width="500" height="370">

## Team Members:
- Andress Eduardo Arana Bejar
- Adrián Roberto Carmona Rodriguez
- Alejandro Rodriguez Trillo
- Emmanuel Alejandro Hurtado Alejandre
- Jason Maximiliano Salazar Bustillos

# Project Understanding
## Determine Objectives 
### Objectives and Background

The Universidad Politécnica de Yucatán is an independent, public higher education institution that provides advanced and specialized courses in Data, Embedded Systems, Robotics, and Engineering, all while following a Bilingual, International and Sustainable (BIS) approach.

UPY is a public institution focused on the Information and Communication Technology (ICT) domain. It follows a Bilingual, International, and Sustainable (BIS) model to enrich the academic experience of its undergraduate students through creative instruction and cultural exposure with the purpose of producing successful professionals.

The main business objective is to build a system that will classify a tweet into one of two topics and generate a tweet for the other topic based on the original tweet, you must build an API for a tweet classification system and add a real time visualization dashboard. The dynamic tweet capture strategy should be used to get tweets about the two topics which are being compared.

### Success Criteria 

- Build algorithms to predict classes of tweets and to generate fake tweets from a specific label given a real tweet from the opposite label. 
- Generation of fake tweets given a well gotten categorization from specific topics.
- Shown proficient knowledge in the subjects covered by this specific project.

## Situation Assessment

### Inventory of resources
The 6 members of the team:
- 6 Laptops
- Teacher’s accessories
- Internet connection
- Google Cloud Platform
- GCP Credits
- Twitter API
- 1 Twitter Developer Account
- Google Locker Studio
- Google Collab
- Google Meet for daily video calls
- Discord channel for announcements
- GitHub repository
- Microsoft Teams  

### Requirements, assumptions and constraints

<strong>Requirements</strong>
- Create a Tweet visualization System by applying the CRISP DM Methodology.
- Perform preprocessing to enhance the classification of the tweets of the selected topics.
- Create a class to preprocess your data and add it to the input of the classifier.
- Create a tweet classification model using neural networks.
- Collect tweets on the selected topics into a database.
- Create a visualization dashboard with the following characteristics:
- Tweet class distribution: A chart about the distribution of the tweets as classified by the model.
- Tweet location distribution: A chart showing the geographical distribution of the tweets distinguishable by class.
- Tweet timeline: A chart with the tweet frequency in each timeframe with both the total amount of tweets and the count for each class.
- Using the collected tweets build a tweet generative model using char encoder decoder or a transformer model.
- In real time, as you detect a tweet with any of the topic hashtags use the generative model to create a tweet about the other topic.

<strong>Assumptions</strong>
- Spotify and Apple Music are comparable topics.
- Since both music apps are extremely popular, there should be enough tweets of both to train the models.

<strong>Constraints</strong>
- The minimum Dashboard refresh period must be 1 minute, due to Looker Studio limitations.
- Data Studio does not allow automatic refresh of data in real time, it must be done manually.
- Tweet’s location data might be not available due to the version of the Twitter Developer API.  
- Tweet processing speed might be slower than getting tweets in real time.
- Tweets must be in English only, because of limitations of NLP techniques in other languages.

### Risks and contingencies

<strong>Risks</strong>
- Generative Model might be not good enough to generate logic sentences.
- Geolocation of tweets might not be available.
- The number of tweets from 1 topic could be much bigger than the other topic, so it is important to use the same number of tweets from both.
- Real-time limitations, so the system might work as a kind of batch/real-time system.

<strong>Contingencies</strong>
- If for any reason the system crashes during ETL process; purge subscriber and reboot the system to start again. The tweets are stored directly in Big - - - Query when they are obtained from the API, so there is no data loss.

## Determine data mining goals
### Data mining goals

- Build a predictive model capable of categorizing a series of tweets in real time. Categorization must be between two labels: “spotify” and “apple music”
- Build a generative model capable of generating tweets with a specific label given a real tweet categorized with the “opposite” label. 
- Build predictive model with 70% accuracy
- Build predictive model with 70% recall
- Build predictive model with 70% precision
- Build generative model with 70% accuracy
- Build generative model with 70% recall
- Build generative model with 70% precision
- Integrate the system as a whole
- Build a dashboard with insights gotten from the data mining tasks


### Data mining success criteria

- Get predictive model with 70% accuracy
- Get predictive model with 70% recall
- Get predictive model with 70% precision
- Get generative model with 70% accuracy
- Get generative model with 70% recall
- Get generative model with 70% precision
- Deploy a functional dashboard showing tweets in real time and the output of the predictive and generative model.

Most of the criteria for achieving our data mining goals must be completely fulfilled or at least nearly fulfilled with a difference not greater than 0.1

# Activites for this project:
<img src = "https://snipboard.io/Ngo3zj.jpg" alt="Team Members" width="750" height="370">

# Next steps
<img width="1233" alt="image" src="https://user-images.githubusercontent.com/46505958/205354208-e8a9a3f9-14b6-4e43-a0b7-7e88889fe6f4.png" width="800" height="270">

