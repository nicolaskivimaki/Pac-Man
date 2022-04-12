```mermaid
classDiagram
  Start<|--Vihollinen
  Start<|--Robo
  Start<|--Level

  class Start{
    _lataa_naytto()
    _handle_events()

  }
  class Level{


  }

  class Robo{
    _liikuta()

  }

  class Vihollinen{
    _liikuta_vihollista()

  }
 

```
