from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai
from django.shortcuts import render

# Configure the Gemini AI
genai.configure(api_key='AIzaSyCgZxMbdMmYVyo2zTK-J-6GRLYcGdGHYWQ')
model = genai.GenerativeModel('gemini-pro')

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        if user_message.lower() in ['exit', 'quit', 'bye']:
            response_message = "Preciouse: Take care! Remember, it's okay to seek help if you need it."
        else:
            chat = model.start_chat(history=[])
            response = chat.send_message(f"User: {user_message}\nRespond as a supportive mental health chatbot:")
            response_message = f"Preciouse: {response.text}"

        return JsonResponse({'message': response_message})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
