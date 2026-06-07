---
type: protein-evaluation
gene: "CHST2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHST2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHST2 / GN6ST |
| 蛋白名称 | Carbohydrate sulfotransferase 2 |
| 蛋白大小 | 530 aa / 57.9 kDa |
| UniProt ID | Q9Y4C5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Golgi apparatus, trans-Golgi network membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 530 aa / 57.9 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=77.1; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR016469, IPR051135, IPR027417, IPR000863; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)
- trans-Golgi network (GO:0005802)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GN6ST |

**关键文献**:
1. Discovery of a Therapeutic Agent for Glioblastoma Using a Systems Biology-Based Drug Repositioning Approach.. *International journal of molecular sciences*. PMID: 39063109
2. CHST2-mediated sulfation of MECA79 antigens is critical for breast cancer cell migration and metastasis.. *Cell death & disease*. PMID: 37095090
3. CHST1 and CHST2 sulfotransferases expressed by human vascular endothelial cells: cDNA cloning, expression, and chromosomal localization.. *Genomics*. PMID: 10049591
4. Genome-wide Identification of Foxf2 Target Genes in Palate Development.. *Journal of dental research*. PMID: 32040930
5. Proteomic analysis of bone tissues of patients with osteonecrosis of the femoral head.. *Omics : a journal of integrative biology*. PMID: 20001860

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.1 |
| 高置信度残基 (pLDDT>90) 占比 | 56.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 25.8% |
| 有序区域 (pLDDT>70) 占比 | 68.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.1，有序区 68.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016469, IPR051135, IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHST4 | 0.915 | 0.000 | — |
| NTAN1 | 0.913 | 0.000 | — |
| LUM | 0.638 | 0.000 | — |
| CHST15 | 0.497 | 0.000 | — |
| GALNT6 | 0.496 | 0.000 | — |
| FMOD | 0.475 | 0.000 | — |
| PRELP | 0.468 | 0.000 | — |
| GCNT1 | 0.467 | 0.000 | — |
| ACAN | 0.466 | 0.000 | — |
| B4GALT4 | 0.466 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CANX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.1 + PDB: 无 | pLDDT=77.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network membrane / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CHST2 -- Carbohydrate sulfotransferase 2，非常新颖，仅有少数基础研究。
2. 蛋白大小530 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4C5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175040-CHST2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHST2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4C5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4C5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y4C5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016469;IPR051135;IPR027417;IPR000863; |
| Pfam | PF00685; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175040-CHST2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
