---
type: protein-evaluation
gene: "SDR39U1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SDR39U1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SDR39U1 / C14orf124, HCDI |
| 蛋白名称 | Epimerase family protein SDR39U1 |
| 蛋白大小 | 293 aa / 31.1 kDa |
| UniProt ID | Q9NRG7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 293 aa / 31.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=97.2; PDB: 4B4O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013549, IPR001509, IPR036291, IPR010099; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf124, HCDI |

**关键文献**:
1. Single Gene Prognostic Biomarkers in Ovarian Cancer: A Meta-Analysis.. *PloS one*. PMID: 26886260
2. LDHA is a prognostic biomarker on the immune response in pancreatic adenocarcinoma and associated with m6A modification.. *Journal of cancer research and clinical oncology*. PMID: 36269388
3. Proteomic analysis and biochemical alterations in marine mussel gills after exposure to the organophosphate flame retardant TDCPP.. *Aquatic toxicology (Amsterdam, Netherlands)*. PMID: 33316748
4. Unveiling alterative splice diversity from human oligodendrocyte proteome data.. *Journal of proteomics*. PMID: 27222040

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 98.6% |
| 置信残基 (pLDDT 70-90) 占比 | 1.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 4B4O |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=97.2，有序区 100.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013549, IPR001509, IPR036291, IPR010099; Pfam: PF08338, PF01370 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STOML1 | 0.616 | 0.000 | — |
| NYNRIN | 0.588 | 0.000 | — |
| TRMT2A | 0.581 | 0.000 | — |
| GIMAP7 | 0.564 | 0.000 | — |
| TUBGCP6 | 0.547 | 0.000 | — |
| STXBP6 | 0.512 | 0.000 | — |
| CBLN3 | 0.510 | 0.000 | — |
| NCLN | 0.491 | 0.000 | — |
| FECH | 0.483 | 0.000 | — |
| FCGR1B | 0.446 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 4B4O | pLDDT=97.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SDR39U1 — Epimerase family protein SDR39U1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小293 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRG7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100445-SDR39U1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SDR39U1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRG7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000100445-SDR39U1/subcellular

![](https://images.proteinatlas.org/44294/1145_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/44294/1145_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/44294/605_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/44294/605_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/44294/606_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/44294/606_A10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRG7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
