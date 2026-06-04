---
type: protein-evaluation
gene: "MFAP3L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MFAP3L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MFAP3L / KIAA0626 |
| 蛋白名称 | Microfibrillar-associated protein 3-like |
| 蛋白大小 | 409 aa / 45.4 kDa |
| UniProt ID | O75121 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cell Junctions; UniProt: Cell membrane; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 409 aa / 45.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR013098, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cell Junctions | Supported |
| UniProt | Cell membrane; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- neuron projection (GO:0043005)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0626 |

**关键文献**:
1. Identifying platelet-derived factors as amplifiers of B. burgdorferi-induced cytokine production.. *Clinical and experimental immunology*. PMID: 36001729
2. Identification of Recurrence-associated Gene Signatures and Machine Learning-based Prediction in IDH-Wildtype Histological Glioblastoma.. *Journal of molecular neuroscience : MN*. PMID: 40227386
3. MFAP3L activation promotes colorectal cancer cell invasion and metastasis.. *Biochimica et biophysica acta*. PMID: 24735981
4. The mouse retinal pigment epithelium mounts an innate immune defense response following retinal detachment.. *Journal of neuroinflammation*. PMID: 38528525
5. A novel gene expression signature for bone metastasis in breast carcinomas.. *Breast cancer research and treatment*. PMID: 26965286

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.6 |
| 高置信度残基 (pLDDT>90) 占比 | 17.8% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 15.9% |
| 低置信 (pLDDT<50) 占比 | 43.3% |
| 有序区域 (pLDDT>70) 占比 | 40.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.6），有序残基占 40.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR013098, IPR003599; Pfam: PF07679 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SFT2D2 | 0.582 | 0.000 | — |
| FAM204A | 0.527 | 0.000 | — |
| NIP7 | 0.479 | 0.000 | — |
| MMS22L | 0.472 | 0.000 | — |
| CSPG5 | 0.470 | 0.000 | — |
| KCNS1 | 0.468 | 0.000 | — |
| AADAT | 0.453 | 0.000 | — |
| PALM2AKAP2 | 0.445 | 0.000 | — |
| MBIP | 0.442 | 0.000 | — |
| ATL2 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-25475894 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 1
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.6 + PDB: 无 | pLDDT=61.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Nucleus; Cytoplasm / Nucleoplasm; 额外: Cell Junctions | 一致 |
| PPI | STRING + IntAct | 11 + 1 interactions | 数据充分 |

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
1. MFAP3L — Microfibrillar-associated protein 3-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小409 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75121
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198948-MFAP3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MFAP3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75121
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
