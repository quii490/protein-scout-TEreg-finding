---
type: protein-evaluation
gene: "ACD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACD — REJECTED (研究热度过高 (PubMed strict=1015，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACD / PIP1, PTOP, TINT1, TPP1 |
| 蛋白名称 | Adrenocortical dysplasia protein homolog |
| 蛋白大小 | 458 aa / 49.0 kDa |
| UniProt ID | Q96AP0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; UniProt: Nucleus; Chromosome, telomere |
| 蛋白大小 | 10/10 | ×1 | 10 | 458 aa / 49.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1015 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.4; PDB: 2I46, 5H65, 5I2X, 5I2Y, 5UN7, 5XYF, 7QXA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028631, IPR019437; Pfam: PF10341 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Enhanced |
| UniProt | Nucleus; Chromosome, telomere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear body (GO:0016604)
- nuclear telomere cap complex (GO:0000783)
- nucleoplasm (GO:0005654)
- shelterin complex (GO:0070187)
- telomerase holoenzyme complex (GO:0005697)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1015 |
| PubMed broad count | 10077 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PIP1, PTOP, TINT1, TPP1 |

**关键文献**:
1. Plasma proteomic profiles predict future dementia in healthy adults.. *Nature aging*. PMID: 38347190
2. ATF4 links ER stress with reticulophagy in glioblastoma cells.. *Autophagy*. PMID: 33111629
3. Activation of Mast-Cell-Expressed Mas-Related G-Protein-Coupled Receptors Drives Non-histaminergic Itch.. *Immunity*. PMID: 31027996
4. CSF Findings in Relation to Clinical Characteristics, Subtype, and Disease Course in Patients With Guillain-Barré Syndrome.. *Neurology*. PMID: 37076309
5. Allergic contact dermatitis.. *European journal of dermatology : EJD*. PMID: 15358566

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.4 |
| 高置信度残基 (pLDDT>90) 占比 | 20.5% |
| 置信残基 (pLDDT 70-90) 占比 | 22.7% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 38.9% |
| 有序区域 (pLDDT>70) 占比 | 43.2% |
| 可用 PDB 条目 | 2I46, 5H65, 5I2X, 5I2Y, 5UN7, 5XYF, 7QXA, 7QXB, 7QXS, 7S1T |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.4），有序残基占 43.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028631, IPR019437; Pfam: PF10341 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TERF1 | 0.999 | 0.878 | — |
| TERF2IP | 0.999 | 0.874 | — |
| TINF2 | 0.999 | 0.991 | — |
| TERF2 | 0.999 | 0.922 | — |
| POT1 | 0.999 | 0.991 | — |
| TERT | 0.982 | 0.926 | — |
| STN1 | 0.927 | 0.301 | — |
| CTC1 | 0.906 | 0.000 | — |
| TEN1 | 0.813 | 0.000 | — |
| H2AC15 | 0.800 | 0.800 | — |

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
| 三维结构 | AlphaFold pLDDT=62.4 + PDB: 2I46, 5H65, 5I2X, 5I2Y, 5UN7,  | pLDDT=62.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, telomere / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ACD — Adrenocortical dysplasia protein homolog，研究基础较多，新颖性有限。
2. 蛋白大小458 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1015 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1015 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AP0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102977-ACD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AP0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (enhanced)。来源: https://www.proteinatlas.org/ENSG00000102977-ACD/subcellular

![](https://images.proteinatlas.org/49411/725_D6_6_red_green.jpg)
![](https://images.proteinatlas.org/49411/725_D6_8_red_green.jpg)
![](https://images.proteinatlas.org/57660/1015_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/57660/1015_G6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96AP0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96AP0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028631;IPR019437; |
| Pfam | PF10341; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
