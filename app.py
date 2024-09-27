from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

# Route to handle YouTube transcription and save it as a file
@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        # Get the video ID from the POST request
        video_id = request.json.get('video_id')
        
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Convert transcript list to text
        transcript_text = "\n".join([t['text'] for t in transcript])

        # Save transcript to a file
        file_name = f"transcript_{video_id}.txt"
        with open(file_name, 'w') as f:
            f.write(transcript_text)
        
        # Return success response with the file name
        return jsonify({"message": f"Transcript saved as {file_name}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


