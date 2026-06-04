---
type: protein-evaluation
gene: "SERTAD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERTAD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SERTAD4 |
| 蛋白名称 | SERTA domain-containing protein 4 |
| 蛋白大小 | 356 aa / 39.3 kDa |
| UniProt ID | Q9NUC0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 356 aa / 39.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009263, IPR029708; Pfam: PF06031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Dynamic Chromatin Targeting of BRD4 Stimulates Cardiac Fibroblast Activation.. *Circulation research*. PMID: 31409188
2. Exploring SERTAD4 as a prognostic biomarker and therapeutic target in breast cancer: insights from multidatabase analyses and in vitro studies.. *Clinical and experimental medicine*. PMID: 40658117
3. Sertad4 Regulates Pathological Cardiac Remodeling.. *bioRxiv : the preprint server for biology*. PMID: 41889836
4. Neuroprotective effects of acteoside in a glaucoma mouse model by targeting Serta domain-containing protein 4.. *International journal of ophthalmology*. PMID: 38638260
5. KRAS mutation promotes the colonization of Fusobacterium nucleatum in colorectal cancer by down-regulating SERTAD4.. *Journal of cellular and molecular medicine*. PMID: 39462261

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.6 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 68.0% |
| 有序区域 (pLDDT>70) 占比 | 14.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=51.6），有序残基占 14.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009263, IPR029708; Pfam: PF06031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP2R2C | 0.843 | 0.838 | — |
| PPP2R1A | 0.826 | 0.826 | — |
| PPP2R2A | 0.826 | 0.824 | — |
| PPP2R2D | 0.795 | 0.792 | — |
| CBLL2 | 0.789 | 0.789 | — |
| PPP2R1B | 0.773 | 0.773 | — |
| SERTAD1 | 0.700 | 0.000 | — |
| PPP2CB | 0.690 | 0.687 | — |
| PPP2CA | 0.678 | 0.675 | — |
| SYT14 | 0.676 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| AKT1 | psi-mi:"MI:0096"(pull down) | imex:IM-11703|pubmed:20368287 |
| BCAP31 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PPP2R2A | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R2C | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R2D | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| POTEF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP2R1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.6 + PDB: 无 | pLDDT=51.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SERTAD4 — SERTA domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小356 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=51.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUC0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082497-SERTAD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERTAD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NUC0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
