from qt_core import *
from gui.widgets.app_widgets import *
from gui.pages.page_ip import *
from gui.pages.pages_one import *
from gui.pages.home import *
from gui.pages.hazirlama import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        self.MainWindow=parent
        parent.setObjectName("window")
        parent.setStyleSheet(open("gui/themes/dark.qss","r").read())
        parent.setWindowFlags(Qt.WindowType.FramelessWindowHint)

################### VARIABLE Start ##################################################

        #Parameters
        self.app_icon_adress="gui/image/icon/ico.ico" # uygulama ikon adresi
        self.app_icon_x=32  # uygulama ikon x boyutu
        self.app_icon_y=32  # uygulama ikon y boyutu
        self.user="Admin"   # kullanıcı bilgisi
        self.menuTabsNumber=0   # menu iceriklerinden oluşan alt tab başlıklarına verilen numara
        self.menuTitleList=[]   # menu içeriklerinden oluşan alt tabların listesi
        self.pageList=[]
        self.pageListActive=0
        #Menu header and index value
        self.menu_list={
            "isletme":{
                        "metin":"İşletme",
                        "objeismi":"isletme",
                        "icerikler":{
                            "ip":["İp","ip","gui/image/icon/ip.png",40,40,"gui/image/icon/ip_h.png"],
                            "likra":["Likra","likra","gui/image/icon/likra.png",40,40,"gui/image/icon/likra_h.png"],
                            "fason":["Fason","fason","gui/image/icon/fason.png",40,40,"gui/image/icon/fason_h.png"],
                            "boyahane":["Boyahane","boyahane","gui/image/icon/boyahane.png",40,40,"gui/image/icon/boyahane_h.png"],
                            "kumas":["Kumaş","kumas","gui/image/icon/kumas.png",40,40,"gui/image/icon/kumas_h.png"]
                        }
                    },
            "muhasebe":{
                        "metin":"Muhasebe",
                        "objeismi":"muhasebe",
                        "icerikler":{
                            "gelir":["Gelir","gelir","gui/image/icon/gelir.png",40,40,"gui/image/icon/gelir_h.png"],
                            "gider":["Gider","gider","gui/image/icon/gider.png",40,40,"gui/image/icon/gider_h.png"],
                            "maas":["Maaş","maas","gui/image/icon/maas.ico",40,40,"gui/image/icon/maas_h.ico"],
                            "avans":["Avans","avans","gui/image/icon/avans.ico",40,40,"gui/image/icon/avans_h.ico"],
                            "babs":["Ba Bs","babs","gui/image/icon/babs.ico",40,40,"gui/image/icon/babs_h.ico"]
                        }
                    },
            "ik":{
                        "metin":"İK",
                        "objeismi":"ik",
                        "icerikler":{
                            "calisan":["Çalışan","calisan","gui/image/icon/worker.ico",40,40,"gui/image/icon/worker_h.ico"],
                            "izin":["İzin","izin","gui/image/icon/izin.ico",40,40,"gui/image/icon/izin_h.ico"],
                            "mesai":["Fazla Mesai","mesai","gui/image/icon/mesai.ico",40,40,"gui/image/icon/mesai_h.ico"],
                            "bordro":["Bordro","bordro","gui/image/icon/bordro.ico",40,40,"gui/image/icon/bordro_h.ico"],
                            "tutanak":["Tutanak","tutanak","gui/image/icon/tutanak.ico",40,40,"gui/image/icon/tutanak_h.ico"]
                        }
                    },
            "rapor":{
                        "metin":"Rapor",
                        "objeismi":"rapor",
                        "icerikler":{
                            "sorgu":["SQL","sorgu","gui/image/icon/sql.ico",40,40,"gui/image/icon/sql_h.ico"]
                            
                        }
                    },
            "ayarlar":{
                        "metin":"Ayarlar",
                        "objeismi":"ayarlar",
                        "icerikler":{
                            "hakkimizda":["Hakkımızda","hakkimizda","gui/image/icon/info.ico",40,40,"gui/image/icon/info_h.ico"]
                        }
                    }
        }


################### VARIABLE Finish #################################################
################### CONTAINAR Start #################################################

        #Contanier
        self.container_frame=QFrame()
        self.container_frame.setObjectName("mainFrame")

        #Contanier Layout
        self.container_layout=QVBoxLayout(self.container_frame)
        self.container_layout.setContentsMargins(0,0,0,0)
        self.container_layout.setSpacing(0)

