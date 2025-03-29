import json
from transformers import pipeline
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

# Load pre-trained text classification model
nlp_model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base")



# Convert raw model labels to name categories
label_mapping = {
    "HRM": "Harmful", 
    "SAF": "Safe", 
    "NEA": "Needs Attention",
    "LABEL_0": "Safe",
    "LABEL_1": "Needs Attention",
    "LABEL_2": "Harmful"
}

""" Classifies each message as either Harmful, Needs Attention, or Safe """
def classify_message(messages):
    text = messages["content"]
    # Runs the NLP classification
    result = nlp_model(text)[0]

    # Gets the classification label, which defaults to Needs Attention if unknown
    # Gets the confidence score for each cla
    harm_level = label_mapping.get(result["label"], "Needs Attention") 
    conf_score = result["score"]

    # Update the data for each message
    messages["classification"] = harm_level
    messages["confidence_score"] = conf_score
    return messages

"""Takes in the inputted json file and analyzes each message"""
def message_analysis(input):

    with open(input, "r") as file:
        total_data = json.load(file)

    with ProcessPoolExecutor() as executor:
        classed_data = list(executor.map(classify_message, total_data))

    # Save updated data to a new JSON file
    output = "analyzed_messages.json"
    with open(output, "w") as file:
        json.dump(classed_data, file)

    # Convert the results to a DataFrame for easy inspection and save to a CSV file
    df = pd.DataFrame(classed_data)
    output_csv_file = "classed_messages.csv"
    df.to_csv(output_csv_file, index=False)


message_analysis("scraped_messages.json")