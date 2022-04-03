mermaid

´´´
  classDiagram
    Pelilauta <|-- Pelaaja
    Pelilauta <|-- Noppa1
    Pelilauta <|-- Noppa2
    Pelilauta <|-- Aloitusruutu
    Pelilauta <|-- Vankila
    Pelilauta <|-- Sattumaruutu
    Pelilauta <|-- Yhteismaaruutu
    Pelilauta <|-- Kadut
    Pelilauta <|-- Asema
    Pelilauta <|-- Laitos
    Sattumaruutu <|-- Sattumakortit
    Yhteismaaruutu <|-- Yhteismaakortit
    Pelaaja <|-- Pankkitili

    class Pelaaja{
      nimi
      pelinappula
      siirrä()
      ruutu

    }

    class Pelilauta{
           
    }

      class Noppa_1{
        heitä()
      }

      class Noppa_2{      
        heitä()
      }
      
      class Aloitusruutu{
        sijainti
        toiminto()
      }
      
      class Vankila{
        sijainti
        toiminto()
      }
      class Sattumaruutu{
      
      toiminto()
        
      }
      
      class Yhteismaaruutu{
      
      toiminto()
        
      }
      
     
      class Sattumakortit{
        toiminto()
      }
      
      class Yhteismaakortit{
        toiminto()
      }
      
      class Kadut{
        nimi
        omistaja
        rakenna_talo()
        rakenna_hotelli()
      }
      
      class Asema{
      
      toiminto()
      
      }
      
      class Laitos{
      
      toiminto()
      
      }
      
      class Pankkitili{
        saldo
        maksutapahtuma()
      }
´´´
