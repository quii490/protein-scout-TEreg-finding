---
type: protein-evaluation
gene: "GLI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLI1 / GLI |
| 蛋白名称 | Zinc finger protein GLI1 |
| 蛋白大小 | 1106 aa / 117.9 kDa |
| UniProt ID | P08151 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Primary cilium tip, Basal body, Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1106 aa / 117.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.5; PDB: 2GLI, 4BLB, 4KMD, 5OM0, 7T91 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043359, IPR056436, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Primary cilium tip, Basal body, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axoneme (GO:0005930)
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- ciliary tip (GO:0097542)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- GLI-SUFU complex (GO:1990788)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

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
| AlphaFold 平均 pLDDT | 45.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 79.6% |
| 有序区域 (pLDDT>70) 占比 | 15.1% |
| 可用 PDB 条目 | 2GLI, 4BLB, 4KMD, 5OM0, 7T91 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=45.5），有序残基占 15.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043359, IPR056436, IPR036236, IPR013087; Pfam: PF00096, PF23561 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUFU | 0.999 | 0.994 | — |
| KIF7 | 0.997 | 0.396 | — |
| SPOP | 0.990 | 0.296 | — |
| SMO | 0.988 | 0.275 | — |
| BTRC | 0.983 | 0.710 | — |
| SHH | 0.979 | 0.126 | — |
| PTCH1 | 0.978 | 0.150 | — |
| STK36 | 0.966 | 0.767 | — |
| PRKACA | 0.966 | 0.332 | — |
| IHH | 0.965 | 0.126 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK4 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| SUFU | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-17321|pubmed:22439934 |
| RPS6KB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-17321|pubmed:22439934 |
| STK36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10806483 |
| "Su | psi-mi:"MI:0018"(two hybrid) | pubmed:14611647|imex:IM-16925 |
| Ncoa3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14611647|imex:IM-16925 |
| Pias1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14611647|imex:IM-16925 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CRYBA4 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| PIN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.5 + PDB: 2GLI, 4BLB, 4KMD, 5OM0, 7T91 | pLDDT=45.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm; Nucleus / Nucleoplasm; 额外: Primary cilium tip, Basal body, C | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GLI1 — Zinc finger protein GLI1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1106 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=45.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P08151
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111087-GLI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P08151
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
