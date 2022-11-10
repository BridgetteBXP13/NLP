# Snake Debate Chatbot
# Developed by Bridgette Bryant & Tera Parish


# Importing libraries
import pandas as pd
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

def read_in_data(filename):
    # Reading in the csv file with pandas
    df = pd.read_csv(filename)
    # Converting the category column to categorical data
    df.Category = df.Category.astype('category')
    # Displaying the counts of each author
    #print("Counts: ")
    #print(df.Category.value_counts())
    # Displaying the first few rows of the data frame
    #print("\nFirst few rows of data frame:")
    #df.head()
    return df

def split_data(df):
    # Divide into train and test (80/20 with seed 1234 for replicable results)
    # X contains the predictor columns and y contains the target column
    X_train, X_test, y_train, y_test = train_test_split(
        df.Input, df.Category, test_size=0.2, random_state=1234,
        stratify=df.Category)

    # Outputting the dimensions of train and test
    #print("Dimensions of train data: ", X_train.shape)
    #print("Dimensions of test data: ", X_test.shape)
    return X_train, X_test, y_train, y_test

def vectorize_data(X_train, X_test):
    # This is our set of stopwords, it will be used during vectorization
    stopwd = set(stopwords.words('English'))
    # Setting up our stopwords for our vectorizer
    vectorizer = CountVectorizer(stop_words=stopwd, strip_accents='unicode')
    # Perform tf-idf vectorization and fit to training data
    X_train_vect = vectorizer.fit_transform(X_train)
    # Transforming the test data with the fitted tf-idf vectorization
    X_test_vect = vectorizer.transform(X_test)
    # Outputting the dimensions of train and test
    print("Dimensions of the vectorized train data: ", X_train_vect.shape)
    print("Dimensions of the vectorized test data: ", X_test_vect.shape)
    return X_train_vect, X_test_vect, vectorizer

def create_input_model(X_train_vect, y_train, X_test_vect, y_test):
    # Training our model, using liblinear solver
    logreg = LogisticRegression(solver='liblinear', random_state=1234, class_weight='balanced', C=10, max_iter=5000)
    logreg.fit(X_train_vect, y_train)
    # Printing the accuracy on the training data
    print("Accuracy on Training Data: ", logreg.score(X_train_vect, y_train))

    # Testing and evaluating
    logreg_pred = logreg.predict(X_test_vect)

    print("\nResults on testing data:\n")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, logreg_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, logreg_pred))
    return logreg

if __name__ == "__main__":
    # Let's read in our data into a dataframe
    question_df = read_in_data('Data/inputs.csv')

    # Next we need to split up our dataframe
    X_train, X_test, y_train, y_test = split_data(question_df)

    # Then we need to vectorize our data
    X_train_vect, X_test_vect, vectorizer = vectorize_data(X_train, X_test)

    # Finally we need to create our model for the input data
    input_model = create_input_model(X_train_vect, y_train, X_test_vect, y_test)

    # Testing some inputs on our model
    print("Input: Snakes are awful")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["Snakes are awful"])))
    print("Input: Snakes are gross")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["Snakes are gross"])))
    print("Input: Snakes feel no love and are emotionless")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["Snakes feel no love and are emotionless"])))
    print("Input: I dislike snakes")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["I dislike snakes"])))
    print("Input: Snakes like to bite")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["Snakes like to bite"])))
    print("Input: Snakes are mean creatures")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["Snakes are mean creatures"])))
    print("Input: Snakes shouldn't exist")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["Snakes shouldn't exist"])))
    print("Input: How are snakes any good")
    print("Predicted Category: ", input_model.predict(vectorizer.transform(["How are snakes any good"])))
