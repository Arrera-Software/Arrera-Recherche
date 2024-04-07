#include "cuirecherche.h"
#include "ui_cuirecherche.h"
#include <QDesktopServices>
#include <QUrl>


CUIRecherche::CUIRecherche(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::CUIRecherche)
{
    bool sortieFile;
    fileConfig = "configRecherche.ini";
    ui->setupUi(this);
    arecherche = CArreraRecheche();
    wApropos = new CArreraApropos(this);
    ui->FPARAMETRE->setVisible(false);
    ui->IDC_LISTMOTEUR->setSelectionMode(QAbstractItemView::SingleSelection);
    connect(this,&CUIRecherche::destroyed,wApropos,&CUIRecherche::close);
    // Fichier parametre
    sortieFile = filePara.charger(fileConfig);
    if (!sortieFile)
    {
        filePara.creerFichierIni(fileConfig);
    }
}

CUIRecherche::~CUIRecherche()
{
    delete ui;
}

void CUIRecherche::on_IDC_DUCKDUCKGO_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchDuckduckgo(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_GOOGLE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchGoogle(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_BING_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchBing(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_BRAVE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchBrave(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_ECOSIA_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchEcosia(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_QWANT_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchQwant(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_GRECHERCHE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchAll(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_WIKIPEDIA_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchWikipedia(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_AMAZON_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchAmazon(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_WORKREFERENCE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchWordreference(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_YTMUSIC_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchYTmusic(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_REVERSO_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchReverso(query);
    ui->IDC_RECHERCHE->setText("");
}


void CUIRecherche::on_IDC_APROPOS_clicked()
{
    wApropos->show();
}


void CUIRecherche::on_IDC_RETOURMAIN_clicked()
{
    ui->FPARAMETRE->setVisible(false);
    ui->FRECHERCHE->setVisible(true);
    ui->FBTN->setVisible(true);
}


void CUIRecherche::on_IDC_PARA_clicked()
{
    ui->FRECHERCHE->setVisible(false);
    ui->FBTN->setVisible(false);
    ui->FPARAMETRE->setVisible(true);
}


void CUIRecherche::on_IDC_VALIDERMOTEUR_clicked()
{
    QListWidgetItem* item;
    item = ui->IDC_LISTMOTEUR->currentItem();
    if(item)
    {
        filePara.definirParametre("moteur",item->text().toStdString());
        filePara.sauvegarder(fileConfig);
        on_IDC_RETOURMAIN_clicked();
    }
}

