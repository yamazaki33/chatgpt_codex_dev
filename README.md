# chatgpt_codex_dev

このリポジトリは GUI テスト自動化のサンプルです。`pyautogui` と `Robot Framework` を利用して HMI ツールの動作確認を行うための最小構成を用意しています。

## 内容
- `gui_test_utils.py` : Robot Framework から利用できる簡易 GUI テスト用ライブラリ
- `tests/gui_test.robot` : 上記ライブラリを利用したサンプルテストケース

## 使い方
1. Python 環境に `pyautogui` と `Pillow`、そして Robot Framework をインストールしてください。
2. `robot tests/gui_test.robot` を実行するとサンプルテストが開始されます。
   期待画像 (`expected/sample.png`) を用意しておくと、取得したスクリーンショットとの差分を検証します。

実際のプロジェクトでは HMI ツールの起動処理やより詳細なアクションをキーワードとして追加し、テストシナリオを拡充してください。

