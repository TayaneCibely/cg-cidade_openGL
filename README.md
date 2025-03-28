# MiniCidade - Simulador de Trânsito 3D

Este projeto é uma simulação gráfica 3D simples de uma cidade com rua, prédios com janelas, semáforo e um carro em movimento, desenvolvido em Python com PyOpenGL.

## 🎯 Objetivo

Demonstrar os conceitos básicos de modelagem 3D, interação com teclado, uso de estruturas de dados e renderização em tempo real com OpenGL. Também aprimorar a visualização adicionando mais detalhes gráficos como prédios com janelas e um carro mais realista.

---

## 📁 Estrutura do Projeto

```
minicidade/
├── main.py          # Ponto de entrada
├── config.py        # Configurações e estado da simulação
├── logic.py         # Lógica do semáforo e movimentação do carro
├── objects.py       # Funções para desenhar objetos 3D
└── renderer.py      # Renderização da cena 3D
```

---

## 💻 Requisitos

- Python 3.8+
- Bibliotecas:
  ```bash
  pip install PyOpenGL PyOpenGL_accelerate
  ```

No Linux, também pode ser necessário instalar o FreeGLUT:

```bash
sudo apt-get install freeglut3-dev
```

---

## ▶️ Como Executar

1. Baixe o repositório ou descompacte o `.zip`
2. Acesse a pasta do projeto:

```bash
cd minicidade
```

3. Execute o programa:

```bash
python main.py
```

---

## 🎮 Controles

- Pressione `Espaço` para alternar o estado do semáforo entre vermelho e verde.

---

## 🛠 Melhorias visuais

- **Prédios com janelas:** adicionados cubos menores sobre a fachada frontal representando janelas.
- **Carro aprimorado:** agora composto por dois cubos (base e cabine) com cores distintas para maior realismo.

---

## 👨‍💻 Desenvolvido por

BCC - Ciência da Computação – Projeto da disciplina de Computação Gráfica (2025)
Integrantes: Leonardo Nunes, Marcos Nascimento, Tayane Cibely e Tiago Cunha

---
