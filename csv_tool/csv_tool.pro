#-------------------------------------------------
#
# Project created by QtCreator 2015-12-19T12:06:44
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = csv_tool
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += \
    view.ui

OTHER_FILES += \
    python/controller.py \
    python/main.py
