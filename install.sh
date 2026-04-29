#!/bin/bash

echo "Обновляем систему..."
sudo apt update -y

echo "Устанавливаем Python, pip и venv..."
sudo apt install -y python3 python3-pip python3-venv

echo "Создаем виртуальное окружение..."
python3 -m venv venv

echo "Активируем окружение..."
source venv/bin/activate

echo "Устанавливаем зависимости..."
pip install -r requirements.txt

echo "Запускаем приложение..."
python app.py

rm -rf venv
