import os 
import matplotlib.pyplot as plt
path = os.getcwd() + '/DroneVideoDataset'
SSIMFiles = [i for i in os.listdir(path)]
for SSIMF in SSIMFiles:
    if SSIMF.find('_ssim.txt') > -1:
        dirname = f'{SSIMF.strip("_ssim.txt")}SSIM'
        if os.path.exists(os.path.join(path, dirname)):
            continue
        os.mkdir(os.path.join(path, dirname))
        f = open(os.path.join(path, SSIMF), 'r')
        SSIMData = f.readlines()
        SSIMData = [float(i) for i in SSIMData]
        SSIMAccumulate = []
        cnt = 0
        for d in SSIMData:
            SSIMAccumulate.append(d)
            x_axis = [i for i in range(len(SSIMAccumulate))]
            plt.plot(x_axis, SSIMAccumulate, 'r')
            plt.xlim([0, len(SSIMData) + 10])
            plt.ylim([min(SSIMData) - 0.1, max(SSIMData) + 0.1])
            plt.savefig(f'{os.path.join(path, dirname)}/frame{str(cnt).zfill(4)}.jpg')
            plt.close()
            cnt += 1
        
