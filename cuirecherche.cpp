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
    ahistorique = CArreraRechercheHist();
    wApropos = new CArreraApropos(this);
    ui->FPARAMETRE->setVisible(false);
    ui->FHIST->setVisible(false);
    ui->IDC_THIST->setReadOnly(true);
    connect(this,&CUIRecherche::destroyed,wApropos,&CUIRecherche::close);
    // Fichier parametre
    sortieFile = filePara.charger(fileConfig);
    if (!sortieFile)
    {
        filePara.creerFichierIni(fileConfig);
        filePara.definirParametre("moteur","google");
        filePara.sauvegarder(fileConfig);
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
    ahistorique.add("duck->"+query);
}


void CUIRecherche::on_IDC_GOOGLE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchGoogle(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("google->"+query);
}


void CUIRecherche::on_IDC_BING_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchBing(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("bing->"+query);
}


void CUIRecherche::on_IDC_BRAVE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchBrave(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("brave->"+query);
}


void CUIRecherche::on_IDC_ECOSIA_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchEcosia(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("ecosia->"+query);
}


void CUIRecherche::on_IDC_QWANT_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchQwant(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("qwant->"+query);
}


void CUIRecherche::on_IDC_GRECHERCHE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchAll(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("grand recherche->"+query);
}


void CUIRecherche::on_IDC_WIKIPEDIA_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchWikipedia(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("wikipedia->"+query);
}


void CUIRecherche::on_IDC_AMAZON_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchAmazon(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("amazon->"+query);
}


void CUIRecherche::on_IDC_WORKREFERENCE_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchWordreference(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("workreference->"+query);
}


void CUIRecherche::on_IDC_YTMUSIC_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchYTmusic(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("ytmusic->"+query);
}


void CUIRecherche::on_IDC_REVERSO_clicked()
{
    QString query = ui->IDC_RECHERCHE->toPlainText();
    arecherche.searchReverso(query);
    ui->IDC_RECHERCHE->setText("");
    ahistorique.add("reverso->"+query);
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
    QString moteurSelectionner = ui->IDC_LISTMOTEUR->currentText();
    filePara.definirParametre("moteur",moteurSelectionner.toStdString());
    filePara.sauvegarder(fileConfig);
    on_IDC_RETOURMAIN_clicked();
}


void CUIRecherche::on_IDC_VALIDERRECHERCHE_clicked()
{
    string moteur = filePara.obtenirParametre("moteur");
    if (moteur=="google")
    {
        on_IDC_GOOGLE_clicked();
    }
    else
    {
        if (moteur=="Bing")
        {
            on_IDC_BING_clicked();
        }
        else
        {
            if (moteur=="duckduckgo")
            {
                on_IDC_DUCKDUCKGO_clicked();
            }
            else
            {
                if(moteur=="Ecosia")
                {
                    on_IDC_ECOSIA_clicked();
                }
                else
                {
                    if(moteur=="Brave")
                    {
                        on_IDC_BRAVE_clicked();
                    }
                    else
                    {
                        if (moteur=="Qwant")
                        {
                            on_IDC_QWANT_clicked();
                        }
                        else
                        {
                            on_IDC_GOOGLE_clicked();
                        }
                    }
                }
            }
        }
    }
}


void CUIRecherche::on_IDC_CLEARHIST_clicked()
{
    ahistorique.clear();
}


void CUIRecherche::on_IDC_RETOURMAINHIST_clicked()
{
    ui->FHIST->setVisible(false);
    ui->FRECHERCHE->setVisible(true);
    ui->FBTN->setVisible(true);
}


void CUIRecherche::on_IDC_HIST_clicked()
{
    ui->FHIST->setVisible(true);
    ui->FRECHERCHE->setVisible(false);
    ui->FBTN->setVisible(false);
    ui->IDC_THIST->setPlainText(ahistorique.read());
}

