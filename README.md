# 🎙️ Realtime Mic-to-Browser Audio Streaming (即時音訊串流系統)

這是一個從零開始打造的【即時聲音串流實驗專案】，  
可以讓你使用 Python 擷取麥克風的即時聲音，並透過 WebSocket 傳送到瀏覽器即時播放！

> ✅ 沒有用到第三方語音 SDK  
> ✅ 沒有用到 WebRTC  
> ✅ 100% 自己寫出來的程式碼

---

## 🔥 功能特色

- 🎧 即時播放：從電腦麥克風擷取聲音，直接播放到瀏覽器。
- 🔗 WebSocket 串流：利用 WebSocket 傳輸聲音資料，實現近乎即時的傳輸。
- 🔊 無雜音版本：固定取樣率、封包大小與格式，確保播放乾淨穩定。
- 🧪 可擴充：未來可整合語音辨識、遠端監聽、雙向語音等功能。

---

## 🚀 使用說明

### 1. 安裝 Python 套件


- pip install websockets sounddevice numpy


### 2. 啟動伺服器
- python server.py
伺服器啟動後會顯示：

- WebSocket server listening on ws://localhost:5678


### 3. 打開 index.html
使用 Chrome 或 Firefox 開啟 index.html，允許 Audio 播放權限後，你就會聽到自己麥克風即時發出的聲音！

## 📦 檔案結構

📁 your-project-folder
├── server.py         ← Python WebSocket 錄音伺服器
└── index.html        ← 前端頁面，接收並播放音訊

## 🛠️ 技術重點
Python + sounddevice: 擷取即時聲音（int16, 16kHz）

WebSockets：雙向即時資料傳輸

HTML + JavaScript：AudioContext 實現聲音播放

音訊封包格式對齊：int16 → float32 → 播放，避免雜音/失真

## 🧭 延伸發展（TODO Ideas）
## 📡 支援遠端多裝置連線（非 localhost）

## 🧠 結合 Speech-to-Text 實現語音轉文字

## 🔐 加入傳輸加密與驗證（例如 TLS）

## 🖥️ 建立管理介面 / 音訊視覺化圖表

## 📱 將 Python server 搬進手機裝置（Kivy / 原生）

## 🙌 作者
本專案由 eric039eric 開發。
靈感來源與技術協助：ChatGPT（OpenAI）

## 🧡 特別感謝
如果你也對這類即時聲音系統有興趣，歡迎 star ⭐️、fork 🍴、或來 issue 一起交流！# Real-time-audio-streaming-system