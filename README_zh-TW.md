# 文字摘要小工具

## 使用前安裝

> 由於下載Youtube音檔背後需要FFmpeg作為底層轉換套件，因此需先安裝FFmpeg並設定環境變數

### Windows 安裝指令

[安裝參考](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)

### MacOs 安裝指令

```bash
brew install ffmpeg
```

### Linux 安裝指令

#### Ubuntu

```bash
sudo apt update && sudo apt upgrade
```

```bash
sudo apt install ffmpeg
```

#### Fedora 或 RHEL

[安裝參考](https://computingforgeeks.com/how-to-install-ffmpeg-on-centos-rhel-8/)

## 至openai官網申請api-keys

[申請點這裡](https://platform.openai.com/account/api-keys)

取得KEY之後，新增一個文字檔key.txt，並將KEY放入key.txt

## 安裝python相關套件

此專案用poetry為python管理套件因此需安裝poetry

[官方安裝文件](https://python-poetry.org/docs/)

> 執行下列指令即可安裝所有套件

```bash
poetry install
```

> 進入poetry虛擬環境

```bash
poetry shell
```

## 摘要來源

### 在main.py設定Youtube URL

> 設定想下載的youtube連結

```python
url = 'https://youtu.be/fPBNGLghVLU'
prefix = 'audio'
suffix = '.mp3'
```

> 執行主程式

```bash
python main.py
```
