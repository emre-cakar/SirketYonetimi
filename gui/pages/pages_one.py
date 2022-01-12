from qt_core import *
from gui.widgets.app_widgets import  *

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):

        #Variable
        self.stacked=StackedWidget
        self.sayfanumarasi=0
    
################### Variable Finish #################################################
################### PAGE-1 Start ####################################################

        self.sayfa1=QWidget()
        self.sayfa1.setObjectName(u"islemTuru")
        self.sayfa1.setStyleSheet("""
            margin:25px;
            background-color:#2C394B;
            border:1px solid #3498db;
        """)
        self.sayfa1_layout=QHBoxLayout()
        self.sayfa1_layout.setContentsMargins(0,0,0,0)
        self.sayfa1_layout.setSpacing(0)
        self.sayfa1.setLayout(self.sayfa1_layout)

        self.sayfa1_sol=QPushButton()
        self.sayfa1_sol.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            background-image: url('gui/image/icon/double_left128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0;
        """)
        self.sayfa1_sol.setCursor(QCursor(Qt.PointingHandCursor))
        self.center_Layout=QVBoxLayout()

        
        self.baslik=QLabel(self.sayfa1)
        self.baslik.setText("İŞLEMİNİZ")
        self.baslik.setStyleSheet("""
            padding-bottom:20px;
            border:0;
            border-bottom:1px solid #3498db;
            font-size:40pt;
            color:white;
            font-family:"Times New Roman";
            letter-spacing:15px;
        """)
        self.baslik.setAlignment(Qt.AlignCenter)

        self.contentLayout=QVBoxLayout()
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.contentLayout.setSpacing(10)
        
        self.secenek1_Layout=QHBoxLayout()
        self.secenek1_Layout.setContentsMargins(0,0,0,0)
        self.secenek1_Layout.setSpacing(0)
        self.islem1=QPushButton("SATIŞ")
        self.islem1.setObjectName("satis")
        self.islem1.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem1.setStyleSheet("""
            QPushButton{
                max-width:650px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QPushButton:hover{
                background-color: #3498db;
            }
        """)
        self.secenek1_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.secenek1_Layout.addWidget(self.islem1)
        self.secenek1_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.secenek2_Layout=QHBoxLayout()
        self.secenek2_Layout.setContentsMargins(0,0,0,0)
        self.secenek2_Layout.setSpacing(0)
        self.islem2=QPushButton("ALIŞ")
        self.islem2.setObjectName("alis")
        self.islem2.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem2.setStyleSheet("""
            QPushButton{
                max-width:650px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QPushButton:hover{
                background-color: #3498db;
            }
        """)
        self.secenek2_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.secenek2_Layout.addWidget(self.islem2)
        self.secenek2_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.secenek3_Layout=QHBoxLayout()
        self.secenek3_Layout.setContentsMargins(0,0,0,0)
        self.secenek3_Layout.setSpacing(0)
        self.islem3=QPushButton("SATIŞ İADE")
        self.islem3.setObjectName("satisIade")
        self.islem3.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem3.setStyleSheet("""
            QPushButton{
                max-width:650px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QPushButton:hover{
                background-color: #3498db;
            }
        """)
        self.secenek3_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.secenek3_Layout.addWidget(self.islem3)
        self.secenek3_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.secenek4_Layout=QHBoxLayout()
        self.secenek4_Layout.setContentsMargins(0,0,0,0)
        self.secenek4_Layout.setSpacing(0)
        self.islem4=QPushButton("ALIŞ İADE")
        self.islem4.setObjectName("alisIade")
        self.islem4.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem4.setStyleSheet("""
            QPushButton{
                max-width:650px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QPushButton:hover{
                background-color: #3498db;
            }
        """)
        self.secenek4_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.secenek4_Layout.addWidget(self.islem4)
        self.secenek4_Layout.addItem(QSpacerItem(350,0,QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.contentLayout.addStretch()
        self.contentLayout.addLayout(self.secenek1_Layout)
        self.contentLayout.addLayout(self.secenek2_Layout)
        self.contentLayout.addLayout(self.secenek3_Layout)
        self.contentLayout.addLayout(self.secenek4_Layout)
        self.contentLayout.addStretch()

        self.rd_sheets_layout=QHBoxLayout()
        self.rd_sheets_layout.setContentsMargins(0,0,0,0)
        self.rd_sheets_layout.setSpacing(0)
        self.rd_sheets_layout.addItem(QSpacerItem(550,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        for i in range(7):
            self.rd_sheets1=QRadioButton(self.sayfa1)
            self.rd_sheets1.setStyleSheet("border:0; margin:0;")
            if (i==0):
                self.rd_sheets1.setChecked(True)
            else:
                self.rd_sheets1.setCheckable(False)
            self.rd_sheets_layout.addWidget(self.rd_sheets1)
        self.rd_sheets_layout.addItem(QSpacerItem(450,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        

        self.center_Layout.addSpacing(20)
        self.center_Layout.addWidget(self.baslik)
        self.center_Layout.addItem(QSpacerItem(100,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.center_Layout.addLayout(self.contentLayout)
        self.center_Layout.addItem(QSpacerItem(100,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.center_Layout.addLayout(self.rd_sheets_layout)
        self.center_Layout.addSpacing(50)

        self.sayfa1_sag=QPushButton()
        self.sayfa1_sag.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            min-height:128px;
            background-image: url('gui/image/icon/double_right128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0px;
        """)
        self.sayfa1_sag.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayfa1_sag.clicked.connect(self.ileri)

        self.sayfa1_layout.addSpacing(20)
        self.sayfa1_layout.addWidget(self.sayfa1_sol)
        self.sayfa1_layout.addSpacing(20)
        self.sayfa1_layout.addLayout(self.center_Layout)
        self.sayfa1_layout.addSpacing(20)
        self.sayfa1_layout.addWidget(self.sayfa1_sag)
        self.sayfa1_layout.addSpacing(20)

        StackedWidget.addWidget(self.sayfa1)
        
################### PAGE-1 Finish ###################################################
################### PAGE-2 Start ####################################################
        
        self.sayfa2=QWidget()
        self.sayfa2.setObjectName(u"birimveTarih")
        self.sayfa2.setStyleSheet("""
            margin:25px;
            background-color:#2C394B;
            border:1px solid #3498db;
        """)
        self.sayfa2_layout=QHBoxLayout()
        self.sayfa2_layout.setContentsMargins(0,0,0,0)
        self.sayfa2_layout.setSpacing(0)
        self.sayfa2.setLayout(self.sayfa2_layout)

        self.sayfa2_sol=QPushButton()
        self.sayfa2_sol.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            min-width:100px;
            background-image: url('gui/image/icon/double_left128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0;
        """)
        self.sayfa2_sol.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayfa2_sol.clicked.connect(self.geri)
        self.center_Layout=QVBoxLayout()
        
        
        self.baslik=QLabel(self.sayfa2)
        self.baslik.setText("PARA BİRİMİ")
        self.baslik.setStyleSheet("""
            padding-bottom:20px;
            border:0;
            border-bottom:1px solid #3498db;
            font-size:40pt;
            color:white;
            font-family:"Times New Roman";
            letter-spacing:15px;
        """)
        self.baslik.setAlignment(Qt.AlignCenter)

        self.contentLayout=QHBoxLayout()
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.contentLayout.setSpacing(10)

        self.islem1=QRadioButton(" ( ₺ ) Türk Lirası")
        self.islem1.setObjectName("lira")
        self.islem1.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem1.setStyleSheet("""
            QRadioButton{
                min-width:350px;
                max-width:350px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QRadioButton:hover{
                background-color: #3498db;
            }
        """)
        self.islem2=QRadioButton(" ( $ ) Dolar")
        self.islem2.setObjectName("usd")
        self.islem2.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem2.setStyleSheet("""
            QRadioButton{
                min-width:350px;
                max-width:350px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QRadioButton:hover{
                background-color: #3498db;
            }
        """)
        self.islem3=QRadioButton("( € ) Euro")
        self.islem3.setObjectName("eur")
        self.islem3.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem3.setStyleSheet("""
            QRadioButton{
                min-width:350px;
                max-width:350px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QRadioButton:hover{
                background-color: #3498db;
            }
        """)


        self.contentLayout.addStretch()
        self.contentLayout.addWidget(self.islem1)
        self.contentLayout.addWidget(self.islem2)
        self.contentLayout.addWidget(self.islem3)
        self.contentLayout.addStretch()


        self.baslik2=QLabel()
        self.baslik2.setText("TARİH")
        self.baslik2.setStyleSheet("""
            padding-bottom:20px;
            border:0;
            border-bottom:1px solid #3498db;
            font-size:40pt;
            color:white;
            font-family:"Times New Roman";
            letter-spacing:15px;
        """)
        self.baslik2.setAlignment(Qt.AlignCenter)

        self.cal_layout=QHBoxLayout()
        self.cal = QCalendarWidget()
        self.cal.setMaximumSize(365,400)
        self.cal.setMinimumSize(365,400)
        self.cal.setGridVisible(True)
        date = self.cal.selectedDate()
        self.cal_layout.addStretch()
        self.cal_layout.addWidget(self.cal)
        self.cal_layout.addStretch()
        






        self.rd_sheets_layout=QHBoxLayout()
        self.rd_sheets_layout.setContentsMargins(0,0,0,0)
        self.rd_sheets_layout.setSpacing(0)
        self.rd_sheets_layout.addItem(QSpacerItem(550,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        for i in range(7):
            self.rd_sheets1=QRadioButton(self.sayfa2)
            self.rd_sheets1.setStyleSheet("border:0; margin:0;")
            if (i==1):
                self.rd_sheets1.setChecked(True)
            else:
                self.rd_sheets1.setCheckable(False)
            self.rd_sheets_layout.addWidget(self.rd_sheets1)
        self.rd_sheets_layout.addItem(QSpacerItem(450,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        

        self.center_Layout.addSpacing(20)
        self.center_Layout.addWidget(self.baslik)
        self.center_Layout.addLayout(self.contentLayout)
        self.center_Layout.addWidget(self.baslik2)
        self.center_Layout.addLayout(self.cal_layout)
        self.center_Layout.addItem(QSpacerItem(100,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.center_Layout.addLayout(self.rd_sheets_layout)
        self.center_Layout.addSpacing(50)

        self.sayfa2_sag=QPushButton()
        self.sayfa2_sag.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            min-width:100px;
            min-height:128px;
            background-image: url('gui/image/icon/double_right128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0px;
        """)
        self.sayfa2_sag.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayfa2_sag.clicked.connect(self.ileri)

        self.sayfa2_layout.addSpacing(20)
        self.sayfa2_layout.addWidget(self.sayfa2_sol)
        self.sayfa2_layout.addSpacing(20)
        self.sayfa2_layout.addLayout(self.center_Layout)
        self.sayfa2_layout.addSpacing(20)
        self.sayfa2_layout.addWidget(self.sayfa2_sag)
        self.sayfa2_layout.addSpacing(20)

        StackedWidget.addWidget(self.sayfa2)


################### PAGE-2 Finish ###################################################
################### PAGE-3 Start ####################################################


        self.sayfa3=QWidget()
        self.sayfa3.setObjectName(u"sirket")
        self.sayfa3.setStyleSheet("""
            margin:25px;
            background-color:#2C394B;
            border:1px solid #3498db;
        """)
        self.sayfa3_layout=QHBoxLayout()
        self.sayfa3_layout.setContentsMargins(0,0,0,0)
        self.sayfa3_layout.setSpacing(0)
        self.sayfa3.setLayout(self.sayfa3_layout)

        self.sayfa3_sol=QPushButton()
        self.sayfa3_sol.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            background-image: url('gui/image/icon/double_left128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0;
        """)
        self.sayfa3_sol.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayfa3_sol.clicked.connect(self.geri)
        self.center_Layout=QVBoxLayout()

        
        self.baslik=QLabel(self.sayfa3)
        self.baslik.setText("ŞİRKET")
        self.baslik.setStyleSheet("""
            padding-bottom:20px;
            border:0;
            border-bottom:1px solid #3498db;
            font-size:40pt;
            color:white;
            font-family:"Times New Roman";
            letter-spacing:15px;
        """)
        self.baslik.setAlignment(Qt.AlignCenter)

        self.contentLayout=QVBoxLayout()
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.contentLayout.setSpacing(10)
        
        self.secenek1_Layout=QHBoxLayout()
        self.secenek1_Layout.setContentsMargins(0,0,0,0)
        self.secenek1_Layout.setSpacing(0)
        self.islem1=QComboBox()
        self.islem1.setObjectName("sirketSecimi")
        self.islem1.setCursor(QCursor(Qt.PointingHandCursor))
        self.islem1.setStyleSheet("""
            QComboBox{
            
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QComboBox:hover{
                background-color: #3498db;
            }
        """)
        self.islem1.addItems([
            'NoInsert',
            'InsertAtTop',
            'InsertAtCurrent',
            'InsertAtBottom',
            'InsertAfterCurrent',
            'InsertBeforeCUrrent',
            'InsertAtCurrent',
            'InsertAtBottom',
            'InsertAfterCurrent',
            'InsertBeforeCUrrent',
            'InsertAlphabetically'
        ])
        self.secenek1_Layout.addItem(QSpacerItem(100,0,QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.secenek1_Layout.addWidget(self.islem1)
        self.secenek1_Layout.addItem(QSpacerItem(100,0,QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.contentLayout.addStretch()
        self.contentLayout.addLayout(self.secenek1_Layout)
        self.contentLayout.addStretch()

        self.rd_sheets_layout=QHBoxLayout()
        self.rd_sheets_layout.setContentsMargins(0,0,0,0)
        self.rd_sheets_layout.setSpacing(0)
        self.rd_sheets_layout.addItem(QSpacerItem(550,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        for i in range(7):
            self.rd_sheets1=QRadioButton(self.sayfa3)
            self.rd_sheets1.setStyleSheet("border:0; margin:0;")
            if (i==2):
                self.rd_sheets1.setChecked(True)
            else:
                self.rd_sheets1.setCheckable(False)
            self.rd_sheets_layout.addWidget(self.rd_sheets1)
        self.rd_sheets_layout.addItem(QSpacerItem(450,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        

        self.center_Layout.addSpacing(20)
        self.center_Layout.addWidget(self.baslik)
        self.center_Layout.addItem(QSpacerItem(100,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.center_Layout.addLayout(self.contentLayout)
        self.center_Layout.addItem(QSpacerItem(100,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.center_Layout.addLayout(self.rd_sheets_layout)
        self.center_Layout.addSpacing(50)

        self.sayfa3_sag=QPushButton()
        self.sayfa3_sag.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            min-height:128px;
            background-image: url('gui/image/icon/double_right128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0px;
        """)
        self.sayfa3_sag.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayfa3_sag.clicked.connect(self.ileri)

        self.sayfa3_layout.addSpacing(20)
        self.sayfa3_layout.addWidget(self.sayfa3_sol)
        self.sayfa3_layout.addSpacing(20)
        self.sayfa3_layout.addLayout(self.center_Layout)
        self.sayfa3_layout.addSpacing(20)
        self.sayfa3_layout.addWidget(self.sayfa3_sag)
        self.sayfa3_layout.addSpacing(20)

        StackedWidget.addWidget(self.sayfa3)




################### PAGE-3 Finish ###################################################
################### PAGE-4 Start ####################################################


        self.sayfa3=QWidget()
        self.sayfa3.setObjectName(u"malzeme")
        self.sayfa3.setStyleSheet("""
            margin:25px;
            background-color:#2C394B;
            border:1px solid #3498db;
        """)
        self.sayfa3_layout=QHBoxLayout()
        self.sayfa3_layout.setContentsMargins(0,0,0,0)
        self.sayfa3_layout.setSpacing(0)
        self.sayfa3.setLayout(self.sayfa3_layout)

        self.sayfa3_sol=QPushButton()
        self.sayfa3_sol.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            min-width:100px;
            background-image: url('gui/image/icon/double_left128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0;
        """)
        self.sayfa3_sol.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayfa3_sol.clicked.connect(self.geri)
        self.center_Layout=QVBoxLayout()
        self.center_Layout.setContentsMargins(0,0,0,0)
        self.center_Layout.setSpacing(0)
        
        self.baslik=QLabel(self.sayfa3)
        self.baslik.setText("MALZEME")
        self.baslik.setStyleSheet("""
            padding-bottom:20px;
            border:0;
            border-bottom:1px solid #3498db;
            font-size:40pt;
            color:white;
            font-family:"Times New Roman";
            letter-spacing:15px;
        """)
        self.baslik.setAlignment(Qt.AlignCenter)

        self.contentLayout=QVBoxLayout()
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.contentLayout.setSpacing(15)

############
        self.secenek1_Layout=QHBoxLayout()
        self.secenek1_Layout.setContentsMargins(0,0,0,0)
        self.secenek1_Layout.setSpacing(5)

        
        self.secenek_sutun_Layout1=QVBoxLayout()
        self.secenek_sutun_Layout1.setContentsMargins(0,0,0,0)
        self.secenek_sutun_Layout1.setSpacing(0)
        self.tur=QLabel("Tür")
        self.tur.setAlignment(Qt.AlignCenter)
        self.tur.setStyleSheet("""
            max-height:10px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.tur_giris=QComboBox()
        self.tur_giris.setStyleSheet("""
            max-height:20px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.tur_giris.addItems(
          ['İp',"Kumaş","Likra"]  
        )
        self.secenek_sutun_Layout1.addWidget(self.tur)
        self.secenek_sutun_Layout1.addWidget(self.tur_giris)


        self.secenek_sutun_Layout2=QVBoxLayout()
        self.secenek_sutun_Layout2.setContentsMargins(0,0,0,0)
        self.secenek_sutun_Layout2.setSpacing(0)
        self.malzeme=QLabel("Malzeme")
        self.malzeme.setAlignment(Qt.AlignCenter)
        self.malzeme.setStyleSheet("""
            max-height:10px;
            min-width:750px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.malzeme_secim=QComboBox()
        self.malzeme_secim.setStyleSheet("""
            max-height:20px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.secenek_sutun_Layout2.addWidget(self.malzeme)
        self.secenek_sutun_Layout2.addWidget(self.malzeme_secim)


        self.secenek_sutun_Layout3=QVBoxLayout()
        self.secenek_sutun_Layout3.setContentsMargins(0,0,0,0)
        self.secenek_sutun_Layout3.setSpacing(0)
        self.adet=QLabel("Adet/Top")
        self.adet.setAlignment(Qt.AlignCenter)
        self.adet.setStyleSheet("""
            max-height:10px;
            max-width:150px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.adet_giris=QLineEdit()
        self.adet_giris.setStyleSheet("""
            max-height:20px;
            max-width:150px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.secenek_sutun_Layout3.addWidget(self.adet)
        self.secenek_sutun_Layout3.addWidget(self.adet_giris)



        self.secenek_sutun_Layout4=QVBoxLayout()
        self.secenek_sutun_Layout4.setContentsMargins(0,0,0,0)
        self.secenek_sutun_Layout4.setSpacing(0)
        self.netKilo=QLabel("NetKilo")
        self.netKilo.setAlignment(Qt.AlignCenter)
        self.netKilo.setStyleSheet("""
            max-height:10px;
            max-width:150px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.netKilo_giris=QLineEdit()
        self.netKilo_giris.setStyleSheet("""
            max-height:20px;
            max-width:150px;
            color:white;
            font-size:10pt;
            border:0px;
            margin:0px;
            border-bottom:1px solid #3498db;
        """)
        self.secenek_sutun_Layout4.addWidget(self.netKilo)
        self.secenek_sutun_Layout4.addWidget(self.netKilo_giris)

        
        self.secenek_sutun_Layout5=QVBoxLayout()
        self.secenek_sutun_Layout5.setContentsMargins(0,0,0,0)
        self.secenek_sutun_Layout5.setSpacing(0)
        self.ekleme=QPushButton("EKLE")
        self.ekleme.setStyleSheet("""
            QPushButton{
                max-width:650px;
                color:white;
                font-size:30px;
                letter-spacing:5px;
                padding:20px;
                border-radius:15px;
                margin:0;
            }
            QPushButton:hover{
                background-color: #3498db;
            }
            
        """)
        self.ekleme.setCursor(QCursor(Qt.PointingHandCursor))
        self.secenek_sutun_Layout5.addWidget(self.ekleme)

        self.secenek1_Layout.addItem(QSpacerItem(0,0,QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.secenek1_Layout.addLayout(self.secenek_sutun_Layout1)
        self.secenek1_Layout.addLayout(self.secenek_sutun_Layout2)
        self.secenek1_Layout.addLayout(self.secenek_sutun_Layout3)
        self.secenek1_Layout.addLayout(self.secenek_sutun_Layout4)
        self.secenek1_Layout.addLayout(self.secenek_sutun_Layout5)
        self.secenek1_Layout.addItem(QSpacerItem(0,0,QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.table = QTableWidget()
        self.table.setStyleSheet("""
            background-color:white;
            margin:0;
            padding:0;
            color:black;
            border:1px;
        """)
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["No", "Malzeme", "Adet/Top", "Net"])
        self.header = self.table.horizontalHeader()
        self.header.setStyleSheet("color:red;")
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.vh=self.table.verticalHeader()
        self.vh.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.contentLayout.addSpacing(50)
        self.contentLayout.addLayout(self.secenek1_Layout)
        self.contentLayout.addSpacing(80)
        self.contentLayout.addWidget(self.table)

        self.contentLayout.addStretch()




############
        self.rd_sheets_layout=QHBoxLayout()
        self.rd_sheets_layout.setContentsMargins(0,0,0,0)
        self.rd_sheets_layout.setSpacing(0)
        self.rd_sheets_layout.addItem(QSpacerItem(550,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        for i in range(7):
            self.rd_sheets1=QRadioButton(self.sayfa3)
            self.rd_sheets1.setStyleSheet("border:0; margin:0;")
            if (i==3):
                self.rd_sheets1.setChecked(True)
            else:
                self.rd_sheets1.setCheckable(False)
            self.rd_sheets_layout.addWidget(self.rd_sheets1)
        self.rd_sheets_layout.addItem(QSpacerItem(450,0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        

        self.center_Layout.addSpacing(20)
        self.center_Layout.addWidget(self.baslik)
        self.center_Layout.addLayout(self.contentLayout)
        self.center_Layout.addStretch()
        self.center_Layout.addLayout(self.rd_sheets_layout)
        self.center_Layout.addSpacing(50)

        self.sayfa3_sag=QPushButton()
        self.sayfa3_sag.setStyleSheet(f"""
            min-height:128px;
            max-width:100px;
            min-width:100px;
            min-height:128px;
            background-image: url('gui/image/icon/double_right128.png');
            background-repeat: no-repeat;
            background-position: center;
            border:0px;
        """)
        self.sayfa3_sag.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayfa3_sag.clicked.connect(self.ileri)

        self.sayfa3_layout.addSpacing(20)
        self.sayfa3_layout.addWidget(self.sayfa3_sol)
        self.sayfa3_layout.addSpacing(20)
        self.sayfa3_layout.addLayout(self.center_Layout)
        self.sayfa3_layout.addSpacing(20)
        self.sayfa3_layout.addWidget(self.sayfa3_sag)
        self.sayfa3_layout.addSpacing(20)

        StackedWidget.addWidget(self.sayfa3)



################### PAGE-4 Finish ###################################################
################### PAGE-5 Start ####################################################


################### PAGE-5 Finish ###################################################
################### SETTING Start ###################################################

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def geri(self):
        self.sayfanumarasi-=1
        self.stacked.setCurrentIndex(self.sayfanumarasi)
    def ileri(self):
        self.sayfanumarasi+=1
        self.stacked.setCurrentIndex(self.sayfanumarasi)


