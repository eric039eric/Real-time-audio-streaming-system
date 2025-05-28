# 🎙️ 即時音訊串流系統（Mic-to-Browser Realtime Audio Streaming）

這是一個使用 Python 和 HTML 製作的「即時聲音監聽系統」。

你可以：

* 使用筆電或桌機的麥克風錄音
* 透過 WebSocket 即時傳送聲音到網頁
* 在瀏覽器中 **立即聽見自己麥克風的聲音**

---

## ✨ 功能特色

* 📡 即時錄音 → 傳輸 → 播放
* 🧠 全部自行寫成，不依賴語音 SDK
* 📦 使用標準 Python 函式庫 + HTML 原生 API
* 🔁 連接順暢無雜音（使用固定取樣率與封包大小）
* 🔧 可成為遠端語音監聽、智慧聲音觸發系統的雛形

---

## 🔧 執行方式（本地使用）

### ✅ 第一步：安裝套件

使用 pip 安裝所需套件（一次安裝即可）：

```bash
pip install websockets sounddevice numpy
```

### ✅ 第二步：啟動 Python 錄音伺服器

```bash
python server.py
```

若一切順利，會看到以下訊息：

```
WebSocket server listening on ws://localhost:5678
```

### ✅ 第三步：開啟瀏覽器播放頁面

* 使用瀏覽器開啟 `index.html`

  * ✅ 建議使用 Chrome 或 Firefox
  * ✅ 若遇無法播放，可點擊頁面以啟用 AudioContext
* 畫面上會顯示「已連線」，你就會開始聽到自己說話的聲音！

---

## 📁 專案結構

```
your-folder/
├── server.py       ← Python 音訊伺服器（錄音 + 傳送）
└── index.html      ← 瀏覽器前端介面（接收 + 播放）
```

---

## 🔬 技術重點整理（學習筆記）

| 部分    | 技術與重點                                      |
| ----- | ------------------------------------------ |
| 麥克風錄音 | 使用 `sounddevice.InputStream` 錄音，16-bit PCM |
| 音訊格式  | 固定 16000 Hz 取樣率，int16 格式傳輸                 |
| 傳輸協定  | 使用 `websockets` 建立雙向 WebSocket 通道          |
| 瀏覽器播放 | JavaScript `AudioContext` 解析 int16 並播放     |
| 延遲控制  | 使用固定封包大小（1024 frame）以確保穩定                  |
| 格式轉換  | 將 int16 → float32 以符合 Web Audio 標準         |

---

## 🧩 未來發展方向（TODO）

* 🔁 支援雙向語音傳輸（對話模式）
* 🌍 將伺服器部署到遠端伺服器，實現跨網路語音串流
* 🧠 整合語音轉文字（Speech-to-Text）
* 📈 加入視覺化波形或音量條
* 🧪 加入語音觸發事件（如：聲音超過某分貝時發出警報）

---

## 🙌 作者與靈感

本專案由 eric039eric 建立。
ChatGPT（OpenAI）協助排除 bug、修正音訊邏輯並從零做出這套系統。

---

## 備註

這是我第一次寫出一個能「實際聽到聲音」的作品。
它不只是程式，它是一條把現實聲音變成資料、在網路中傳遞、再被還原出來的 **完整邏輯鏈**。

