from qt_core import *
from gui.widgets.app_widgets import  *
class Ip_Page(QFrame):
    def setupUi(self, app_page):
        self.kapsayici=app_page

        self.kapsayici_Layout=QHBoxLayout(self.kapsayici)
        self.kapsayici_Layout.setContentsMargins(30,0,30,0)
        self.kapsayici_Layout.setSpacing(10)

        self.sol_menu=QFrame()
        self.sol_menu.setStyleSheet("background-color:white;")

        op=QGraphicsOpacityEffect(self)
        op.setOpacity(0.70) #0 to 1 will cause the fade effect to kick in
        self.sol_menu.setGraphicsEffect(op)
        self.sol_menu.setAutoFillBackground(True)

        self.sol_menu_Layout=QVBoxLayout(self.sol_menu)
        self.sol_menu_Layout.setContentsMargins(0,0,0,0)
        self.sol_menu_Layout.setSpacing(10)

        self.sm_islemTuru=QHBoxLayout()
        
        self.sm_islemTuru_Lbl=QLabel("İşlem Türü : ")
        self.sm_islemTuru_Lbl.setStyleSheet("min-width:50px;")
        self.sm_islemTuru_group=QGridLayout()
        self.sm_islemTuru_secenek1=QRadioButton("SATIŞ")
        self.sm_islemTuru_secenek2=QRadioButton("ALIŞ")
        self.sm_islemTuru_secenek3=QRadioButton("SATIŞ İPTAL")
        self.sm_islemTuru_secenek4=QRadioButton("SATIŞ İPTAL")
        self.sm_islemTuru_group.addWidget(self.sm_islemTuru_secenek1,0,0)
        self.sm_islemTuru_group.addWidget(self.sm_islemTuru_secenek2,0,1)
        self.sm_islemTuru_group.addWidget(self.sm_islemTuru_secenek3,0,2)
        self.sm_islemTuru_group.addWidget(self.sm_islemTuru_secenek4,0,3)
        
        self.takvim=QFrame()
        self.getTakvim=Takvim()
        self.getTakvim.setupUi(self.takvim)

        

        self.sm_islemTuru.addWidget(self.sm_islemTuru_Lbl)
        self.sm_islemTuru.addLayout(self.sm_islemTuru_group)
        self.sm_islemTuru.addStretch()
        self.sm_islemTuru.addWidget(self.takvim)

       



        self.sol_menu_Layout.addLayout(self.sm_islemTuru)
        self.sol_menu_Layout.addStretch()




        
        self.sag_menu=QFrame()
        self.sag_menu.setStyleSheet("background-color:red;min-width:450px;")
        self.sag_menu_frame=QVBoxLayout(self.sag_menu)



        self.kapsayici_Layout.addWidget(self.sol_menu)
        self.kapsayici_Layout.addWidget(self.sag_menu)



