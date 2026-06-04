---
type: protein-evaluation
gene: "POPDC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POPDC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POPDC3 / POP3 |
| 蛋白名称 | Popeye domain-containing protein 3 |
| 蛋白大小 | 291 aa / 33.9 kDa |
| UniProt ID | Q9HBV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 291 aa / 33.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018490, IPR006916, IPR055272; Pfam: PF04831 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)
- sarcolemma (GO:0042383)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: POP3 |

**关键文献**:
1. Progress on the study of Popeye domain-containing 3 (POPDC3) in malignancies and striated muscle function and homeostasis.. *Clinical genetics*. PMID: 36843357
2. Loss of popdc3 Impairs Mitochondrial Function and Causes Skeletal Muscle Atrophy and Reduced Swimming Ability in Zebrafish.. *Journal of cachexia, sarcopenia and muscle*. PMID: 40237439
3. POPDC3 Gene Variants Associate with a New Form of Limb Girdle Muscular Dystrophy.. *Annals of neurology*. PMID: 31610034
4. Homozygous missense variant in POPDC3 causes recessive limb-girdle muscular dystrophy type 26.. *The journal of gene medicine*. PMID: 35075722
5. The Role of the Popeye Domain Containing Gene Family in Organ Homeostasis.. *Cells*. PMID: 31817925

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.3 |
| 高置信度残基 (pLDDT>90) 占比 | 53.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 15.5% |
| 低置信 (pLDDT<50) 占比 | 7.9% |
| 有序区域 (pLDDT>70) 占比 | 76.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.3，有序区 76.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018490, IPR006916, IPR055272; Pfam: PF04831 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KCNK2 | 0.553 | 0.000 | — |
| ARHGEF25 | 0.501 | 0.091 | — |
| OR7A10 | 0.480 | 0.000 | — |
| SLU7 | 0.471 | 0.000 | — |
| BVES | 0.466 | 0.000 | — |
| CPNE8 | 0.462 | 0.000 | — |
| KIF20A | 0.451 | 0.000 | — |
| TSPYL2 | 0.430 | 0.000 | — |
| SCRN1 | 0.415 | 0.399 | — |
| MROH9 | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SCRN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 1
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.3 + PDB: 无 | pLDDT=82.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 10 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. POPDC3 — Popeye domain-containing protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小291 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132429-POPDC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POPDC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
