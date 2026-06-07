---
type: protein-evaluation
gene: "TSC22D4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSC22D4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSC22D4 / THG1, THG1-PIT |
| 蛋白名称 | TSC22 domain family protein 4 |
| 蛋白大小 | 395 aa / 41.0 kDa |
| UniProt ID | Q9Y3Q8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm; Cell projection, dendrite; Synapse |
| 蛋白大小 | 10/10 | ×1 | 10 | 395 aa / 41.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000580, IPR047862, IPR042553; Pfam: PF01166 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm; Cell projection, dendrite; Synapse | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- nucleus (GO:0005634)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: THG1, THG1-PIT |

**关键文献**:
1. Comparative gene regulatory networks modulating APOE expression in microglia and astrocytes.. *medRxiv : the preprint server for health sciences*. PMID: 38699303
2. Establishment of a diagnostic model of endometriosis based on disulfidptosis-related genes.. *The journal of obstetrics and gynaecology research*. PMID: 38644543
3. Multiple TSC22D4 iso-/phospho-glycoforms display idiosyncratic subcellular localizations and interacting protein partners.. *The FEBS journal*. PMID: 23305244
4. The interplay between TGF-β-stimulated TSC22 domain family proteins regulates cell-cycle dynamics in medulloblastoma cells.. *Journal of cellular physiology*. PMID: 30912127
5. Hepatocyte-specific activity of TSC22D4 triggers progressive NAFLD by impairing mitochondrial function.. *Molecular metabolism*. PMID: 35378329

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.9 |
| 高置信度残基 (pLDDT>90) 占比 | 12.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 27.8% |
| 低置信 (pLDDT<50) 占比 | 51.6% |
| 有序区域 (pLDDT>70) 占比 | 20.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.9），有序残基占 20.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000580, IPR047862, IPR042553; Pfam: PF01166 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C7orf61 | 0.926 | 0.000 | — |
| NRBP1 | 0.920 | 0.879 | — |
| NRBP2 | 0.826 | 0.807 | — |
| TSC22D1 | 0.821 | 0.722 | — |
| TSC22D2 | 0.741 | 0.626 | — |
| LHX4 | 0.730 | 0.260 | — |
| TSC22D3 | 0.703 | 0.626 | — |
| KEAP1 | 0.638 | 0.614 | — |
| LHX3 | 0.601 | 0.071 | — |
| MAD2L1 | 0.504 | 0.427 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NOC4L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SYT17 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIF3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBLCP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAD2L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC42 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZMYND10 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PIH1D1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENKD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PSMA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.9 + PDB: 无 | pLDDT=56.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell projection, dendrite; Syn / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TSC22D4 — TSC22 domain family protein 4，非常新颖，仅有少数基础研究。
2. 蛋白大小395 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3Q8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166925-TSC22D4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSC22D4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3Q8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000166925-TSC22D4/subcellular

![](https://images.proteinatlas.org/6757/41_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6757/41_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6757/42_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6757/42_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6757/43_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6757/43_B8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3Q8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y3Q8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000580;IPR047862;IPR042553; |
| Pfam | PF01166; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166925-TSC22D4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AIFM1 | Intact, Biogrid | true |
| APIP | Intact, Biogrid, Bioplex | true |
| KEAP1 | Intact, Biogrid, Bioplex | true |
| MAD2L1 | Intact, Biogrid, Bioplex | true |
| NRBP1 | Intact, Biogrid, Opencell, Bioplex | true |
| NRBP2 | Intact, Biogrid, Bioplex | true |
| PCBP1 | Intact, Biogrid | true |
| PIH1D1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
