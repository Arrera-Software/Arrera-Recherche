#include "carrerarecherchehist.h"

CArreraRechercheHist::CArreraRechercheHist()
{
    filePath = "hist.txt";
}


bool CArreraRechercheHist::add(QString valeur)
{
    QFile file(filePath);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Append))
    {
        return false;
    }
    QTextStream out(&file);
    out << valeur << Qt::endl;
    file.close();
    return true;
}

bool CArreraRechercheHist::clear()
{
    QFile file(filePath);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
        return false;
    }

    // Fermer le fichier après l'avoir ouvert en mode écriture
    file.close();
    return true;
}
