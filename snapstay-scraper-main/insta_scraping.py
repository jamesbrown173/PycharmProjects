import instaloader
import json
from time import sleep
from datetime import datetime
import sys
import random
import os
import requests


# To extract tagged posts from an Instagram profile	
def get_data(post_url):
	
	try:
		loader = instaloader.Instaloader()
		
		if not post_url.endswith('/'):
			post_url = post_url + '/'

		post = instaloader.Post.from_shortcode(loader.context, post_url.split('/')[-2])
		
		post_data = {}

		print('Searching...')

		post_id = 1
		post_id_general = 1

		# Get Instagram username
		ig_user = post.owner_username

		if not os.path.exists(f"data-{ig_user}"):
			os.makedirs(f"data-{ig_user}")

		# Verify post type
		if post.is_video:
			
			video_response = requests.get(post.video_url)
			
			video_content = video_response.content

			date_now = datetime.now()

			formatted_date = date_now.strftime("%Y-%m-%d_%H-%M-%S")

			file_path = f"data-{ig_user}/vid-{ig_user}-{formatted_date}.mp4"

			with open(file_path, "wb") as f:
				f.write(video_content)

		else:

			image_response = requests.get(post.url)
		
			image_content = image_response.content

			date_now = datetime.now()

			formatted_date = date_now.strftime("%Y-%m-%d_%H-%M-%S")

			file_path = f"data-{ig_user}/img-{ig_user}-{formatted_date}.jpg"

			with open(file_path, "wb") as f:
				f.write(image_content)


		# Handle carousels
		sidecar_nodes = post.get_sidecar_nodes()
		
		num_post = 1
		
		for i, sidecar_node in enumerate(sidecar_nodes):
			
			if sidecar_node.is_video:
				video_response = requests.get(sidecar_node.video_url)
			
				video_content = video_response.content

				date_now = datetime.now()

				formatted_date = date_now.strftime("%Y-%m-%d_%H-%M-%S")

				file_path = f"data-{ig_user}/vid-{num_post}-{ig_user}-{formatted_date}.mp4"

				with open(file_path, "wb") as f:
					f.write(video_content)

			else:				
				image_response = requests.get(sidecar_node.display_url)
		
				image_content = image_response.content

				date_now = datetime.now()

				formatted_date = date_now.strftime("%Y-%m-%d_%H-%M-%S")

				file_path = f"data-{ig_user}/img-{num_post}-{ig_user}-{formatted_date}.jpg"

				with open(file_path, "wb") as f:
					f.write(image_content)

			num_post += 1


		print(f'Successfully obtained post from user "@{post.owner_username}".')
				
		sleep(0.1)
			

	except Exception as e:
		print(f"An error occurred while obtaining post data: {str(e)}")


post_url = input('Paste the Post URL for Download: ')
get_data(post_url)