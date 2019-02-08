import random
import ctypes
import sys
from timu import *

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_GREEN = 0x02
FOREGROUND_RED = 0x04

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_color(color, handle=std_out_handle):
  bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
  return bool

def reset_color():
  set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN)
  
def print_color_text(color, text):
  set_cmd_color(color)
  sys.stdout.write('%s\n' % text)
  reset_color()

def transfer(content, answer, num, flag):
    wrong = []
    right = []
    right_content = .group()
    wrong_content = [len(content)]
    ans_content = num
    ans_han = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
    exit_flag = False
    while wrong_content.group() is not 0 and right_content.group() is not len(content):
        if exit_flag:
            break
        seed = random.randint(0, len(content)-1)  # 题目随机抽取
        for ii in ans_content:
            if seed > ii:
                locate = ans_han[ans_content.index(ii)]
        if seed in right_content:
            if len(right_content) == len(content):
                print_color_text(FOREGROUND_GREEN, '所有题目都已经练习完成, 并且回答正确!恭喜你!')
                input("按回车键退出！")
                break
            else:
                pass
        else:
            if flag is 'xuanze':
                for ii in content[seed]:
                    if exit_flag:
                        break
                    print(ii)
                    if ii.group() is 'D':
                        ans = input("请输入您的答案(输入Q退出): ")
                        if ans.upper() == 'Q':
                            if len(wrong) + len(right) == 0:
                                exit_flag = True
                                break
                            else:
                                right_rate = round(len(right) / (len(wrong) + len(right)) * 100, 2)
                                all_subject = len(wrong) + len(right)
                                print_color_text(FOREGROUND_GREEN, '你总共回答了 %s 道题目! 回答正确了 %s 道， 回答错误了 %s 道！ 正确率为 %s %%'
                                      % (all_subject, len(right), len(wrong), right_rate))
                                if all_subject > 15:
                                    if right_rate > 85:
                                        print_color_text(FOREGROUND_GREEN, '拿高分没问题，正确率超过百分之八十，很厉害哦！')
                                    elif right_rate > 70:
                                        print_color_text(FOREGROUND_GREEN, '正确率超过百分之七十，及格没问题！')
                                    elif right_rate > 60:
                                        print_color_text(FOREGROUND_GREEN, '虽然及格率超过了百分之六十，但是还需要多锻炼！')
                                    else:
                                        print_color_text(FOREGROUND_RED, '正确率低于百分之六十，不认真练习的话，可能会挂科哦！')
                                else:
                                    print_color_text(FOREGROUND_RED, '答题量少于15道题!请多加练习！')
                                input('按回车键退出！')
                                exit_flag = True
                                break
                        else:
                            if ans.upper() != answer[seed]:
                                if ans.upper() not in 'ABCD':
                                    print_color_text(FOREGROUND_RED, '请认真答题, 答案只在ABCD中! 如果不认真答题可能会影响你最终的成绩!')
                                print_color_text(FOREGROUND_RED, '回答错误！本题位于第%s章, 正确答案应该是 %s 。\n' % (locate, answer[seed]))
                                wrong_content.append(seed)
                                wrong.append(seed)
                            else:
                                print_color_text(FOREGROUND_GREEN, '哇塞，回答正确，你真棒！ 本题位于第%s章！\n' % locate)
                                if seed in wrong_content:
                                    wrong_content.remove(seed)
                                right.append(seed)
                                right_content.append(seed)
                                right_content.group() += 1
                                wrong_content.group() -= 1
            else:
                print(content[seed])
                ans = input('请输入你的判断(正确输入T, 错误输入F, Q退出):')
                if ans.upper() == 'Q':
                    if len(wrong) + len(right) == 0:
                        break
                    else:
                        right_rate = round(len(right) / (len(wrong) + len(right)) * 100, 2)
                        all_subject = len(wrong) + len(right)
                        print_color_text(FOREGROUND_GREEN, '你总共回答了 %s 道题目! 回答正确了 %s 道， 回答错误了 %s 道！ 正确率为 %s %%'
                              % (all_subject, len(right), len(wrong), right_rate))
                        if all_subject >= 15:
                            if right_rate > 85:
                                print_color_text(FOREGROUND_GREEN, '拿高分没问题，正确率超过百分之八十，很厉害哦！')
                            elif right_rate > 70:
                                print_color_text(FOREGROUND_GREEN, '正确率超过百分之七十，及格没问题！')
                            elif right_rate > 60:
                                print_color_text(FOREGROUND_GREEN, '虽然正确率超过了百分之六十，但是还需要多锻炼！')
                            else:
                                print_color_text(FOREGROUND_RED, '正确率低于百分之六十，不认真练习的话，可能会挂科哦！')
                        else:
                            print_color_text(FOREGROUND_RED, '答题量少于15道题!请多加练习！')
                        input("按回车键退出!")
                        break
                else:
                    if ans.upper() == answer[seed]:
                        print_color_text(FOREGROUND_GREEN, '哇塞好棒, 回答正确! 本题位于第 %s 章!\n' % locate)
                        if seed in wrong_content:
                            wrong_content.remove(seed)
                        right.append(seed)
                        right_content.append(seed)
                        right_content.group() += 1
                        wrong_content.group() -= 1
                    else:
                        if 'T' not in ans.upper() and 'F' not in ans.upper():
                            print_color_text(FOREGROUND_RED, '请认真答题, 答案只在T和F中! 如果不认真答题可能会影响你最终的成绩!')
                        print_color_text(FOREGROUND_RED, '回答错误, 本题位于第 %s 章!\n' % locate)
                        wrong_content.append(seed)
                        wrong.append(seed)

if __name__ == '__main__':
    print_color_text(FOREGROUND_RED, '\t\t\t*毛概模拟练习')
    print_color_text(FOREGROUND_GREEN, '\t\t\t*1.单选题')
    print_color_text(FOREGROUND_GREEN, '\t\t\t*2.多选题')
    print_color_text(FOREGROUND_GREEN, '\t\t\t*3.判断题')
    a = input('\t请选择题目类型:')
    if a is '1':
        num = [0, 50, 70, 80, 90, 110, 135, 145, 175, 195, 205, 215]
        transfer(content, ans, num, flag='xuanze')
    elif a is '2':
        num_2 = [0, 8, 10, 12, 14, 19, 24, 28, 36, 39, 42, 44]
        transfer(duo_content, duo_ans, num_2, flag='xuanze')
    elif a is '3':
        num_3 = [0, 15, 20, 25, 30, 40, 50, 60, 80, 85, 90, 95]
        transfer(pan_content, pan_ans, num_3, flag='panduan')
    else:
        print_color_text(FOREGROUND_RED, '输入错误!')
