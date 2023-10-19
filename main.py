import sys
import PyPDF2
import os

def split_pdf(file_name):
    # PDFのディレクトリパスを取得
    output_dir = os.path.dirname(file_name)
    if output_dir == "":
        output_dir = "."

    # PDFを開く
    with open(file_name, 'rb') as f:
        reader = PyPDF2.PdfReader(f)

        total_pages = len(reader.pages)
        split_count = total_pages // 100 + (1 if total_pages % 100 else 0)

        for i in range(split_count):
            writer = PyPDF2.PdfWriter()

            start_page = i * 100
            end_page = min((i + 1) * 100, total_pages)

            for j in range(start_page, end_page):
                writer.add_page(reader.pages[j]) 

            # PDFのディレクトリパスに連番付きのファイル名を追加
            output_file_name = os.path.join(output_dir, f"{os.path.basename(file_name).split('.pdf')[0]}_{i + 1}.pdf")
            with open(output_file_name, 'wb') as output_file:
                writer.write(output_file)

            print(f"Saved {output_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <pdf_file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    split_pdf(file_name)
