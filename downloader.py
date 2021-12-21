import requests
img_url = 'https://i.pinimg.com/736x/4a/9e/ef/4a9eefccad674a1227bd70228eac6132.jpg'
video_url = 'https://www.tiktok.com/@l.lluka/video/7043809258135244034?is_copy_url=1&is_from_webapp=v1'
def download_img(url=''):
	try:
		response = requests.get(url=url)
		with open('req_img.jpg', 'wb') as file:
			file.write(response.content)
		return 'Img successfully downloaded!'
	except Exception as _ex:
		return 'Upps... Check the URL please!'

def download_video(url=''):
	try:
		response = requests.get(url=url)
		with open('req_video.mp4', 'wb') as file:
			file.write(response.content)
		return 'Video successfully downloaded!'
	except Exception as _ex:
		return 'Upps... Check the URL please!'

def main():
	print(download_video(url=video_url))
if __name__ == '__main__':
	main()