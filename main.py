import os
from dotenv import load_dotenv
from openai import OpenAI





def main() -> None:

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
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
            }
        ]
    )

    response_text = response.choices[0].message.content

    print(f"\nResponse:\n{response_text}\n")
    


if __name__ == "__main__":
    main()
