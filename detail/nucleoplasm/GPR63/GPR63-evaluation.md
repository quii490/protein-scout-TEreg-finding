---
type: protein-evaluation
gene: "GPR63"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPR63 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR63 / PSP24B |
| 蛋白名称 | Probable G-protein coupled receptor 63 |
| 蛋白大小 | 419 aa / 47.6 kDa |
| UniProt ID | Q9BZJ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane, Cytosol; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 419 aa / 47.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051880, IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane, Cytosol | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PSP24B |

**关键文献**:
1. Constitutive Activity among Orphan Class-A G Protein Coupled Receptors.. *PloS one*. PMID: 26384023
2. Gpr63 is a modifier of microcephaly in Ttc21b mouse mutants.. *PLoS genetics*. PMID: 31730647
3. Endothelial cell-derived S1P promotes migration and stemness by binding with GPR63 in colorectal cancer.. *Pathology, research and practice*. PMID: 36371997
4. Identification of four novel human G protein-coupled receptors expressed in the brain.. *Brain research. Molecular brain research*. PMID: 11165367
5. Genetic study of intracranial aneurysms.. *Stroke*. PMID: 25649796

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.0 |
| 高置信度残基 (pLDDT>90) 占比 | 48.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 66.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.0，有序区 66.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051880, IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLHL32 | 0.677 | 0.000 | — |
| GPR88 | 0.588 | 0.000 | — |
| NDUFA4 | 0.518 | 0.000 | — |
| GPR150 | 0.511 | 0.000 | — |
| GPR52 | 0.494 | 0.000 | — |
| GPR27 | 0.490 | 0.000 | — |
| GPR3 | 0.489 | 0.000 | — |
| GPR22 | 0.484 | 0.000 | — |
| GPR6 | 0.479 | 0.000 | — |
| MANEA | 0.475 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP2 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.0 + PDB: 无 | pLDDT=75.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Nucleoplasm, Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. GPR63 — Probable G-protein coupled receptor 63，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小419 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZJ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112218-GPR63/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR63
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZJ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000112218-GPR63/subcellular

![](https://images.proteinatlas.org/39103/1511_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/39103/1511_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/39103/517_H11_3_red_green.jpg)
![](https://images.proteinatlas.org/39103/517_H11_5_red_green.jpg)
![](https://images.proteinatlas.org/39103/520_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/39103/520_H11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZJ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BZJ6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051880;IPR000276;IPR017452; |
| Pfam | PF00001; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112218-GPR63/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
