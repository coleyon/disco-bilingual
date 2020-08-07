# Description

Translate and respond to messages posted on discord Bot. Translation is done by Google Cloud Translation.

# How to use on discord

**Japanese to English**

    /j2e 日本語メッセージです

**English to Japanese**

    /e2j It's English Messages.

# Requirement

* Python 3.7
* discord.py 1.4.0

# Quick Start

1. [サービスアカウントJSON形式のキーファイルを得て](https://cloud.google.com/translate/docs/setup#using_the_service_account_key_file_in_your_environment)、 `docker-compose.yml` の `GOOGLE_APPLICATION_CREDENTIALS` が示すパスに置く。デフォルトでは `${workspaceFolder}/sa-key.json`.
1. [Discord のサーバーを作る](https://support.discord.com/hc/ja/articles/204849977-%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%81%AE%E4%BD%9C%E6%88%90%E3%81%AE%E4%BB%95%E6%96%B9)
1. [Discord Developer Portal](https://discord.com/developers/applications) 上で、[Botを作ってOAUTH2 URLを得る](https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f)
1. OAUTH2 URL へアクセスして、Botが作ったサーバーに参加することを許可（認証）する
   * https://discord.com/oauth2/authorize?client_id=${CLIENT_ID}&permissions=0&scope=bot

      URLにアクセスすると、次のようにサーバへBOTを参加させて良いかを問われるので、よければ認証する。

      <img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/157638/2b006f68-d8b2-8eb5-81c6-aaa4c6af59cd.jpeg" width=50%>

      ロボットではないこと確認をする。

      <img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/157638/a5e18cbc-14d4-12d5-fdd5-830635c385e1.jpeg" width=50%>

      認証完了。これでサーバにBOTが参加してくる。

      <img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/157638/75b28f89-6090-eca4-0d03-7499aed19590.jpeg" width=50%>

      サーバにBOTが入った事確認をする。

      <img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/157638/7bafcd0c-9d00-2b49-2122-583afe83542d.jpeg">

1. `docker-compose.yml` の `DISCORD_BOT_TOKEN` 環境変数 にBotのトークンを指定する
1. `docker-copose up -d` する


# TODO

Allow translations in more languages.
