# ai-vs-human-text-classification
Focuses on distinguishing between AI-generated and human-written text
Introduction:
In the era of AI-generated content, distinguishing between human-written and AI-generated text has become crucial across various fields, including journalism, academic integrity, and creative industries. This project, AI vs Human Text Classifier, leverages machine learning techniques to classify text as either human-written or AI-generated, providing an automated solution to this emerging challenge.

### Project Overview:
This project aims to build a robust text classifier using Natural Language Processing (NLP) and machine learning techniques. The model identifies whether a given text is human-generated or AI-generated. The dataset used contains labeled text examples for both categories, and a machine learning model is trained to recognize patterns and characteristics unique to each.

### Problem Statement:

The rise of AI-generated content makes it difficult to differentiate between human and machine-written text. This project solves that issue by creating a classifier model.

### Dataset:

Utilized a labeled dataset containing examples of both human-generated and AI-generated text. Data cleaning and preprocessing were carried out, including tokenization, removing stop words, and stemming.

### Model Selection:

Experimented with various machine learning models such as Logistic Regression, Random Forest, and Support Vector Machines (SVM). After testing, a fine-tuned Random Forest model provided the highest accuracy.
### Feature Engineering:

Used TF-IDF (Term Frequency - Inverse Document Frequency) to convert the text into numerical features.

### Challenges:

Challenge 1: Balancing the dataset with an equal distribution of AI and human text.
Solution: Oversampling and undersampling techniques to balance the dataset.
Challenge 2: Handling ambiguity in some texts that resemble both human and AI characteristics.
Solution: Applied regularization techniques to avoid overfitting and improve generalization.
### Programming Framework:

Programming Language: Python
### Libraries Used:
NLP: NLTK, spaCy for text preprocessing.
Machine Learning: Scikit-learn for model building and evaluation.
Web Application: Flask for building the web interface where users can input text and see classification results.
### Model Training:

Split the dataset into training and testing sets.
Performed cross-validation and hyperparameter tuning to optimize model performance.
Web Deployment:

Built a simple web interface using Flask where users can input text to classify.
Added a feature that displays the prediction in real-time.
Evaluation:

Achieved an accuracy of around 90% in classifying texts correctly.
Deployed the final model with real-time feedback and visualization.
