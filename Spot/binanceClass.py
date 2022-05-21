from binance.client import Client
import sqlite3
import pandas as pd
import algorithmClass
import time

class bClass:

    def __init__(self,name,coin,roud,apiKey,secretKey):
        self.name = name
        self.coin = coin
        self.roud = roud
        self.apiKey = apiKey
        self.secretKey = secretKey
        self.client = Client(apiKey, secretKey)
        # DB Online #
        self.db = sqlite3.connect("cyriptoDB.db")
        self.dbcursor = self.db.cursor()
    def cuzdan(self):
        balance = self.client.get_asset_balance(asset='USDT')
        return float(balance['free'])
    def coinVeri(self):
        balance = self.client.get_asset_balance(asset=self.coin)
        return float(balance['free'])
    def veri(self,sayi):
        symbol = self.name
        interval = "15m"
        limit = 5
        attributes = ["timestamp","open","high","low","close","volume","1","2","3","4","5","6"]
        veri15 = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        veri = pd.DataFrame(veri15, columns = attributes)
        if sayi == 0:
            return float(veri.close[4])
        elif sayi == 1:
            return float(veri.close[3])
        elif sayi == 2:
            return float(veri.close[2])
        elif sayi == 3:
            return float(veri.close[1])
        elif sayi == 4:
            return float(veri.close[0])
    def log(self,yazi):
        saat = time.strftime('%c')
        with open('log.txt', 'a') as f:
            f.write(yazi+' Saat: '+saat+'\n')
    
    def veriGuncelleMiktar(self,miktar):
        self.dbcursor.execute("UPDATE Cyripto SET miktar = ? WHERE name = ?",(miktar,self.name))
        self.db.commit()
    def veriGuncelleSonAlis(self,sonAlis):
        self.dbcursor.execute("UPDATE Cyripto SET sonAlis = ? WHERE name = ?",(sonAlis,self.name))
        self.db.commit()
    def veriGuncelleAlisOrtalama(self,alisOrtalama):
        self.dbcursor.execute("UPDATE Cyripto SET alisOrtalama = ? WHERE name = ?",(alisOrtalama,self.name))
        self.db.commit()
    def veriGuncelleSatmadanAlis(self,satmadanAlis):
        self.dbcursor.execute("UPDATE Cyripto SET satmadanAlis = ? WHERE name = ?",(satmadanAlis,self.name))
        self.db.commit()
    def veriGuncelleAlisToplamPara(self,alisToplamPara):
        self.dbcursor.execute("UPDATE Cyripto SET alisToplamPara = ? WHERE name = ?",(alisToplamPara,self.name))
        self.db.commit()
    def veriGuncelleAlis(self,alis):
        self.dbcursor.execute("UPDATE Cyripto SET alis = ? WHERE name = ?",(alis,self.name))
        self.db.commit()
    def veriGuncelleSatis(self,satis):
        self.dbcursor.execute("UPDATE Cyripto SET satis = ? WHERE name = ?",(satis,self.name))
        self.db.commit()
    def veriGuncelleKomisyon(self,komisyon):
        self.dbcursor.execute("UPDATE Cyripto SET komisyon = ? WHERE name = ?",(komisyon,self.name))
        self.db.commit()
    
    def veriAlMiktar(self):
        self.dbcursor.execute("SELECT miktar FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def veriAlSonAlis(self):
        self.dbcursor.execute("SELECT sonAlis FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def veriAlAlisOrtalama(self):
        self.dbcursor.execute("SELECT alisOrtalama FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def veriAlSatmadanAlis(self):
        self.dbcursor.execute("SELECT satmadanAlis FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def veriAlAlisToplamPara(self):
        self.dbcursor.execute("SELECT alisToplamPara FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def veriAlAlis(self):
        self.dbcursor.execute("SELECT alis FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def veriAlSatis(self):
        self.dbcursor.execute("SELECT satis FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def veriAlKomisyon(self):
        self.dbcursor.execute("SELECT komisyon FROM Cyripto WHERE name= '"+self.name+"'")
        data=self.dbcursor.fetchall()
        for i in data:
            return i[0]
    def komisyonKes(self,para):
        return para-para/1000
    def al(self,alisCoinFiyat,alisPara):
        if self.cuzdan() >= alisPara and self.cuzdan()>=10:
            alis = round(alisPara/alisCoinFiyat,self.roud)
            order = self.client.order_market_buy(symbol=self.name,quantity=alis)
            self.veriGuncelleMiktar(self.veriAlMiktar()+self.komisyonKes(alisPara/alisCoinFiyat))
            self.veriGuncelleSonAlis(alisCoinFiyat)
            self.veriGuncelleAlisToplamPara(self.veriAlAlisToplamPara()+alisPara)
            self.veriGuncelleAlisOrtalama((self.veriAlAlisToplamPara()/self.veriAlMiktar()))
            self.veriGuncelleSatmadanAlis(self.veriAlSatmadanAlis()+1)
            self.veriGuncelleAlis(self.veriAlAlis()+1)
            try:
                self.log(self.name+", alindi.")
            except:
                print("Log girilemedi")
            
    def sat(self):
        if (self.veri(0)*self.coinVeri()) > 10:
            try:
                if self.veriAlAlisOrtalama() < self.veri(0):
                    self.log(self.name+", satıldı,")
                else:
                    self.log(self.name+",  Stop oldun,")
            except:
                print("Log girilemedi")
            try:
                order = self.client.order_market_sell(symbol=self.name,quantity=round(self.coinVeri(),self.roud))
            except:
                order = self.client.order_market_sell(symbol=self.name,quantity=round(round(self.coinVeri(),self.roud)-((round(self.coinVeri(),self.roud)/100)*1.5),self.roud))
            self.veriGuncelleAlisToplamPara(0)
            self.veriGuncelleMiktar(0)
            self.veriGuncelleSatmadanAlis(0)
            self.veriGuncelleSonAlis(0)
            self.veriGuncelleAlisOrtalama(0)
            self.veriGuncelleSatis(self.veriAlSatis()+1)

    
    def cagir(self):
        saat = time.strftime('%c')
        print(self.name," güncel fiyat: ",self.veri(0))
        print("Saat: ",saat)
        if self.veri(0) < (self.veriAlAlisOrtalama()-((self.veriAlAlisOrtalama()/100)*15)):
            if (self.coinVeri()*self.veri(0))>=15:
                try:
                    self.sat()
                    saat = time.strftime('%c')
                    print("Stop oldum 15 dk ara veriyorum Saat: ",saat)
                    time.sleep(900)
                except Exception as e:
                    print("Satamadım Hata:",e)
        if self.veriAlSatmadanAlis() <4:
            if algorithmClass.yuzdeHesap(self.veri(2),self.veri(3)) <= -0.45:
                if algorithmClass.yuzdeHesap(self.veri(1),self.veri(2)) <= -0.45:
                    if self.veriAlSatmadanAlis() == 0:
                        if self.cuzdan() >= 35:
                            try:
                                self.al(self.veri(0),35)
                                print("İlk alış Aldım 15 dk ara veriyorum Saat: ",saat)
                                time.sleep(900)
                            except Exception as e:
                                print("Alamadım, Hata:",e)
                    elif self.veriAlSatmadanAlis() < 4:
                        if self.cuzdan() >= 40*(self.veriAlSatmadanAlis()+1):
                            try:
                                self.al(self.veri(0),35*(self.veriAlSatmadanAlis()+1))
                                print("Aldım 15 dk ara veriyorum Saat: ",saat)
                                time.sleep(900)
                            except Exception as e:
                                print("Alamadım, Hata:",e)
            if algorithmClass.yuzdeHesap(self.veri(3),self.veri(4)) <= -0.5:
                if algorithmClass.yuzdeHesap(self.veri(2),self.veri(3)) > -0.5 and algorithmClass.yuzdeHesap(self.veri(2),self.veri(3)) < 0.25:
                    if algorithmClass.yuzdeHesap(self.veri(1),self.veri(2)) <= -0.5:
                        if self.veriAlSatmadanAlis() == 0:
                            if self.cuzdan() >= 35:
                                try:
                                    self.al(self.veri(0),35)
                                    print("İlk alış Aldım 15 dk ara veriyorum Saat: ",saat)
                                    time.sleep(900)
                                except Exception as e:
                                    print("Alamadım, Hata:",e)
                        elif self.veriAlSatmadanAlis() < 4:
                            if self.cuzdan() >= 35*(self.veriAlSatmadanAlis()+1):
                                try:
                                    self.al(self.veri(0),35*(self.veriAlSatmadanAlis()+1))
                                    print("Aldım 15 dk ara veriyorum Saat: ",saat)
                                    time.sleep(900)
                                except Exception as e:
                                    print("Alamadım, Hata:",e)
        if self.veri(0) > (((self.veriAlAlisOrtalama()/100)*3)+self.veriAlAlisOrtalama()):
            if (self.coinVeri()*self.veri(0))>=10:
                if self.veriAlSatmadanAlis() >1:
                    try:
                        self.sat()
                        print(self.name," Satıldı. Guncel para: ",self.cuzdan())
                    except Exception as e:
                        print("Satamadım Hata:",e)
            
