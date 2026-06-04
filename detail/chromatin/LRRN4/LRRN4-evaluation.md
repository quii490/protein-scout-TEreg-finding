---
type: protein-evaluation
gene: "LRRN4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRN4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRN4 / LRN, LRRN1, LRRN4 |
| 蛋白名称 | Leucine-rich repeat and calponin homology domain-containing protein 4 |
| 蛋白大小 | 683 aa / 73.5 kDa |
| UniProt ID | O75427 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Nucleoli rim, Mitotic chromosome; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 683 aa / 73.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001715, IPR036872, IPR001611, IPR003591, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim, Mitotic chromosome | Uncertain |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)
- PML body (GO:0016605)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LRN, LRRN1, LRRN4 |

**关键文献**:
1. Prognostic value and biological function of LRRN4 in colorectal cancer.. *Cancer cell international*. PMID: 35440048
2. Leucine-rich repeat neuronal protein 4 (LRRN4) potentially functions in dilated cardiomyopathy.. *International journal of clinical and experimental pathology*. PMID: 31966882
3. Expression pattern of leucine-rich repeat neuronal protein 4 in adult mouse dorsal root ganglia.. *Neuroscience letters*. PMID: 23069668
4. Targeting cholecystokinin-2 receptor for pancreatic cancer chemoprevention.. *Molecular carcinogenesis*. PMID: 31313401
5. Genome-Wide Analysis of Structural Variants in Parkinson Disease.. *Annals of neurology*. PMID: 36695634

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.2 |
| 高置信度残基 (pLDDT>90) 占比 | 23.7% |
| 置信残基 (pLDDT 70-90) 占比 | 28.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 42.3% |
| 有序区域 (pLDDT>70) 占比 | 51.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.2），有序残基占 51.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001715, IPR036872, IPR001611, IPR003591, IPR032675; Pfam: PF00307, PF13855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UPK3B | 0.738 | 0.000 | — |
| ADGRL2 | 0.515 | 0.514 | — |
| ADGRL1 | 0.514 | 0.514 | — |
| ADGRL3 | 0.514 | 0.514 | — |
| MSLN | 0.489 | 0.000 | — |
| NKAIN4 | 0.482 | 0.000 | — |
| GPM6A | 0.454 | 0.000 | — |
| HIGD1B | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 8，IntAct interactions: 0
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.2 + PDB: 无 | pLDDT=64.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Nucleoli, Nucleoli rim, Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 8 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRN4 — Leucine-rich repeat and calponin homology domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小683 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75427
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125872-LRRN4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75427
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
