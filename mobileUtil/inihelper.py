import configparser
import os



class IniHelper(object):
    def __init__(self):
        '''
        具体的配置文件在哪一个文件夹里面
        '''
        self.source_folder = 'pageObject'

    @staticmethod
    def get_file_path(folder_name,file_name):
        '''

        :param folder_name: 文件夹的名字
        :param file_name: 文件的名字
        :return: 具体ini文件的绝对路径
        '''
        source_path = os.path.abspath('..')
        folder_path = os.path.join(source_path,folder_name)
        file_path = os.path.join(folder_path, file_name)
        return file_path

    def get_source_file(self,filename):
        '''
         获取读取完init文件的config
        :param filename: 文件名字
        :return: config
        '''
        try:
            config = configparser.ConfigParser()
            file_path = self.get_file_path(self.source_folder,filename)
            config.read(file_path, encoding='utf-8')
            return config
        except Exception as e:
            print('read config file error：'+str(e))

    def get_value(self,filename,section,key):
        '''

        :return:
        '''
        try:
            config = self.get_source_file(filename)
            value = config.get(section,key)
            return value
        except Exception as e:
            print('get value fail：' + str(e))


if __name__ == '__main__':
    print(IniHelper().get_value('modouPage.ini', 'Button', '我的'))

