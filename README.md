[readme_md.md](https://github.com/user-attachments/files/35419469/readme_md.md)
# 🌿 Smart Agro-Logic (SAL)

> **Sistema de Irrigação Automatizado com Análise Estatística Aplicada**  
> *Projeto acadêmico desenvolvido para a disciplina de Matemática Computacional.*

---

## 📌 Sobre o Projeto

O **Smart Agro-Logic (SAL)** é uma solução baseada em **Lógica Booleana** e **Análise Estatística de Dados** desenvolvida para otimizar o uso da água no agronegócio. 

O sistema toma decisões automatizadas sobre a ativação da irrigação com base na leitura de três sensores estratégicos e analisa a correlação entre a quantidade de água fornecida e o crescimento vegetativo da cultura.

---

## 🚀 Funcionalidades

- **Controle Lógico Booleano:** Decisão automática de acionamento baseada nos sensores de solo, chuva e nível de reservatório.
- **Simulador Interativo via Terminal:** Permite testar cenários manuais, visualizar a tabela verdade e executar testes automáticos.
- **Análise Estatística (Pearson):** Cálculo da correlação linear ($r$) e p-valor entre o volume de água e o crescimento das plantas durante um período de 30 dias.
- **Visualização de Dados:** Geração de gráficos de dispersão, regressão linear e evolução diária utilizando Matplotlib.

---

## 📐 Fundamentação Matemática & Lógica

### 1. Expressão Booleana

A decisão de irrigar ($S$) é ativada apenas quando o solo está seco ($U=1$), não está chovendo ($C=0$) e há água no reservatório ($R=1$).

$$S(U, C, R) = U \land (\neg C) \land R$$

### 2. Tabela Verdade

| $U$ (Solo Seco) | $C$ (Chovendo) | $R$ (Reservatório) | $\neg C$ | $S$ (Irrigar?) | Status |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 1 | **0** | Desligado |
| 0 | 0 | 1 | 1 | **0** | Desligado |
| 0 | 1 | 0 | 0 | **0** | Desligado |
| 0 | 1 | 1 | 0 | **0** | Desligado |
| 1 | 0 | 0 | 1 | **0** | Desligado |
| **1** | **0** | **1** | **1** | **1** | **✅ IRRIGAR** |
| 1 | 1 | 0 | 0 | **0** | Desligado |
| 1 | 1 | 1 | 0 | **0** | Desligado |

> **Observação:** Apenas 1 das 8 combinações possíveis ativa a irrigação, garantindo alta eficiência hídrica e segurança aos equipamentos.

---

## 📂 Estrutura do Repositório

```text
.
├── parte1_logica_booleana.py   # Implementação básica da Lógica Booleana e Tabela Verdade
├── parte2_simulador.py         # Simulador de hardware interativo (Menu, testes e logs)
├── parte3_correlacao.py        # Análise estatística de Pearson e plotagem de gráficos
├── AgroLogic_SAL_Apresentacao.pptx  # Apresentação do projeto
└── README.md                   # Documentação do projeto
```

---

## ⚙️ Como Executar

### Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina, além das seguintes bibliotecas:

```bash
pip install numpy scipy matplotlib
```

### Executando os Scripts

1. **Lógica Booleana Básica:**
   ```bash
   python parte1_logica_booleana.py
   ```

2. **Simulador Interativo de Hardware:**
   ```bash
   python parte2_simulador.py
   ```

3. **Análise de Correlação e Gráficos:**
   ```bash
   python parte3_correlacao.py
   ```

---

## 📊 Análise Estatística (Parte III)

O script `parte3_correlacao.py` simula dados de 30 dias de cultivo para calcular o **Coeficiente de Correlação de Pearson ($r$)**:

- **Métrica:** Avalia a relação entre o Volume de Água ($L/m^2$) e o Crescimento ($cm$).
- **Saída Visual:** Gera uma figura contendo:
  1. *Scatter plot* com linha de regressão linear.
  2. Gráfico de barras do volume de água por dia.
  3. Gráfico de linha da taxa de crescimento ao longo do tempo.

---

## 🎯 Impactos Estimados

- 💧 **40% de redução** no desperdício de água doce.
- ⚡ **35% de economia** na conta de energia elétrica (bombeamento).
- 📉 **30% de redução** nas emissões de $\text{CO}_2$ associadas ao uso de bombas hídricas.

---

## 📜 Licença

Este projeto foi desenvolvido com fins educacionais para a disciplina de **Matemática Computacional Aplicada**. Livre para consulta e modificação.
