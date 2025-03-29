from transformers import pipeline
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

# Load pre-trained text classification model
nlp_model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base")

def analyze_text(message):
    """Analyze a single message and return the classification result."""
    result = nlp_model(message)[0]
    return {"message": message, "label": result["label"], "score": result["score"]}

def analyze_batch(messages):
    """Analyze a batch of messages in parallel."""
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(analyze_text, messages))
    return results

# Example usage with a list of messages
messages = [
    "You're stupid!",
    "Great job, well done!",
    "You should leave this place!",
    "That's awesome, keep it up!"
]

# Analyze the messages in batches
results = analyze_batch(messages)

# Convert the results to a DataFrame for easy inspection and save to a CSV file
df = pd.DataFrame(results)
df.to_csv("cyberbullying_analysis_results.csv", index=False)

print(df)