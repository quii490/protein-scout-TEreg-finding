---
type: protein-evaluation
gene: "CXXC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CXXC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CXXC1 / CFP1, CGBP, PCCX1, PHF18 |
| 蛋白名称 | CXXC-type zinc finger protein 1 |
| 蛋白大小 | 656 aa / 75.7 kDa |
| UniProt ID | Q9P0U4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus speckle; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 656 aa / 75.7 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=69.8; PDB: 3QMB, 3QMC, 3QMD, 3QMG, 3QMH, 3QMI |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR022056, IPR037869, IPR019786, IPR002857, IPR011 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus speckle; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- histone methyltransferase complex (GO:0035097)
- nuclear matrix (GO:0016363)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- Set1C/COMPASS complex (GO:0048188)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 88 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CFP1, CGBP, PCCX1, PHF18 |

**关键文献**:
1. Role of CxxC-finger protein 1 in establishing mouse oocyte epigenetic landscapes.. *Nucleic acids research*. PMID: 33621320
2. CXXC finger protein 1 is critical for T-cell intrathymic development through regulating H3K4 trimethylation.. *Nature communications*. PMID: 27210293
3. The Gene-Regulatory Footprint of Aging Highlights Conserved Central Regulators.. *Cell reports*. PMID: 32997995
4. CXXC-finger protein 1 associates with FOXP3 to stabilize homeostasis and suppressive functions of regulatory T cells.. *eLife*. PMID: 40183773
5. CXXC finger protein 1-mediated histone H3 lysine-4 trimethylation is essential for proper meiotic crossover formation in mice.. *Development (Cambridge, England)*. PMID: 32094118

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.8 |
| 高置信度残基 (pLDDT>90) 占比 | 29.0% |
| 置信残基 (pLDDT 70-90) 占比 | 28.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 33.7% |
| 有序区域 (pLDDT>70) 占比 | 57.5% |
| 可用 PDB 条目 | 3QMB, 3QMC, 3QMD, 3QMG, 3QMH, 3QMI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.8），有序残基占 57.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022056, IPR037869, IPR019786, IPR002857, IPR011011; Pfam: PF12269, PF00628, PF02008 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SETD1B | 0.999 | 0.982 | — |
| WDR5 | 0.999 | 0.931 | — |
| SETD1A | 0.999 | 0.987 | — |
| ASH2L | 0.999 | 0.994 | — |
| RBBP5 | 0.999 | 0.994 | — |
| DPY30 | 0.999 | 0.923 | — |
| WDR82 | 0.999 | 0.966 | — |
| HCFC1 | 0.993 | 0.614 | — |
| PRDM9 | 0.976 | 0.000 | — |
| BOD1L1 | 0.928 | 0.835 | — |

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
| 三维结构 | AlphaFold pLDDT=69.8 + PDB: 3QMB, 3QMC, 3QMD, 3QMG, 3QMH,  | pLDDT=69.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus speckle; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CXXC1 -- CXXC-type zinc finger protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小656 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0U4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154832-CXXC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CXXC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0U4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000154832-CXXC1/subcellular

![](https://images.proteinatlas.org/44511/1046_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/44511/1046_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/44511/1182_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/44511/1182_F7_3_red_green.jpg)
![](https://images.proteinatlas.org/44511/528_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/44511/528_F12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P0U4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
