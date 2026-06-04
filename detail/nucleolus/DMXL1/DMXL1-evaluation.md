---
type: protein-evaluation
gene: "DMXL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMXL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMXL1 / XL1 |
| 蛋白名称 | DmX-like protein 1 |
| 蛋白大小 | 3027 aa / 337.8 kDa |
| UniProt ID | Q9Y485 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoli, Nucleoli fibrillar center; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 0/10 | x1 | 0 | 3027 aa / 337.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (<=20->10) |
| 三维结构 | 4/10 | x3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR052208, IPR022033, IPR015943, IPR036322, IPR001 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli fibrillar center; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- RAVE complex (GO:0043291)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XL1 |

**关键文献**:
1. A heterotrimeric protein complex assembles the metazoan V-ATPase upon dissipation of proton gradients.. *Nature structural & molecular biology*. PMID: 40646309
2. Mapping and structure of DMXL1, a human homologue of the DmX gene from Drosophila melanogaster coding for a WD repeat protein.. *Genomics*. PMID: 10708522
3. Dmxl1 Is an Essential Mammalian Gene that Is Required for V-ATPase Assembly and Function In Vivo.. *Function (Oxford, England)*. PMID: 38984989
4. Human cytomegalovirus degrades DMXL1 to inhibit autophagy, lysosomal acidification, and viral assembly.. *Cell host & microbe*. PMID: 38479395
5. Germline gene fusions across species reveal the chromosomal instability regions and cancer susceptibility.. *iScience*. PMID: 38205119

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: AlphaFold数据未获取。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052208, IPR022033, IPR015943, IPR036322, IPR001680; Pfam: PF12234, PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ROGDI | 0.969 | 0.886 | — |
| ATP6V1B1 | 0.907 | 0.883 | — |
| ATP6V1B2 | 0.877 | 0.839 | — |
| WDR7 | 0.864 | 0.629 | — |
| ATP6V1C2 | 0.835 | 0.810 | — |
| ATP6V1G1 | 0.806 | 0.782 | — |
| RAB3GAP1 | 0.762 | 0.126 | — |
| ATP6V1E1 | 0.725 | 0.641 | — |
| RAB3GAP2 | 0.720 | 0.000 | — |
| BDP1 | 0.629 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2826714 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PDIA6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2AC14 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| POGZ | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATP6V1C2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP6V1B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ROGDI | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RNASEH2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli, Nucleoli fibrillar center; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DMXL1 -- DmX-like protein 1，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小3027 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y485
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172869-DMXL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMXL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y485
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
