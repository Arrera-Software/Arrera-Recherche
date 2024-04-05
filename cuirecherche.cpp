#include "cuirecherche.h"
#include "ui_cuirecherche.h"
#include <QDesktopServices>
#include <QUrl>


CUIRecherche::CUIRecherche(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::CUIRecherche)
{
    ui->setupUi(this);
}

CUIRecherche::~CUIRecherche()
{
    delete ui;
}

void CUIRecherche::on_IDC_DUCKDUCKGO_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_GOOGLE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_BING_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_BRAVE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_ECOSIA_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_QWANT_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_GRECHERCHE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_WIKIPEDIA_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_AMAZON_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_WORKREFERENCE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_YTMUSIC_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_REVERSO_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    ui->IDC_RECHERCHE->setText("");
}

