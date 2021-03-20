from PIL import Image
import os 
def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
    
path = os.getcwd() + '/DroneVideoDataset'
movies = os.listdir(path)
for movie in movies:
    if movie.find('mp4') > -1:
        frameFilename = movie.strip('.mp4')
        frameDir = os.path.join(path, frameFilename)
        frames = os.listdir(frameDir)
        frames.sort()
        SSIMFrameFilename = movie.strip('.mp4') + 'SSIM'
        SSIMFrameDir = os.path.join(path, SSIMFrameFilename)
        SSIMFrames = os.listdir(SSIMFrameDir)
        SSIMFrames.sort()
        concatFramesDir = os.path.join(path, frameFilename + 'Concat')
        if os.path.exists(concatFramesDir):
            continue
        os.mkdir(concatFramesDir)
        cnt = 0
        for f, s in zip(frames, SSIMFrames):
            background = Image.open(frameDir + "/" + f)
            foreground = Image.open(SSIMFrameDir + "/" + s)
            widthBackground, heightBackground = background.size
            widthForeground, heightForeground = foreground.size
            background.paste(foreground, (widthBackground - widthForeground, 0))
            background.save(concatFramesDir + f"/frame{cnt:4d}.jpg" )
            cnt += 1