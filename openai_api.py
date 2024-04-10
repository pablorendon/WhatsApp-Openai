import json

from openai import OpenAI

import config
from tools import tools
from tool_functions import *

client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


def chat_completion(messages: list[dict[str, str]]) -> str:
    response = client.chat.completions.create(
        model=config.GPT_MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
        #max_tokens=100000  # Adjust this value as needed
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            # Check if arguments are provided
            if tool_call.function.arguments:  # Assuming this checks for non-empty argument string
                function_args = json.loads(tool_call.function.arguments)
                # Ensure function_args is not empty; call function with or without args accordingly
                if function_args:
                    function_response = function_to_call(function_args)
                else:
                    function_response = function_to_call()
            else:
                # No arguments provided, call the function without arguments
                function_response = function_to_call()
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": str(function_response),
                }
            )
        second_response = client.chat.completions.create(
            model=config.GPT_MODEL,
            messages=messages,
        )
        return second_response.choices[0].message.content
    else:
        return response_message.content
