# Import the GPT-3.5 tokenizer
from transformers import AutoTokenizer


def convert_tokens_to_text(text):
    # Initialize the tokenizer for GPT-3.5
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")

    # Tokenize the text input
    tokens = tokenizer.tokenize(text)
    # Count the number of tokens
    num_tokens = len(tokens)
    # Print the number of tokens
    #print("Number of tokens:", num_tokens)
    token_limit = 4096
    # Check if the number of tokens exceeds the limit
    if len(tokens) > token_limit:
        # Truncate the tokens to fit within the limit
        tokens = tokens[:token_limit]
        # Print a warning message
    #     print(f"Warning: The input text exceeds the token limit of {token_limit}. Some text may be omitted.")
    # else:
    #     # Print a success message
    #     print(f"Success: The input text fits within the token limit of {token_limit}.")

    # Print the number of tokens
    #print(tokens)
    text = tokenizer.convert_tokens_to_string(tokens)
    # Print the text
    #print(text)
    #print(len(tokens))
    return text