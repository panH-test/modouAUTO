import os
'''
主要封装两个dos命令
1.执行需要获取结果的命令行
2.执行不需要获取结果的命令行
'''
class DosCmd:
    def excute_cmd(self,command):
        '''
        不需要结果，只运行就可以
        :return:
        '''
        os.system(command)

    def excute_cmd_result(self,command):
        '''
        需要收集结果的
        :param command:
        :return:
        '''
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            # print(i)
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list


if __name__ == '__main__':
    print(DosCmd().excute_cmd_result('adb devices'))