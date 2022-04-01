import yaml
class WriteUserCommand:
    def read_data(self):
        '''
        读取数据
        :return: data
        '''
        with open('../data/userconfig.yml') as f:
            #绝对路径   C:\Users\86133\.PyCharmCE2017.2\modou\data\userconfig.yml
            #相对路径   '../data/userconfig.yml'
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data
    def get_value(self,section,key):
        '''
        获取yml文件指定user_inf里对应key的值
        :param section: user_info_0
        :param key: bp、port、devicename
        :return: bp\port\devicename ->value
        '''
        data = self.read_data()
        try:
            uinfo = data.get(section)
            value = uinfo.get(key)
            return value
        except:
            print('没有可用设备')
            return None

    def write_data(self,i,devicename,bp,port):
        '''
        yml 写入数据
        :param i: user_info index
        :param devicename:
        :param bp:
        :param port:
        :return:
        '''
        data = self.join_data(i,devicename,bp,port)
        with open('../data/userconfig.yml','a') as f:
            yaml.dump(data,f)

    def join_data(self,i,device,bp,port):
        '''

        :param i:
        :param device:
        :param bp:
        :param port:
        :return:
        '''
        data = {
            'user_info_'+str(i):{
                'devicename':device,
                'bp':bp,
                'port':port
            }

        }
        return data

    def get_file_lines(self):
        '''
        获取有几个设备
        :return:
        '''
        data = self.read_data()
        return len(data)

    def clear_data(self):
        '''
        清除yaml数据,全清
        :return:
        '''
        with open('../data/userconfig.yml','w') as f:
            f.truncate()


if __name__ == '__main__':
    se = WriteUserCommand()
    se.clear_data()
    se.write_data(0,'MYQUT20116024960','bp','4723')
    print(se.get_file_lines())

