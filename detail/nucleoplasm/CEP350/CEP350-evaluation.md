---
type: protein-evaluation
gene: "CEP350"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CEP350 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP350 / CAP350, KIAA0480 |
| 蛋白名称 | Centrosome-associated protein 350 |
| 蛋白大小 | 3117 aa / 350.9 kDa |
| UniProt ID | Q5VT06 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CEP350/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CEP350/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Centrosome; 额外: Basal body, End piece; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 📏 蛋白大小 | 0/10 | ×1 | 0 | 3117 aa / 350.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 2COZ |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036859, IPR000938, IPR028750, IPR025486; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Basal body, End piece | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, c... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAP350, KIAA0480 |

**关键文献**:
1. A disease-associated PPP2R3C-MAP3K1 phospho-regulatory module controls centrosome function.. *Current biology : CB*. PMID: 39317195
2. The central scaffold protein CEP350 coordinates centriole length, stability, and maturation.. *The Journal of cell biology*. PMID: 36315013
3. The effect of Diosmin on the blood proteome in a rat model of venous thrombosis.. *International journal of biological macromolecules*. PMID: 28606843
4. CAKUT variants in PRPF8, DYRK2, and CEP78: implications for splicing and ciliogenesis.. *bioRxiv : the preprint server for biology*. PMID: 40777246
5. CEP78 functions downstream of CEP350 to control biogenesis of primary cilia by negatively regulating CP110 levels.. *eLife*. PMID: 34259627

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 2COZ |


**PAE**: AlphaFold 数据未获取，无 PAE 可用。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036859, IPR000938, IPR028750, IPR025486; Pfam: PF01302, PF14309 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FGFR1OP | 0.977 | 0.920 | — |
| CEP19 | 0.877 | 0.615 | — |
| CYLD | 0.825 | 0.469 | — |
| PHF3 | 0.784 | 0.000 | — |
| PPP2CB | 0.766 | 0.764 | — |
| CEP135 | 0.749 | 0.168 | — |
| PPP2R3C | 0.736 | 0.735 | — |
| PCNT | 0.702 | 0.306 | — |
| RABL2B | 0.702 | 0.536 | — |
| NIN | 0.685 | 0.162 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q8BXM7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| APTX | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PLEKHA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Cep43 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CTNNA1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PAWR | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PPP2R3C | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| SAPCD2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CCDC85C | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TLN1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 2COZ | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm, Centrosome; 额外: Basal body, End piece | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CEP350 — Centrosome-associated protein 350，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小3117 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VT06
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135837-CEP350/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP350
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VT06
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:49:15
