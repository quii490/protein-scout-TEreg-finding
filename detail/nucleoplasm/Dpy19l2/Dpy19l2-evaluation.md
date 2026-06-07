---
type: protein-evaluation
gene: "Dpy19l2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Dpy19l2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Dpy19l2 |
| 蛋白名称 | Probable C-mannosyltransferase DPY19L2 |
| 蛋白大小 | 758 aa / 87.4 kDa |
| UniProt ID | Q6NUT2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Nucleus inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 758 aa / 87.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=64 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018732; Pfam: PF10034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear inner membrane (GO:0005637)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 64 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. FAM209 associates with DPY19L2, and is required for sperm acrosome biogenesis and fertility in mice.. *Journal of cell science*. PMID: 34471926
3. Assessment of DPY19L2 Deletion in Familial and Non-Familial Individuals with Globozoospermia and DPY19L2 Genotyping.. *International journal of fertility & sterility*. PMID: 27441053
4. Duplication and relocation of the functional DPY19L2 gene within low copy repeats.. *BMC genomics*. PMID: 16526957
5. Teratozoospermia: spotlight on the main genetic actors in the human.. *Human reproduction update*. PMID: 25888788

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.4 |
| 高置信度残基 (pLDDT>90) 占比 | 53.3% |
| 置信残基 (pLDDT 70-90) 占比 | 28.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 81.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.4，有序区 81.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018732; Pfam: PF10034 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPATA16 | 0.898 | 0.000 | — |
| ZPBP | 0.835 | 0.000 | — |
| SPACA1 | 0.766 | 0.000 | — |
| PICK1 | 0.762 | 0.000 | — |
| SUN5 | 0.683 | 0.000 | — |
| AURKC | 0.682 | 0.000 | — |
| DNAH1 | 0.655 | 0.000 | — |
| C7orf61 | 0.635 | 0.000 | — |
| GOPC | 0.634 | 0.000 | — |
| PLCZ1 | 0.615 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GUK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| Q01160 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| Q7TLC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| EBI-25475914 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| EBI-25475903 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32838362|imex:IM-27901| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.4 + PDB: 无 | pLDDT=81.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus inner membrane / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. Dpy19l2 — Probable C-mannosyltransferase DPY19L2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小758 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 64 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NUT2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177990-DPY19L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Dpy19l2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NUT2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000177990-DPY19L2/subcellular

![](https://images.proteinatlas.org/71264/1304_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71264/1304_G1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/71264/1323_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71264/1323_G1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/71264/1559_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71264/1559_F9_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6NUT2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6NUT2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018732; |
| Pfam | PF10034; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177990-DPY19L2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
