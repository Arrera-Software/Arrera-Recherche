#ifndef CUIRECHERCHE_H
#define CUIRECHERCHE_H

#include <QMainWindow>
#include "carrerarecheche.h"
#include "carreraapropos.h"
#include "CConfiguration.h"
#include "carrerarecherchehist.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class CUIRecherche;
}
QT_END_NAMESPACE

class CUIRecherche : public QMainWindow
{
    Q_OBJECT

public:
    CUIRecherche(QWidget *parent = nullptr);
    ~CUIRecherche();

private slots:
    void on_IDC_DUCKDUCKGO_clicked();

    void on_IDC_GOOGLE_clicked();

    void on_IDC_BING_clicked();

    void on_IDC_BRAVE_clicked();

    void on_IDC_ECOSIA_clicked();

    void on_IDC_QWANT_clicked();

    void on_IDC_GRECHERCHE_clicked();

    void on_IDC_WIKIPEDIA_clicked();

    void on_IDC_AMAZON_clicked();

    void on_IDC_WORKREFERENCE_clicked();

    void on_IDC_YTMUSIC_clicked();

    void on_IDC_REVERSO_clicked();

    void on_IDC_APROPOS_clicked();

    void on_IDC_RETOURMAIN_clicked();

    void on_IDC_PARA_clicked();

    void on_IDC_VALIDERMOTEUR_clicked();

    void on_IDC_VALIDERRECHERCHE_clicked();

    void on_IDC_CLEARHIST_clicked();

    void on_IDC_RETOURMAINHIST_clicked();

    void on_IDC_HIST_clicked();

private:
    Ui::CUIRecherche *ui;
    string fileConfig ;
    CArreraRecheche arecherche;
    CArreraApropos* wApropos;
    Cconfiguration filePara;
    CArreraRechercheHist ahistorique;
};
#endif // CUIRECHERCHE_H
