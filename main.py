import os
from embedchain import App

# Set Hugging Face token
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

# Configuration for Hugging Face models
'''config = {
    'llm': {
        'provider': 'huggingface',
        'config': {
            'model': 'mistralai/Mistral-7B-Instruct-v0.2',
            'top_p': 0.5
        }
    },
    'embedder': {
        'provider': 'huggingface',
        'config': {
            'model': 'sentence-transformers/all-mpnet-base-v2'
        }
    }
}

# Initialize the app
app = App.from_config(config=config)

# Add URLs to the app
try:
    app.add("https://www.forbes.com/profile/elon-musk")
    app.add("https://en.wikipedia.org/wiki/Elon_Musk")
except Exception as e:
    print(f"Error adding sources: {e}")

# Query information
try:
    answer = app.query("What is the net worth of Elon Musk today?")
    print("Answer:", answer)
except Exception as e:
    print(f"Error querying the model: {e}")'''


import os
from embedchain import App

# Set Hugging Face token
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

# Configuration for Hugging Face models
config = {
    'llm': {
        'provider': 'huggingface',
        'config': {
            'model': 'mistralai/Mistral-7B-Instruct-v0.2',
            'top_p': 0.5
        }
    },
    'embedder': {
        'provider': 'huggingface',
        'config': {
            'model': 'sentence-transformers/all-mpnet-base-v2'
        }
    }
}

# Initialize the app
app = App.from_config(config=config)

# Add URLs to the app
try:
    app.add("https://www.forbes.com/profile/elon-musk")
    app.add("https://en.wikipedia.org/wiki/Elon_Musk")
except Exception as e:
    print(f"Error adding sources: {e}")

# Query information

response = app.query("What is the net worth of Elon Musk today?")

print(response.split(':')[-1])


'''try:
    # Get the full response
    response = app.query("What is the net worth of Elon Musk today?")

    # Extract only the answer
    if isinstance(response, dict) and 'answer' in response:
        answer = response['answer']
    else:
        # If it's not a dictionary, assume it's already the answer text
        answer = 'all'

    print("Answer:", answer)

except Exception as e:
    print(f"Error querying the model: {e}")'''

