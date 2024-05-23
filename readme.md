Componentes Necessários:

ESP32.
LEDs: Vermelho, Amarelo e Verde.
Resistores (220Ω ou valor similar).
Protoboard e Jumpers.

Conexões:
LED Vermelho: Conectado ao GPIO 25 através de um resistor.
LED Amarelo: Conectado ao GPIO 26 através de um resistor.
LED Verde: Conectado ao GPIO 27 através de um resistor.

Montagem do Circuito:

LED Vermelho:
Conecte o cátodo (perna mais curta) ao GND.
Conecte o anodo (perna mais longa) a um dos terminais do resistor.
Conecte o outro terminal do resistor ao GPIO 25.

LED Amarelo:
Conecte o cátodo ao GND.
Conecte o anodo a um dos terminais do resistor.
Conecte o outro terminal do resistor ao GPIO 26.

LED Verde:
Conecte o cátodo ao GND.
Conecte o anodo a um dos terminais do resistor.
Conecte o outro terminal do resistor ao GPIO 27.

Esquema de Ligação

LED Vermelho:
  Anodo (perna longa) -> Resistor -> GPIO 25
  Cátodo (perna curta) -> GND

LED Amarelo:
  Anodo (perna longa) -> Resistor -> GPIO 26
  Cátodo (perna curta) -> GND

LED Verde:
  Anodo (perna longa) -> Resistor -> GPIO 27
  Cátodo (perna curta) -> GND

  -----------------------------------------------------------

  Explicação do Código:
Importações: As classes Pin e sleep das bibliotecas machine e time, respectivamente, são importadas.

Configuração dos Pinos: Os pinos GPIO 25, 26 e 27 são configurados como saídas para os LEDs vermelho, amarelo e verde.

Função semaforo: Controla o ciclo do semáforo:
O LED verde acende por 5 segundos.
O LED amarelo acende por 2 segundos.
O LED vermelho acende por 5 segundos.

Esse ciclo se repete indefinidamente.

Como Executar:
Conecte o ESP32 ao computador e carregue o código usando uma IDE compatível com MicroPython, como o Thonny.

Conecte os LEDs e os resistores ao ESP32 conforme especificado.
Execute o código na placa ESP32.
Com isso, você terá um semáforo funcionando, onde os LEDs acendem em sequência para simular um semáforo real.
