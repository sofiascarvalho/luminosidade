# Projeto Luminosidade

Este repositório contém projetos práticos de Internet Indutrial das Coisas (IIoT) desenvolvidos cmo exercícios de apredizagem, utilizando sensores simples para autoação e monitoramento.

---

## 1. Detecção de Luminosidade com LDR

![](./img/20250826_093437.jpg)

### Descrição:
Circuito com LDR e LED. O LED acende automaticamente em ambientes escuros e apaga em ambientes claros.

### Componentes:
- LDR (Light Dependent Resistor)
- LED
- Resistor
- Protoboard e Jumpers

### Como funciona:
O LDR vai medir a intensidade da luz. Quando a luminosidade estiver abaixo de um determinado limiar, o LED acende. Quando a luminosidade aumentar, o LED apaga. 

---

## 2. Detecção de Obstáculos com HC-SR04

![](/img/20250826_110028.jpg)

### Descrição:
Circuito com sensor ultrassônico HC-SR04 e LED. O LED acende automaticamente quando detecta um obstáculo ou intruso próximo.

### Componentes:
- HC-SR04
- LED
- Resistor
- Protoboard e Jumpers

### Como funciona:
O HC-SR04 mede a distância até um objeto usando ultrassom. Se o objeto estiver dentro do limite definido, o LED acende. Caso contrário, o LED permanece desligado.

### Tecnologias:
- ESP32
- Sensores: LDR, HC-SR04
- LEDs e resistores
- Protoboard