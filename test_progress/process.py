import time  # 导入time模块，用于实现时间延迟，模拟耗时操作
import sys  # 导入sys模块，特别是为了使用sys.stdout.write和sys.stdout.flush来直接写入和刷新标准输出


def simple_progress_bar(total, progress,page,totalPage):
    """
    显示一个简单的进度条

    :param total: 进度条的总长度（或总任务量）
    :param progress: 当前进度（已完成的任务量）
    """
    bar_length = 50  # 进度条的长度，这里设置为50个字符
    filled_length = int(round(bar_length * progress / float(total)))  # 计算已完成的进度条长度
    # 注意这里使用了float(total)确保除法结果是浮点数，然后通过round和int转换得到整数长度
    percents = round(100.0 * progress / float(total), 1)  # 计算并格式化当前进度的百分比，保留一位小数
    bar = '=' * filled_length + '-' * (bar_length - filled_length)  # 根据已完成和未完成的长度生成进度条字符串
    # 使用'='表示已完成的进度，'-'表示未完成的进度
    sys.stdout.write(f'\r进度：[{bar}] {percents}%   {page}/{totalPage}页')  # 将进度条信息写回标准输出，\r使光标回到行首
    # 这样新的进度信息就会覆盖旧的进度信息，实现进度条的更新效果
    sys.stdout.flush()  # 刷新标准输出缓冲区，确保进度条信息立即显示


if __name__ == "__main__":  # 当程序执行时
    # 模拟进度
    total = 100  # 设置总任务量为100
    page = 1
    totalPage = 3
    for i in range(1,4):
        for j in range(total + 1):  # 循环从0到total（包含total），即模拟从0%到100%的进度
            simple_progress_bar(total, j,page,totalPage)  # 调用simple_progress_bar函数，传入总任务量和当前进度
            time.sleep(0.1)  # 暂停0.1秒，模拟耗时操作
        print(f"\n完成 {page} !")  # 当循环完成后，打印“完成!”信息，并自动换行
        page += 1
    print("\n完成!")  # 当循环完成后，打印“完成!”信息，并自动换行
