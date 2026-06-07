---
type: protein-evaluation
gene: "ECD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ECD — REJECTED (研究热度过高 (PubMed strict=2058，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ECD |
| 蛋白名称 | Protein ecdysoneless homolog |
| 蛋白大小 | 644 aa / 72.8 kDa |
| UniProt ID | O95905 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 644 aa / 72.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2058 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010770; Pfam: PF07093 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.0/180** | |
| **归一化总分** | | | **46.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2058 |
| PubMed broad count | 17441 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Erdheim-Chester disease.. *Best practice & research. Clinical rheumatology*. PMID: 32305313
2. RYK is a GPNMB receptor that drives MASH.. *Nature*. PMID: 41708863
3. Environmental circadian disruption re-writes liver circadian proteomes.. *Nature communications*. PMID: 38956413
4. Ecdysoneless Protein Regulates Viral and Cellular mRNA Splicing to Promote Cervical Oncogenesis.. *Molecular cancer research : MCR*. PMID: 34670863
5. Imaging in Erdheim-Chester Disease.. *Radiographics : a review publication of the Radiological Society of North America, Inc*. PMID: 39172709

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 33.4% |
| 置信残基 (pLDDT 70-90) 占比 | 37.1% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 17.1% |
| 有序区域 (pLDDT>70) 占比 | 70.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.0，有序区 70.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010770; Pfam: PF07093 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AAR2 | 0.955 | 0.866 | — |
| PRPF8 | 0.901 | 0.865 | — |
| SNRNP200 | 0.884 | 0.821 | — |
| ZNHIT2 | 0.868 | 0.777 | — |
| TSSC4 | 0.851 | 0.804 | — |
| SNRNP40 | 0.829 | 0.777 | — |
| EAPP | 0.817 | 0.814 | — |
| PIH1D1 | 0.782 | 0.616 | — |
| EFTUD2 | 0.762 | 0.671 | — |
| KIAA1143 | 0.636 | 0.628 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 无 | pLDDT=76.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ECD — Protein ecdysoneless homolog，研究基础较多，新颖性有限。
2. 蛋白大小644 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2058 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2058 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95905
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122882-ECD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ECD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95905
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000122882-ECD/subcellular

![](https://images.proteinatlas.org/6465/110_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/6465/110_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/6465/111_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/6465/111_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/6465/159_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/6465/159_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95905-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95905 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010770; |
| Pfam | PF07093; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000122882-ECD/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AAR2 | Biogrid, Bioplex | true |
| EAPP | Biogrid, Bioplex | true |
| EFTUD2 | Biogrid, Opencell, Bioplex | true |
| PIH1D1 | Intact, Biogrid | true |
| PRPF8 | Intact, Biogrid, Opencell, Bioplex | true |
| PTGES3 | Biogrid, Opencell, Bioplex | true |
| RUVBL1 | Intact, Biogrid, Bioplex | true |
| SNRNP200 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
