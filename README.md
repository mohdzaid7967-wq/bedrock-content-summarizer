# Bedrock Content Summarizer – Micro Tool  
By **Mohd Zaid**

## Problem

Students and professionals read long articles, notes and reports.  
It is difficult and time-consuming to manually extract the key points.

## Solution

This micro-tool uses **Amazon Bedrock** to generate a short summary from long text.  
The user pastes any paragraph, the model returns a clear summary.

## How it works

1. User enters long text in the client (or Bedrock console)
2. The text is sent as a prompt to an LLM on Amazon Bedrock
3. The model generates a short summary
4. The summary is shown back to the user

## Technologies

- Amazon Bedrock (text model like Titan / Claude)
- Python (sample code)
- AWS Workshop Studio environment from AI for Bharat

## Sample Prompt

> Summarize the following text into short and clear bullet points.  
> Focus only on the most important ideas.

## Future improvements

- Simple web UI using HTML/JavaScript + API Gateway + Lambda  
- Upload PDF and generate summary  
- Support for Indian languages  
