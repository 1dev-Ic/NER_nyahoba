import json

# Load your exported annotated data
with open("project.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)

predictions_output = []

for task in tasks:
    task_id = task["id"]
    
    preds = []
    
    for ann in task.get("annotations", []):
        preds.append({
            "model_version": "from-annotations",
            "score": 0.99,
            "result": ann["result"]
        })
    
    if preds:
        predictions_output.append({
            "id": task_id,
            "predictions": preds
        })

# Save predictions file
with open("predictions.json", "w", encoding="utf-8") as f:
    json.dump(predictions_output, f, indent=2, ensure_ascii=False)

print("✅ Predictions file created successfully!")