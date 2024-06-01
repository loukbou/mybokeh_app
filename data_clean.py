import pandas as pd

def clean_data():
    # Load the dataset
    df = pd.read_csv('survey_result.csv')

    # Drop unnecessary columns
    columns_to_drop = ['lastSubmit', 'userId', 'Fav_Coding_Drink', 'Covid_Productivity']
    data = df.drop(columns=columns_to_drop, errors='ignore')

    # Drop rows with NaN values in significant columns
    columns_to_check = ['Wanted_Programming_Languages', 'Teaching_Problems_POV', 'Open_Source_Participation',
                        'Daily_Web_Frameworks', 'Continuous_Learning_Frequency', 'Immigration_Plans', 'Employment_Status']
    data = data.dropna(subset=columns_to_check)

    # Save the cleaned data to a new file
    data.to_csv('survey_result_cleaned.csv', index=False)

if __name__ == "__main__":
    clean_data()
