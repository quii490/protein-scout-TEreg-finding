---
type: protein-evaluation
gene: "GLI2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLI2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLI2 / THP |
| 蛋白名称 | Zinc finger protein GLI2 |
| 蛋白大小 | 1586 aa / 167.8 kDa |
| UniProt ID | P10070 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm, Centrosome, Basal body; UniProt: Nucleus; Cytoplasm; Cell projection, cilium; Nucleus; Nucleu |
| 蛋白大小 | 5/10 | ×1 | 5 | 1586 aa / 167.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043359, IPR056436, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Centrosome, Basal body | Supported |
| UniProt | Nucleus; Cytoplasm; Cell projection, cilium; Nucleus; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- ciliary tip (GO:0097542)
- cilium (GO:0005929)
- cytosol (GO:0005829)
- GLI-SUFU complex (GO:1990788)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 84.2% |
| 有序区域 (pLDDT>70) 占比 | 12.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.0），有序残基占 12.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043359, IPR056436, IPR036236, IPR013087; Pfam: PF00096, PF23561 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUFU | 0.999 | 0.815 | — |
| KIF7 | 0.997 | 0.579 | — |
| THOC2 | 0.992 | 0.045 | — |
| SPOP | 0.991 | 0.726 | — |
| CYLD | 0.988 | 0.000 | — |
| THOC3 | 0.986 | 0.000 | — |
| BTRC | 0.984 | 0.621 | — |
| SMO | 0.980 | 0.275 | — |
| SHH | 0.975 | 0.126 | — |
| PTCH1 | 0.972 | 0.150 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STK36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10806483 |
| SUFU | psi-mi:"MI:0096"(pull down) | pubmed:10564661|imex:IM-19149 |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| SMAD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:25670079|imex:IM-24169 |
| SMAD3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:25670079|imex:IM-24169 |
| BTRC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:25670079|imex:IM-24169 |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25670079|imex:IM-24169 |
| SMAD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25670079|imex:IM-24169 |
| KIF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CARM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.0 + PDB: 无 | pLDDT=42.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell projection, cilium; Nucle / Nucleoli; 额外: Nucleoplasm, Centrosome, Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. GLI2 — Zinc finger protein GLI2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1586 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=42.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10070
- Protein Atlas: https://www.proteinatlas.org/ENSG00000074047-GLI2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10070
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
