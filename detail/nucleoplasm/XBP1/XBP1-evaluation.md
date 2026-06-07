---
type: protein-evaluation
gene: "XBP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## XBP1 — REJECTED (研究热度过高 (PubMed strict=3290，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XBP1 / TREB5, XBP2 |
| 蛋白名称 | X-box-binding protein 1 |
| 蛋白大小 | 261 aa / 28.7 kDa |
| UniProt ID | P17861 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum; Nucleus; Cytoplasm; Endoplasmic retic |
| 蛋白大小 | 10/10 | ×1 | 10 | 261 aa / 28.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3290 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.3; PDB: 6R5Q, 6R6G, 6R6P, 6R7Q, 9NDP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR052470; Pfam: PF07716 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum; Nucleus; Cytoplasm; Endoplasmic reticulum membrane; Endoplasmic reticulum mem... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3290 |
| PubMed broad count | 4201 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TREB5, XBP2 |

**关键文献**:
1. Role of XBP1 in regulating the progression of non-alcoholic steatohepatitis.. *Journal of hepatology*. PMID: 35292349
2. XBP1 promotes triple-negative breast cancer by controlling the HIF1α pathway.. *Nature*. PMID: 24670641
3. IRE1α-XBP1 controls T cell function in ovarian cancer by regulating mitochondrial activity.. *Nature*. PMID: 30305738
4. Unfolded protein response transcription factor XBP1 suppresses necroptosis-induced colitis by reinforcing the mucus barrier.. *Immunity*. PMID: 40865520
5. Cancer cell-intrinsic XBP1 drives immunosuppressive reprogramming of intratumoral myeloid cells by promoting cholesterol production.. *Cell metabolism*. PMID: 36351432

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.3 |
| 高置信度残基 (pLDDT>90) 占比 | 30.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 26.1% |
| 低置信 (pLDDT<50) 占比 | 29.9% |
| 有序区域 (pLDDT>70) 占比 | 44.1% |
| 可用 PDB 条目 | 6R5Q, 6R6G, 6R6P, 6R7Q, 9NDP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.3），有序残基占 44.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR052470; Pfam: PF07716 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATF6 | 0.998 | 0.574 | — |
| ERN1 | 0.997 | 0.079 | — |
| DDIT3 | 0.988 | 0.071 | — |
| HIF1A | 0.988 | 0.292 | — |
| HSPA5 | 0.980 | 0.345 | — |
| EDEM1 | 0.976 | 0.000 | — |
| DNAJB9 | 0.952 | 0.000 | — |
| DNAJC3 | 0.951 | 0.000 | — |
| HYOU1 | 0.938 | 0.000 | — |
| TBP | 0.938 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RpS26 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CycB | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RpL36 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Vta1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ciz1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Neos | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmc1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RpS18 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mkk4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Nep2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.3 + PDB: 6R5Q, 6R6G, 6R6P, 6R7Q, 9NDP | pLDDT=68.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum; Nucleus; Cytoplasm; Endopla / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. XBP1 — X-box-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小261 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3290 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3290 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17861
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100219-XBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17861
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P17861-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P17861 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 70..133; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR046347;IPR052470; |
| Pfam | PF07716; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100219-XBP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF6 | Intact | false |
| CREBZF | Intact | false |
| ESR1 | Biogrid | false |
| HIF1A | Intact | false |
| MDM2 | Biogrid | false |
| UBE2I | Biogrid | false |
| UBE2V1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
