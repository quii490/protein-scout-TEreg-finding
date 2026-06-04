---
type: protein-evaluation
gene: "MOSPD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MOSPD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MOSPD1 |
| 蛋白名称 | Motile sperm domain-containing protein 1 |
| 蛋白大小 | 213 aa / 24.1 kDa |
| UniProt ID | Q9UJG1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Endoplasmic reticulum membrane; Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 213 aa / 24.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR039283, IPR000535, IPR008962; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi membrane (GO:0000139)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Deciphering MOSPD1's impact on breast cancer progression and therapeutic response.. *Biology direct*. PMID: 39369222
2. Motile sperm domain containing 1 is upregulated by the Wnt/β-catenin signaling pathway in colorectal cancer.. *Oncology letters*. PMID: 35814826
3. A Role for MOSPD1 in Mesenchymal Stem Cell Proliferation and Differentiation.. *Stem cells (Dayton, Ohio)*. PMID: 26175344
4. Mospd1, a new player in mesenchymal versus epidermal cell differentiation.. *Journal of cellular physiology*. PMID: 21792907
5. MOSPD1 facilitates fatty acid metabolism and gastric cancer progression by promoting the MAPK pathway.. *Tissue & cell*. PMID: 39864210

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.1 |
| 高置信度残基 (pLDDT>90) 占比 | 46.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 15.0% |
| 低置信 (pLDDT<50) 占比 | 16.0% |
| 有序区域 (pLDDT>70) 占比 | 69.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.1，有序区 69.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR039283, IPR000535, IPR008962; Pfam: PF00635 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MOSPD2 | 0.737 | 0.047 | — |
| STARD3NL | 0.531 | 0.292 | — |
| RTL8A | 0.516 | 0.067 | — |
| OSBP | 0.515 | 0.281 | — |
| VAPA | 0.491 | 0.000 | — |
| ANTXRL | 0.472 | 0.099 | — |
| VAPB | 0.470 | 0.000 | — |
| STARD3 | 0.470 | 0.292 | — |
| SPATA31E1 | 0.445 | 0.000 | — |
| CCDC117 | 0.443 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FAM241B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EDAR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.1 + PDB: 无 | pLDDT=78.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus me / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MOSPD1 — Motile sperm domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小213 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJG1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101928-MOSPD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MOSPD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJG1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
