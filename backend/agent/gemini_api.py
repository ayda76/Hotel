from google import genai
from google.genai import types

from decouple import config as env_config
from .time_tool import get_current_time
client=genai.Client(api_key=env_config("GEMINI_API_KEY"))


generation_config  = types.GenerateContentConfig(
    tools=[get_current_time]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="what time it is?",
    config=generation_config
)

tools = {
    "get_current_time": get_current_time,
    
}

if response.function_calls:
    function_call = response.function_calls[0]
    
    tool = tools[function_call.name]    
    result = tool(**function_call.args)
    tool_response = types.Part.from_function_response(
        name=function_call.name,
        response={
            "result": result
        }
    )


    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            response.candidates[0].content,
            tool_response
        ]
    )

    print(final_response.text)

else:
    print(response.text)


#python -m agent.gemini_api