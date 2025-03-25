# CREA 法人リスト スクレイピングツール

このPythonスクリプトは、CREAの企業検索ページから法人情報を取得し、Googleスプレッドシートに自動で書き込むツールです。

---

## 🔍 機能概要

- CREA掲載企業の法人名、業種、所在地などを自動で取得
- Google Sheets API を利用して、スプレッドシートに出力
- エクセルや営業リスト作成などに活用可能

---

## 💻 使用技術・ライブラリ

- `requests` - Webサイトへのアクセス
- `BeautifulSoup4` - HTML解析
- `pandas` - データ整形
- `gspread` - Googleスプレッドシート連携
- `oauth2client` - 認証用ライブラリ

---

## 🚀 セットアップ手順

### 1. ライブラリのインストール

以下のコマンドで必要なパッケージをインストールしてください：

```bash
pip install requests beautifulsoup4 pandas gspread oauth2client
