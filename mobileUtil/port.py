'''
1.判断端口是否被占用
 1.1 如果端口被占用了  有返回值
 1.2 如果端口没有被占用  没有返回值
'''
from mobileUtil.dos_cmd import DosCmd


class Port:
    def port_is_used(self,port_num):
        '''

        :param port_num:
        :return:
        '''
        self.dos = DosCmd()
        command = 'netstat -ano | findstr '+str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result)>0:
            # 被占用
            flag = True
        else:
            # 没有被占用
            flag = False
        return flag

    def create_port_list(self,start_port,device_list):
        '''
        生成可用端口
        :param start_port:
        :param device_list: 设备的list
        :return:
        '''
        port_list = []
        if len(device_list) != 0:
            # 需要去创建端口
            while len(port_list) != len(device_list):
                # 端口是否可用
                if self.port_is_used(start_port) == False:
                    # # 没有被占用
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            print('生成端口失败')
            return None


if __name__ == '__main__':
    port = Port()
    li = ['1','2','3']
    print(port.create_port_list(4723, li))