---
type: protein-evaluation
gene: "MEIOB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEIOB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEIOB / C16orf73 |
| 蛋白名称 | Meiosis-specific with OB domain-containing protein |
| 蛋白大小 | 442 aa / 49.3 kDa |
| UniProt ID | Q8N635 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 442 aa / 49.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052469, IPR012340, IPR056880; Pfam: PF24903 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf73 |

**关键文献**:
1. Meiotic chromatin-associated HSF5 is indispensable for pachynema progression and male fertility.. *Nucleic acids research*. PMID: 39162221
2. New feature of hMEIOB and hSPATA22 binding to ssDNA from a single-molecule perspective.. *Acta biochimica et biophysica Sinica*. PMID: 40296718
3. The ssDNA-binding protein MEIOB acts as a dosage-sensitive regulator of meiotic recombination.. *Nucleic acids research*. PMID: 33166385
4. Novel MEIOB variants cause primary ovarian insufficiency and non-obstructive azoospermia.. *Frontiers in genetics*. PMID: 35991565
5. A new MEIOB mutation is a recurrent cause for azoospermia and testicular meiotic arrest.. *Human reproduction (Oxford, England)*. PMID: 30838384

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.9 |
| 高置信度残基 (pLDDT>90) 占比 | 43.7% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 13.8% |
| 低置信 (pLDDT<50) 占比 | 9.7% |
| 有序区域 (pLDDT>70) 占比 | 76.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.9，有序区 76.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052469, IPR012340, IPR056880; Pfam: PF24903 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPATA22 | 0.967 | 0.000 | — |
| FANCM | 0.963 | 0.913 | — |
| RAD52 | 0.870 | 0.792 | — |
| ATR | 0.842 | 0.753 | — |
| TERT | 0.803 | 0.767 | — |
| DNA2 | 0.764 | 0.627 | — |
| MCM9 | 0.715 | 0.314 | — |
| RAD51 | 0.711 | 0.410 | — |
| SPO11 | 0.706 | 0.000 | — |
| MSH4 | 0.705 | 0.183 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GAPDHS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.9 + PDB: 无 | pLDDT=80.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MEIOB — Meiosis-specific with OB domain-containing protein，非常新颖，仅有少数基础研究。
2. 蛋白大小442 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N635
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162039-MEIOB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEIOB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N635
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
