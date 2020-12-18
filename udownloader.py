from pytube import YouTube

url = input('Input your URL-> ')
video = YouTube(url)
for stream in video.streams:
    items = str(stream).split(' ')
    tag = items[1].split('"')[1]
    mimeType = items[2].split('"')[1].split('/')[1]
    resOrAbr = items[3].split('"')[1]
    fpsOrAcodec = items[4].split('"')[1]
    videoType = items[-1].split('"')[1]
    if videoType == 'video':
        print(f'Tag={tag}\t\tType={videoType}\tFormat={mimeType}\tResolution={resOrAbr}\t\tFrame_Per_Second={fpsOrAcodec}\n')
    else:
        print(f'Tag={tag}\t\tType={videoType}\tFormat={mimeType}\tAverage_Bit_Rate={resOrAbr}\t\tCodec={fpsOrAcodec}\n')

tag = int(input('Enter your Tag-> '))
stream = video.streams.get_by_itag(tag)
name = input('Enter the name of the file-> ')
print('Downloading...')
stream.download(filename=name)
print('Done!')
