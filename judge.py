import subprocess
import os

input_data = "\n".join([str(i) for i in range(1, 11)])

tasks = [
    #第一題
    ("test/q1_408/q1_408correct.py", "test/q1_408/q1_408answer.py", "Q1 練習檔A ", "text", input_data),
    ("test/q1_408/q1_408wrong.py", "test/q1_408/q1_408answer.py", "Q1 練習檔B", "text", input_data), 
    # 第二題
    ("test/q2_602/q2_602correct.py", "test/q2_602/q2_602answer.py", "Q2 練習檔A", "text", input_data),
    ("test/q2_602/q2_602wrong.py", "test/q2_602/q2_602answer.py", "Q2 練習檔B", "text", input_data), 
    # 第三題 (第 9 類題目)
    ("test/q3_904/q3_904correct.py", "test/q3_904/q3_904answer.py", "Q3 練習檔A", "text", input_data),
    ("test/q3_904/q3_904wrong.py", "test/q3_904/q3_904answer.py", "Q3 練習檔B", "text", input_data), 
]
print("=== 全功能判定系統 (含檔案內容比對) ===\n")

# 3. 進入比對循環
for stu, ans, label, mode, val in tasks:
    is_ok = False # 初始化
    try:
        # 先執行學生的檔案
        res_stu = subprocess.run(['python', stu], capture_output=True, text=True, input=val, timeout=5)
        
        if mode == "file":
            # --- 第 9 類：學生檔跑完，立刻讀取它產生的 write.txt ---
            if os.path.exists("write.txt"):
                with open("write.txt", "r", encoding="utf-8") as f:
                    content = f.read().strip()
                
                # 執行答案檔，拿答案檔的螢幕輸出 (res_ans.stdout) 當標準
                res_ans = subprocess.run(['python', ans], capture_output=True, text=True, input=val, timeout=5)
                
                # 比對：學生的檔案內容 vs 答案檔的螢幕輸出
                is_ok = (content == res_ans.stdout.strip())
                
                # 為了下次測試乾淨，讀完就把 write.txt 刪掉
                os.remove("write.txt")
            else:
                is_ok = False
        else:
            # 普通題：正常比對
            res_ans = subprocess.run(['python', ans], capture_output=True, text=True, input=val, timeout=5)
            is_ok = (res_stu.stdout.strip() == res_ans.stdout.strip())
            
    except Exception:
        is_ok = False

    # 4. 輸出
    status = "正確 ✅" if is_ok else "錯誤 ❌"
    print(f"【{label}】 判定結果: {status}")
    print("-" * 40)