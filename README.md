# my-tips
my tips for javascript, jQuery, python


# python 
## keras

#model visualization
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
