#ifndef CUIRECHERCHE_H
#define CUIRECHERCHE_H

#include <QMainWindow>

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

private:
    Ui::CUIRecherche *ui;
};
#endif // CUIRECHERCHE_H
