---
type: protein-evaluation
gene: "EQTN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EQTN — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EQTN / AFAF, C9orf11 |
| 蛋白名称 | Equatorin |
| 蛋白大小 | 294 aa / 32.8 kDa |
| UniProt ID | Q9NQ60 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Actin filaments; UniProt: Cytoplasmic vesicle, secretory vesicle, acrosome membrane; C |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 32.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029282; Pfam: PF15339 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Actin filaments | Approved |
| UniProt | Cytoplasmic vesicle, secretory vesicle, acrosome membrane; Cytoplasmic vesicle, secretory vesicle, a... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- inner acrosomal membrane (GO:0002079)
- outer acrosomal membrane (GO:0002081)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AFAF, C9orf11 |

**关键文献**:
1. Equatorin is not essential for acrosome biogenesis but is required for the acrosome reaction.. *Biochemical and biophysical research communications*. PMID: 24480441
2. Transcription factors involved in the regulatory networks governing the Calvin-Benson-Bassham cycle.. *Tree physiology*. PMID: 30941430
3. Deletion of Eqtn in mice reduces male fertility and sperm-egg adhesion.. *Reproduction (Cambridge, England)*. PMID: 30328350
4. Identification of Anoikis-Related Genes in Gastric Cancer: Bioinformatics and Experimental Validation.. *Cancer medicine*. PMID: 40263929
5. Establishment of a male fertility prediction model with sperm RNA markers in pigs as a translational animal model.. *Journal of animal science and biotechnology*. PMID: 35794675

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.9 |
| 高置信度残基 (pLDDT>90) 占比 | 9.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 30.6% |
| 低置信 (pLDDT<50) 占比 | 40.5% |
| 有序区域 (pLDDT>70) 占比 | 28.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.9），有序残基占 28.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029282; Pfam: PF15339 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCNA | 0.658 | 0.416 | — |
| PAN3 | 0.574 | 0.498 | — |
| MOB3B | 0.554 | 0.000 | — |
| FAM170B | 0.496 | 0.000 | — |
| APMAP | 0.485 | 0.000 | — |
| IFNK | 0.471 | 0.000 | — |
| TEX101 | 0.464 | 0.000 | — |
| IZUMO1 | 0.462 | 0.000 | — |
| SPAM1 | 0.454 | 0.000 | — |
| EXOSC10 | 0.435 | 0.156 | — |

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
| 三维结构 | AlphaFold pLDDT=58.9 + PDB: 无 | pLDDT=58.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle, acrosome m / Plasma membrane, Actin filaments | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EQTN — Equatorin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ60
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120160-EQTN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EQTN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ60
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000120160-EQTN/subcellular

![](https://images.proteinatlas.org/15504/1973_A7_22_cr5df78be05c666_blue_red_green.jpg)
![](https://images.proteinatlas.org/15504/1973_A7_5_cr5df78be05bfa7_blue_red_green.jpg)
![](https://images.proteinatlas.org/15504/1977_B9_38_cr5e568627511dd_blue_red_green.jpg)
![](https://images.proteinatlas.org/15504/1977_B9_51_cr5e5686275140c_blue_red_green.jpg)
![](https://images.proteinatlas.org/15504/2030_D9_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/15504/2030_D9_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQ60-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
