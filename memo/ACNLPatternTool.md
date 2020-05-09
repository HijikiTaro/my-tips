# note
- この環境を Docker で実現してみる
  - Dockerfile 作成?
- 各コマンドが何をやっているのか調べる

# ACNLPatternTool set up
- 環境
  - WSL Ubuntu
- npm install 
```
sudo apt install npm
```

- Homebrew install
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
- Warning: /home/linuxbrew/.linuxbrew/bin is not in your PATH. への対応
```
echo 'export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"' >>  ~/.bashrc
source ~/.bashrc
```
- yarn install
```
brew install yarn
```

- ACNLPatternTool install
```
git clone https://github.com/Thulinma/ACNLPatternTool
cd ACNLPatternTool
git submodule update --init --recursive
cd zxing-js-library
yarn
cd ..
npm install
npm run build:submodule
```

- RUN ACNLPatternTool
```
npm run dev
```
