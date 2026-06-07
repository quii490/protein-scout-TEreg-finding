---
type: protein-evaluation
gene: "TRNAU1AP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRNAU1AP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRNAU1AP / SECP43, TRSPAP1 |
| 蛋白名称 | tRNA selenocysteine 1-associated protein 1 |
| 蛋白大小 | 287 aa / 32.5 kDa |
| UniProt ID | Q9NX07 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 287 aa / 32.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.7; PDB: 2DHG, 2DIV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR035979, IPR000504, IPR034510, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.0/180** | |
| **归一化总分** | | | **77.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SECP43, TRSPAP1 |

**关键文献**:
1. Phase separation of TRNAU1AP protein sustains selenoprotein translation and promotes glioblastoma tumorigenesis.. *Neuro-oncology*. PMID: 42080969
2. Novel somatic alterations underlie Chinese papillary thyroid carcinoma.. *Cancer biomarkers : section A of Disease markers*. PMID: 32065787
3. Knockdown of Trnau1ap inhibits the proliferation and migration of NIH3T3, JEG-3 and Bewo cells via the PI3K/Akt signaling pathway.. *Biochemical and biophysical research communications*. PMID: 29758194
4. Role of tRNA selenocysteine 1 associated protein 1 in the proliferation and apoptosis of cardiomyocyte‑like H9c2 cells.. *Molecular medicine reports*. PMID: 28101579
5. Selenium Deficiency-Induced Damage and Altered Expression of Mitochondrial Biogenesis Markers in the Kidneys of Mice.. *Biological trace element research*. PMID: 32172502

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.7 |
| 高置信度残基 (pLDDT>90) 占比 | 49.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 18.8% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 61.6% |
| 可用 PDB 条目 | 2DHG, 2DIV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2DHG, 2DIV）+ AlphaFold高质量预测（pLDDT=75.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR035979, IPR000504, IPR034510, IPR040434; Pfam: PF00076, PF17654 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRPF39 | 0.947 | 0.904 | — |
| PSTK | 0.938 | 0.000 | — |
| SEPSECS | 0.925 | 0.045 | — |
| SECISBP2 | 0.922 | 0.362 | — |
| EEFSEC | 0.913 | 0.144 | — |
| SEPHS2 | 0.858 | 0.000 | — |
| RBM25 | 0.838 | 0.750 | — |
| SNRPC | 0.828 | 0.752 | — |
| U2AF2 | 0.809 | 0.746 | — |
| SNRPA1 | 0.807 | 0.750 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| PRPF39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| KLK6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| - | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| SMN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| TOR1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| DLST | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CALR | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| DNM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.7 + PDB: 2DHG, 2DIV | pLDDT=75.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRNAU1AP — tRNA selenocysteine 1-associated protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小287 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NX07
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180098-TRNAU1AP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRNAU1AP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX07
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000180098-TRNAU1AP/subcellular

![](https://images.proteinatlas.org/32068/1444_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/32068/1444_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/32068/1449_A9_7_red_green.jpg)
![](https://images.proteinatlas.org/32068/1449_A9_8_red_green.jpg)
![](https://images.proteinatlas.org/32068/1516_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/32068/1516_A8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NX07-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NX07 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 3..86; /note="RRM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 96..175; /note="RRM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR012677;IPR035979;IPR000504;IPR034510;IPR040434;IPR041085; |
| Pfam | PF00076;PF17654; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000180098-TRNAU1AP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CALR | Intact | false |
| DLST | Intact | false |
| KLK6 | Intact | false |
| NEK7 | Intact | false |
| PRPF39 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