################### CONTAINAR Finish ################################################
################### TOP BAR Start ###################################################
        
        # Top Bar
        self.top_frame=QFrame()
        self.top_frame.setObjectName("top_frame")

        # Top Layout
        self.top_layout=QHBoxLayout(self.top_frame)
        self.top_layout.setContentsMargins(0,0,0,0)
        self.top_layout.setSpacing(0)

        # Top İcon
        self.top_lbl_icon=QLabel()
        self.icon_image=QPixmap(self.app_icon_adress)
        self.top_lbl_icon.setPixmap(self.icon_image.scaled(self.app_icon_x,self.app_icon_y))
        self.top_lbl_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Top Company Name
        self.top_lbl_companyName=QLabel("BAYBURT ANONİM ŞİRKETİ")
        self.top_lbl_companyName.setObjectName("lblcompanyName")
        self.top_lbl_companyName.setAlignment(Qt.AlignCenter)

        # Top UserName 
        self.top_lbl_userName=QLabel(self.user)
        self.top_lbl_userName.setObjectName("lbluserName")
        
        # Top DateTime
        self.top_lbl_dateTime=Saat()
        self.top_lbl_dateTime.setObjectName("lbldateTime")

        # Top Button 
        self.top_btn_minimize=QPushButton()
        self.top_btn_minimize.setObjectName("btnminimize")

        self.top_btn_close=QPushButton()
        self.top_btn_close.setObjectName("btnclose")
        self.top_btn_close.clicked.connect(QApplication.instance().quit)

        #Add Widgets to top_layout
        self.top_layout.addWidget(self.top_lbl_icon)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.top_lbl_companyName)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.top_lbl_userName)
        self.top_layout.addSpacing(50)
        self.top_layout.addWidget(self.top_lbl_dateTime)
        self.top_layout.addSpacing(50)
        self.top_layout.addWidget(self.top_btn_minimize)
        self.top_layout.addWidget(self.top_btn_close)

        
################### TOP BAR Finish ##################################################
################### MENU BAR Start ##################################################

        #Menu Container
        self.menu_frame=QFrame()
        self.menu_frame.setObjectName("menuFrame")

        #Menu Container Layout
        self.menu_layout=QVBoxLayout(self.menu_frame)
        self.menu_layout.setContentsMargins(0,0,0,0)
        self.menu_layout.setSpacing(0)

        #Menu Title Frame
        self.menu_title_frame=QFrame()
        self.menu_title_frame.setObjectName("menuHeaderFrame")

        #Menu Title Layout
        self.menu_title_layout=QHBoxLayout(self.menu_title_frame)
        self.menu_title_layout.setContentsMargins(40,0,0,0)
        self.menu_title_layout.setSpacing(0)

        #Create Button and Add to Menu Title Layout
        for key in self.menu_list.keys():
            i=QPushButton(self.menu_list[key]["metin"])
            i.setObjectName(self.menu_list[key]["objeismi"])
            i.clicked.connect(self.designPropertyTitle)
            i.setCursor(QCursor(Qt.PointingHandCursor))
            self.menu_title_layout.addWidget(i)
        self.menu_title_layout.addStretch()

        #Menu contents Frame
        self.menu_contents_frame=QFrame()
        self.menu_contents_frame.setObjectName("menuContentsFrame")

        #Menu Contents Layout
        self.menu_contents_layout=QHBoxLayout(self.menu_contents_frame)
        self.menu_contents_layout.setContentsMargins(40,0,0,0)
        self.menu_contents_layout.setSpacing(15)

        #Create Buton and Add to Menu Contents Layout
        for i_key in self.menu_list["isletme"]["icerikler"].keys():
            self.i=buttonSpeacial(self.menu_list["isletme"]["icerikler"][i_key])
            self.i.clicked.connect(self.menuTitleAdd)
            self.menu_contents_layout.addWidget(self.i)
        self.menu_contents_layout.addStretch()

        #Menu Tab Frame
        self.menu_tab_frame=QFrame()
        self.menu_tab_frame.setObjectName("menıTabFrame")

        #Menu Tab Layout
        self.menu_tab_layout=QHBoxLayout(self.menu_tab_frame)
        self.menu_tab_layout.setContentsMargins(15,10,15,10)
        self.menu_tab_layout.setSpacing(5)

        #Add widgets to Menu Tab Layout
        self.menu_tab_layout.addWidget(self.tabsCreater("Anasayfa",0))
        self.menu_tab_layout.addStretch()

        #Set Add Line
        self.gray_line_frame=QFrame()
        self.gray_line_frame.setObjectName("grayLine")


        #Add Widgets to Menu Layout
        self.menu_layout.addWidget(self.menu_title_frame)
        self.menu_layout.addWidget(self.menu_contents_frame)
        self.menu_layout.addWidget(self.menu_tab_frame)
        self.menu_layout.addWidget(self.gray_line_frame)

