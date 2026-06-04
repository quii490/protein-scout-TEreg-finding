---
type: protein-evaluation
gene: "BPNT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BPNT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BPNT2 / IMPA3, IMPAD1 |
| 蛋白名称 | Golgi-resident adenosine 3',5'-bisphosphate 3'-phosphatase |
| 蛋白大小 | 359 aa / 38.7 kDa |
| UniProt ID | Q9NX62 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:43:29 |

**IF 图像**:
![](https://images.proteinatlas.org/9411/48_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9411/48_E6_2_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Golgi apparatus; UniProt: Golgi ... |
| 蛋白大小 | 10/10 | x1 | 10 | 359 aa / 38.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (<=20->10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=87.7 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR050725, IPR000760... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **155.5/180** | |
| **归一化总分 (/1.83)** | | | **85.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Golgi apparatus, Cytosol | Supported |
| UniProt | Golgi apparatus, Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endomembrane system (GO:0012505)
- Golgi apparatus (GO:0005794)
- Golgi lumen (GO:0005796)
- membrane (GO:0016020)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- trans-Golgi network membrane (GO:0032588)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IMPA3, IMPAD1 |

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 68.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 8.6% |
| 有序区域 (pLDDT>70) 占比 | 88.5% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold高质量预测（pLDDT=87.7），预测结构可信。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050725, IPR000760, IPR020550; Pfam: PF00459 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAPSS2 | 0.975 | 0.000 | -- |
| PAPSS1 | 0.974 | 0.000 | -- |
| IMPA1 | 0.963 | 0.000 | -- |
| IMPA2 | 0.958 | 0.000 | -- |
| BPNT1 | 0.929 | 0.000 | -- |
| CDIPT | 0.922 | 0.058 | -- |
| INPP1 | 0.915 | 0.000 | -- |
| MTM1 | 0.915 | 0.000 | -- |
| INPP4B | 0.912 | 0.000 | -- |
| INPP4A | 0.901 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| N4BP3 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| MLH3 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| HTR3C | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ST8SIA4 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CRP | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PCDHB11 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| UST | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MCOLN3 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| TCTN2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ATP1B3 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=87.7 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 85.0/100

**核心优势**:
1. BPNT2 -- Golgi-resident adenosine 3',5'-bisphosphate 3'-phosphatase，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold高质量预测（pLDDT=87.7），结构可信度高。
4. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 核定位信号较弱或存在矛盾（评分 5/10），需IF实验验证
3. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9NX62
- Protein Atlas: https://www.proteinatlas.org/search/BPNT2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BPNT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX62
- STRING: https://string-db.org/network/9606.BPNT2
- Packet data timestamp: 2026-06-03 03:43:29
