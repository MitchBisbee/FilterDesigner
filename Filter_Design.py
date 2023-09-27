from math import pi,sqrt 
# @author: Mitchell Bisbee
class OrderAndRipple:
    #trying to make a order and ripple class for oder and ripple objects
    def __init__(self,filter_Type ,order,ripple):
    
    def setChebOrderAndRipple(order,ripple):

        if not (isinstance(ripple, (float,int)) and (ripple == 1 or ripple == .1)): #checks if the ripple is correct
                raise ValueError(f"""Invalid argument: Chebyshev ripple must 
                be .1 or 1 got {ripple}""")
            
            if not (isinstance(order,int) and (order >= 2 and order <= 10)):
                raise ValueError(f"""Invalid argument: order must be 
                2,3,4,5,6,7,8,9,10 got {order}""") #checks if the order is corrrect

            order = order
            if ripple == .10:
                if order == 2:
                    fo1 = 1.820
                    self.Q1 = .767
            
                if order == 3:
                    self.fo1 = 1.300
                    self.Q1 = 1.341
                    self.fo2 = .969
                
                if order == 4:
                    self.fo1 = 1.153
                    self.Q1 = 2.183
                    self.fo2 = .789
                    self.Q2 = .619

                if order == 5:
                    self.fo1 = 1.093
                    self.Q1 = 3.282
                    self.fo2 = .797
                    self.Q2 = .915
                    self.fo3 = .539
                
                if order == 6:
                    self.fo1 = 1.063
                    self.Q1 = 4.633
                    self.fo2 = .834
                    self.Q2 = 1.332
                    self.fo3 = .513
                    self.Q3 = .599
                
                if order == 7:
                    self.fo1 = 1.045
                    self.Q1 = 6.233
                    self.fo2 = .868
                    self.Q2 = 1.847
                    self.fo3 = .575
                    self.Q3 = .846
                    self.fo4 = .377
                
                if order == 8:
                    self.fo1 = 1.034
                    self.Q1 = 8.082
                    self.fo2 = .894
                    self.Q2 = 2.453
                    self.fo3 = .645
                    self.Q3 = 1.183
                    self.fo4 = .382
                    self.Q4 =  .593
                
                if order == 9: 
                    self.fo1 = 1.027
                    self.Q1 = 10.178
                    self.fo2 = .913
                    self.Q2 = 3.145
                    self.fo3 = .705
                    self.Q3 = 1.585
                    self.fo4 = .449
                    self.Q4 =  .822
                    self.fo5 = .290
                
                if order == 10: 
                    self.fo1 = 1.022
                    self.Q1 = 12.522
                    self.fo2 = .928
                    self.Q2 = 3.921
                    self.fo3 = .754
                    self.Q3 = 2.044
                    self.fo4 = .524
                    self.Q4 =  1.127
                    self.fo5 = .304
                    self.Q5 = .590
            
            elif ripple == 1:
                if order == 2: 
                    self.fo1 = 1.050
                    self.Q1 = .957
                
                if order == 3: 
                    self.fo1 = .997
                    self.Q1 = 2.018
                    self.fo2 = .494 
                
                if order == 4:
                    self.fo1 = .993
                    self.Q1 = 3.559
                    self.fo2 = .529
                    self.Q2 = .785

                if order == 5:
                    self.fo1 = .994
                    self.Q1 = 5.556
                    self.fo2 = .655
                    self.Q2 = 1.399
                    self.fo3 = .289
                
                if order == 6:
                    self.fo1 = .995
                    self.Q1 = 8.004
                    self.fo2 = .747
                    self.Q2 = 2.198
                    self.fo3 = .353
                    self.Q3 = .761
                
                if order == 7:
                    self.fo1 = .996
                    self.Q1 = 10.899
                    self.fo2 = .808
                    self.Q2 = 3.156
                    self.fo3 = .480
                    self.Q3 = 1.297
                    self.fo4 = .205
                
                if order == 8: 
                    self.fo1 = .997
                    self.Q1 = 14.240
                    self.fo2 = .851
                    self.Q2 = 4.266
                    self.fo3 = .584
                    self.Q3 = 1.956
                    self.fo4 = .265
                    self.Q4 =  .753
                
                if order == 9: 
                    self.fo1 = .998
                    self.Q1 = 18.029
                    self.fo2 = .881
                    self.Q2 = 5.527
                    self.fo3 = .662
                    self.Q3 = 2.713
                    self.fo4 = .377
                    self.Q4 =  1.260
                    self.fo5 = .159
                
                if order == 10: 
                    self.fo1 = .998
                    self.Q1 = 22.263
                    self.fo2 = .902
                    self.Q2 = 6.937
                    self.fo3 = .721
                    self.Q3 = 3.561
                    self.fo4 = .476
                    self.Q4 =  1.864
                    self.fo5 = .212
                    self.Q5 = .749


i = {1: 2, 3:4}


