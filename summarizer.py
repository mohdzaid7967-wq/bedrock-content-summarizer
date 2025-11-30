import boto3

# Create a Bedrock runtime client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

def summarize_text(text):
    prompt = f"Summarize the following text in short and clear bullet points:\n\n{text}"

    body = {
        "inputText": prompt
    }

    response = client.invoke_model(
        modelId="amazon.titan-text-lite-v1",  # example model
        body=str(body)
    )

    print(response)  # In a real app we would parse and show the summary

if __name__ == "__main__":
    sample_text = "Paste any long paragraph here and the model will summarize it."
    summarize_text(sample_text)
