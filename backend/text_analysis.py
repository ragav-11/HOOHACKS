import json


def message_analysis(input_file="scraped_messages.json", output_json="analyzed_messages.json"):
    from transformers import pipeline
    import pandas as pd

    nlp_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

    label_map = {
        "negative": "Harmful",
        "neutral": "Needs Attention",
        "positive": "Safe"
    }

    with open(input_file, "r") as f:
        data = json.load(f)

    classified = []
    for msg in data:
        result = nlp_model(msg["message"])[0]
        msg["classification"] = label_map.get(result["label"].lower(), "Needs Attention")
        msg["confidence_score"] = result["score"]
        classified.append(msg)

    with open(output_json, "w") as f:
        json.dump(classified, f, indent=4)

    pd.DataFrame(classified).to_csv("classed_messages.csv", index=False)
    return classified