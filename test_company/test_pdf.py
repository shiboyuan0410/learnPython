# -*- codeing = utf-8 -*-
import re  # 正则表达式，进行文字匹配`
import pdfplumber

# 读取pdf 识别关键字
def search_text(pdf_path, search_term):
    with pdfplumber.open(pdf_path) as pdf:
        results = []
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            matches = re.finditer(search_term, text, re.IGNORECASE)
            for match in matches:
                results.append({
                    'page': i + 1,
                    'text': match.group(),
                    'position': match.start()
                })
    return results

if __name__ == "__main__":  # 当程序执行时
    # 调用函数

    pdf_path = "D:/ideaPycharmProject/learnPython/test_company/pdf/2c983761953542f0915581cd80ec8d91.pdf"
    search_term = "机箱"
    search_results = search_text(pdf_path, search_term)
    for result in search_results:
        print(f"Found '{result['text']}' on page {result['page']} at position {result['position']}")
    print("爬取完毕！")
