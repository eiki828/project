#!/usr/bin/env python
import os
import sys

def run_celery():
    # Celery タスクを非同期に実行
    from classroom.views.task import detect_drowsiness  # ここで your_app を実際の Django アプリケーションの名前に変更し、detect_drowsiness を実際の Celery タスクの関数名に変更
    detect_drowsiness.delay()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_school.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django のインポートに失敗しました。Django がインストールされていること、"
            "および PYTHONPATH 環境変数に追加されていることを確認してください。"
            "仮想環境をアクティベートし忘れていないかも確認してください。"
        ) from exc

    # ここで run_celery 関数を呼び出す
    run_celery()

    execute_from_command_line(sys.argv)
