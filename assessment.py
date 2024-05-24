import requests


def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json()
        sorted_models = sorted(models, key=lambda x: x.get('downloads', 0), reverse=True)
        top_ten_models = sorted_models[:10]
        return top_ten_models
    else:
        print(f"Failed to fetch models: {response.status_code}")
        return []


def generate_report(models):
    report = "Top 10 Downloaded Models on Hugging Face:\n\n"
    for i, model in enumerate(models):
        report += f"{i + 1}. {model['modelId']} - {model.get('downloads', 0)} downloads\n"
    with open("/output/report.txt", "w") as file:
        file.write(report)


if __name__ == "__main__":
    top_models = fetch_top_models()
    if top_models:
        generate_report(top_models)
    print("Report generation completed. Stopping container.")

