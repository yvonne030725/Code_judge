# 判定系統 (Code Judger)
自製程式碼評判工具，作為 `compare.bat` 的替代品，透過自動化驗證 Python 腳本的輸出結果，告別手動對答案的繁瑣過程。

## 功能 (Key Features)
* **比對輸出**：比較兩個程式的螢幕輸出是否一致。
* **Safety**：設定 `timeout` 機制，避免程式陷入無限迴圈。

## 執行方式
確認 Python 已安裝後，在專案根目錄執行：
```bash
python judge.py
```

執行後會自動比對所有題目並顯示判定結果。

## 專案結構
```
Code_judge/
├── judge.py                        # 主程式，負責執行比對所有題目
├── images/
│   └── screenshot.png                  
├── test/
│   ├── q1_408/                     # 第一題
│   │   ├── q1_408correct.py        # 練習檔（正確版本）
│   │   ├── q1_408wrong.py          # 練習檔（錯誤版本）
│   │   └── q1_408answer.py         # 標準答案
│   ├── q2_602/                     # 第二題
│   │   ├── q2_602correct.py        # 練習檔（正確版本）
│   │   ├── q2_602wrong.py          # 練習檔（錯誤版本）
│   │   └── q2_602answer.py         # 標準答案
│   └── q3_904/                     # 第三題（第 9 類，讀取檔案題）
│       ├── q3_904correct.py        # 練習檔（正確版本）
│       ├── q3_904wrong.py          # 練習檔（錯誤版本）
│       ├── q3_904answer.py         # 標準答案
│       └── q3_904_read.txt         # 題目所需的輸入資料檔
└── README.md                       # 專案說明文件
```
## 套件列表 (Dependencies)
僅使用 Python 內建套件，無需額外安裝。
- **Python** 3.10+
- **subprocess**（內建）

## 成果 (Demo Results)
![執行結果截圖](images/screenshot.png)

[專案操作演示影片](https://youtu.be/yMp2BNcLM78)
