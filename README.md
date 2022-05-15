# Pacman
Pac-Man raha edition:

Pac-Man on sokkelopeli, jossa Pac-Man-niminen keltainen pallo syö pisteitä ja erilaisia raha-palkintoja. Kentällä liikkuu myös haamuja, jotka yrittävät saada Pac-Manin kiinni. Jokainen kenttä alkaa tilanteesta, jossa aaveet ovat lähtöruudussaan ja Pac-Man sokkelossa omalla paikallaan. Tavoitteena on kerätä Pac-Manille mahdollisimman paljon rahaa, vältellessä haamuja. Pac-Manilla on vain muutama elämä, jotka vähenevät kerta kerralta osuessa haamuihin. Auta Pac-Mania keräämään kadottamansa rahat.
## Dokumentaatiot

[vaatimusmaarittely.md](https://github.com/nicolaskivimaki/ot-harjoitustyo2/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/nicolaskivimaki/ot-harjoitustyo2/blob/main/dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri.md](https://github.com/nicolaskivimaki/ot-harjoitustyo2/blob/main/dokumentaatio/arkkitehtuuri.md)

[changelog.md](https://github.com/nicolaskivimaki/ot-harjoitustyo2/blob/main/dokumentaatio/changelog.md)

[releases](https://github.com/nicolaskivimaki/ot-harjoitustyo2/releases)

[kayttoohje](https://github.com/nicolaskivimaki/ot-harjoitustyo2/blob/main/dokumentaatio/kayttoohje.md)


## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan poetry shell ympäristössä hakemistossa ot-harjoitustyo/pacman-app seuraavalla komennolla:

```bash
poetry run invoke start
```


### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Pylintin voi generoida komennolla:

```bash
poetry run invoke pylint
```
