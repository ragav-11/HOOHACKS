import json
from transformers import pipeline
import pandas as pd


# Load pre-trained text classification model
nlp_model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base")



# Convert raw model labels to name categories
label_mapping = {
    "HRM": "Harmful", 
    "SAF": "Safe", 
    "NEA": "Needs Attention",
}

""" Classifies each message as either Harmful, Needs Attention, or Safe """
def classify_message(messages):
    text = messages["message"]
    try:
        # Runs the NLP classification
        result = nlp_model(text)[0]

        # Gets the classification label, which defaults to Needs Attention if unknown
        # Gets the confidence score for each cla
        harm_level = label_mapping.get(result["label"], "Needs Attention") 
        conf_score = result.get("score", 0.0)

    except Exception as e:
        print(f"Erro processing message: {messages['message']}, Error: {e}")
        harm_level = "Needs Attention"
        conf_score = 0.0
    # Update the data for each message
    messages["classification"] = harm_level
    messages["confidence_score"] = conf_score
    return messages

"""Takes in the inputted json file and analyzes each message"""
def message_analysis(input):
    try:
        with open(input, "r") as file:
            total_data = json.load(file)

        if not isinstance(total_data, list):
            raise ValueError("Expected a list of messages in the JSON file")
    
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading JSON file: {e}")
        return #exits function of file error occurs
    
    # Process each message and classify it
    classed_data = [classify_message(msg for msg in total_data)]

    # Save updated data to a new JSON file
    output = "analyzed_messages.json"
    with open(output, "w") as file:
        json.dump(classed_data, file)

    # Convert the results to a DataFrame for easy inspection and save to a CSV file
    df = pd.DataFrame(classed_data)
    output_csv_file = "classed_messages.csv"
    df.to_csv(output_csv_file, index=False)

    return classed_data

if __name__ == "__main__":
    message_analysis("scraped_messages.json")
