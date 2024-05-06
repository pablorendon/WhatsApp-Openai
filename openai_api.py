import json

from openai import OpenAI
import tiktoken
import config
from tools import tools
from tool_functions import *

client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


def chat_completion(messages: list[dict[str, str]]) -> str:
    
    #print(messages)##################################
    print("Tokens uses for first request: " , num_tokens_from_string(str(messages), "cl100k_base"))
    
    response = client.chat.completions.create(
        model=config.GPT_MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
        #max_tokens=100000  # Adjust this value as needed
    )
    
    #print(response)###############################
    response_message = response.choices[0].message
    #print(response_message)##############################

    tool_calls = response_message.tool_calls
    if tool_calls:
        second_messages = [] #Fresh message without the long device map, not needed for second request to openai
        second_messages.append(response_message) #append the tools response . was just messages before
        #print(messages)#######################
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
            #print(function_response)#####################
            second_messages.append( #append the tool and function response to the second message 
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": str(function_response),
                }
            )
        #print(second_messages)###################
        print("Tokens uses for second request: " , num_tokens_from_string(str(second_messages), "cl100k_base"))
        second_response = client.chat.completions.create(
            model=config.GPT_MODEL,
            messages=second_messages #send the new and much shorter second message TOKEN SAVINGS HERE
        )
        return second_response.choices[0].message.content
    else:
        return response_message.content




def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
