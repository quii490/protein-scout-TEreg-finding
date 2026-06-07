---
type: protein-evaluation
gene: "DNAJB6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJB6 — REJECTED (研究热度过高 (PubMed strict=200，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB6 |
| 蛋白名称 | DnaJ heat shock protein family (Hsp40) member B6 |
| 蛋白大小 | 334 aa / 36.7 kDa |
| UniProt ID | A0A0J9YX62 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 334 aa / 36.7 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=200 篇 (>100->REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=59.2; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **67/180** | |
| **归一化总分** | | | **37.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 200 |
| PubMed broad count | 227 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DNAJB6: A guardian against neurodegeneration.. *Neural Regen Res*. PMID: 40536953
2. TGEV infection activates pro‑inflammatory signaling via the YY1/HSP40/NF‑κB pathway in intestinal epithelial cells and organoids.. *Vet Microbiol*. PMID: 41797175
3. Transient Aggregation-Prone States in Disordered Proteins as Therapeutic Targets: The Amyloid-β Case.. *J Chem Inf Model*. PMID: 41981770
4. Novel cell-based assay enables FRET-based measurements of the dimerization activity of the chaperone DNAJB6.. *Biol Methods Protoc*. PMID: 41717343
5. DNAJB6 as an immuno-oncogenic hub in liver hepatocellular carcinoma: multi-omic profiling reveals prognostic significance and therapeutic vulnerability.. *J Mol Histol*. PMID: 41559348

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.2 |
| 高置信度残基 (pLDDT>90) 占比 | 4.8% |
| 置信残基 (pLDDT 70-90) 占比 | 35.6% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 46.4% |
| 有序区域 (pLDDT>70) 占比 | 40.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.2），有序残基占 40.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| BAG3 | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |
| STUB1 | 0.000 | 0.000 | — |
| HSPA9 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| MLF2 | 0.000 | 0.000 | — |
| GRPEL1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.2 + PDB: 无 | pLDDT=59.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DNAJB6 -- DnaJ heat shock protein family (Hsp40) member B6，研究基础较多，新颖性有限。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 200 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 200 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A0J9YX62
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105993-DNAJB6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A0J9YX62
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A0A0J9YX62-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75190 |
| SMART | SM00271; |
| UniProt Domain [FT] | DOMAIN 2..69; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286" |
| InterPro | IPR001623;IPR018253;IPR043183;IPR036869; |
| Pfam | PF00226; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
