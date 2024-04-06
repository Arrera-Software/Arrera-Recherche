#include "carreraapropos.h"
#include "./ui_carreraapropos.h"
#include <QDesktopServices>
#include <QUrl>

CArreraApropos::CArreraApropos(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::CArreraApropos)
{
    ui->setupUi(this);
}

CArreraApropos::~CArreraApropos()
{
    delete ui;
}

void CArreraApropos::on_IDC_SOURCE_clicked()
{
    QDesktopServices::openUrl(QUrl("https://github.com/Arrera-Software/Arrera-Recherche"));
}


void CArreraApropos::on_IDC_QUIT_clicked()
{
    this->close();
}

