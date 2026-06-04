---
type: protein-evaluation
gene: "CTDSPL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTDSPL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTDSPL / C3orf8, NIF1, NIFL, SCP3, YA22 |
| 蛋白名称 | CTD small phosphatase-like protein |
| 蛋白大小 | 276 aa / 31.1 kDa |
| UniProt ID | O15194 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 276 aa / 31.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=77.8; PDB: 2HHL |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011948, IPR004274, IPR036412, IPR023214, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 56 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf8, NIF1, NIFL, SCP3, YA22 |

**关键文献**:
1. [SCP Phosphatases and Oncogenesis].. *Molekuliarnaia biologiia*. PMID: 34432772
2. Tumor Suppressor Properties of Small C-Terminal Domain Phosphatases in Clear Cell Renal Cell Carcinoma.. *International journal of molecular sciences*. PMID: 37629167
3. [Interaction of two tumor suppressors: Phosphatase CTDSPL and Rb protein].. *Molekuliarnaia biologiia*. PMID: 27414789
4. Hsa-miR-503-5p regulates CTDSPL to accelerate cisplatin resistance and angiogenesis of lung adenocarcinoma cells.. *Chemical biology & drug design*. PMID: 37341065
5. Epigenetic alterations of chromosome 3 revealed by NotI-microarrays in clear cell renal cell carcinoma.. *BioMed research international*. PMID: 24977159

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 63.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 27.2% |
| 有序区域 (pLDDT>70) 占比 | 65.6% |
| 可用 PDB 条目 | 2HHL |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=77.8，有序区 65.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011948, IPR004274, IPR036412, IPR023214, IPR040078; Pfam: PF03031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDCA3 | 0.861 | 0.847 | — |
| CTDSP1 | 0.842 | 0.833 | — |
| MBP | 0.833 | 0.833 | — |
| GTF2F1 | 0.775 | 0.477 | — |
| CTDP1 | 0.749 | 0.000 | — |
| REST | 0.733 | 0.048 | — |
| CTDSP2 | 0.640 | 0.608 | — |
| WDR35 | 0.507 | 0.000 | — |
| ITGA9 | 0.504 | 0.045 | — |
| VILL | 0.494 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDCA3 | psi-mi:"MI:0090"(protein complementation assay) | pubmed:32296183|imex:IM-25472 |
| CTDSP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAGEA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CTDSP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 2HHL | pLDDT=77.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CTDSPL — CTD small phosphatase-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小276 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15194
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144677-CTDSPL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTDSPL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15194
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CTDSPL/IF_images/CTDSPL_IF_red_green.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CTDSPL/CTDSPL-PAE.png]]
