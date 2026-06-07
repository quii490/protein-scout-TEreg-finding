---
type: protein-evaluation
gene: "GIMAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GIMAP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GIMAP2 / IMAP2 |
| 蛋白名称 | GTPase IMAP family member 2 |
| 蛋白大小 | 337 aa / 38.0 kDa |
| UniProt ID | Q9UG22 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Lipid droplets; 额外: Nucleoplasm; UniProt: Lipid droplet |
| 蛋白大小 | 10/10 | ×1 | 10 | 337 aa / 38.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.9; PDB: 2XTM, 2XTN, 2XTO, 2XTP, 3P1J |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.5/180** | |
| **归一化总分** | | | **79.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Lipid droplets; 额外: Nucleoplasm | Supported |
| UniProt | Lipid droplet | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- lipid droplet (GO:0005811)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IMAP2 |

**关键文献**:
1. Identification and clinical validation of diverse cell-death patterns-associated prognostic features among low-grade gliomas.. *Scientific reports*. PMID: 38789729
2. [Subcellular localization of GTPase of immunity-associated protein 2].. *Beijing da xue xue bao. Yi xue ban = Journal of Peking University. Health sciences*. PMID: 32306002
3. Aberrant GIMAP2 expression affects oral squamous cell carcinoma progression by promoting cell cycle and inhibiting apoptosis.. *Oncology letters*. PMID: 34992682
4. Structural basis of oligomerization in septin-like GTPase of immunity-associated protein 2 (GIMAP2).. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 21059949
5. Identification of the GTPase IMAP family as an immune-related prognostic biomarker in the breast cancer tumor microenvironment.. *Gene*. PMID: 34896519

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.9 |
| 高置信度残基 (pLDDT>90) 占比 | 71.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 5.6% |
| 有序区域 (pLDDT>70) 占比 | 89.9% |
| 可用 PDB 条目 | 2XTM, 2XTN, 2XTO, 2XTP, 3P1J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2XTM, 2XTN, 2XTO, 2XTP, 3P1J）+ AlphaFold极高置信度预测（pLDDT=88.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOR1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STOM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRMT8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM54 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ARFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PNPLA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LDAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 9
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.9 + PDB: 2XTM, 2XTN, 2XTO, 2XTP, 3P1J | pLDDT=88.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lipid droplet / Lipid droplets; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 9 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GIMAP2 — GTPase IMAP family member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小337 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UG22
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106560-GIMAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GIMAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UG22
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Lipid droplets (supported)。来源: https://www.proteinatlas.org/ENSG00000106560-GIMAP2/subcellular

![](https://images.proteinatlas.org/14746/1878_A7_11_cr5b803a9ded872_red_green.jpg)
![](https://images.proteinatlas.org/14746/1878_A7_6_cr5b803a9dec532_red_green.jpg)
![](https://images.proteinatlas.org/14746/1976_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/14746/1976_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/14746/2027_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/14746/2027_G10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UG22-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UG22 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 20..223; /note="AIG1-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01057" |
| InterPro | IPR006703;IPR045058;IPR027417; |
| Pfam | PF04548; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106560-GIMAP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HTT | Intact | false |
| LDAF1 | Bioplex | false |
| PNPLA2 | Bioplex | false |
| STOM | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
