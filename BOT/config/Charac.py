
from src.classes.Config import Config

config_file = open('config/env')
config = Config(file=config_file)
config_file.close()


os = config.get_param('os')

if os == 'windows':
    import wmi
    computer = wmi.WMI()
    computer_info = computer.Win32_ComputerSystem()[0]
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]
    gpu_info = computer.Win32_VideoController()[0]

    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576

    characteristics = 'OS Name: {0}'.format(os_info.name) +'\n' +'OS Version: {0}'.format(os_version) + '\n' + 'CPU: {0}'.format(proc_info.Name) + '\n' + 'RAM: {0} GB'.format(system_ram) + '\n' + 'Graphics Card: {0}'.format(gpu_info.Name)
