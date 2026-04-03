import subprocess

#準備輸入資料
input_data = "\n".join([str(i) for i in range(1, 11)])

tasks = [
    #第一題
    ("test/q1_408/q1_408correct.py", "test/q1_408/q1_408answer.py", "Q1 練習檔A ", input_data),
    ("test/q1_408/q1_408wrong.py", "test/q1_408/q1_408answer.py", "Q1 練習檔B", input_data), 
    # 第二題
    ("test/q2_602/q2_602correct.py", "test/q2_602/q2_602answer.py", "Q2 練習檔A", input_data),
    ("test/q2_602/q2_602wrong.py", "test/q2_602/q2_602answer.py", "Q2 練習檔B", input_data), 
    # 第三題 (第 9 類題目)
    ("test/q3_904/q3_904correct.py", "test/q3_904/q3_904answer.py", "Q3 練習檔A", input_data),
    ("test/q3_904/q3_904wrong.py", "test/q3_904/q3_904answer.py", "Q3 練習檔B", input_data), 
]
print("=== 全功能判定系統 (含檔案內容比對) ===\n")

for stu, ans, label, val in tasks:
    is_ok = False # 初始化
    try:
        # 先執行學生的檔案
        res_stu = subprocess.run(['python', stu], capture_output=True, text=True, input=val)
        
        # 普通題：正常比對
        res_ans = subprocess.run(['python', ans], capture_output=True, text=True, input=val)
        is_ok = (res_stu.stdout.strip() == res_ans.stdout.strip())
            
    except Exception:
        is_ok = False

    # 4. 輸出
    status = "正確 ✅" if is_ok else "錯誤 ❌"
    print(f"【{label}】 判定結果: {status}")
    print("-" * 40)