class Chebyshev:
    def __init__(self,ripple,order):
        
        if not (isinstance(ripple, (float,int)) and (ripple == 1 or ripple == .1)): #checks if the ripple is correct
            raise ValueError(f"""Invalid argument: Chebyshev ripple must 
            be .1 or 1 got {ripple}""")
        
        if not (isinstance(order,int) and (order >= 2 and order <= 10)):
            raise ValueError(f"""Invalid argument: order must be 
            2,3,4,5,6,7,8,9,10 got {order}""") #checks if the order is corrrect

        self.order = order
        if ripple == .10:
            if order == 2:
                self.fo1 = 1.820
                self.Q1 = .767
        
            if order == 3:
                self.fo1 = 1.300
                self.Q1 = 1.341
                self.fo2 = .969
            
            if order == 4:
                self.fo1 = 1.153
                self.Q1 = 2.183
                self.fo2 = .789
                self.Q2 = .619

            if order == 5:
                self.fo1 = 1.093
                self.Q1 = 3.282
                self.fo2 = .797
                self.Q2 = .915
                self.fo3 = .539
            
            if order == 6:
                self.fo1 = 1.063
                self.Q1 = 4.633
                self.fo2 = .834
                self.Q2 = 1.332
                self.fo3 = .513
                self.Q3 = .599
            
            if order == 7:
                self.fo1 = 1.045
                self.Q1 = 6.233
                self.fo2 = .868
                self.Q2 = 1.847
                self.fo3 = .575
                self.Q3 = .846
                self.fo4 = .377
            
            if order == 8:
                self.fo1 = 1.034
                self.Q1 = 8.082
                self.fo2 = .894
                self.Q2 = 2.453
                self.fo3 = .645
                self.Q3 = 1.183
                self.fo4 = .382
                self.Q4 =  .593
            
            if order == 9: 
                self.fo1 = 1.027
                self.Q1 = 10.178
                self.fo2 = .913
                self.Q2 = 3.145
                self.fo3 = .705
                self.Q3 = 1.585
                self.fo4 = .449
                self.Q4 =  .822
                self.fo5 = .290
            
            if order == 10: 
                self.fo1 = 1.022
                self.Q1 = 12.522
                self.fo2 = .928
                self.Q2 = 3.921
                self.fo3 = .754
                self.Q3 = 2.044
                self.fo4 = .524
                self.Q4 =  1.127
                self.fo5 = .304
                self.Q5 = .590
        
        elif ripple == 1:
            if order == 2: 
                self.fo1 = 1.050
                self.Q1 = .957
            
            if order == 3: 
                self.fo1 = .997
                self.Q1 = 2.018
                self.fo2 = .494 
            
            if order == 4:
                self.fo1 = .993
                self.Q1 = 3.559
                self.fo2 = .529
                self.Q2 = .785

            if order == 5:
                self.fo1 = .994
                self.Q1 = 5.556
                self.fo2 = .655
                self.Q2 = 1.399
                self.fo3 = .289
            
            if order == 6:
                self.fo1 = .995
                self.Q1 = 8.004
                self.fo2 = .747
                self.Q2 = 2.198
                self.fo3 = .353
                self.Q3 = .761
            
            if order == 7:
                self.fo1 = .996
                self.Q1 = 10.899
                self.fo2 = .808
                self.Q2 = 3.156
                self.fo3 = .480
                self.Q3 = 1.297
                self.fo4 = .205
            
            if order == 8: 
                self.fo1 = .997
                self.Q1 = 14.240
                self.fo2 = .851
                self.Q2 = 4.266
                self.fo3 = .584
                self.Q3 = 1.956
                self.fo4 = .265
                self.Q4 =  .753
            
            if order == 9: 
                self.fo1 = .998
                self.Q1 = 18.029
                self.fo2 = .881
                self.Q2 = 5.527
                self.fo3 = .662
                self.Q3 = 2.713
                self.fo4 = .377
                self.Q4 =  1.260
                self.fo5 = .159
            
            if order == 10: 
                self.fo1 = .998
                self.Q1 = 22.263
                self.fo2 = .902
                self.Q2 = 6.937
                self.fo3 = .721
                self.Q3 = 3.561
                self.fo4 = .476
                self.Q4 =  1.864
                self.fo5 = .212
                self.Q5 = .749
 
    def krc2_LPF(self,f_c,cap):
        '''
           Computes the values for 2nd order krc

           low pass filter using the unity gain technique
           
           f_c = cutoff freq in hertz

           cap = capacitor value in Farads

           returns ---> list 
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c * self.fo1
        w_1 = 2 * pi * f_1
        n_1 = 4 * Q1_squared + 100
        k_1 = (n_1 / (2 * Q1_squared)) - 1
        k_1_squared = k_1 ** 2
        m_1 = k_1 + sqrt(k_1_squared - 1)
        R_1 = 1 / ((sqrt(m_1 * n_1)) * w_1 * cap)
        nC_1 = n_1 * cap
        mR_1 = m_1 * R_1
        
        str1 = "\nLPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"k_1: {k_1}"
        str8 = f"m_1: {m_1}"
        str9 = f"n_1: {n_1}"
        str10 = f"R_1: {R_1} ohms"
        str11 = f"nC_1: {nC_1 * 10**9} nF"
        str12 = f"mR_1: {mR_1} ohms"

        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9)
        print(str10)
        print(str11)
        print(str12)
        
        return [str1,str2,str3,str4,str5,str6,
                str7,str8,str9,str10,str11,str12]

    def krc2_HPF(self,f_c,cap):
        '''
        Computes the values for 2d order krc 
        
        high pass filter design using the unity gain technique.

        Filter design values are for one 2nd order HPF krc circuit. 
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads
        
        returns ---> list
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c / self.fo1
        w = 2 * pi * f_1
        n = 4 * Q1_squared + 100
        m =  n / ((self.Q1 * n + self.Q1)**2)
        R_1 = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
        nC = n * cap
        mR_1 = m * R_1

        str1 = f"\nHPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q_1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"m: {m}"
        str8 = f"n: {n}"
        str9 = f"R_1: {R_1} ohms"
        str10 = f"nC: {nC * 10**9} nF"
        str11 = f"mR_1: {mR_1} ohms"
        
        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9) 
        print(str10)
        print(str11)

        return [str1,str2,str3,str4,str5,
                str6,str7,str8,str9,str10,str11]
        
    def krc3_LPF(self,f_c,cap): 
        '''
        Computes the values for 3rd order krc 
        
        low pass filter design using the unity gain technique.

        Filter design values are for one 2nd order krc LPF circuit 
        
        and one 1st order active LPF. The filters are cascaded

        to create the 3rd order krc design.

        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [ list ] 
        '''
        cap = float(cap)
        f_c = float(f_c)
        
        #2ND order KRC Filter calculations
        Q1_squared = self.Q1 ** 2
        f_1 = f_c * self.fo1
        w_1 = 2 * pi * f_1
        n_1 = 4 * Q1_squared + 100
        k_1 = (n_1 / (2 * Q1_squared)) - 1
        k_1_squared = k_1 ** 2
        m_1 = k_1 + sqrt(k_1_squared - 1)
        R_1 = 1 / ((sqrt(m_1 * n_1)) * w_1 * cap)
        nC_1 = n_1 * cap
        mR_1 = m_1 * R_1

        #first order active LPF calculations
        f_2 = f_c * self.fo2  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)
        
        str1 = "\nLPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"k_1: {k_1}"
        str8 = f"m_1: {m_1}"
        str9 = f"n_1: {n_1}"
        str10 = f"R_1: {R_1} ohms"
        str11 = f"nC_1: {nC_1 * 10**9} nF"
        str12 = f"mR_1: {mR_1} ohms"
        str13 = "\n<-------------------------------->\n"
        
        print("\nLPF KRC_1(2nd Order filter):")
        print(f"Cutoff Frequency: {f_c} Hz")
        print(f"Input Capacitor: {cap * 10**9} nF")
        print(f"Q1: {self.Q1}")
        print(f"fo_1: {self.fo1}")
        print(f"f_1: {f_1} Hz")
        print(f"k_1: {k_1}")
        print(f"m_1: {m_1}")
        print(f"n_1: {n_1}")
        print(f"R_1: {R_1} ohms")
        print(f"nC_1: {nC_1 * 10**9} nF")
        print(f"mR_1: {mR_1} ohms")
        print("\n<-------------------------------->\n")

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [[str1,str2,str3,str4,str5,str6,str7,
                     str8,str9,str10,str11,str12,str13], 
                        [strA,strB,strC,strD,strE,strF,strG]]

    def krc3_HPF(self,f_c,cap):
        '''
        Computes the values for 3rd order krc 
        
        high pass filter design using the unity gain technique.

        Filter design values are for one 2nd order HPF krc circuit 
        
        and one 1st order active HPF. The filters are cascaded

        to create the 3rd order krc design.

        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c / self.fo1
        w = 2 * pi * f_1
        n = 4 * Q1_squared + 100
        m =  n / ((self.Q1 * n + self.Q1)**2)
        R_1 = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
        nC = n * cap
        mR_1 = m * R_1

        #first order active HPF calculations
        f_2 = f_c / self.fo2  #frequency for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        str1 = f"\nHPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q_1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"m: {m}"
        str8 = f"n: {n}"
        str9 = f"R_1: {R_1} ohms"
        str10 = f"nC: {nC * 10**9} nF"
        str11 = f"mR_1: {mR_1} ohms"
        str12 = "\n<-------------------------------->\n"
    
        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9) 
        print(str10)
        print(str11)
        print(str12)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [[str1,str2,str3,str4,str5,str6,str7,
                     str8,str9,str10,str11,str12], 
                    [strA,strB,strC,strD,strE,strF,strG]]

    def krc4_LPF(self,f_c,cap):
        '''
        Computes the values for 4th order krc

        low pass filter using the unity gain technique.

        Filter design values are for two 2nd order KRC circuits

        that will be cascaded to make a 4th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
        
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R

            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
                  
        return out

    def krc4_HPF(self,f_c,cap):
        '''
        Computes the values for 4th order krc

        high pass filter using the unity gain technique
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
            
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out
    
    def krc5_LPF(self,f_c,cap):
        '''
        Computes the values for 5th order krc

        low pass filter using the unity gain technique.

        Filter design values are for two 2nd order LPF krc

        circuits and one 1st order active LPF circuit.

        The filters are cascaded to create the 5th order krc design.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
            
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)

        #first order active LPF calculations
        f_2 = f_c * self.fo3  #frequency used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)
        
        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out,[strA,strB,strC,strD,strE,strF,strG]]

    def krc5_HPF(self,f_c,cap):
        '''
        Computes the values for 5th order krc

        high pass filter using the unity gain technique.

        Filter design values are for two 2nd order HPF krc

        circuits and one 1st order active HPF circuit.

        The filters are cascaded to create the 5th order krc design.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list]
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo3  #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]
    
    def krc6_LPF(self,f_c,cap):
        '''
        Computes the values for 6th order krc

        low pass filter using the unity gain technique.

        Filter design values are for three 2nd order LPF krc

        circuits that will be cascaded to make a 6th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out

    def krc6_HPF(self,f_c,cap):
        '''
        Computes the values for 6th order krc

        high pass filter using the unity gain technique
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out

    def krc7_LPF(self,f_c,cap):
        '''
        Computes the values for 7th order krc

        low pass filter using the unity gain technique.

        Filter design values are for three 2nd order LPF krc

        circuits and one 1st order active LPF circuit.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)

        #first order active LPF calculations
        f_2 = f_c * self.fo4  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out, [strA,strB,strC,strD,strE,strF,strG]]

    def krc7_HPF(self,f_c,cap):
        '''
        Computes the values for 7th order krc

        high pass filter using the unity gain technique.

        Filter design values are for three 2nd order HPF krc

        circuits and one 1st order active HPF circuit.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
            
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo4  #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]

    def krc8_LPF(self,f_c,cap):
        '''
        Computes the values for 8th order krc

        low pass filter using the unity gain technique.

        Filter design values are for four 2nd order LPF krc

        circuits that will be cascaded to make a 8th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out
    
    def krc8_HPF(self,f_c,cap):
        '''
        Computes the values for 8th order krc

        high pass filter using the unity gain technique.

        Filter design values are for four 2nd order HPF krc

        circuits that will be cascaded to make a 8th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out
    
    def krc9_LPF(self,f_c,cap):
        '''
        Computes the values for 9th order krc

        low pass filter using the unity gain technique.

        Filter design values are for four 2nd order LPF krc

        circuits and one 1st order active HPF circuit. The

        circuits are cascaded to make the 9th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list]
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        #first order active LPF calculations
        f_2 = f_c * self.fo5  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out, [strA,strB,strC,strD,strE,strF,strG]]

    def krc9_HPF(self,f_c,cap):
        '''
        Computes the values for 9th order krc

        high pass filter using the unity gain technique.

        Filter design values are for four 2nd order HPF krc

        circuits and one 1st order active HPF circuit. The 

        circuits are cascaded to make the 9th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo5 #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]
    
    def krc10_LPF(self,f_c,cap):
        '''
        Computes the values for 10th order krc

        low pass filter using the unity gain technique.

        Filter design values are for five 2nd order LPF krc

        circuits that will be cascaded to make a 10th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(5):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            if c == 5:
                Q = self.fo5 
                fo = self.Q5
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
            
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out

    def krc10_HPF(self,f_c,cap):
        '''
        Computes the values for 10th order krc

        high pass filter using the unity gain technique.

        Filter design values are for five 2nd order HPF krc

        circuits that will be cascaded to make a 10th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            if c == 5:
                Q = self.fo5 
                fo = self.Q5
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out

class Bessel:
    def __init__(self,order):

        if not (isinstance(order,int) and (order >= 2 and order <= 10)):
            raise ValueError(f"""Invalid argument: order must be 
            2,3,4,5,6,7,8,9,10 got {order}""") #checks if the order is corrrect

        self.order = order

        if order == 2:
            self.fo1 = 1.274
            self.Q1 = .577
    
        if order == 3:
            self.fo1 = 1.453
            self.Q1 = .691
            self.fo2 = 1.327
        
        if order == 4:
            self.fo1 = 1.419    
            self.Q1 = .522
            self.fo2 = 1.591
            self.Q2 = .806

        if order == 5:
            self.fo1 = 1.561
            self.Q1 = .564
            self.fo2 = 1.760
            self.Q2 = .917
            self.fo3 = 1.507
        
        if order == 6:
            self.fo1 = 1.606
            self.Q1 = .510
            self.fo2 = 1.691
            self.Q2 = .611
            self.fo3 = 1.907
            self.Q3 = 1.023
        
        if order == 7:
            self.fo1 = 1.719
            self.Q1 = .533
            self.fo2 = 1.824
            self.Q2 = .661
            self.fo3 = 2.051
            self.Q3 = 1.127
            self.fo4 = 1.685
        
        if order == 8:
            self.fo1 = 1.784
            self.Q1 = .506
            self.fo2 = 1.838
            self.Q2 = .560
            self.fo3 = 1.958
            self.Q3 = .711
            self.fo4 = 2.196
            self.Q4 =  1.226
        
        if order == 9: 
            self.fo1 = 1.880
            self.Q1 = .520
            self.fo2 = 1.949
            self.Q2 = .589
            self.fo3 = 2.081
            self.Q3 = .760
            self.fo4 = 2.324
            self.Q4 =  1.322
            self.fo5 = 1.858
        
        if order == 10: 
            self.fo1 = 1.949
            self.Q1 = .504
            self.fo2 = 1.987
            self.Q2 = .538
            self.fo3 = 2.068
            self.Q3 = .620
            self.fo4 = 2.211
            self.Q4 =  .810
            self.fo5 = 2.485
            self.Q5 = 1.415

    def krc2_LPF(self,f_c,cap):
        '''
           Computes the values for 2nd order krc

           low pass filter using the unity gain technique
           
           f_c = cutoff freq in hertz

           cap = capacitor value in Farads

           returns ---> list 
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c * self.fo1
        w_1 = 2 * pi * f_1
        n_1 = 4 * Q1_squared + 100
        k_1 = (n_1 / (2 * Q1_squared)) - 1
        k_1_squared = k_1 ** 2
        m_1 = k_1 + sqrt(k_1_squared - 1)
        R_1 = 1 / ((sqrt(m_1 * n_1)) * w_1 * cap)
        nC_1 = n_1 * cap
        mR_1 = m_1 * R_1
        
        str1 = "\nLPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"k_1: {k_1}"
        str8 = f"m_1: {m_1}"
        str9 = f"n_1: {n_1}"
        str10 = f"R_1: {R_1} ohms"
        str11 = f"nC_1: {nC_1 * 10**9} nF"
        str12 = f"mR_1: {mR_1} ohms"

        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9)
        print(str10)
        print(str11)
        print(str12)
        
        return [str1,str2,str3,str4,str5,str6,
                str7,str8,str9,str10,str11,str12]

    def krc2_HPF(self,f_c,cap):
        '''
        Computes the values for 2d order krc 
        
        high pass filter design using the unity gain technique.

        Filter design values are for one 2nd order HPF krc circuit. 
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads
        
        returns ---> list
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c / self.fo1
        w = 2 * pi * f_1
        n = 4 * Q1_squared + 100
        m =  n / ((self.Q1 * n + self.Q1)**2)
        R_1 = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
        nC = n * cap
        mR_1 = m * R_1

        str1 = f"\nHPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q_1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"m: {m}"
        str8 = f"n: {n}"
        str9 = f"R_1: {R_1} ohms"
        str10 = f"nC: {nC * 10**9} nF"
        str11 = f"mR_1: {mR_1} ohms"
        
        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9) 
        print(str10)
        print(str11)

        return [str1,str2,str3,str4,str5,
                str6,str7,str8,str9,str10,str11]
        
    def krc3_LPF(self,f_c,cap):
        '''
        Computes the values for 3rd order krc 
        
        low pass filter design using the unity gain technique.

        Filter design values are for one 2nd order krc LPF circuit 
        
        and one 1st order active LPF. The filters are cascaded

        to create the 3rd order krc design.

        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [ list ] 
        '''
        cap = float(cap)
        f_c = float(f_c)
        
        #2ND order KRC Filter calculations
        Q1_squared = self.Q1 ** 2
        f_1 = f_c * self.fo1
        w_1 = 2 * pi * f_1
        n_1 = 4 * Q1_squared + 100
        k_1 = (n_1 / (2 * Q1_squared)) - 1
        k_1_squared = k_1 ** 2
        m_1 = k_1 + sqrt(k_1_squared - 1)
        R_1 = 1 / ((sqrt(m_1 * n_1)) * w_1 * cap)
        nC_1 = n_1 * cap
        mR_1 = m_1 * R_1

        #first order active LPF calculations
        f_2 = f_c * self.fo2  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)
        
        str1 = "\nLPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"k_1: {k_1}"
        str8 = f"m_1: {m_1}"
        str9 = f"n_1: {n_1}"
        str10 = f"R_1: {R_1} ohms"
        str11 = f"nC_1: {nC_1 * 10**9} nF"
        str12 = f"mR_1: {mR_1} ohms"
        str13 = "\n<-------------------------------->\n"
        
        print("\nLPF KRC_1(2nd Order filter):")
        print(f"Cutoff Frequency: {f_c} Hz")
        print(f"Input Capacitor: {cap * 10**9} nF")
        print(f"Q1: {self.Q1}")
        print(f"fo_1: {self.fo1}")
        print(f"f_1: {f_1} Hz")
        print(f"k_1: {k_1}")
        print(f"m_1: {m_1}")
        print(f"n_1: {n_1}")
        print(f"R_1: {R_1} ohms")
        print(f"nC_1: {nC_1 * 10**9} nF")
        print(f"mR_1: {mR_1} ohms")
        print("\n<-------------------------------->\n")

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [[str1,str2,str3,str4,str5,str6,str7,
                     str8,str9,str10,str11,str12,str13], 
                        [strA,strB,strC,strD,strE,strF,strG]]

    def krc3_HPF(self,f_c,cap):
        '''
        Computes the values for 3rd order krc 
        
        high pass filter design using the unity gain technique.

        Filter design values are for one 2nd order HPF krc circuit 
        
        and one 1st order active HPF. The filters are cascaded

        to create the 3rd order krc design.

        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c / self.fo1
        w = 2 * pi * f_1
        n = 4 * Q1_squared + 100
        m =  n / ((self.Q1 * n + self.Q1)**2)
        R_1 = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
        nC = n * cap
        mR_1 = m * R_1

        #first order active HPF calculations
        f_2 = f_c / self.fo2  #frequency for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        str1 = f"\nHPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q_1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"m: {m}"
        str8 = f"n: {n}"
        str9 = f"R_1: {R_1} ohms"
        str10 = f"nC: {nC * 10**9} nF"
        str11 = f"mR_1: {mR_1} ohms"
        str12 = "\n<-------------------------------->\n"
    
        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9) 
        print(str10)
        print(str11)
        print(str12)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [[str1,str2,str3,str4,str5,str6,str7,
                     str8,str9,str10,str11,str12], 
                    [strA,strB,strC,strD,strE,strF,strG]]

    def krc4_LPF(self,f_c,cap):
        '''
        Computes the values for 4th order krc

        low pass filter using the unity gain technique.

        Filter design values are for two 2nd order KRC circuits

        that will be cascaded to make a 4th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
        
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R

            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
                  
        return out

    def krc4_HPF(self,f_c,cap):
        '''
        Computes the values for 4th order krc

        high pass filter using the unity gain technique
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
            
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out
    
    def krc5_LPF(self,f_c,cap):
        '''
        Computes the values for 5th order krc

        low pass filter using the unity gain technique.

        Filter design values are for two 2nd order LPF krc

        circuits and one 1st order active LPF circuit.

        The filters are cascaded to create the 5th order krc design.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
            
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)

        #first order active LPF calculations
        f_2 = f_c * self.fo3  #frequency used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)
        
        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out,[strA,strB,strC,strD,strE,strF,strG]]

    def krc5_HPF(self,f_c,cap):
        '''
        Computes the values for 5th order krc

        high pass filter using the unity gain technique.

        Filter design values are for two 2nd order HPF krc

        circuits and one 1st order active HPF circuit.

        The filters are cascaded to create the 5th order krc design.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list]
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo3  #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]
    
    def krc6_LPF(self,f_c,cap):
        '''
        Computes the values for 6th order krc

        low pass filter using the unity gain technique.

        Filter design values are for three 2nd order LPF krc

        circuits that will be cascaded to make a 6th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out

    def krc6_HPF(self,f_c,cap):
        '''
        Computes the values for 6th order krc

        high pass filter using the unity gain technique
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out

    def krc7_LPF(self,f_c,cap):
        '''
        Computes the values for 7th order krc

        low pass filter using the unity gain technique.

        Filter design values are for three 2nd order LPF krc

        circuits and one 1st order active LPF circuit.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)

        #first order active LPF calculations
        f_2 = f_c * self.fo4  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out, [strA,strB,strC,strD,strE,strF,strG]]

    def krc7_HPF(self,f_c,cap):
        '''
        Computes the values for 7th order krc

        high pass filter using the unity gain technique.

        Filter design values are for three 2nd order HPF krc

        circuits and one 1st order active HPF circuit.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
            
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo4  #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]

    def krc8_LPF(self,f_c,cap):
        '''
        Computes the values for 8th order krc

        low pass filter using the unity gain technique.

        Filter design values are for four 2nd order LPF krc

        circuits that will be cascaded to make a 8th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out
    
    def krc8_HPF(self,f_c,cap):
        '''
        Computes the values for 8th order krc

        high pass filter using the unity gain technique.

        Filter design values are for four 2nd order HPF krc

        circuits that will be cascaded to make a 8th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out
    
    def krc9_LPF(self,f_c,cap):
        '''
        Computes the values for 9th order krc

        low pass filter using the unity gain technique.

        Filter design values are for four 2nd order LPF krc

        circuits and one 1st order active HPF circuit. The

        circuits are cascaded to make the 9th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list]
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        #first order active LPF calculations
        f_2 = f_c * self.fo5  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out, [strA,strB,strC,strD,strE,strF,strG]]

    def krc9_HPF(self,f_c,cap):
        '''
        Computes the values for 9th order krc

        high pass filter using the unity gain technique.

        Filter design values are for four 2nd order HPF krc

        circuits and one 1st order active HPF circuit. The 

        circuits are cascaded to make the 9th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo5 #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]
    
    def krc10_LPF(self,f_c,cap):
        '''
        Computes the values for 10th order krc

        low pass filter using the unity gain technique.

        Filter design values are for five 2nd order LPF krc

        circuits that will be cascaded to make a 10th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(5):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            if c == 5:
                Q = self.fo5 
                fo = self.Q5
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
            
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out

    def krc10_HPF(self,f_c,cap):
        '''
        Computes the values for 10th order krc

        high pass filter using the unity gain technique.

        Filter design values are for five 2nd order HPF krc

        circuits that will be cascaded to make a 10th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            if c == 5:
                Q = self.fo5 
                fo = self.Q5
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out

