---
type: protein-evaluation
gene: "PIR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PIR — REJECTED (研究热度过高 (PubMed strict=845，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PIR |
| 蛋白名称 | Pirin |
| 蛋白大小 | 290 aa / 32.1 kDa |
| UniProt ID | O00625 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 290 aa / 32.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=845 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.0; PDB: 1J1L, 3ACL, 4ERO, 4EWA, 4EWD, 4EWE, 4GUL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012093, IPR008778, IPR003829, IPR014710, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 845 |
| PubMed broad count | 4468 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nuclear Pirin promotes HCC by acting as a key inflammation-facilitating factor.. *Gut*. PMID: 40579121
2. UniProtKB/Swiss-Prot.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 18287689
3. piR-RCC Suppresses Renal Cell Carcinoma Progression by Facilitating YBX-1 Cytoplasm Localization.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40411401
4. The PIR-International databases.. *Nucleic acids research*. PMID: 8332528
5. Specification of claustro-amygdalar and palaeocortical neurons and circuits.. *Nature*. PMID: 39814878

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.0 |
| 高置信度残基 (pLDDT>90) 占比 | 98.3% |
| 置信残基 (pLDDT 70-90) 占比 | 1.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.3% |
| 可用 PDB 条目 | 1J1L, 3ACL, 4ERO, 4EWA, 4EWD, 4EWE, 4GUL, 4HLT, 5JCT, 6H1H |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1J1L, 3ACL, 4ERO, 4EWA, 4EWD, 4EWE, 4GUL, 4HLT, 5JCT, 6H1H）+ AlphaFold极高置信度预测（pLDDT=97.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012093, IPR008778, IPR003829, IPR014710, IPR011051; Pfam: PF02678, PF05726 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BCL3 | 0.983 | 0.516 | — |
| PIWIL4 | 0.981 | 0.000 | — |
| PIWIL1 | 0.971 | 0.000 | — |
| PIWIL2 | 0.941 | 0.000 | — |
| CTF1 | 0.910 | 0.000 | — |
| AGO3 | 0.639 | 0.095 | — |
| RDX | 0.609 | 0.000 | — |
| C2orf68 | 0.606 | 0.606 | — |
| MSN | 0.600 | 0.000 | — |
| PIWIL3 | 0.597 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KHDRBS1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| C2orf68 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RIN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32552912|imex:IM-28480 |
| PUF60 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NAP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17267444|imex:IM-19126 |
| NCKAP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15296760 |
| ARAC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15294869 |
| RAC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15294869 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.0 + PDB: 1J1L, 3ACL, 4ERO, 4EWA, 4EWD,  | pLDDT=97.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
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
1. PIR — Pirin，研究基础较多，新颖性有限。
2. 蛋白大小290 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 845 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 845 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00625
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087842-PIR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PIR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00625
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000087842-PIR/subcellular

![](https://images.proteinatlas.org/75091/1803_B1_4_red_green.jpg)
![](https://images.proteinatlas.org/75091/1803_B1_5_red_green.jpg)
![](https://images.proteinatlas.org/75091/1893_M10_14_cr5bc33767c58fe_red_green.jpg)
![](https://images.proteinatlas.org/75091/1893_M10_31_red_green.jpg)
![](https://images.proteinatlas.org/75091/2096_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/75091/2096_H6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00625-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O00625 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012093;IPR008778;IPR003829;IPR014710;IPR011051; |
| Pfam | PF02678;PF05726; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000087842-PIR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCL3 | Biogrid | false |
| MIF | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
