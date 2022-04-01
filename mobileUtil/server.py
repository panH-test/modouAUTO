'''
启动appium服务
获取多个设备及执行adb命令
'''
import multiprocessing
import time

from mobileUtil.dos_cmd import DosCmd
from mobileUtil.port import Port
from mobileUtil.write_user_command import WriteUserCommand


class Server:
    def __init__(self):
        self.doscmd = DosCmd()
        self.device_list = self.get_devices()
        # 把写的类进行一个实例化
        self.write_file = WriteUserCommand()

    def get_devices(self):
        '''
        获取设备的list
        :return:
        '''
        devices_list = []
        result_list = self.doscmd.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                # print(i)
                if 'List' in i:
                    continue
                device_info = i.split('\t')
                if device_info[1] == 'device':
                    devices_list.append(device_info[0])
            return devices_list
    def create_port_list(self,start_port):
        '''
        创建端口bp port
        :param start_port:
        :return:
        '''
        port = Port()
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self,i):
        '''
        构造开启appium服务的命令
        appium -p 4723 -bp 4800 -U 127.0.0.1:62001
        i:0,1,2
        :return:
        '''
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        command = "appium -p"+str(appium_port_list[i])+"-bp" + \
                  str(bootstrap_port_list[i])+"-U" + device_list[i]
        command_list.append(command)
        # 把设备的相关信息写到yml文件里面userconfig.yml
        self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))
        return command_list

    def start_server(self, i):
        '''
        启动服务
        :return:
        '''
        self.start_list = self.create_command_list(i)
        # ['appium -p4700-bp4900-U127.0.0.1:62025']
        print(self.start_list)
        self.doscmd.excute_cmd(self.start_list[0])

    def kill_server(self):
        '''
        杀死服务
        :return:
        '''
        server_list = self.doscmd.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.doscmd.excute_cmd('taskkill -F -PID node.exe')

    def main(self):
        '''
        入口，主程序
        业务逻辑的调用 都会在这里面去调用
        1.杀死服务
        2.清空数据
        3.遍历设备列表，用多进程实现多任务(任务就是开启的appium服务)
         3.1 遍历设备列表 目的是什么？？
        :return:
        '''
        process_list = []
        # 1.杀死服务
        self.kill_server()
        #2.清空数据
        self.write_file.clear_data()
        # 3.循环遍历
        for i in range(len(self.device_list)):
            # 创建进程：multiprocessing.Process(target=self.start_server, args=(i,))
            #
            # args参数，可有可无，target任务后面的函数决定，如果这个函数有参数的话，
            # args(元组)参数要有，需要传递 return 进程
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            process_list.append(appium_start)
        # 循环遍历进程
        for j in process_list:
            # 启动进程:procee.start()
            j.start()
        time.sleep(25)



if __name__ == '__main__':
    server = Server()
    server.main()
    # server.start_server(0)
    # for i in range(2):
    #     server.create_command_list(i)