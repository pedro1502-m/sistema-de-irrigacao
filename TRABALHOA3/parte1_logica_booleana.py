# ============================================================
# SMART AGRO-LOGIC (SAL) - Parte I
# Sistema de Irrigação Automatizado - Lógica Booleana
# Disciplina: Matemática Computacional
# ============================================================

def tabela_verdade():
    """Exibe a tabela verdade completa para S(U, C, R)"""
    print("=" * 55)
    print("     TABELA VERDADE - Sistema de Irrigação (SAL)")
    print("=" * 55)
    print("  U (Solo Seco) | C (Chovendo) | R (Reserv. c/ água) | S (Irrigar?)")
    print("-" * 55)

    for u in [0, 1]:
        for c in [0, 1]:
            for r in [0, 1]:
                # Expressão Booleana: S = U AND (NOT C) AND R
                s = u and (not c) and r
                print(f"       {u}            |      {c}          |          {r}            |     {int(s)}")
    print("-" * 55)
    print("Expressão Booleana: S = U ∧ (¬C) ∧ R")
    print("=" * 55)


def sistema_irrigacao():
    """Simula o sistema de decisão de irrigação com entradas do usuário"""
    print("\n" + "=" * 55)
    print("   SMART AGRO-LOGIC (SAL) - Painel de Controle")
    print("=" * 55)
    print("Legenda de Entradas:")
    print("  U: 1 = Solo Seco    | 0 = Solo Úmido")
    print("  C: 1 = Chovendo     | 0 = Sem Chuva")
    print("  R: 1 = Reserv. Cheio| 0 = Reserv. Vazio")
    print("-" * 55)

    while True:
        try:
            u = int(input("\nUmidade do Solo    [U] (0 ou 1): "))
            c = int(input("Presença de Chuva  [C] (0 ou 1): "))
            r = int(input("Nível Reservatório [R] (0 ou 1): "))

            if any(v not in [0, 1] for v in [u, c, r]):
                print("  [!] Entrada inválida. Use apenas 0 ou 1.")
                continue

            # Lógica Booleana: S = U AND (NOT C) AND R
            s = u and (not c) and r

            print("\n" + "=" * 55)
            if s:
                print("   ✅  IRRIGAÇÃO ATIVADA")
                print("   O solo está seco, não está chovendo")
                print("   e o reservatório possui água.")
            else:
                print("   ⛔  SISTEMA DESLIGADO")
                if not u:
                    print("   Motivo: Solo já está úmido.")
                elif c:
                    print("   Motivo: Está chovendo no momento.")
                elif not r:
                    print("   Motivo: Reservatório sem água.")
            print("=" * 55)

            continuar = input("\nDeseja testar outro cenário? (s/n): ").strip().lower()
            if continuar != 's':
                break

        except ValueError:
            print("  [!] Por favor, insira apenas números inteiros (0 ou 1).")

    print("\nSistema encerrado. Obrigado!")


if __name__ == "__main__":
    tabela_verdade()
    sistema_irrigacao()
