# Import required libraries
from openai import OpenAI
import gradio as gr

# Initialize OpenAI client with DeepSeek API configuration
client = OpenAI(
    api_key="sk-your-key",
    base_url="https://api.deepseek.com/v1")


def predict(message, history):
    """"
    Process chat messages and generate AI responses
    Args:
        message: Current user input
        history: Previous conversation history
    """
    try:
        # Convert chat history to OpenAI format
        history_openai_format = []
        for human, ai in history:
            history_openai_format.append({"role": "user", "content": human})
            history_openai_format.append({"role": "assistant", "content": ai})
        history_openai_format.append({"role": "user", "content": message})

        try:
            # Create a chat completion request using DeepSeek API
            # This is the core part of the chat application that handles the interaction with the AI model
            response = client.chat.completions.create(
                # DeepSeek's chat model identifier
                model='deepseek-chat',
                # Conversation history in OpenAI format: [{"role": "user", "content": "msg"}, ...]
                messages=history_openai_format,
                # Controls response randomness (0-2): higher = more creative, lower = more focused
                temperature=1.0,
                # Enable real-time response streaming
                stream=True
            )

            # Initialize empty string for accumulating streamed response
            partial_message = ""
            # Process each chunk from the streaming response
            for chunk in response:
                # Check if the chunk contains new content in its delta
                # This verification is crucial for handling streaming responses properly:
                # - Ensures we only process chunks with actual content
                # - Prevents processing empty/null content chunks
                # - Maintains smooth streaming output flow
                if chunk.choices[0].delta.content is not None:
                    # Accumulate new content to partial_message
                    partial_message += chunk.choices[0].delta.content
                    # Yield the current accumulated message
                    # This creates a generator that:
                    # - Returns the growing message in real-time
                    # - Enables progressive/typewriter-like display in the UI
                    # - Provides immediate feedback to the user
                    # - Maintains a smooth streaming experience
                    yield partial_message
        except Exception as api_error:
            # Handle API-related errors
            yield f"API Error: {str(api_error)}"
    except Exception as format_error:
        # Handle message format errors
        yield f"Format Error: {str(format_error)}"


# Create Gradio chat interface
iface = gr.ChatInterface(
    predict,
    chatbot=gr.Chatbot(height=500, type='messages'),
    title="DeepSeek Chat - Multi-turn Conversation",
    description="Chat with the DeepSeek AI model. Your conversation history will be maintained.",
    theme="soft",
    examples=["Hello, how are you?", "What's the weather like today?"],
    # Specify the type parameter
    type='messages',
)

# Launch the web interface
iface.launch()
