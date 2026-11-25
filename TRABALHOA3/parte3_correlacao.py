# ============================================================
# SMART AGRO-LOGIC (SAL) - Parte III
# Correlação Linear entre Volume de Água e Crescimento
# Disciplina: Matemática Computacional
# ============================================================

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ---------------------------------------------
# 1. GERACAO DOS DADOS SIMULADOS (30 dias)
# ---------------------------------------------
np.random.seed(42)  # semente para reprodutibilidade

dias = np.arange(1, 31)

# X: Volume de água utilizado (litros/m²) — entre 2 e 10 L/m²
volume_agua = np.round(np.random.uniform(2, 10, 30), 2)

# Y: Crescimento da planta (cm) — correlacionado com X + ruído
crescimento = np.round(0.8 * volume_agua + np.random.normal(0, 0.6, 30), 2)

# ---------------------------------------------
# 2. COEFICIENTE DE CORRELACAO DE PEARSON
# ---------------------------------------------
r, p_valor = stats.pearsonr(volume_agua, crescimento)

print("=" * 55)
print("  ANÁLISE DE CORRELAÇÃO - Smart Agro-Logic (SAL)")
print("=" * 55)
print(f"\n{'Dia':<6} {'Volume (L/m²)':<18} {'Crescimento (cm)'}")
print("-" * 40)
for i in range(30):
    print(f"  {dias[i]:<6} {volume_agua[i]:<18} {crescimento[i]}")

print("\n" + "=" * 55)
print(f"  Coeficiente de Correlação de Pearson (r): {r:.4f}")
print(f"  P-valor:                                  {p_valor:.6f}")

print("\n  INTERPRETAÇÃO:")
if abs(r) >= 0.9:
    forca = "muito forte"
elif abs(r) >= 0.7:
    forca = "forte"
elif abs(r) >= 0.5:
    forca = "moderada"
else:
    forca = "fraca"

if r > 0:
    direcao = "positiva"
    descricao = "Mais água → Mais crescimento"
elif r < 0:
    direcao = "negativa"
    descricao = "Mais água → Menos crescimento"
else:
    direcao = "nula"
    descricao = "Sem relação entre as variáveis"

print(f"  r = {r:.4f} → Correlação {direcao} e {forca}")
print(f"  {descricao}")

if p_valor < 0.05:
    print(f"  P-valor = {p_valor:.6f} → Resultado estatisticamente significativo (p < 0.05)")
else:
    print(f"  P-valor = {p_valor:.6f} → Resultado NÃO significativo (p >= 0.05)")
print("=" * 55)

# ---------------------------------------------
# 3. LINHA DE REGRESSAO
# ---------------------------------------------
slope, intercept, _, _, _ = stats.linregress(volume_agua, crescimento)
linha_regressao = slope * volume_agua + intercept

# ---------------------------------------------
# 4. GRAFICOS
# ---------------------------------------------
fig = plt.figure(figsize=(14, 10))
fig.suptitle("Smart Agro-Logic (SAL) - Análise de Correlação Hídrica",
             fontsize=15, fontweight='bold', y=0.98)

gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.35)

# --- Gráfico 1: Dispersão com Regressão ---
ax1 = fig.add_subplot(gs[0, :])
ax1.scatter(volume_agua, crescimento, color='steelblue', edgecolors='navy',
            s=80, zorder=5, label='Observações (30 dias)')
ax1.plot(volume_agua, linha_regressao, color='tomato', linewidth=2,
         label=f'Regressão Linear: y = {slope:.2f}x + {intercept:.2f}')
ax1.set_xlabel("Volume de Água Utilizado (L/m²)", fontsize=11)
ax1.set_ylabel("Crescimento da Planta (cm)", fontsize=11)
ax1.set_title(f"Scatter Plot — Correlação de Pearson: r = {r:.4f}", fontsize=12)
ax1.legend(fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.text(0.05, 0.92, f"r = {r:.4f}   p = {p_valor:.4f}",
         transform=ax1.transAxes, fontsize=11,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# --- Gráfico 2: Volume de Água ao longo dos dias ---
ax2 = fig.add_subplot(gs[1, 0])
ax2.bar(dias, volume_agua, color='dodgerblue', edgecolor='navy', alpha=0.8)
ax2.set_xlabel("Dia", fontsize=10)
ax2.set_ylabel("Volume (L/m²)", fontsize=10)
ax2.set_title("Volume de Água por Dia", fontsize=11)
ax2.grid(axis='y', linestyle='--', alpha=0.4)

# --- Gráfico 3: Crescimento das plantas ao longo dos dias ---
ax3 = fig.add_subplot(gs[1, 1])
ax3.plot(dias, crescimento, marker='o', color='seagreen',
         linewidth=1.5, markersize=5, label='Crescimento (cm)')
ax3.fill_between(dias, crescimento, alpha=0.15, color='seagreen')
ax3.set_xlabel("Dia", fontsize=10)
ax3.set_ylabel("Crescimento (cm)", fontsize=10)
ax3.set_title("Crescimento das Plantas por Dia", fontsize=11)
ax3.grid(True, linestyle='--', alpha=0.4)

plt.savefig("/mnt/user-data/outputs/grafico_correlacao_SAL.png",
            dpi=150, bbox_inches='tight')
print("\n  Gráfico salvo em: grafico_correlacao_SAL.png")
plt.show()
