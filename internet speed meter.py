import speedtest
test=speedtest.Speedtest()
download=test.download()
upload=test.upload()
printf(f"Download speed  : {download} \n upload speed : {upload})
       print("done ")
