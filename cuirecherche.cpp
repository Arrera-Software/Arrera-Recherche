#include "cuirecherche.h"
#include "ui_cuirecherche.h"

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
