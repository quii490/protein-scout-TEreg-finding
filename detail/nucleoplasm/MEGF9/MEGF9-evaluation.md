---
type: protein-evaluation
gene: "MEGF9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEGF9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEGF9 / EGFL5, KIAA0818 |
| 蛋白名称 | Multiple epidermal growth factor-like domains protein 9 |
| 蛋白大小 | 602 aa / 63.0 kDa |
| UniProt ID | Q9H1U4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 602 aa / 63.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000742, IPR050440, IPR002049, IPR056863; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- basement membrane (GO:0005604)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EGFL5, KIAA0818 |

**关键文献**:
1. Plasma proteomics profiles predict the risk of future aortic aneurysm and aortic dissection.. *International journal of surgery (London, England)*. PMID: 40576182
2. MEGF9 prevents lipopolysaccharide-induced cardiac dysfunction through activating AMPK pathway.. *Redox report : communications in free radical research*. PMID: 39737911
3. MEGF9: a novel transmembrane protein with a strong and developmentally regulated expression in the nervous system.. *The Biochemical journal*. PMID: 16981854
4. Identification of Key Modules and Genes Associated with Major Depressive Disorder in Adolescents.. *Genes*. PMID: 35328018
5. DNA methylation differences during development distinguish sympatric morphs of Arctic charr (Salvelinus alpinus).. *Molecular ecology*. PMID: 35848921

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.5 |
| 高置信度残基 (pLDDT>90) 占比 | 34.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 42.0% |
| 有序区域 (pLDDT>70) 占比 | 47.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.5），有序残基占 47.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000742, IPR050440, IPR002049, IPR056863; Pfam: PF00053, PF24973 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EGF | 0.615 | 0.085 | — |
| CCNJ | 0.571 | 0.000 | — |
| DLK2 | 0.482 | 0.000 | — |
| EGFL6 | 0.449 | 0.000 | — |
| EGFL8 | 0.439 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LGALS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TCAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DPP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYH4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DYRK1A | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| ENST00000373930 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 6
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.5 + PDB: 无 | pLDDT=66.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 5 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MEGF9 — Multiple epidermal growth factor-like domains protein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小602 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H1U4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106780-MEGF9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEGF9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H1U4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
