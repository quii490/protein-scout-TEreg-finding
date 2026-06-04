---
type: protein-evaluation
gene: "MITF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MITF — REJECTED (研究热度过高 (PubMed strict=2344，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MITF / BHLHE32 |
| 蛋白名称 | Microphthalmia-associated transcription factor |
| 蛋白大小 | 526 aa / 58.8 kDa |
| UniProt ID | O75030 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm; Lysosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 526 aa / 58.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2344 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.8; PDB: 4C7N, 7D8R, 7D8S, 7D8T, 7EOD, 8E1D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR021802, IPR031867; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm; Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lysosomal membrane (GO:0005765)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2344 |
| PubMed broad count | 3994 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE32 |

**关键文献**:
1. Epigenetic regulation of melanogenesis.. *Ageing research reviews*. PMID: 33984527
2. MITF-the first 25 years.. *Genes & development*. PMID: 31123060
3. Acetylation reprograms MITF target selectivity and residence time.. *Nature communications*. PMID: 37770430
4. MITF Pathway-Activated Cutaneous Neoplasms.. *Advances in anatomic pathology*. PMID: 40387110
5. MITF promotes MFN2-dependent mitochondrial fusion to protect retinal pigment epithelial cells from mitochondrial damage.. *Free radical biology & medicine*. PMID: 40681059

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.8 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 24.1% |
| 低置信 (pLDDT<50) 占比 | 43.2% |
| 有序区域 (pLDDT>70) 占比 | 32.7% |
| 可用 PDB 条目 | 4C7N, 7D8R, 7D8S, 7D8T, 7EOD, 8E1D |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.8），有序残基占 32.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR021802, IPR031867; Pfam: PF11851, PF00010, PF15951 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TFE3 | 0.996 | 0.832 | — |
| TYR | 0.981 | 0.095 | — |
| TFEB | 0.976 | 0.808 | — |
| SPI1 | 0.968 | 0.292 | — |
| DCT | 0.956 | 0.091 | — |
| MAPK3 | 0.940 | 0.072 | — |
| SOX10 | 0.940 | 0.073 | — |
| TYRP1 | 0.936 | 0.091 | — |
| MAPK1 | 0.932 | 0.072 | — |
| JUN | 0.923 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HK3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| STUB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Pou5f1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20362542|imex:IM-16970 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFEB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.8 + PDB: 4C7N, 7D8R, 7D8S, 7D8T, 7EOD,  | pLDDT=60.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Lysosome membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MITF — Microphthalmia-associated transcription factor，研究基础较多，新颖性有限。
2. 蛋白大小526 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2344 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2344 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75030
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187098-MITF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MITF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75030
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
