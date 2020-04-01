import os
import json

def mk_dir_write_content(file_name_type,writer_type,writer_content,open_mode,file_path =None):
        '''
        :param file_name_type: 文件名称+文件扩展名  例如 aaa.info bbb.txt jd.cookies
        :param writer_type: 写入方式‘w’和‘j’，w代表writer  j代表json
        :param writer_content: 写入的内容
        :param file_path: 文件存放地址，
                例如d://      d:/abc/
                如果没有就自动创建存放在，默认地址为该工程下NEW_file_path目录
        :param open_mode: 
                writer=='w'，可以输入w，a，wb，ab
                writer=='j'，可以输入w，a
                    w是清空再写入
                    a是在原内容后追加写入
                    wb、ab是用于存放二进制文件，例如图片、音乐等
        :return: 
        '''
        writer_type=writer_type.lower()
        open_mode=open_mode.lower()

        if file_path is None:
            project_path= os.path.dirname(os.getcwd())
            file_path=project_path+'/Document/'
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            writer_type_judge(file_path,file_name_type,writer_type,writer_content,open_mode)
        else:
            writer_type_judge(file_path, file_name_type, writer_type, writer_content, open_mode)
        print(file_path)
        print(open_mode)


def writer_type_judge(file_path,filename_filetype,writer_type,writer_content,open_mode):
    if writer_type == 'w':
        if open_mode =='w':
            with open(file_path + filename_filetype, open_mode)as c:
                c.write(writer_content)
        elif open_mode =='a':
            with open(file_path + filename_filetype, open_mode)as c:
                c.write(writer_content)
        # elif open_mode =='wb':
        #     with open(file_path + filename_filetype, open_mode)as c:
        #         c.write(writer_content)
        # elif open_mode == 'ab':
        #     with open(file_path + filename_filetype, open_mode)as c:
        #         c.write(writer_content)

    elif writer_type=='j':
        if open_mode =='w':
            with open(file_path +filename_filetype, open_mode)as c:
                json.dump(writer_content, c)
        elif open_mode =='a':
            with open(file_path + filename_filetype, open_mode)as c:
                json.dump(writer_content, c)
        # elif open_mode =='wb':
        #     with open(file_path + filename + '.' + filetype, open_mode)as c:
        #         json.dump(writer_content, c)
        # elif open_mode == 'ab':
        #     with open(file_path + filename + '.' + filetype, open_mode)as c:
        #         json.dump(writer_content, c)





