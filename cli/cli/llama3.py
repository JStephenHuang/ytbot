import requests
import json



class Llama3:
  
    url = "http://localhost:11434/api/generate"
    headers = {
        'Content-Type': 'application/json'
    }
    
    def get_summary(self, text: str):

        context = """
                Generate a concise 2-3 sentence summary that captures the main plot points, key characters, and overall message of this story. 
                Provide only the summary please. Here is the text:"""
        data = {
            "model": "llama3",
            "prompt": f"{context} {text}",
            "stream": False
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))

        return {"status": response.status_code, "value": response.json()["response"]}

    def get_short_narration(self, text: str):

        context = """
               Please summarize the story in a way that is both concise and captivating, focusing on the most dramatic and intriguing plot points. 
               The summary should be structured to keep the viewer's attention, with a strong opening hook and a satisfying conclusion. 
               Use language that is lively and relatable, as if narrating for a TikTok reel or YouTube Short, where the goal is to entertain and engage the audience quickly. 
               Ensure the tone is dynamic, with a balance of excitement and clarity, making the story easy to follow yet compelling enough to encourage viewers to watch till the end."""
        
        data = {
            "model": "llama3",
            "prompt": f"{context} Here is the story: {text}",
            "stream": False
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))

        return {"status": response.status_code, "value": response.json()["response"]}

        
    def get_image_description(self, text: str):
            context = """
               Create a vivid yet concise description of a key moment in this story. 
               Focus on the most visually impactful elements—such as the characters, their emotions, and the setting. 
               Highlight only the essential details that define this moment, ensuring the description is specific enough to guide an image AI generator in creating a clear and compelling representation. 
               Avoid unnecessary complexity, and ensure that the content is entirely safe for work (NSFW)"""
            
            data = {
                "model": "llama3",
                "prompt": f"{context} {text}",
                "stream": False
            }

            response = requests.post(self.url, headers=self.headers, data=json.dumps(data))

            return {"status": response.status_code, "value": response.json()["response"]}



    def get_thumbnail_description(self, text: str):
            context = """
                Create an exceptionally detailed paragraph that vividly embodies one key moment in the story, preferably the climax 
                while ensuring the content is entirely safe for work (NSFW).
                The description should be rich enough to guide a Text-to-Image model in generating a clear and visually accurate thumbnail for a video discussing this story.
                Here is the text:"""
            
            data = {
                "model": "llama3",
                "prompt": f"{context} {text}",
                "stream": False
            }

            response = requests.post(self.url, headers=self.headers, data=json.dumps(data))

            return {"status": response.status_code, "value": response.json()["response"]}



 