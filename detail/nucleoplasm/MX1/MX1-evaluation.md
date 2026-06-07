---
type: protein-evaluation
gene: "MX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MX1 — REJECTED (研究热度过高 (PubMed strict=1351，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MX1 |
| 蛋白名称 | Interferon-induced GTP-binding protein Mx1 |
| 蛋白大小 | 662 aa / 75.5 kDa |
| UniProt ID | P20591 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Cytosol; UniProt: Cytoplasm; Endoplasmic reticulum membrane; Cytoplasm, perinu |
| 蛋白大小 | 10/10 | ×1 | 10 | 662 aa / 75.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1351 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.2; PDB: 3LJB, 3SZR, 3ZYS, 4P4S, 4P4T, 4P4U, 5GTM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR022812, IPR001401, IPR019762, IPR045063, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Cytosol | Supported |
| UniProt | Cytoplasm; Endoplasmic reticulum membrane; Cytoplasm, perinuclear region; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- microtubule (GO:0005874)
- nuclear membrane (GO:0031965)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1351 |
| PubMed broad count | 2722 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. SARS-CoV-2 human challenge reveals biomarkers that discriminate early and late phases of respiratory viral infections.. *Nature communications*. PMID: 39616162
2. Rare variant MX1 alleles increase human susceptibility to zoonotic H7N9 influenza virus.. *Science (New York, N.Y.)*. PMID: 34413236
3. Endoplasmic reticulum stress-related gene expression causes the progression of dilated cardiomyopathy by inducing apoptosis.. *Frontiers in genetics*. PMID: 38699233
4. MX1 and UBE2L6 are potential metaflammation gene targets in both diabetes and atherosclerosis.. *PeerJ*. PMID: 38406276
5. A new serological autoantibody signature associated with multiple sclerosis.. *Neurobiology of disease*. PMID: 41038542

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 48.0% |
| 置信残基 (pLDDT 70-90) 占比 | 38.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 8.6% |
| 有序区域 (pLDDT>70) 占比 | 86.7% |
| 可用 PDB 条目 | 3LJB, 3SZR, 3ZYS, 4P4S, 4P4T, 4P4U, 5GTM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3LJB, 3SZR, 3ZYS, 4P4S, 4P4T, 4P4U, 5GTM）+ AlphaFold极高置信度预测（pLDDT=83.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022812, IPR001401, IPR019762, IPR045063, IPR000375; Pfam: PF01031, PF00350, PF02212 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ISG15 | 0.994 | 0.104 | — |
| IFIT1 | 0.989 | 0.000 | — |
| OAS1 | 0.985 | 0.000 | — |
| RSAD2 | 0.983 | 0.000 | — |
| IRF9 | 0.982 | 0.000 | — |
| MX2 | 0.979 | 0.000 | — |
| EIF2AK2 | 0.979 | 0.070 | — |
| OAS2 | 0.978 | 0.000 | — |
| IFIT3 | 0.972 | 0.000 | — |
| DDX58 | 0.971 | 0.047 | — |

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
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 3LJB, 3SZR, 3ZYS, 4P4S, 4P4T,  | pLDDT=83.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endoplasmic reticulum membrane; Cytopla / Nuclear membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. MX1 — Interferon-induced GTP-binding protein Mx1，研究基础较多，新颖性有限。
2. 蛋白大小662 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1351 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1351 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20591
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157601-MX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20591
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P20591-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P20591 |
| SMART | SM00053;SM00302; |
| UniProt Domain [FT] | DOMAIN 67..340; /note="Dynamin-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01055"; DOMAIN 574..662; /note="GED"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00720" |
| InterPro | IPR022812;IPR001401;IPR019762;IPR045063;IPR000375;IPR030381;IPR003130;IPR020850;IPR027417; |
| Pfam | PF01031;PF00350;PF02212; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157601-MX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LGALS3BP | Intact, Biogrid | true |
| BCS1L | Intact | false |
| C18orf21 | Bioplex | false |
| CAB39L | Intact | false |
| DAXX | Biogrid | false |
| ISG15 | Biogrid | false |
| MCCD1 | Intact | false |
| PIAS1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
