#指定フォルダのpngからgif作成

from PIL import Image
import glob

files = sorted(glob.glob('xxx/*.png'))
images = list(map(lambda file: Image.open(file), files))
images[0].save('xxx.gif', save_all=True, 
               append_images=images[1:], 
               duration=200, loop=0)
