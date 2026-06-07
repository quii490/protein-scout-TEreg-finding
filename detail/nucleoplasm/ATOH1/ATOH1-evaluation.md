---
type: protein-evaluation
gene: "ATOH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATOH1 — REJECTED (研究热度过高 (PubMed strict=335，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATOH1 / ATH1, BHLHA14 |
| 蛋白名称 | Transcription factor ATOH1 |
| 蛋白大小 | 354 aa / 38.2 kDa |
| UniProt ID | Q92858 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 354 aa / 38.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=335 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032661, IPR011598, IPR050359, IPR036638; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 335 |
| PubMed broad count | 858 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATH1, BHLHA14 |

**关键文献**:
1. Increased mitophagy protects cochlear hair cells from aminoglycoside-induced damage.. *Autophagy*. PMID: 35471096
2. Molecular ontology of the parabrachial nucleus.. *The Journal of comparative neurology*. PMID: 35134251
3. AAV-ie-K558R mediated cochlear gene therapy and hair cell regeneration.. *Signal transduction and targeted therapy*. PMID: 35449181
4. Divergent combinations of enhancers encode spatial gene expression.. *Nature communications*. PMID: 40456823
5. A medullary centre for lapping in mice.. *Nature communications*. PMID: 34728601

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.2 |
| 高置信度残基 (pLDDT>90) 占比 | 15.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 30.8% |
| 低置信 (pLDDT<50) 占比 | 45.2% |
| 有序区域 (pLDDT>70) 占比 | 24.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.2），有序残基占 24.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032661, IPR011598, IPR050359, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASCL1 | 0.855 | 0.098 | — |
| BARHL1 | 0.854 | 0.000 | — |
| POU4F1 | 0.820 | 0.000 | — |
| POU4F3 | 0.818 | 0.000 | — |
| MUC6 | 0.794 | 0.057 | — |
| MYO7A | 0.786 | 0.000 | — |
| SHH | 0.778 | 0.102 | — |
| MUC5AC | 0.743 | 0.057 | — |
| GFI1 | 0.736 | 0.074 | — |
| TCF4 | 0.726 | 0.467 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.2 + PDB: 无 | pLDDT=59.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATOH1 — Transcription factor ATOH1，研究基础较多，新颖性有限。
2. 蛋白大小354 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 335 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 335 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92858
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172238-ATOH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATOH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92858
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000172238-ATOH1/subcellular

![](https://images.proteinatlas.org/65568/1918_H3_19_cr5cb45d7be4739_red_green.jpg)
![](https://images.proteinatlas.org/65568/1918_H3_30_cr5cb45d7be5c10_red_green.jpg)
![](https://images.proteinatlas.org/65568/1946_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/65568/1946_E5_4_red_green.jpg)
![](https://images.proteinatlas.org/65568/2158_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/65568/2158_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92858-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92858 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 159..211; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR032661;IPR011598;IPR050359;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172238-ATOH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK1D | Biogrid | false |
| CSNK1E | Biogrid | false |
| HUWE1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
