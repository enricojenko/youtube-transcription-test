from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your YouTube video ID
video_id = "1aA1WGON49E"

# Get transcription for the video
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print(transcript)
except Exception as e:
    print(f"Error fetching transcript: {e}")

