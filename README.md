# text_analysis_services
Microservices platform for multiple text analysis services

## Services

1. **Sentiment Analysis Service:** Determine if the sentiment of a given text is positive, negative, or neutral.
2. **Word Count Analysis Service:** Count the number of words in a text.
3. **Entity Recognition:**Identify named entities (e.g., persons, organizations, locations) in a text.

## Prerequisites
1. Python 3.x installed
2. pip (Python package manager)

## Installation
To install the required packages, run the following command:

```
pip install Flask spacy nltk

```

Additionally, download the necessary NLTK data and spaCy model:

```
import nltk
nltk.download('vader_lexicon')

import spacy
spacy.cli.download("en_core_web_sm")
```
## Running the Application

To run the application, navigate to the project directory and execute:

```

python app.py

```

## API Endpoints with example Requests and Response 

1. POST /analyze: Redirects to relevant service and analyze the text.
Example Request
```
http://localhost:5000/services/add
{
    "name": "sentiment_analysis",
    "url": "http://localhost:8001/analyze"

}
```
Example Successful Response
```

{
    "message": "Service sentiment_analysis added"
}

```

2. POST /services/add: Add a new text analysis service.
Example Request
```
http://localhost:5000/analyze
{
    "service": "sentiment_analysis",
    "text": "The weather is great today"
}
```
Example Response
```
{
    "result": "Positive"
}
```
3. DELETE /services/<service_name>: Remove an existing text analysis service.
```
http://localhost:5000/services/sentiment_analysis
```
```
{
    "message":"Service sentiment_analysis removed"
}
```

4. GET /services: List all available text analysis services.
```
{
    "services": [
        "sentiment_analysis"
    ]
}
```

## Running Tests
```
python -m unittest
```

