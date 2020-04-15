import pandas as pd
from src.FrequencyType import Freq
from src.ConstantType import *

class RowData:
    def __init__(self, df_input, para, data, pd_read_flag):
        self.df_input = df_input
        self.para = para
        self.data = data
        self.pd_read_flag = pd_read_flag

    #################################################################################


    def read_parameters(self):
        return self.df_input, self.para, self.data, self.pd_read_flag

    # 序号
    def config_number(self, counter):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['序号'] = para['序号'] = df_input['序号'][row]
        else:
            data['序号'] = para['序号'] = counter


    #################################################################################

    # 备注
    def config_remarks(self, remarks):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['备注'] = para['备注'] = df_input['备注'][row]
        else:
            data['备注'] = para['备注'] = remarks


    #################################################################################

    # 区段长度
    def config_sec_length(self, len_zhu, len_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['主串区段长度(m)'] = para['主串区段长度'] = df_input['主串区段长度(m)'][row]
            data['被串区段长度(m)'] = para['被串区段长度'] = df_input['被串区段长度(m)'][row]
        else:
            data['主串区段长度(m)'] = para['主串区段长度'] = len_zhu
            data['被串区段长度(m)'] = para['被串区段长度'] = len_bei

        data['主被发送相对位置'] = off_set_send = 0
        para['offset'] = data['被串区段长度(m)'] - data['主串区段长度(m)'] - off_set_send


    #################################################################################

    # 耦合系数
    def config_mutual_coeff(self, coeff):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['耦合系数'] = para['耦合系数'] = df_input['耦合系数'][row]
        else:
            data['耦合系数'] = para['耦合系数'] = coeff


    #################################################################################

    # 区段频率
    def config_freq(self, frq_zhu, frq_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['主串频率(Hz)'] = para['freq_主'] = freq = df_input['主串频率(Hz)'][row]
            data['被串频率(Hz)'] = para['freq_被'] = df_input['被串频率(Hz)'][row]
        else:
            data['主串频率(Hz)'] = para['freq_主'] = freq = frq_zhu
            data['被串频率(Hz)'] = para['freq_被'] = frq_bei

        data['freq'] = para['freq'] = Freq(freq)


    #################################################################################

    # 电容数量
    def config_c_num(self, cnum_zhu, cnum_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        # data['主串电容数'] = para['主串电容数'] = get_c_num(Freq(data['主串频率']), data['区段长度'])
        # data['被串电容数'] = para['被串电容数'] = get_c_num(Freq(data['被串频率']), data['区段长度'])
        if pd_read_flag:
            data['主串电容数(含TB)'] = para['主串电容数'] = df_input['主串电容数(含TB)'][row]
            data['被串电容数(含TB)'] = para['被串电容数'] = df_input['被串电容数(含TB)'][row]
        else:
            data['主串电容数(含TB)'] = para['主串电容数'] = cnum_zhu
            data['被串电容数(含TB)'] = para['被串电容数'] = cnum_bei


    #################################################################################

    # 电容位置
    def config_c_posi(self, c_pst_zhu, c_pst_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        pd_read_flag = False
        if pd_read_flag:
            data['主串电容(不含TB)位置'] = para['主串电容位置'] = df_input['主串电容(不含TB)位置'][row]
            data['被串电容(不含TB)位置'] = para['被串电容位置'] = df_input['主串电容(不含TB)位置'][row]
        else:
            data['主串电容(不含TB)位置'] = para['主串电容位置'] = c_pst_zhu
            data['被串电容(不含TB)位置'] = para['被串电容位置'] = c_pst_bei

        # hlf_pst = list(np.linspace(0, 650, 15))
        # c_pst = [hlf_pst[num * 2 + 1] - 90 for num in range(7)]
        # c_pst = c_pst[1:-1]
        # data['主串电容(不含TB)位置'] = para['主串电容位置'] = c_pst
        # data['被串电容(不含TB)位置'] = para['被串电容位置'] = c_pst

        pass

    #################################################################################

    # 电容换TB
    def config_c2TB(self, change_flag):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        data['是否全部更换TB'] = change_flag

        if data['是否全部更换TB'] is True:
            # if data['主串频率(Hz)'] == 1700 or data['主串频率(Hz)'] == 2000:
            #     data['主串更换TB'] = para['主串更换TB'] = True
            # if data['被串频率(Hz)'] == 1700 or data['被串频率(Hz)'] == 2000:
            #     data['被串更换TB'] = para['被串更换TB'] = True

            data['主串更换TB'] = para['主串更换TB'] = True
            data['被串更换TB'] = para['被串更换TB'] = True
        else:
            data['主串更换TB'] = para['主串更换TB'] = False
            data['被串更换TB'] = para['被串更换TB'] = False


    #################################################################################

    # 电容容值
    def config_c_value(self, c_val_zhu, c_val_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['主串电容值(μF)'] = c_value1 = df_input['主串电容值(μF)'][row]
            data['被串电容值(μF)'] = c_value2 = df_input['被串电容值(μF)'][row]
        else:
            data['主串电容值(μF)'] = c_value1 = c_val_zhu
            data['被串电容值(μF)'] = c_value2 = c_val_bei

        c_value1 = c_value1 * 1e-6
        c_value2 = c_value2 * 1e-6

        para['Ccmp_z_change_zhu'].rlc_s = {
            1700: [10e-3, None, c_value1],
            2000: [10e-3, None, c_value1],
            2300: [10e-3, None, c_value1],
            2600: [10e-3, None, c_value1]}
        para['Ccmp_z_change_chuan'].rlc_s = {
            1700: [10e-3, None, c_value2],
            2000: [10e-3, None, c_value2],
            2300: [10e-3, None, c_value2],
            2600: [10e-3, None, c_value2]}

        # para['Ccmp_z_change_chuan'].rlc_s = {
        #     1700: [10e-3, 390e-6, 11.9e-6],
        #     2000: [10e-3, 390e-6, 11.9e-6],
        #     2300: [10e-3, 390e-6, 11.9e-6],
        #     2600: [10e-3, 390e-6, 11.9e-6]}

        # data['被串电容值'] = '抑制装置'
        # para['抑制装置电感短路'] = ImpedanceMultiFreq()
        # para['抑制装置电感短路'].rlc_s = {
        #     1700: [10e-3, None, 11.9e-6],
        #     2000: [10e-3, None, 11.9e-6],
        #     2300: [10e-3, None, 11.9e-6],
        #     2600: [10e-3, None, 11.9e-6]}

        # data['换电容位置'] = para['换电容位置'] = cv2
        # data['换电容位置'] = para['换电容位置'] = 0


    #################################################################################

    # 道床电阻
    def config_rd(self, rd_zhu, rd_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        data['道床电阻'] = rd_zhu

        if pd_read_flag:
            data['主串道床电阻(Ω·km)'] = df_input['主串道床电阻(Ω·km)'][row]
            data['被串道床电阻(Ω·km)'] = df_input['被串道床电阻(Ω·km)'][row]
        else:
            data['主串道床电阻(Ω·km)'] = data['道床电阻']
            data['被串道床电阻(Ω·km)'] = data['道床电阻']

        para['主串道床电阻'] = Constant(data['主串道床电阻(Ω·km)'])
        para['被串道床电阻'] = Constant(data['被串道床电阻(Ω·km)'])

        # data['道床电阻最大(Ω·km)'] = 1000
        # data['道床电阻最小(Ω·km)'] = 2

        para['Rd'].value = data['道床电阻']


    #################################################################################

    # 钢轨阻抗
    def config_trk_z(self):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        freq = data['主串频率(Hz)']

        if pd_read_flag:
            data['钢轨电阻(Ω/km)'] = df_input['钢轨电阻(Ω/km)'][row]
            data['钢轨电感(H/km)'] = df_input['钢轨电感(H/km)'][row]
            para['Trk_z'].rlc_s = \
                    {freq: [data['钢轨电阻(Ω/km)'], data['钢轨电感(H/km)'], None]}
        else:
            data['钢轨电阻(Ω/km)'] = round(para['Trk_z'].rlc_s[freq][0], 10)
            data['钢轨电感(H/km)'] = round(para['Trk_z'].rlc_s[freq][1], 10)


        # data['钢轨电阻(Ω/km)'] = round(para['Trk_z'].rlc_s[freq][0], 10)
        # data['钢轨电感(H/km)'] = round(para['Trk_z'].rlc_s[freq][1], 10)

        para['主串钢轨阻抗'] = para['Trk_z']
        para['被串钢轨阻抗'] = para['Trk_z']



        # # data['主串钢轨电阻'] = cv3
        # data['主串钢轨电阻'] = df_input['主串钢轨电阻'][temp_temp]
        #
        # # data['主串钢轨电感'] = cv4
        # data['主串钢轨电感'] = df_input['主串钢轨电感'][temp_temp]
        #
        # # data['被串钢轨电阻'] = 1.558
        # data['被串钢轨电阻'] = df_input['被串钢轨电阻'][temp_temp]
        #
        # # data['被串钢轨电感'] = 1.291e-3
        # data['被串钢轨电感'] = df_input['被串钢轨电感'][temp_temp]
        #
        # para['主串钢轨阻抗'] = ImpedanceMultiFreq()
        # para['主串钢轨阻抗'].rlc_s = \
        #     {data['主串频率']: [data['主串钢轨电阻'], data['主串钢轨电感'], None]}
        # para['被串钢轨阻抗'] = ImpedanceMultiFreq()
        # para['被串钢轨阻抗'].rlc_s = \
        #     {data['主串频率']: [data['被串钢轨电阻'], data['被串钢轨电感'], None]}


    #################################################################################

    # TB模式
    def config_TB_mode(self, tb_mode):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        pd_read_flag = False

        if pd_read_flag:
            data['TB模式'] = flag_tb = df_input['TB模式'][row]
        else:
            data['TB模式'] = flag_tb = tb_mode

        if flag_tb == '双端TB':
            para['TB模式'] = '双'
        elif flag_tb == '发送端单TB':
            para['TB模式'] = '右'
        elif flag_tb == '接收端单TB':
            para['TB模式'] = '左'
        elif flag_tb == '无TB':
            para['TB模式'] = '无'
        else:
            raise KeyboardInterrupt('TB模式错误')


    #################################################################################

    # 发码方向
    def config_sr_mode(self, sr_zhu, sr_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        data['主串发送器位置'] = para['sr_mod_主'] = sr_zhu
        data['被串发送器位置'] = para['sr_mod_被'] = sr_bei

        # # 发码方向
        # if pd_read_flag:
        #     data['发码继电器状态'] = df_input['发码继电器状态'][temp_temp]
        # else:
        #     # data['发码继电器状态'] = 1
        #     data['发码继电器状态'] = 0
        #
        # if data['发码继电器状态'] == 1:
        #     data['被串发送器位置'] = para['sr_mod_被'] = '不发码'
        # elif data['发码继电器状态'] == 0:
        #     data['被串发送器位置'] = para['sr_mod_被'] = '右发'


    #################################################################################

    # 设备拆卸情况
    def config_pop(self, pop_zhu, pop_bei):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        pd_read_flag = False
        if pd_read_flag:
            data['主串拆卸情况'] = para['主串拆卸情况'] = eval(df_input['主串拆卸情况'][row])
            data['被串拆卸情况'] = para['被串拆卸情况'] = eval(df_input['被串拆卸情况'][row])
        else:
            data['主串拆卸情况'] = para['主串拆卸情况'] = pop_zhu
            data['被串拆卸情况'] = para['被串拆卸情况'] = pop_bei


    #################################################################################

    # 电缆参数
    def config_cable_para(self):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        data['电缆电阻最大(Ω/km)'] = 45
        data['电缆电阻最小(Ω/km)'] = 43
        # data['电缆电容最大(F/km)'] = 30e-9
        # data['电缆电容最小(F/km)'] = 26e-9
        data['电缆电容最大(F/km)'] = 28e-9
        data['电缆电容最小(F/km)'] = 28e-9

        para['Cable_R'].value = data['电缆电阻最小(Ω/km)']
        para['Cable_C'].value = data['电缆电容最大(F/km)']


    #################################################################################

    # 电缆长度
    def config_cable_length(self, len_cable):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        pd_read_flag = False
        if pd_read_flag:
            data['电缆长度(km)'] = para['cab_len'] = df_input['电缆长度(km)'][row]
        else:
            data['电缆长度(km)'] = para['cab_len'] = len_cable


    #################################################################################

    # 电缆长度
    def config_cable_length_respectively(self, len_cable):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        pd_read_flag = False
        if pd_read_flag:
            data['电缆长度(km)'] = para['cab_len'] = df_input['电缆长度(km)'][row]
        else:
            data['电缆长度(km)'] = para['cab_len'] = len_cable


    #################################################################################

    # 分路电阻
    def config_r_sht(self, r_sht):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        pd_read_flag = False
        if pd_read_flag:
            data['分路电阻(Ω)'] = para['Rsht_z'] = df_input['分路电阻(Ω)'][row]
        else:
            data['分路电阻(Ω)'] = para['Rsht_z'] = r_sht


    #################################################################################

    # 功出电源
    def config_power(self, send_level, v_power):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['主串电平级'] = para['send_level'] = df_input['主串电平级'][row]
        else:
            data['主串电平级'] = para['send_level'] = send_level

        data['电源电压'] = para['pwr_v_flg'] = v_power


    #################################################################################

    # 分路间隔
    def config_interval(self, interval):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        if pd_read_flag:
            data['分路间隔(m)'] = df_input['分路间隔(m)'][row]
        else:
            data['分路间隔(m)'] = interval

        return data['分路间隔(m)']


    #################################################################################

    # 特殊位置
    def config_sp_posi(self):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        # 极性交叉位置
        data['极性交叉位置'] = para['极性交叉位置'] = []

        # data['特殊位置'] = para['special_point'] = list(np.linspace(0,length + length, 21))
        data['特殊位置'] = para['special_point'] = data['极性交叉位置']

        data['节点选取模式'] = para['节点选取模式'] = '特殊'


    #################################################################################

    # 机车信号
    def config_train_signal(self):
        df_input, para, data, pd_read_flag = self.read_parameters()
        row = 0

        data['最小机车信号位置'] = '-'

        data['机车信号感应系数'] = \
            str(para['机车信号比例V']) + '/' + str(para['机车信号比例I'][para['freq_主']])
        para['机车信号系数值'] = para['机车信号比例V'] / para['机车信号比例I'][para['freq_主']]