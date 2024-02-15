import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")
# チャット履歴を初期化
chat = model.start_chat(history=[])

print("チャットボットです。何か質問はありますか？（終了するには「終了」と入力してください）")

while True:
    # ユーザーからの入力を受け取る
    user_input = input("質問内容を入力してください: ")

    # 終了条件
    if user_input == "終了":
        print("チャットを終了します。またのお越しを！")
        break
    
    # チャットの応答
    response = chat.send_message(user_input)
    print(response.text)