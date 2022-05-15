# Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Aloitusnäyttö
- Pelaaminen
- Lopetusnäyttö

```mermaid
classDiagram
  Aloitusnaytto--|>Peli
  Peli--|>Lopetus
 
  class Aloitusnaytto{
    aloita_peli()
   
   }
  class Peli{
    pelaa()
  }
 
  class Lopetus{
    lopeta_peli()
  }
```
Jokainen näistä näkymistä on toteutettu omina luokkinaan. Näkymistä pääsee siirtymään erinlaisilla näppäimistö komennuksilla. Sovelluksen näkymä muokkaantuu pelin kulkiessa.

# Pelin rakenteita

```mermaid
classDiagram
src--Features
Features--Assets
Assets--Sprites
Sprites--Tests
class Features{
    

  }
  class Assets{
    

  }
  class Sprites{
    

  }
  class Tests{
    

  }
  class src{
    

  }

```
# Rakennelogiikka

Rakennuslogiikan avulla ohjelman järjestelmällisyys pysyy järkevänä. Näin eri luokituksille suunnatut kansiot auttavat kuvastamaan niihin sisällettyjä tiedostoja.

# Päätoiminnallisuutta

```mermaid
classDiagram
  Main<|--Game
  Main<|--Events
  
  
  
  class Main{
  main()

  }

  class Events{
   

  }
  
  
  class Game{
  
  


  }


 

```



# Pelin aloituksesta lopettamiseen

Aloitusnäytöstä päästään peliin painamalla näppäintä "a". Pelin hahmoja voi liikutella nuolinäppäimillä.

```mermaid

sequenceDiagram
participant Main
participant Peli
participant Events
participant Pelipyörii

Main->>Peli: Peli()
activate Peli
Peli->>Peli: Peli.kaynnista()
Peli->>Peli: Peli._aloita_tapahtumat()
Peli->>Peli: Peli.start_draw()
Peli->>Peli: Peli._aloita_peli()

Peli->>Events: pygame.get()
activate Events
Events->>Peli: 
deactivate Events

Peli->>Pelipyörii: start()
activate Pelipyörii
Pelipyörii->>Peli: 
deactivate Pelipyörii
Peli->>Main: sys.exit()
deactivate Peli
```
Pelin lopetuksen voi toteuttaa "SPACE" tämä toteuttaa ohjelmmalle exit komennon.


# Pelin eri hahmot ja niiden toiminnallisuus

```mermaid
classDiagram

Game<|--Pacman
Game<|--Ghosts

class Pacman{
  move()
  can_move()
  collision()
  

  }
  
  
class Ghosts{
  move()
  can_move()
  collision()
  


  }
```

