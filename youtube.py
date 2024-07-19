from pytube import YouTube
import yt_dlp

# Function to download the video using yt_dlp
def download_video(link):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([link])
            print("Download completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

# Function to display video details
def display_video_details(yt, link):
    print("Title:", yt.title)
    print("Views:", yt.views)
    print("Duration (seconds):", yt.length)
    print("Description:", yt.description)
    print("Ratings:", yt.rating)
    print("Publish Date:", yt.publish_date)
    print("Author:", yt.author)
    print("Keywords:", yt.keywords)
    print("Video ID:", yt.video_id)
    print("Thumbnail URL:", yt.thumbnail_url)
    print("Channel Name:", yt.channel_id)

    # Extract number of likes and comments using yt_dlp
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(link, download=False)
            likes = info_dict.get('like_count', 'Not available')
            comments = info_dict.get('comment_count', 'Not available')
            print("Number of Likes:", likes)
            print("Number of Comments:", comments)
        except Exception as e:
            print("Number of Likes: Not available")
            print("Number of Comments: Not available")

# Main function to get video info and download
def main():
    link = input("Enter Link of YouTube Video: ")
    
    try:
        yt = YouTube(link)
        display_video_details(yt, link)
        
        download = input("Do you want to download this video? (yes/no): ").strip().lower()
        if download == 'yes':
            download_video(link)
        else:
            print("Download skipped.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the main function
if __name__ == "__main__":
    main()
