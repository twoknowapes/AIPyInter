from openai import OpenAI
import json

# Initialize client
client = OpenAI(
    api_key="sk-your-key",
    base_url="https://api.deepseek.com/v1"
)

def debug_response_chunk():
    """Debug function to examine the structure of streaming response chunks"""
    try:
        # Create a simple chat request
        response = client.chat.completions.create(
            model='deepseek-chat',
            messages=[{"role": "user", "content": "Say hello"}],
            stream=True
        )

        print("=== Starting Stream Analysis ===")
        
        for i, chunk in enumerate(response):
            # Print chunk details
            print(f"\nChunk #{i}:")
            print(f"Type: {type(chunk)}")
            print(f"Choices length: {len(chunk.choices)}")
            
            # Process chunk only if choices list is not empty
            if chunk.choices:
                choice = chunk.choices[0]
                print(f"Delta content: {choice.delta.content}")
                
                # Print full chunk structure
                print("\nFull chunk structure:")
                print(json.dumps(chunk.model_dump(), indent=2))        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Run debug function
if __name__ == "__main__":
    debug_response_chunk()
