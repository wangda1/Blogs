#coding:utf8

import os
import time
import datetime

blog_path = 'C:/Users/wangc/Desktop/Blogs/blog-hexo/source/_posts/'

# 对一个文件夹下的文件操作
# 输出形式为： {'file_path': [dir1, dir2, dir3]}
# root 请务必以 '/' 结尾
file_dict = {}

def search(root):

    items = os.listdir(root)

    for item in items:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            search(path)
        # 找到 .md 文件
        elif path.endswith('.md'):
            # print(path)
            dir_list = []
            dir_path = path.replace(blog_path, '')
            # print(dir_path)
            dir_list = dir_path.split('\\')
            # print(dir_list)
            file_dict[path] = dir_list
        else:
            continue
# 读取文件的修改时间，并添加时间，标题，标签等信息
def process(file_path, dir_list):
    title_ = dir_list[-1].split('.')[0]
    time_ = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))
    dirs_ = dir_list[:-1]
    print(title_)
    print(time_)
    print(dirs_)
    with open(file_path, 'r+', encoding='UTF-8') as f:
        old_data = f.read()
        f.seek(0)
        f.writelines('---\n')
        f.writelines('title: {}\n'.format(title_))
        f.writelines('date: {}\n'.format(time_))
        f.writelines('categories:\n')
        for d in dirs_:
            f.writelines('- {}\n'.format(d))
        f.writelines('tags:\n')
        for d in dirs_:
            f.writelines('- {}\n'.format(d))
        f.writelines('---\n\n')
        f.write(old_data)


if __name__ == '__main__':
    search(blog_path)
    for k, v in file_dict.items():
        print('processing:   {}'.format(k))
        process(k ,v)
    # process('C:/Users/wangc/Desktop/Blogs/blog-hexo/source/_posts/SQL\\SqlInjection.md', ['SQL', 'SqlInjection.md'])
