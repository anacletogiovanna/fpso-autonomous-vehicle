# Veículos autônomos em FPSO's
### Projeto de Desenvolvimento de Veículos Autônomos de Inspeção e Monitoramento em Unidades Flutuantes de Armazenamento e Transferência de Petróleo e Gás Natural (FPSO’s)

Acidentes na indústria brasileira causam prejuízos em diversas esferas, como por exemplo econômica e ambiental. Com o aumento da perfuração e exploração de novos poços para extração de petróleo e gás natural, é imprescindível que os ambientes offshore estejam munidos de informações para realizar ações preventivas a fim de evitar tragédias. Sendo assim, é de suma importância trazer elementos da tecnologia, tal como robótica, para apoiar na realização dessas tarefas, tais como a utilização de robôs autônomos que monitorem continuamente o ambiente no qual esteja inserido por meio de câmeras e sensores. Neste cenário, os principais objetivos da solução proposta nesse artigo são a navegação autônoma do robô e a inspeção/monitoramento do local por meio extração de imagens coletadas pela câmera

![gazebo_fpso_world](https://user-images.githubusercontent.com/33101169/113529606-3b75a500-959a-11eb-896f-45be785995d4.png)

#### Tecnologias utilizadas:
Para criação de pacotes do tipos ROS 1, simulaçao e utilização do robô para teste, foram utilizadas as seguintes ferramentas:
- [ROS - Noetic](http://wiki.ros.org/noetic): Framework ROS para comunicação entre nós do robô para o sistema operacional Ubuntu 20.
- [Gazebo](http://gazebosim.org/): Ambiente para simulação de modelos do mundo real, a fim de gerar um ambiente simulado para o robô.
- [Turtlebot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/): Robô utilizado para a simulação da inspeção e o monitoramento em um FPSO.

#### Estrutura do projeto:

```bash
├── article                      # Diretório com o artigo 
│   ├── images                   # Images com prints de evidência
├── extras                       # Extras com vídeos de evidência
├── fpso_identify_image_tag      # Pacote responsável pelo reconhecimento das tags através de visão computacional     
├── fpso_navigation              # Pacote responsável pela navegação autônoma 
├── fpso_world                   # Diretório com os arquivos de mapa e mundo relacionados ao gazebo
```



TODO - Melhorias posteriores na documentação no Github