################### MENU BAR Finish #################################################
################### PAGES Start #####################################################

        
        
        
        self.page_frame=QStackedWidget()
        #self.pages=Ui_StackedWidget()
        #self.pages.setupUi(self.page_frame)
        self.page_frame.setObjectName("pageFrame")
        self.pageList.append(self.page_frame)
        















        # Add Widget to Container Layout
        self.container_layout.addWidget(self.top_frame)
        self.container_layout.addWidget(self.menu_frame)
        self.container_layout.addWidget(self.page_frame)
        self.container_layout.addSpacerItem(QSpacerItem(0,20,QSizePolicy.Minimum, QSizePolicy.Expanding))
        


        #orta widget set etme
        parent.setCentralWidget(self.container_frame)

        parent.showMaximized()
 


################### CLASS Finish ####################################################
################### FUNCTION Start ##################################################

    #Design property when click button of menu title
    def designPropertyTitle(self):
        self.changeContentsofMenu(self.MainWindow.sender().objectName())
        for key in self.menu_list.keys():
            if ( self.menu_list[key]["objeismi"]==self.MainWindow.sender().objectName() ):
                self.MainWindow.sender().setStyleSheet("background-color: #2C394B")
            else:
                self.MainWindow.findChild(QPushButton, "{}".format(self.menu_list[key]["objeismi"])).setStyleSheet("background-color: #082032;")
    
    #Change contents of menu when clicked button of menu title
    def changeContentsofMenu(self,secim):
        self.clearContentsofMenu(self.menu_contents_layout.count()-1)
        for i_key in self.menu_list[secim]["icerikler"].keys():
            self.i=buttonSpeacial(self.menu_list[secim]["icerikler"][i_key])
            self.i.clicked.connect(self.menuTitleAdd)
            self.menu_contents_layout.insertWidget(self.menu_contents_layout.count()-1,self.i)

    #Clear contents of menu when clicked button of menu title
    def clearContentsofMenu (self, uzunluk):
            for i in range(uzunluk):
                self.menu_contents_layout.itemAt(i).widget().deleteLater()


    # Tabs and Pages clear when click button of close button on tabs
    def tabsAndPagesClear(self):
        for i in  range(len(self.menuTitleList)):
            if int(self.menuTitleList[i]) == int(self.MainWindow.sender().objectName()):
                self.menu_tab_layout.itemAt(int(i+1) ).widget().deleteLater()
                self.menuTitleList.pop(i)
                self.pageList[i+1].deleteLater()
                self.pageList.pop(i+1)
                self.pageList[i].show()
                
                if (int(self.container_layout.count())==5 and i==0):
                    self.page_frame.show()
                    self.pageListActive=0
                break

    #Tab title create when click button of menu contents
    def tabsCreater(self, isim, numara, renk="#FF203451"):
        #Tab Frame
        self.tab_frame=QFrame()
        self.tab_frame.setObjectName("tabFrame")

        #Tab Layout
        self.tab_layout=QHBoxLayout(self.tab_frame)
        self.tab_layout.setContentsMargins(5,1,0,2)
        self.tab_layout.setSpacing(0)
        self.title=QLabel(isim)
        self.title.setObjectName("isim")
        

        self.tab_btn_cls=QPushButton()
        self.tab_btn_cls.setObjectName(str(numara))
        self.tab_btn_cls.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab_btn_cls.setStyleSheet(f"""
            border:0;
            background-image:url("gui/image/icon/close16.ico");
            background-repeat: no-repeat;
            background-color: #FF203451;
            background-position: center;
        """)
        self.addPage(isim)


        self.tab_btn_cls.clicked.connect(self.tabsAndPagesClear)
        self.tab_layout.addWidget(self.title)
        self.tab_layout.addWidget(self.tab_btn_cls)
        return self.tab_frame
            
    def menuTitleAdd(self):
        self.menuTabsNumber+=1
        self.menu_tab_layout.insertWidget(self.menu_tab_layout.count()-1,self.tabsCreater(self.MainWindow.sender().text(), self.menuTabsNumber))
        self.menuTitleList.append(self.menuTabsNumber)

    def addPage(self, isim):
        self.yeni=QStackedWidget()            
        if self.pageListActive!=0:
            self.pageList[self.pageListActive].hide()
        if isim=="İp":
            self.page_frame.hide()
            #self.page_frame=self.pageList[1]
            self.yeni_UI=Ui_StackedWidget()
            self.yeni_UI.setupUi(self.yeni) 
            self.container_layout.insertWidget(self.container_layout.count()-1,self.yeni)
            self.pageList.append(self.yeni)
            self.pageListActive+=1
        elif isim !="Anasayfa":
            self.page_frame.hide()
            #self.page_frame=self.pageList[1]
            self.yeni_UI=hazirlamaSayfasi()
            self.yeni_UI.setupUi(self.yeni) 
            self.container_layout.insertWidget(self.container_layout.count()-1,self.yeni)
            self.pageList.append(self.yeni)
            self.pageListActive+=1
        
    def deneme(self):
        pass

