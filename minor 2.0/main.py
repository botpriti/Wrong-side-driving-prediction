# Step 1: Load the data from CSV file into a pandas DataFrame
import pandas as pd

data = pd.read_csv(r'C:\Users\KIIT\Documents\Aniket\MInor project\minor 2.0\merged_data.csv')

# Step 2: Split the data into training and testing sets
from sklearn.model_selection import train_test_split

X = data[['Longitude', 'Latitude', 'Direction']]
y = data['Wrong side']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3 and 4: Create feature matrix and label vectors
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Train a SVM model using SVC from sklearn
from sklearn.svm import SVC

svm = SVC(kernel='linear', C=1.0, random_state=42)
svm.fit(X_train_scaled, y_train)

# Step 6: Evaluate the model on the test set and calculate accuracy, precision, recall, and F1-score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_pred = svm.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
print('F1-score:', f1)

# Step 8: Build a predictive system to predict whether a given input corresponds to wrong side driving
def predict_wrong_side_driving(longitude, latitude, direction):
    input_data = [[longitude, latitude, direction]]
    input_data_scaled = scaler.transform(input_data)
    prediction = svm.predict(input_data_scaled)
    if prediction[0] == 1:
        return 'Wrong Side Driving'
    else:
        return 'Not Wrong Side Driving'
    
# Sample longitude, latitude and direction values
longitude = 179.4830479
latitude = 68.46091078
direction = 167.7957415

# Call the function
result = predict_wrong_side_driving(longitude, latitude, direction)

# Print the result
print(result)