class Buttersworth:
    def __init__(self,order):

        if not (isinstance(order,int) and (order >= 2 and order <= 10)):
            raise ValueError(f"""Invalid argument: order must be 
            2,3,4,5,6,7,8,9,10 got {order}""") #checks if the order is corrrect

        self.order = order

        if order == 2:
            self.fo1 = 1
            self.Q1 = .707
    
        if order == 3:
            self.fo1 = 1
            self.Q1 = 1.000
            self.fo2 = 1
        
        if order == 4:
            self.fo1 = 1    
            self.Q1 = .541
            self.fo2 = 1
            self.Q2 = 1.306

        if order == 5:
            self.fo1 = 1
            self.Q1 = .618
            self.fo2 = 1
            self.Q2 = 1.620
            self.fo3 = 1
        
        if order == 6:
            self.fo1 = 1
            self.Q1 = .518
            self.fo2 = 1
            self.Q2 = .707
            self.fo3 = 1
            self.Q3 = 1.932
        
        if order == 7:
            self.fo1 = 1
            self.Q1 = .555
            self.fo2 = 1
            self.Q2 = .802
            self.fo3 = 1
            self.Q3 = 2.247
            self.fo4 = 1
        
        if order == 8:
            self.fo1 = 1
            self.Q1 = .510
            self.fo2 = 1
            self.Q2 = .601
            self.fo3 = 1
            self.Q3 = .900
            self.fo4 = 1
            self.Q4 =  2.563
        
        if order == 9: 
            self.fo1 = 1
            self.Q1 = .532
            self.fo2 = 1
            self.Q2 = .653
            self.fo3 = 1
            self.Q3 = 1.000
            self.fo4 = 1
            self.Q4 =  2.879
            self.fo5 = 1
        
        if order == 10: 
            self.fo1 = 1
            self.Q1 = .506
            self.fo2 = 1
            self.Q2 = .561
            self.fo3 = 1
            self.Q3 = .707
            self.fo4 = 1
            self.Q4 = 1.101
            self.fo5 = 1
            self.Q5 = 3.196

    def krc2_LPF(self,f_c,cap):
        '''
           Computes the values for 2nd order krc

           low pass filter using the unity gain technique
           
           f_c = cutoff freq in hertz

           cap = capacitor value in Farads

           returns ---> list 
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c * self.fo1
        w_1 = 2 * pi * f_1
        n_1 = 4 * Q1_squared + 100
        k_1 = (n_1 / (2 * Q1_squared)) - 1
        k_1_squared = k_1 ** 2
        m_1 = k_1 + sqrt(k_1_squared - 1)
        R_1 = 1 / ((sqrt(m_1 * n_1)) * w_1 * cap)
        nC_1 = n_1 * cap
        mR_1 = m_1 * R_1
        
        str1 = "\nLPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"k_1: {k_1}"
        str8 = f"m_1: {m_1}"
        str9 = f"n_1: {n_1}"
        str10 = f"R_1: {R_1} ohms"
        str11 = f"nC_1: {nC_1 * 10**9} nF"
        str12 = f"mR_1: {mR_1} ohms"

        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9)
        print(str10)
        print(str11)
        print(str12)
        
        return [str1,str2,str3,str4,str5,str6,
                str7,str8,str9,str10,str11,str12]

    def krc2_HPF(self,f_c,cap):
        '''
        Computes the values for 2d order krc 
        
        high pass filter design using the unity gain technique.

        Filter design values are for one 2nd order HPF krc circuit. 
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads
        
        returns ---> list
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c / self.fo1
        w = 2 * pi * f_1
        n = 4 * Q1_squared + 100
        m =  n / ((self.Q1 * n + self.Q1)**2)
        R_1 = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
        nC = n * cap
        mR_1 = m * R_1

        str1 = f"\nHPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q_1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"m: {m}"
        str8 = f"n: {n}"
        str9 = f"R_1: {R_1} ohms"
        str10 = f"nC: {nC * 10**9} nF"
        str11 = f"mR_1: {mR_1} ohms"
        
        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9) 
        print(str10)
        print(str11)

        return [str1,str2,str3,str4,str5,
                str6,str7,str8,str9,str10,str11]
        
    def krc3_LPF(self,f_c,cap):
        '''
        Computes the values for 3rd order krc 
        
        low pass filter design using the unity gain technique.

        Filter design values are for one 2nd order krc LPF circuit 
        
        and one 1st order active LPF. The filters are cascaded

        to create the 3rd order krc design.

        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [ list ] 
        '''
        cap = float(cap)
        f_c = float(f_c)
        
        #2ND order KRC Filter calculations
        Q1_squared = self.Q1 ** 2
        f_1 = f_c * self.fo1
        w_1 = 2 * pi * f_1
        n_1 = 4 * Q1_squared + 100
        k_1 = (n_1 / (2 * Q1_squared)) - 1
        k_1_squared = k_1 ** 2
        m_1 = k_1 + sqrt(k_1_squared - 1)
        R_1 = 1 / ((sqrt(m_1 * n_1)) * w_1 * cap)
        nC_1 = n_1 * cap
        mR_1 = m_1 * R_1

        #first order active LPF calculations
        f_2 = f_c * self.fo2  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)
        
        str1 = "\nLPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"k_1: {k_1}"
        str8 = f"m_1: {m_1}"
        str9 = f"n_1: {n_1}"
        str10 = f"R_1: {R_1} ohms"
        str11 = f"nC_1: {nC_1 * 10**9} nF"
        str12 = f"mR_1: {mR_1} ohms"
        str13 = "\n<-------------------------------->\n"
        
        print("\nLPF KRC_1(2nd Order filter):")
        print(f"Cutoff Frequency: {f_c} Hz")
        print(f"Input Capacitor: {cap * 10**9} nF")
        print(f"Q1: {self.Q1}")
        print(f"fo_1: {self.fo1}")
        print(f"f_1: {f_1} Hz")
        print(f"k_1: {k_1}")
        print(f"m_1: {m_1}")
        print(f"n_1: {n_1}")
        print(f"R_1: {R_1} ohms")
        print(f"nC_1: {nC_1 * 10**9} nF")
        print(f"mR_1: {mR_1} ohms")
        print("\n<-------------------------------->\n")

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [[str1,str2,str3,str4,str5,str6,str7,
                     str8,str9,str10,str11,str12,str13], 
                        [strA,strB,strC,strD,strE,strF,strG]]

    def krc3_HPF(self,f_c,cap):
        '''
        Computes the values for 3rd order krc 
        
        high pass filter design using the unity gain technique.

        Filter design values are for one 2nd order HPF krc circuit 
        
        and one 1st order active HPF. The filters are cascaded

        to create the 3rd order krc design.

        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        cap = float(cap)
        f_c = float(f_c)
        Q1_squared = self.Q1 ** 2
        f_1 = f_c / self.fo1
        w = 2 * pi * f_1
        n = 4 * Q1_squared + 100
        m =  n / ((self.Q1 * n + self.Q1)**2)
        R_1 = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
        nC = n * cap
        mR_1 = m * R_1

        #first order active HPF calculations
        f_2 = f_c / self.fo2  #frequency for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        str1 = f"\nHPF KRC_1(2nd Order Filter):"
        str2 = f"Cutoff Frequency: {f_c} Hz"
        str3 = f"Input Capacitor: {cap * 10**9} nF"
        str4 = f"Q_1: {self.Q1}"
        str5 = f"fo_1: {self.fo1}"
        str6 = f"f_1: {f_1} Hz"
        str7 = f"m: {m}"
        str8 = f"n: {n}"
        str9 = f"R_1: {R_1} ohms"
        str10 = f"nC: {nC * 10**9} nF"
        str11 = f"mR_1: {mR_1} ohms"
        str12 = "\n<-------------------------------->\n"
    
        print(str1)
        print(str2)
        print(str3)
        print(str4)
        print(str5)
        print(str6)
        print(str7)
        print(str8)
        print(str9) 
        print(str10)
        print(str11)
        print(str12)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [[str1,str2,str3,str4,str5,str6,str7,
                     str8,str9,str10,str11,str12], 
                    [strA,strB,strC,strD,strE,strF,strG]]

    def krc4_LPF(self,f_c,cap):
        '''
        Computes the values for 4th order krc

        low pass filter using the unity gain technique.

        Filter design values are for two 2nd order KRC circuits

        that will be cascaded to make a 4th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
        
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R

            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
                  
        return out

    def krc4_HPF(self,f_c,cap):
        '''
        Computes the values for 4th order krc

        high pass filter using the unity gain technique
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
            
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out
    
    def krc5_LPF(self,f_c,cap):
        '''
        Computes the values for 5th order krc

        low pass filter using the unity gain technique.

        Filter design values are for two 2nd order LPF krc

        circuits and one 1st order active LPF circuit.

        The filters are cascaded to create the 5th order krc design.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
            
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)

        #first order active LPF calculations
        f_2 = f_c * self.fo3  #frequency used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)
        
        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out,[strA,strB,strC,strD,strE,strF,strG]]

    def krc5_HPF(self,f_c,cap):
        '''
        Computes the values for 5th order krc

        high pass filter using the unity gain technique.

        Filter design values are for two 2nd order HPF krc

        circuits and one 1st order active HPF circuit.

        The filters are cascaded to create the 5th order krc design.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list]
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(2):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo3  #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]
    
    def krc6_LPF(self,f_c,cap):
        '''
        Computes the values for 6th order krc

        low pass filter using the unity gain technique.

        Filter design values are for three 2nd order LPF krc

        circuits that will be cascaded to make a 6th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out

    def krc6_HPF(self,f_c,cap):
        '''
        Computes the values for 6th order krc

        high pass filter using the unity gain technique
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out

    def krc7_LPF(self,f_c,cap):
        '''
        Computes the values for 7th order krc

        low pass filter using the unity gain technique.

        Filter design values are for three 2nd order LPF krc

        circuits and one 1st order active LPF circuit.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)

        #first order active LPF calculations
        f_2 = f_c * self.fo4  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out, [strA,strB,strC,strD,strE,strF,strG]]

    def krc7_HPF(self,f_c,cap):
        '''
        Computes the values for 7th order krc

        high pass filter using the unity gain technique.

        Filter design values are for three 2nd order HPF krc

        circuits and one 1st order active HPF circuit.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(3):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
            
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo4  #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]

    def krc8_LPF(self,f_c,cap):
        '''
        Computes the values for 8th order krc

        low pass filter using the unity gain technique.

        Filter design values are for four 2nd order LPF krc

        circuits that will be cascaded to make a 8th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out
    
    def krc8_HPF(self,f_c,cap):
        '''
        Computes the values for 8th order krc

        high pass filter using the unity gain technique.

        Filter design values are for four 2nd order HPF krc

        circuits that will be cascaded to make a 8th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out
    
    def krc9_LPF(self,f_c,cap):
        '''
        Computes the values for 9th order krc

        low pass filter using the unity gain technique.

        Filter design values are for four 2nd order LPF krc

        circuits and one 1st order active HPF circuit. The

        circuits are cascaded to make the 9th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list]
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
    
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        #first order active LPF calculations
        f_2 = f_c * self.fo5  #this frequency is used for the first order active LPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "LPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"
        
        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)

        return [out, [strA,strB,strC,strD,strE,strF,strG]]

    def krc9_HPF(self,f_c,cap):
        '''
        Computes the values for 9th order krc

        high pass filter using the unity gain technique.

        Filter design values are for four 2nd order HPF krc

        circuits and one 1st order active HPF circuit. The 

        circuits are cascaded to make the 9th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> [list] 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        #first order active HPF calculations
        f_2 = f_c / self.fo5 #this frequency is used for the first order active HPF
        R_2 = (1) / (2*pi * f_2 * cap)

        strA = "HPF(1st order):"
        strB = f"Cutoff Frequency: {f_c} Hz"
        strC = f"Input Capacitor: {cap * 10**9} nF"
        strD = f"fo_2: {self.fo2}"
        strE = f"f_2: {f_2} Hz"
        strF = f"R: {R_2} ohms"
        strG = f"C: {cap * 10**9} nF"

        print(strA)
        print(strB)
        print(strC)
        print(strD)
        print(strE)
        print(strF)
        print(strG)
        
        return [out,[strA,strB,strC,strD,strE,strF,strG]]
    
    def krc10_LPF(self,f_c,cap):
        '''
        Computes the values for 10th order krc

        low pass filter using the unity gain technique.

        Filter design values are for five 2nd order LPF krc

        circuits that will be cascaded to make a 10th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> list
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(5):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            if c == 5:
                Q = self.fo5 
                fo = self.Q5
            
            Q_squared = Q ** 2
            f = f_c * fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            k = (n / (2 * Q_squared)) - 1
            k_squared = k ** 2
            m = k + sqrt(k_squared - 1)
            R = 1 / ((sqrt(m * n)) * w * cap)
            nC = n * cap
            mR = m * R
            
            str1 = f"\nLPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"k_{c}: {k}"
            str8 = f"m_{c}: {m}"
            str9 = f"n_{c}: {n}"
            str10 = f"R_{c}: {R} ohms"
            str11 = f"nC_{c}: {nC * 10**9} nF"
            str12 = f"mR_{c}: {mR} ohms"
            str13 = "\n<-------------------------------->\n"
            
            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            out.append(str13)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9)
            print(str10)
            print(str11)
            print(str12)
            print(str13)
        
        return out

    def krc10_HPF(self,f_c,cap):
        '''
        Computes the values for 10th order krc

        high pass filter using the unity gain technique.

        Filter design values are for five 2nd order HPF krc

        circuits that will be cascaded to make a 10th order filter.
        
        f_c = cutoff freq in hertz

        cap = capacitor value in Farads

        returns ---> none 
        '''
        out = []
        cap = float(cap)
        f_c = float(f_c)
        c = 0
        for e in range(4):
            c += 1
            if c == 1:
                Q = self.Q1
                fo = self.fo1
            if c == 2:
                Q = self.Q2
                fo = self.fo2
            if c == 3:
                Q = self.Q3
                fo = self.fo3
            if c == 4:
                Q = self.fo4 
                fo = self.Q4
            if c == 5:
                Q = self.fo5 
                fo = self.Q5
            
            Q_squared = Q ** 2
            f = f_c / fo
            w = 2 * pi * f
            n = 4 * Q_squared + 100
            m =  n / ((Q * n + Q)**2)
            R = 1 / ((sqrt(m * n)) * w * cap)  #resistance for R2 in KRC HPF 
            nC = n * cap
            mR = m * R
    
            str1 = f"\nHPF KRC_{c}(2nd Order Filter):"
            str2 = f"Cutoff Frequency: {f_c} Hz"
            str3 = f"Input Capacitor: {cap * 10**9} nF"
            str4 = f"Q_{c}: {Q}"
            str5 = f"fo_{c}: {fo}"
            str6 = f"f_{c}: {f} Hz"
            str7 = f"m: {m}"
            str8 = f"n: {n}"
            str9 = f"R_{c}: {R} ohms"
            str10 = f"nC_{c}: {nC * 10**9} nF"
            str11 = f"mR_{c}: {mR} ohms"
            str12 = "\n<-------------------------------->\n"

            out.append(str1)
            out.append(str2)
            out.append(str3)
            out.append(str4)
            out.append(str5)
            out.append(str6)
            out.append(str7)
            out.append(str8)
            out.append(str9)
            out.append(str10)
            out.append(str11)
            out.append(str12)
            
            print(str1)
            print(str2)
            print(str3)
            print(str4)
            print(str5)
            print(str6)
            print(str7)
            print(str8)
            print(str9) 
            print(str10)
            print(str11)
            print(str12)
        
        return out

if __name__ == "__main__":
    obj = Chebyshev(4)
    obj.krc4_HPF(89,1*10**-9)
  
