# PDFSplitter

A simple Python utility to split large PDF files into chunks of 100 pages each, with sequential naming.

## Overview

With the increase in large PDF files, it can be cumbersome to manage and share them. PDFSplitter is a handy utility to break down large PDFs into smaller, manageable chunks of 100 pages each.

## Installation

1. Clone the repository:
```
git clone https://github.com/daishir0/PDFSplitter.git
```

2. Navigate to the cloned directory and install the required packages:
```
cd PDFSplitter
pip install -r requirements.txt
```

## Usage

To split a PDF, simply run:
```
python main.py <path_to_pdf_file>
```

## Notes

- The splitted PDF files will be saved in the same directory as the original PDF.
- Ensure you have appropriate permissions for reading the source PDF and writing to the destination directory.

## License

This project is licensed under the MIT License.

---

# PDFSplitter（日本語）

大きなPDFファイルを100ページごとのチャンクに分割するシンプルなPythonユーティリティです。連番命名が可能です。

## 概要

大きなPDFファイルの増加に伴い、それらを管理・共有するのが面倒になることがあります。PDFSplitterは、大きなPDFを100ページごとの小さなチャンクに分割するための便利なユーティリティです。

## インストール方法

1. リポジトリをクローンします:
```
git clone https://github.com/daishir0/PDFSplitter.git
```

2. クローンしたディレクトリに移動し、必要なパッケージをインストールします:
```
cd PDFSplitter
pip install -r requirements.txt
```

## 使い方

PDFを分割するには、以下のコマンドを実行します:
```
python main.py <pdfファイルへのパス>
```

## 注意点

- 分割されたPDFファイルは、元のPDFと同じディレクトリに保存されます。
- ソースPDFを読み取り、目的のディレクトリに書き込むための適切な権限があることを確認してください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。
