---
type: protein-evaluation
gene: "JAK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## JAK2 — REJECTED (研究热度过高 (PubMed strict=7319，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JAK2 |
| 蛋白名称 | Tyrosine-protein kinase JAK2 |
| 蛋白大小 | 1132 aa / 130.7 kDa |
| UniProt ID | O60674 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Focal adhesion sites; UniProt: Endomembrane system; Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1132 aa / 130.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=7319 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=86.9; PDB: 2B7A, 2W1I, 2XA4, 3E62, 3E63, 3E64, 3FUP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019749, IPR035963, IPR019748, IPR000299, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Focal adhesion sites | Supported |
| UniProt | Endomembrane system; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- caveola (GO:0005901)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- endosome lumen (GO:0031904)
- euchromatin (GO:0000791)
- extrinsic component of cytoplasmic side of plasma membrane (GO:0031234)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7319 |
| PubMed broad count | 17572 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. JAK2 exon 12 mutations in polycythemia vera and idiopathic erythrocytosis.. *The New England journal of medicine*. PMID: 17267906
2. Somatic CALR mutations in myeloproliferative neoplasms with nonmutated JAK2.. *The New England journal of medicine*. PMID: 24325359
3. JAK2-mediated Intracellular Signaling.. *Current molecular medicine*. PMID: 33059575
4. [JAK2, CALR].. *Rinsho byori. The Japanese journal of clinical pathology*. PMID: 30695513
5. Growth-hormone signal transduction.. *The Journal of pediatrics*. PMID: 9255227

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.9 |
| 高置信度残基 (pLDDT>90) 占比 | 66.8% |
| 置信残基 (pLDDT 70-90) 占比 | 22.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 89.4% |
| 可用 PDB 条目 | 2B7A, 2W1I, 2XA4, 3E62, 3E63, 3E64, 3FUP, 3IO7, 3IOK, 3JY9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2B7A, 2W1I, 2XA4, 3E62, 3E63, 3E64, 3FUP, 3IO7, 3IOK, 3JY9）+ AlphaFold极高置信度预测（pLDDT=86.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019749, IPR035963, IPR019748, IPR000299, IPR041155; Pfam: PF18379, PF18377, PF17887 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STAT1 | 0.999 | 0.838 | — |
| LEPR | 0.999 | 0.928 | — |
| STAT5A | 0.999 | 0.802 | — |
| SOCS3 | 0.999 | 0.923 | — |
| EPOR | 0.999 | 0.962 | — |
| IFNGR2 | 0.999 | 0.345 | — |
| STAT3 | 0.999 | 0.885 | — |
| IFNGR1 | 0.999 | 0.525 | — |
| STAT5B | 0.999 | 0.718 | — |
| GHR | 0.999 | 0.787 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LEPR | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11585385 |
| - | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14968112 |
| ASS1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TRAF6 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RBMX | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| Csf2rb | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11911|pubmed:18692472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.9 + PDB: 2B7A, 2W1I, 2XA4, 3E62, 3E63,  | pLDDT=86.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endomembrane system; Cytoplasm; Nucleus / Nucleoplasm; 额外: Plasma membrane, Focal adhesion s | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. JAK2 — Tyrosine-protein kinase JAK2，研究基础较多，新颖性有限。
2. 蛋白大小1132 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7319 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 7319 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60674
- Protein Atlas: https://www.proteinatlas.org/ENSG00000096968-JAK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JAK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60674
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000096968-JAK2/subcellular

![](https://images.proteinatlas.org/43870/1337_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/43870/1337_A2_3_red_green.jpg)
![](https://images.proteinatlas.org/43870/1338_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/43870/1338_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/43870/1587_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/43870/1587_G3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60674-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60674 |
| SMART | SM00295;SM00252;SM00219; |
| UniProt Domain [FT] | DOMAIN 37..380; /note="FERM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00084"; DOMAIN 401..482; /note="SH2; atypical"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191"; DOMAIN 545..809; /note="Protein kinase 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159"; DOMAIN 849..1124; /note="Protein kinase 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR019749;IPR035963;IPR019748;IPR000299;IPR041155;IPR041046;IPR051286;IPR041381;IPR037838;IPR035860;IPR011009;IPR011993;IPR000719;IPR017441;IPR035588;IPR035589;IPR001245;IPR000980;IPR036860;IPR008266;IPR020635;IPR016251;IPR020693; |
| Pfam | PF18379;PF18377;PF17887;PF07714;PF21990; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000096968-JAK2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSF2RB | Intact, Biogrid | true |
| IL5RA | Intact, Biogrid | true |
| PTPN1 | Intact, Biogrid | true |
| CBL | Biogrid | false |
| CDKN1B | Biogrid | false |
| EGFR | Biogrid | false |
| EPOR | Biogrid | false |
| FYN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
