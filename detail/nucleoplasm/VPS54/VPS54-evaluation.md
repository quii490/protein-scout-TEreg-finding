---
type: protein-evaluation
gene: "VPS54"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS54 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS54 / HCC8 |
| 蛋白名称 | Vacuolar protein sorting-associated protein 54 |
| 蛋白大小 | 977 aa / 110.6 kDa |
| UniProt ID | Q9P1Q0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Golgi apparatus, trans-Golgi network; Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 977 aa / 110.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039745, IPR012501, IPR019515; Pfam: PF07928, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Enhanced |
| UniProt | Golgi apparatus, trans-Golgi network; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- GARP complex (GO:0000938)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HCC8 |

**关键文献**:
1. VPS54 and the wobbler mouse.. *Frontiers in neuroscience*. PMID: 26539077
2. Generation and Analysis of hTERT-RPE1 VPS54 Knock-Out and Rescued Cell Lines.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 36512226
3. Loss of vps54 function leads to vesicle traffic impairment, protein mis-sorting and embryonic lethality.. *International journal of molecular sciences*. PMID: 23708095
4. Vps54 Regulates Lifespan and Locomotor Behavior in Adult Drosophila melanogaster.. *Frontiers in genetics*. PMID: 34712272
5. Post-Golgi anterograde transport requires GARP-dependent endosome-to-TGN retrograde transport.. *Molecular biology of the cell*. PMID: 26157166

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 35.0% |
| 置信残基 (pLDDT 70-90) 占比 | 32.7% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 18.6% |
| 有序区域 (pLDDT>70) 占比 | 67.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.9，有序区 67.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039745, IPR012501, IPR019515; Pfam: PF07928, PF10475 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS53 | 0.999 | 0.976 | — |
| VPS51 | 0.999 | 0.643 | — |
| VPS52 | 0.999 | 0.983 | — |
| VPS50 | 0.973 | 0.835 | — |
| STX16 | 0.948 | 0.305 | — |
| STX6 | 0.933 | 0.370 | — |
| EIPR1 | 0.929 | 0.836 | — |
| VAMP4 | 0.884 | 0.084 | — |
| COG4 | 0.854 | 0.071 | — |
| COG6 | 0.833 | 0.165 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VPS52 | psi-mi:"MI:0018"(two hybrid) | pubmed:12395193 |
| SEC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:12395193 |
| EXO84 | psi-mi:"MI:0018"(two hybrid) | pubmed:12395193 |
| SEC15 | psi-mi:"MI:0018"(two hybrid) | pubmed:12395193 |
| KAR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| VPS53 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| HRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 无 | pLDDT=74.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network; Membrane / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. VPS54 — Vacuolar protein sorting-associated protein 54，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小977 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P1Q0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143952-VPS54/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS54
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P1Q0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
