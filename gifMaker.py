import os 
import imageio

path = os.getcwd() + '/DroneVideoDataset'
dirs = os.listdir(path)
GIFpath = os.path.join(path, 'GIF')
if not os.path.exists(GIFpath):
    os.mkdir(GIFpath)
for d in dirs:
    if d.find('Concat') > -1:
        dpath = os.path.join(path, d)
        frames = os.listdir(dpath)
        frames.sort()
        images = []
        thisGIFpath = os.path.join(GIFpath, d.strip('Concat'))
        if os.path.exists(thisGIFpath + '.gif'):
            continue
        for f in frames:
            images.append(imageio.imread(dpath + '/' + f))
        imageio.mimsave(thisGIFpath + '.gif', images, duration=0.04)
            