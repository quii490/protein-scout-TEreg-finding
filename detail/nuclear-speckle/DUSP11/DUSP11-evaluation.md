---
type: protein-evaluation
gene: "DUSP11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP11 / PIR1 |
| 蛋白名称 | RNA/RNP complex-1-interacting phosphatase |
| 蛋白大小 | 330 aa / 38.9 kDa |
| UniProt ID | O75319 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center; 额外: Cytokinetic brid; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 330 aa / 38.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 4JMJ, 4MBB, 4NYH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000340, IPR051029, IPR029021, IPR016130, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center; 额外: Cytokinetic bridge | Supported |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- fibrillar center (GO:0001650)
- intercellular bridge (GO:0045171)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PIR1 |

**关键文献**:
1. Novel autoantibodies identified in ACPA-negative rheumatoid arthritis.. *Annals of the rheumatic diseases*. PMID: 33452006
2. Isolation and characterization of DUSP11, a novel p53 target gene.. *Journal of cellular and molecular medicine*. PMID: 19120688
3. DUSP11 Attenuates Lipopolysaccharide-Induced Macrophage Activation by Targeting TAK1.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 32796023
4. DUSP11 - An RNA phosphatase that regulates host and viral non-coding RNAs in mammalian cells.. *RNA biology*. PMID: 28296624
5. DUSP11 is an Intracellular Innate Immune Checkpoint in Lung Adenocarcinoma.. *Cancer immunology research*. PMID: 40906817

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 52.7% |
| 置信残基 (pLDDT 70-90) 占比 | 1.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 43.6% |
| 有序区域 (pLDDT>70) 占比 | 54.2% |
| 可用 PDB 条目 | 4JMJ, 4MBB, 4NYH |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 54.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR051029, IPR029021, IPR016130, IPR000387; Pfam: PF00782 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DUSP5 | 0.896 | 0.048 | — |
| RNF144B | 0.732 | 0.000 | — |
| DXO | 0.691 | 0.000 | — |
| XRN1 | 0.653 | 0.115 | — |
| XRN2 | 0.624 | 0.084 | — |
| PIWIL1 | 0.612 | 0.000 | — |
| DICER1 | 0.556 | 0.136 | — |
| ERI1 | 0.537 | 0.091 | — |
| TADA1 | 0.517 | 0.326 | — |
| ADARB1 | 0.502 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 4JMJ, 4MBB, 4NYH | pLDDT=69.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / Nucleoplasm, Nucleoli fibrillar center; 额外: Cytoki | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DUSP11 — RNA/RNP complex-1-interacting phosphatase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75319
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144048-DUSP11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75319
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
