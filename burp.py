import re
# 定义一个函数提取burp保存的xml文件URL关键参数的函数
def extract_words_from_xml(xml_file_path):
    # 读取XML文件
    with open(xml_file_path, 'r') as file:
        xml_content = file.read()

    # 定义正则匹配
    word_pattern = re.compile(r'\b\w+\b')

    # 使用正则读取文件内容
    words = word_pattern.findall(xml_content)

    return words

# 将文件保存再output.txt
def save_words_to_file(words, output_file_path):
    with open(output_file_path, 'w') as file:
        for word in words:
            file.write(word + '\n')

# xml文件路径
xml_file_path = 'burp.xml'

# 使用上述函数
extracted_words = extract_words_from_xml(xml_file_path)

# 保存
save_words_to_file(extracted_words, 'output.txt')

print("saved to output.txt")
