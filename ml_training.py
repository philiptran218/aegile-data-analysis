import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import mutual_info_regression
from sklearn.metrics import mean_squared_error

def analyze_student_metrics(csv_file, target_metrics, test_size=0.2, random_state=42):
    # Load the dataset
    print("Loading dataset...")
    data = pd.read_csv(csv_file)
    
    # Preprocess the data
    print("Preprocessing dataset...")
    data.fillna(0, inplace=True)
    data = pd.get_dummies(data, drop_first=True)
    
    # Initialize results dictionary
    results = {}

    for metric_name, metric_columns in target_metrics.items():
        print(f"Analyzing metric: {metric_name}...")
        
        # Combine target columns for the current metric
        y = data[metric_columns].mean(axis=1)  # Use the average of related columns as the metric
        
        # Separate features
        X = data.drop(metric_columns, axis=1)

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # Train a regression model
        print(f"Training model for {metric_name}...")
        model = RandomForestRegressor(random_state=random_state)
        model.fit(X_train, y_train)

        # Evaluate the model
        print(f"Evaluating model for {metric_name}...")
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error for {metric_name}: {mse:.2f}")

        # Feature importance analysis
        feature_importances = model.feature_importances_
        importance_scores = {X.columns[i]: feature_importances[i] for i in range(len(feature_importances))}

        # Mutual Information Analysis
        mutual_info = mutual_info_regression(X, y)
        mutual_info_scores = {X.columns[i]: mutual_info[i] for i in range(len(mutual_info))}

        # Save results
        results[metric_name] = {
            "Mean Squared Error": mse,
            "Feature Importance": importance_scores,
            "Mutual Information": mutual_info_scores
        }

    # Return the results
    return results

if __name__ == "__main__":
    # Specify the path to your CSV file
    csv_file_path = "datasets/xAPI-Edu-Data.csv"  # Replace with your file

    # Define target metrics and their associated columns
    target_metrics = {
        "Student engagement": ["raisedhands", "AnnouncementsView", "Discussion"],
        "Task Completion Time": ["VisITedResources", "Discussion"],
        "Quality of Work": ["VisITedResources", "AnnouncementsView", "Discussion"],
        "Task Completion Rate": ["VisITedResources", "AnnouncementsView"],
        "Team Contribution": ["raisedhands", "Discussion"]
    }

    # Analyze the dataset
    results = analyze_student_metrics(csv_file_path, target_metrics)

    # Print results
    for metric, metrics in results.items():
        print(f"\nResults for {metric}:")
        print(f"Mean Squared Error: {metrics['Mean Squared Error']:.2f}")
        print("Feature Importance:")
        for feature, importance in sorted(metrics['Feature Importance'].items(), key=lambda item: item[1], reverse=True):
            print(f"  {feature}: {importance:.4f}")
        print("Mutual Information:")
        for feature, score in sorted(metrics['Mutual Information'].items(), key=lambda item: item[1], reverse=True):
            print(f"  {feature}: {score:.4f}")
