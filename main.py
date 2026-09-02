import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI




def main() -> None:
    parser = argparse.ArgumentParser(description="bootdev ai chatbot")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to LLM")
    args = parser.parse_args()


    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("Api key not found")


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt
            }
        ]
    )

    response_text = response.choices[0].message.content

    if not response.usage:
        raise RuntimeError("API response appears to be malformed")
    
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens 

    print(f"\nuser prompt:{args.user_prompt}")
    print(f"\nPrompt tokens: {prompt_tokens}")

    print(f"Response tokens: {completion_tokens}")
    print(f"\nResponse:\n{response_text}\n")
    


if __name__ == "__main__":
    main()
