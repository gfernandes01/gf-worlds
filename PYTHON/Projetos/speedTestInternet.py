import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()
print(f"DOWNLOAD speed: {down}")
print(f"UPLOAD speed: {upload}")