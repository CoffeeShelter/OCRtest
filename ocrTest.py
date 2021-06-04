from googleOCR import detect_text

max_num = [18, 26, 14, 16, 16, 16, 17, 23, 16]
file_num = 1

for m_num in max_num:
    detect_text(file_num, m_num)
    file_num += 1
    print("끝!\n")