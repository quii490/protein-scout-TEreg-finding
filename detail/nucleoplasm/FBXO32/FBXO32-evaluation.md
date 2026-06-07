---
type: protein-evaluation
gene: "FBXO32"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO32 — REJECTED (研究热度过高 (PubMed strict=241，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO32 |
| 蛋白名称 | F-box only protein 32 |
| 蛋白大小 | 355 aa / 41.6 kDa |
| UniProt ID | Q969P5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 355 aa / 41.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=241 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR040394 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 241 |
| PubMed broad count | 885 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. F-box protein FBXO32 ubiquitinates and stabilizes D-type cyclins to drive cancer progression.. *Nature communications*. PMID: 40307251
2. Handelin alleviates cachexia- and aging-induced skeletal muscle atrophy by improving protein homeostasis and inhibiting inflammation.. *Journal of cachexia, sarcopenia and muscle*. PMID: 38009816
3. FBXO32 Stimulates Protein Synthesis to Drive Pancreatic Cancer Progression and Metastasis.. *Cancer research*. PMID: 38775804
4. Sepsis induces interleukin 6, gp130/JAK2/STAT3, and muscle wasting.. *Journal of cachexia, sarcopenia and muscle*. PMID: 34821076
5. Exogenous Nucleotides Supplementation Attenuates Age-Related Sarcopenia.. *Journal of cachexia, sarcopenia and muscle*. PMID: 40745399

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 51.8% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 16.6% |
| 有序区域 (pLDDT>70) 占比 | 74.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.9，有序区 74.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR040394 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KDM2A | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| MYOG | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SKP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| MLH1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15124|pubmed:20706999 |
| YTHDC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 5
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 无 | pLDDT=79.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 5 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FBXO32 — F-box only protein 32，研究基础较多，新颖性有限。
2. 蛋白大小355 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 241 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 241 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969P5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156804-FBXO32/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO32
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969P5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000156804-FBXO32/subcellular

![](https://images.proteinatlas.org/58955/1009_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/58955/1009_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/58955/1029_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/58955/1029_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/58955/995_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/58955/995_B5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q969P5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q969P5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 223..271; /note="F-box" |
| InterPro | IPR036047;IPR040394; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156804-FBXO32/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EIF3F | Intact, Biogrid | true |
| ATR | Biogrid | false |
| CTBP1 | Biogrid | false |
| CUL1 | Biogrid | false |
| EIF2AK2 | Opencell | false |
| MYC | Biogrid | false |
| MYOD1 | Biogrid | false |
| PSMC4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
