# ============================================================
# SMART AGRO-LOGIC (SAL) - Parte II
# Implementacao em Python - Simulador de Hardware
# Disciplina: Matematica Computacional
# ============================================================

import os
import time

# ------------------------------------------------------------
# FUNCAO: Limpar o console
# ------------------------------------------------------------
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------
# FUNCAO: Exibe o cabecalho do sistema
# ------------------------------------------------------------
def exibir_cabecalho():
    print("=" * 55)
    print("       SMART AGRO-LOGIC (SAL) v1.0")
    print("    Sistema de Irrigacao Automatizado")
    print("=" * 55)

# ------------------------------------------------------------
# FUNCAO: Le entrada valida do usuario (apenas 0 ou 1)
# ------------------------------------------------------------
def ler_sensor(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor in [0, 1]:
                return valor
            else:
                print("  [!] Valor invalido. Digite apenas 0 ou 1.\n")
        except ValueError:
            print("  [!] Entrada invalida. Digite apenas 0 ou 1.\n")

# ------------------------------------------------------------
# FUNCAO: Logica Booleana principal
#   Expressao: S = U AND (NOT C) AND R
# ------------------------------------------------------------
def decisao_irrigacao(u, c, r):
    return u and (not c) and r

# ------------------------------------------------------------
# FUNCAO: Exibe o resultado com detalhes
# ------------------------------------------------------------
def exibir_resultado(u, c, r, s):
    print("\n" + "-" * 55)
    print("  LEITURA DOS SENSORES:")
    print(f"    U - Umidade do Solo    : {'Solo SECO  (1)' if u else 'Solo UMIDO (0)'}")
    print(f"    C - Presenca de Chuva  : {'CHOVENDO   (1)' if c else 'SEM CHUVA  (0)'}")
    print(f"    R - Nivel Reservatorio : {'COM AGUA   (1)' if r else 'VAZIO      (0)'}")
    print("-" * 55)
    print("  EXPRESSAO BOOLEANA:")
    print(f"    S = U AND (NOT C) AND R")
    print(f"    S = {u} AND (NOT {c}) AND {r}")
    print(f"    S = {u} AND {int(not c)} AND {r}")
    print(f"    S = {int(bool(s))}")
    print("-" * 55)

    if s:
        print("  DECISAO DO SISTEMA:")
        print()
        print("        ** IRRIGACAO ATIVADA **")
        print()
        print("  Condicoes satisfeitas:")
        print("    [OK] Solo esta seco")
        print("    [OK] Nao esta chovendo")
        print("    [OK] Reservatorio tem agua")
    else:
        print("  DECISAO DO SISTEMA:")
        print()
        print("        -- SISTEMA DESLIGADO --")
        print()
        print("  Motivo(s):")
        if not u:
            print("    [--] Solo ja esta umido - irrigacao desnecessaria")
        if c:
            print("    [--] Esta chovendo - irrigacao suspensa")
        if not r:
            print("    [--] Reservatorio sem agua - impossivel irrigar")

    print("=" * 55)

# ------------------------------------------------------------
# FUNCAO: Exibe a tabela verdade completa
# ------------------------------------------------------------
def exibir_tabela_verdade():
    limpar_tela()
    print("=" * 55)
    print("      TABELA VERDADE - S(U, C, R)")
    print("      S = U AND (NOT C) AND R")
    print("=" * 55)
    print(f"  {'U':<6} {'C':<6} {'R':<6} {'S':<6}  Resultado")
    print("-" * 55)

    for u in [0, 1]:
        for c in [0, 1]:
            for r in [0, 1]:
                s = u and (not c) and r
                status = "-> IRRIGAR" if s else "   desligado"
                marcador = "***" if s else "   "
                print(f"  {marcador} {u:<4} {c:<4} {r:<4} {int(s):<4}  {status}")

    print("-" * 55)
    print("  *** = unica combinacao que ativa o sistema")
    print("=" * 55)
    input("\n  Pressione ENTER para voltar ao menu...")

# ------------------------------------------------------------
# FUNCAO: Modo automatico - testa todos os cenarios
# ------------------------------------------------------------
def modo_automatico():
    limpar_tela()
    print("=" * 55)
    print("    MODO AUTOMATICO - Simulacao de Todos os Cenarios")
    print("=" * 55)

    cenarios = [
        (1, 0, 1, "Cenario ideal - deve IRRIGAR"),
        (1, 1, 1, "Solo seco mas esta chovendo"),
        (1, 0, 0, "Solo seco mas reservatorio vazio"),
        (0, 0, 1, "Solo umido, sem chuva, reservatorio cheio"),
        (0, 1, 0, "Solo umido e chovendo"),
        (0, 0, 0, "Solo umido, sem chuva, reservatorio vazio"),
        (1, 1, 0, "Solo seco, chovendo, reservatorio vazio"),
        (0, 1, 1, "Solo umido, chovendo, reservatorio cheio"),
    ]

    for i, (u, c, r, descricao) in enumerate(cenarios, 1):
        s = decisao_irrigacao(u, c, r)
        resultado = "IRRIGACAO ATIVADA" if s else "SISTEMA DESLIGADO"
        print(f"\n  [{i}] {descricao}")
        print(f"      U={u}, C={c}, R={r}  ->  {resultado}")
        time.sleep(0.3)

    print("\n" + "=" * 55)
    input("  Pressione ENTER para voltar ao menu...")

# ------------------------------------------------------------
# FUNCAO: Menu principal
# ------------------------------------------------------------
def menu():
    while True:
        limpar_tela()
        exibir_cabecalho()
        print()
        print("  [1] Simular com entradas manuais")
        print("  [2] Ver Tabela Verdade completa")
        print("  [3] Simulacao automatica (todos os cenarios)")
        print("  [4] Sair")
        print()
        opcao = input("  Escolha uma opcao: ").strip()

        if opcao == "1":
            limpar_tela()
            exibir_cabecalho()
            print()
            print("  Informe o estado de cada sensor (0 ou 1):")
            print()
            print("  U: 1 = Solo Seco     | 0 = Solo Umido")
            print("  C: 1 = Chovendo      | 0 = Sem Chuva")
            print("  R: 1 = Reserv. Cheio | 0 = Reserv. Vazio")
            print()

            u = ler_sensor("  U - Umidade do Solo    : ")
            c = ler_sensor("  C - Presenca de Chuva  : ")
            r = ler_sensor("  R - Nivel Reservatorio : ")

            s = decisao_irrigacao(u, c, r)
            exibir_resultado(u, c, r, s)
            input("\n  Pressione ENTER para continuar...")

        elif opcao == "2":
            exibir_tabela_verdade()

        elif opcao == "3":
            modo_automatico()

        elif opcao == "4":
            limpar_tela()
            print("  Sistema encerrado. Ate logo!")
            print()
            break

        else:
            print("\n  [!] Opcao invalida. Tente novamente.")
            time.sleep(1)

# ------------------------------------------------------------
# PONTO DE ENTRADA
# ------------------------------------------------------------
if __name__ == "__main__":
    menu()
