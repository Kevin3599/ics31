def calculate_letter_grade(average):
    """根据平均分计算字母等级"""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def course_grade(filename):
    try:
        # 读取输入文件
        with open(filename, 'r') as input_file:
            students = []
            midterm1_sum = 0
            midterm2_sum = 0
            final_sum = 0
            count = 0
            
            # 处理每个学生的数据
            for line in input_file:
                # 分割TSV文件的数据
                last, first, mid1, mid2, final = line.strip().split('\t')
                # 转换成绩为整数
                mid1 = int(mid1)
                mid2 = int(mid2)
                final = int(final)
                
                # 计算平均分
                average = (mid1 + mid2 + final) / 3
                # 获取字母等级
                grade = calculate_letter_grade(average)
                
                # 保存学生信息
                students.append((last, first, mid1, mid2, final, grade))
                
                # 累加考试分数
                midterm1_sum += mid1
                midterm2_sum += mid2
                final_sum += final
                count += 1
        
        # 计算平均分
        midterm1_avg = midterm1_sum / count
        midterm2_avg = midterm2_sum / count
        final_avg = final_sum / count
        
        # 写入输出文件
        with open('report.txt', 'w') as output_file:
            # 写入每个学生的信息
            for student in students:
                output_file.write(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\n")
            
            # 写入空行
            output_file.write('\n')
            # 写入平均分
            output_file.write(f"Averages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n")
                
    except FileNotFoundError:
        print(f"Error: Could not open {filename}")

def main():
    filename = input()
    course_grade(filename)

if __name__ == '__main__':
    main()