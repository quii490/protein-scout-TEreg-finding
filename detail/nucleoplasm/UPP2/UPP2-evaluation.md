---
type: protein-evaluation
gene: "UPP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UPP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UPP2 |
| 蛋白名称 | Uridine phosphorylase 2 |
| 蛋白大小 | 317 aa / 35.5 kDa |
| UniProt ID | O95045 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles, Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 317 aa / 35.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.7; PDB: 2XRF, 3P0E, 3P0F |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018016, IPR000845, IPR035994, IPR010059; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- type III intermediate filament (GO:0045098)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Liver mitochondrial cristae organizing protein MIC19 promotes energy expenditure and pedestrian locomotion by altering nucleotide metabolism.. *Cell metabolism*. PMID: 37473754
2. Developmental neurogenetics and multimodal neuroimaging of sex differences in autism.. *Brain imaging and behavior*. PMID: 26781567
3. Identification of BMAL1-Regulated circadian genes in mouse liver and their potential association with hepatocellular carcinoma: Gys2 and Upp2 as promising candidates.. *Biochemical and biophysical research communications*. PMID: 38183795
4. A novel structural mechanism for redox regulation of uridine phosphorylase 2 activity.. *Journal of structural biology*. PMID: 21855639
5. Mining for novel candidate clock genes in the circadian regulatory network.. *BMC systems biology*. PMID: 26576534

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 87.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 5.4% |
| 有序区域 (pLDDT>70) 占比 | 91.5% |
| 可用 PDB 条目 | 2XRF, 3P0E, 3P0F |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2XRF, 3P0E, 3P0F）+ AlphaFold高质量预测（pLDDT=92.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018016, IPR000845, IPR035994, IPR010059; Pfam: PF01048 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TYMP | 0.997 | 0.000 | — |
| CDA | 0.997 | 0.000 | — |
| PNP | 0.996 | 0.000 | — |
| DPYD | 0.988 | 0.000 | — |
| UMPS | 0.984 | 0.000 | — |
| UCKL1 | 0.982 | 0.000 | — |
| UCK1 | 0.982 | 0.000 | — |
| NT5E | 0.980 | 0.000 | — |
| UCK2 | 0.975 | 0.000 | — |
| UPRT | 0.969 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000005756.5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| ENSP00000474090.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EBI-16432858 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MRPL28 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SIAH1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| TAE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:27107014|imex:IM-24995 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| CCZ1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000005756 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 2XRF, 3P0E, 3P0F | pLDDT=92.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles, Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. UPP2 — Uridine phosphorylase 2，非常新颖，仅有少数基础研究。
2. 蛋白大小317 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95045
- Protein Atlas: https://www.proteinatlas.org/ENSG00000007001-UPP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UPP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95045
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
