import math as m

#Расчет разности фаз
def calculation_fi(f, ti_tu):
    
    fi = [(360 * float(i) * (10 ** 3) * float(j) * (10 ** -6)) for i, j in zip(f, ti_tu)]
    
    return fi  

#Расчет индуктивного сопротивления
def calculation_Xl(f):
    
    L = 0.75 * (10 ** -3)
    
    Xl = [round((2 * m.pi * float(i) * (10 ** 3) * L), 3) for i in f]
    
    return Xl

#Расчет емкостного сопротивления
def calculation_Xc(f):
    
    C = 38 * (10 ** -9)
    
    Xc = [round((1 / (float(i) * (10 ** 3) * 2 * m.pi * C)), 3) for i in f]

    return Xc

#Расчет импеданса
def calculation_Z(f):
    
    R = 74
    Xl = calculation_Xl(f)
    Xc = calculation_Xc(f)
    
    Z = [m.sqrt((R ** 2) + ((float(i) - float(j)) ** 2)) for i, j in zip(Xl, Xc)]
    
    return Z
    
def main():
    
    #Сюда вписывать свою резонансную частоту в кГц
    f_res = 15.852
    mps = [0.3, 0.5, 0.7, 0.9, 1, 1.1, 1.2, 1.5, 2]
    # f, ti_tu = input('fнач - ').split(' '), input('ti-tu - ').split(' ')
    
    #Сюда вписывать данные из таблиц [ti-tu в мкс], [f в кГц]
    # f, ti_tu = [f_res * i for i in mps], [-24.71, -13.02, -7.02, -1.99, 0.255, 1.88, 2.83, 3.61, 3.29]
    f, ti_tu = [], []
    
    fi = calculation_fi(f, ti_tu)
    Xl = calculation_Xl(f)
    Xc = calculation_Xc(f)
    Z = calculation_Z(f)
    
    print(f'Fi, Grd = {fi}\nXl, Ohm = {Xl}\nXc, Ohm = {Xc}\nZ, Ohm = {Z}')

    
    
if __name__ == "__main__":
    main()
    
#10 20 40 60 80 100
#9.08 7.22 4.77 3.49 2.74 2.25
#-22.18 -9.77 -3.78 -1.99 -1.22 -0.81