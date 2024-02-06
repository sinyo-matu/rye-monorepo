# rye-workspace

[rye](https://rye-up.com/)を使った、monorepo の Python プロジェクトのサンプルです。
`lib`プロジェクトと`app1`プロジェクトの２つのプロジェクトがあります。
`lib`はレシピを生成するサービスを想定したドメインをを持ち、`app1`はサービスホストする fastapi サーバーです。

## プロジェクト構成

```text
rye-monorepo
├── app1 <- fastapi サーバー
│   ├── src
│   │   ├── app1
│   │   │   ├── __init__.py
│   │   │   └── app.py
│   └── pyproject.toml
│
├── lib <- レシピ生成サービスドメインlib
│   ├── src
│   │   ├── application
│   │   │   ├── __init__.py
│   │   │   └── generate_recipe_then_save.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   └── recipe.py
│   │   └── infrastructure
│   │       ├── __init__.py
│   │       └── openai_client
│   │           └── __init__.py
│   └── pyproject.toml
│
├── pyproject.toml
├── requirements.lock
└── requirements-dev.lock
```

## セットアップ

### 1. rye のインストール

```bash
curl -sSf https://rye-up.com/get | bash
```

### このリポジトリをクローン

```bash
git clone　https://github.com/sinyo-matu/rye-monorepo
```

### 3. プロジェクトのセットアップ

```bash
rye sync
```

## プロジェクトの実行

```bash
rye run app1
```

```bash
curl localhost:8080 -X POST -H "Content-Type: application/json" -d '{"description": "ぶどうをふんだんに使ったカレー"}'
```
