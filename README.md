# my-tips
my tips for javascript, jQuery, python

- [my-tips](#my-tips)
- [IDE](#IDE)
- [python](#python)
  - [mount GDrive at Google Colab](#mount-GDrive-at-Google-Colab)
  - [create gif](#create-gif)
  - [visualize model](#visualize-model)

# IDE
- [Visual Studio Code](/VSCode/VisualStudioCode.md)

# python 

## mount GDrive at Google Colab

```
from google.colab import drive
drive.mount('/content/gdrive')
```

## create gif

``` python
#指定フォルダのpngからgif作成

from PIL import Image
import glob

files = sorted(glob.glob('xxx/*.png'))
images = list(map(lambda file: Image.open(file), files))
images[0].save('xxx.gif', save_all=True, 
               append_images=images[1:], 
               duration=200, loop=0)
```

## visualize model
https://keras.io/ja/visualization/

``` python
from keras.utils import plot_model

#model
Gen = Generator()
Dis = Discriminator()
GAN = Generative_Adversarial_Network(Gen, Dis)

#model png save
plot_model(Gen, to_file='/content/gdrive/My Drive/****/Gen.png')
plot_model(Dis, to_file='/content/gdrive/My Drive/****/Dis.png')
plot_model(GAN, to_file='/content/gdrive/My Drive/****/GAN.png')

```

