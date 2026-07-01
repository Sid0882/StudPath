import requests

def get_enhancv_score(file_storage):
    """
    Sends the resume file to the analyzer and returns the results.
    """
    # If using Enhancv API (replace with actual URL/Key)
    API_URL = "https://api.enhancv.com/api/v1/resumes"
    API_KEY = "YOUR_ENHANCV_API_KEY"
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    files = {'file': (file_storage.filename, file_storage.read(), file_storage.content_type)}
    
    try:
        # In a real scenario, you'd use requests.post
        # response = requests.post(API_URL, headers=headers, files=files)
        # return response.json()
        
        # MOCK DATA for testing your dashboard:
        return {"score": 85, "feedback": "Strong Python skills detected!"}
    except Exception as e:
        print(f"Error: {e}")
        return None