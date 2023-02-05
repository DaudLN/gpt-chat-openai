from django.http import JsonResponse
from django.shortcuts import render
from dotenv import load_dotenv
import openai
import os

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


def chat(request):
    if api_key is not None and request.method == "POST":
        # chat_response = None
        openai.api_key = api_key
        user_text = request.POST.get("text")
        prompt = user_text
        model = None
        if "code" or "program" in prompt:
            model = "code-davinci-002"
        else:
            model = "text-davinci-003"
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=0.9,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"],
        )
        user_text = user_text
        text_response = response["choices"][0]["text"].replace("\n", "<br>")
        print(text_response)
        return JsonResponse({"response": text_response})
    else:
        return JsonResponse({"response": None})

def chat_template(request):
    return render(request, "main.html")
