---
type: protein-evaluation
gene: "TPCN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TPCN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TPCN2 / TPC2 |
| 蛋白名称 | Two pore channel protein 2 |
| 蛋白大小 | 752 aa / 85.2 kDa |
| UniProt ID | Q8NHX9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; UniProt: Late endosome membrane; Lysosome membrane; Melanosome membra |
| 蛋白大小 | 10/10 | ×1 | 10 | 752 aa / 85.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=49 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.9; PDB: 6NQ0, 6NQ1, 6NQ2, 8OUO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005821, IPR028798, IPR027359; Pfam: PF00520 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | Late endosome membrane; Lysosome membrane; Melanosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endolysosome membrane (GO:0036020)
- endosome membrane (GO:0010008)
- late endosome membrane (GO:0031902)
- lysosomal membrane (GO:0005765)
- lysosome (GO:0005764)
- melanosome membrane (GO:0033162)
- monoatomic ion channel complex (GO:0034702)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 49 |
| PubMed broad count | 168 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TPC2 |

**关键文献**:
1. TPCs: FROM PLANT TO HUMAN.. *Physiological reviews*. PMID: 40197126
2. Heart failure in patients is associated with downregulation of mitochondrial quality control genes.. *European journal of clinical investigation*. PMID: 37403271
3. A gain-of-function TPC2 variant R210C increases affinity to PI(3,5)P(2) and causes lysosome acidification and hypopigmentation.. *Nature communications*. PMID: 36641477
4. Transcriptome-Based Treatment for Melanoma With Brain Metastasis: A Case Report.. *Cureus*. PMID: 38638737
5. Electrophysiology of Endolysosomal Two-Pore Channels: A Current Account.. *Cells*. PMID: 35954212

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 34.8% |
| 置信残基 (pLDDT 70-90) 占比 | 45.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 11.0% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 6NQ0, 6NQ1, 6NQ2, 8OUO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6NQ0, 6NQ1, 6NQ2, 8OUO）+ AlphaFold高质量预测（pLDDT=79.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005821, IPR028798, IPR027359; Pfam: PF00520 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TPCN1 | 0.978 | 0.322 | — |
| CD38 | 0.922 | 0.000 | — |
| SLC24A4 | 0.915 | 0.000 | — |
| SLC24A5 | 0.903 | 0.000 | — |
| NADSYN1 | 0.799 | 0.000 | — |
| SLC45A2 | 0.799 | 0.000 | — |
| OCA2 | 0.786 | 0.000 | — |
| MCOLN1 | 0.768 | 0.000 | — |
| MC1R | 0.695 | 0.000 | — |
| ASIP | 0.685 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000294309.3 | psi-mi:"MI:0055"(fluorescent resonance energy tran | pubmed:21903581|imex:IM-17031 |
| TPCN1 | psi-mi:"MI:0055"(fluorescent resonance energy tran | pubmed:21903581|imex:IM-17031 |
| MTOR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23394946|imex:IM-20913 |
| DDX11L8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP3B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP3D1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAP2K7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B4GALT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STX6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 6NQ0, 6NQ1, 6NQ2, 8OUO | pLDDT=79.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome membrane; Lysosome membrane; Melanos / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TPCN2 — Two pore channel protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小752 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHX9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162341-TPCN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TPCN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHX9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000162341-TPCN2/subcellular

![](https://images.proteinatlas.org/16561/131_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16561/131_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16561/132_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16561/132_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16561/164_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16561/164_F5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
