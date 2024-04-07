#ifndef CARRERARECHERCHEHIST_H
#define CARRERARECHERCHEHIST_H
#include <QFile>
#include <QTextStream>
#include <QDebug>

class CArreraRechercheHist
{
private :
    QString filePath;

public:
    CArreraRechercheHist();
    bool add(QString valeur);
    bool clear();
};

#endif // CARRERARECHERCHEHIST_H
