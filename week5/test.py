import os
from shutil import copyfile
# get the current path
dir_path = os.path.dirname(os.path.abspath(__file__))

# get the directory path
dir_abs_pos = os.path.join(dir_path, "non_sample_testcase")
files = os.listdir(dir_abs_pos)

# check if the diff_file exist,
# if exist, delete the content
if os.path.isfile("diff_file.txt"):
    with open("diff_file.txt", 'r+') as f:
        f.truncate(0)

l = []
for file in files:  # 遍歷資料夾
    # if the file is output, then continue
    if file.endswith("out"):
        l.append(file)
        copyfile(dir_abs_pos+"/"+file, file)
        with open(file, "a") as a_file:
            a_file.write("\n")
        continue

# traverse all file
for file in files:  # 遍歷資料夾
    # if the file is output, then continue
    if file.endswith("out"):
        continue
    # open the input test case
    with open(dir_abs_pos+"/"+file) as f:  # 開啟檔案
        input_each = f.read()
    # opent temp file to store the input test case
    with open("temp.txt", "w") as temp:
        temp.write(input_each)
        # get the correct test case since the number isn't ordered
        output_file = file.strip("in")+"out"
        # write in immediately
        temp.flush()
    # input the data from temp and ouput to my_ans
    os.system(f"python3 week5/HW4.py < temp.txt > my_ans.txt")
    # os.system("echo >> my_ans.txt")
    # open the diff_file to write the question number
    with open("diff_file.txt", "a") as diff_file:
        diff_file.write(file+"\n")
    # compare two file and output the result
    os.system(
        f"diff my_ans.txt {output_file} >> diff_file.txt")
    # add the separate line
    with open("diff_file.txt", "a") as diff_file:
        diff_file.write(
            "-------------------------------------------------------\n")
os.remove("temp.txt")
os.remove("my_ans.txt")
for i in range(len(l)):
    os.remove(l[i])
