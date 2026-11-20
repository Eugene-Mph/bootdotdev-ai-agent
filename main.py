import os
import argparse
import json
import sys

from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERATIONS




def main() -> None:
    parser = argparse.ArgumentParser(description="bootdev ai chatbot")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()


    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("Api key not found")


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]


    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    for _ in range(MAX_ITERATIONS):
        try:
            agent_response = generate_content(client, messages, args.verbose)

            if agent_response:
                print(f"Final Response:\n{agent_response}")
                return
        except Exception as err:
            print(f"Error in generate content: {err}")

    print(f"Maxium iterations ({MAX_ITERATIONS}) reached")
    sys.exit(1)


       
    
def generate_content(client: OpenAI, messages: list, verbose: bool) -> str | None:

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,  
    )

    if not response.usage:
        raise RuntimeError("API response appears to be malformed")

    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.prompt_tokens}")


    
    message = response.choices[0].message
    messages.append(message)
    
    if not message.tool_calls:
        # print(f"Response:\n{message.content}")
        # print(message.content)
        return
    
    
    for tool_call in message.tool_calls:
        if tool_call.type != "function":
            continue
        function_args = json.loads(tool_call.function.arguments or "{}") 
        # print(f"Calling function: {tool_call.function.name}({function_args})") 

        result_message = call_function(tool_call)
        

        if not result_message["content"]:
            raise RuntimeError(f"Empty function response for {tool_call.function.name}")

        if verbose:
            print(f"-> {result_message["content"]}")
        messages.append(result_message)

    return None




if __name__ == "__main__":
    main()
