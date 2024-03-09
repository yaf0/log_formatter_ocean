# log_formatter.py

import logging
import numpy as np

def setup_logging():
    # 生成一个随机数作为日志文件名的一部分
    random_number = np.random.randint(1000)  # 生成一个0到999之间的随机整数
    log_file_name = f'logfile_{random_number}.log'  # 构造日志文件名

    # 设置日志格式和级别，并将日志输出到文件中
    logging.basicConfig(
        filename=log_file_name,
        format='%(asctime)s - %(levelname)s - %(message)s', 
        level=logging.INFO
    )

    # 添加一个控制台处理程序，用于在控制台上显示日志
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)
