---
type: protein-evaluation
gene: "S100PBP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## S100PBP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | S100PBP / S100PBPR |
| 蛋白名称 | S100P-binding protein |
| 蛋白大小 | 408 aa / 45.6 kDa |
| UniProt ID | Q96BU1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 408 aa / 45.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026097; Pfam: PF15427 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: S100PBPR |

**关键文献**:
1. Prognostic Value of S100 Family mRNA Expression in Hepatocellular Carcinoma.. *The Turkish journal of gastroenterology : the official journal of Turkish Society of Gastroenterology*. PMID: 39128058
2. S100PBP is regulated by mutated KRAS and plays a tumour suppressor role in pancreatic cancer.. *Oncogene*. PMID: 37794133
3. Novel functions and targets of miR-944 in human cervical cancer cells.. *International journal of cancer*. PMID: 25156441
4. S100P-binding protein, S100PBP, mediates adhesion through regulation of cathepsin Z in pancreatic cancer cells.. *The American journal of pathology*. PMID: 22330678
5. LncRNA S100PBP promotes proliferation and steroid hormone synthesis of granulosa cells by sponging MiR-2285bc-BMPR2 in bovine†.. *Biology of reproduction*. PMID: 38412119

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.8 |
| 高置信度残基 (pLDDT>90) 占比 | 2.5% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 30.4% |
| 低置信 (pLDDT<50) 占比 | 52.9% |
| 有序区域 (pLDDT>70) 占比 | 16.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.8），有序残基占 16.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026097; Pfam: PF15427 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| S100P | 0.982 | 0.000 | — |
| PCED1B | 0.616 | 0.615 | — |
| ANGEL2 | 0.530 | 0.000 | — |
| LRIG2 | 0.530 | 0.000 | — |
| ZG16B | 0.517 | 0.000 | — |
| FAM89A | 0.478 | 0.000 | — |
| TCEANC2 | 0.436 | 0.000 | — |
| NUP43 | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCED1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUDT21 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PCED1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000373475 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 4
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.8 + PDB: 无 | pLDDT=53.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 8 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. S100PBP — S100P-binding protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小408 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=53.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BU1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116497-S100PBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=S100PBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BU1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
